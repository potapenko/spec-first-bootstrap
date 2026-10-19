use pulldown_cmark::{
    BrokenLink, CowStr, Event, HeadingLevel, LinkType, Options, Parser, Tag, TagEnd,
};
use std::collections::{HashMap, HashSet};
use std::fmt::Write as _;
use std::ops::Range;
use std::path::{Component, Path, PathBuf};

#[derive(Default)]
pub struct Report {
    pub output: String,
    pub errors: Vec<String>,
}

impl Report {
    pub fn error(error: String) -> Self {
        Self {
            output: String::new(),
            errors: vec![error],
        }
    }
}

struct Link {
    label: String,
    destination: String,
    context: String,
    section: String,
    line: usize,
    dependency: bool,
    unresolved: bool,
}

struct Document {
    text: String,
    title: String,
    metadata: HashMap<String, String>,
    anchors: HashSet<String>,
    links: Vec<Link>,
}

fn plain(events: &[(Event<'_>, Range<usize>)]) -> String {
    let mut text = String::new();
    for (event, _) in events {
        match event {
            Event::Text(value) | Event::Code(value) => text.push_str(value),
            Event::SoftBreak | Event::HardBreak => text.push(' '),
            _ => (),
        }
    }
    text
}

fn dependency_heading(text: &str) -> bool {
    let first = text
        .split(|c: char| !c.is_alphanumeric() && c != '_')
        .next()
        .unwrap_or("");
    matches!(
        first.to_ascii_lowercase().as_str(),
        "dependency" | "dependencies"
    )
}

impl Document {
    fn parse(text: String) -> Self {
        // Preserve unresolved references so a required dependency cannot disappear.
        let mut broken = |link: BrokenLink<'_>| {
            Some((CowStr::from(link.reference.to_string()), CowStr::from("")))
        };
        let events: Vec<_> =
            Parser::new_with_broken_link_callback(&text, Options::ENABLE_TABLES, Some(&mut broken))
                .into_offset_iter()
                .collect();
        let mut title = String::new();
        let mut metadata = HashMap::new();
        let mut anchors = HashSet::new();
        let mut containers: Vec<(u8, Range<usize>)> = Vec::new();
        let mut section = String::from("(document)");
        let mut dependency = false;
        let mut links = Vec::new();
        for (index, (event, range)) in events.iter().enumerate() {
            match event {
                Event::Start(Tag::Heading { level, .. }) => {
                    let end = events[index + 1..]
                        .iter()
                        .position(|(e, _)| matches!(e, Event::End(TagEnd::Heading(_))))
                        .unwrap()
                        + index
                        + 1;
                    let heading = plain(&events[index + 1..end]);
                    if title.is_empty() && *level == HeadingLevel::H1 {
                        title = heading.clone();
                    }
                    let base: String = heading
                        .to_lowercase()
                        .chars()
                        .filter(|c| c.is_alphanumeric() || matches!(c, '_' | '-' | ' '))
                        .map(|c| if c == ' ' { '-' } else { c })
                        .collect();
                    let mut anchor = base.clone();
                    let mut suffix = 0;
                    while anchors.contains(&anchor) {
                        suffix += 1;
                        anchor = format!("{base}-{suffix}");
                    }
                    anchors.insert(anchor);
                    section = heading.clone();
                    if matches!(level, HeadingLevel::H1 | HeadingLevel::H2) {
                        dependency = *level == HeadingLevel::H2 && dependency_heading(&heading);
                    }
                }
                Event::Start(Tag::Item) => {
                    if !containers.iter().any(|(kind, _)| *kind == 1) {
                        let end = events[index + 1..]
                            .iter()
                            .position(|(e, _)| matches!(e, Event::End(TagEnd::Item)))
                            .unwrap()
                            + index
                            + 1;
                        let value = plain(&events[index + 1..end]);
                        if let Some((key, value)) = value.split_once(':')
                            && matches!(
                                key,
                                "Node type"
                                    | "Status"
                                    | "Read when"
                                    | "Do not read when"
                                    | "Contract revision"
                                    | "Revision"
                                    | "Contract"
                            )
                        {
                            let original = text[range.clone()]
                                .split_once(':')
                                .map(|(_, value)| value)
                                .unwrap_or(value);
                            metadata.entry(key.to_string()).or_insert_with(|| {
                                original.split_whitespace().collect::<Vec<_>>().join(" ")
                            });
                        }
                    }
                    containers.push((1, range.clone()));
                }
                Event::Start(Tag::Paragraph) => containers.push((2, range.clone())),
                Event::Start(Tag::TableRow | Tag::TableHead) => containers.push((3, range.clone())),
                Event::End(
                    TagEnd::Item | TagEnd::Paragraph | TagEnd::TableRow | TagEnd::TableHead,
                ) => {
                    containers.pop();
                }
                Event::Start(Tag::Link {
                    dest_url,
                    link_type,
                    ..
                }) => {
                    let end = events[index + 1..]
                        .iter()
                        .position(|(e, _)| matches!(e, Event::End(TagEnd::Link)))
                        .unwrap()
                        + index
                        + 1;
                    // Prefer the nearest item/row over its inner paragraph.
                    let context = containers
                        .iter()
                        .rev()
                        .find(|(kind, _)| *kind != 2)
                        .or_else(|| containers.last())
                        .map(|(_, r)| r.clone())
                        .unwrap_or(range.clone());
                    links.push(Link {
                        label: plain(&events[index + 1..end]),
                        destination: dest_url.to_string(),
                        context: text[context].trim_end().to_string(),
                        section: section.clone(),
                        line: text[..range.start].bytes().filter(|b| *b == b'\n').count() + 1,
                        dependency,
                        unresolved: matches!(
                            link_type,
                            LinkType::ReferenceUnknown
                                | LinkType::CollapsedUnknown
                                | LinkType::ShortcutUnknown
                        ),
                    });
                }
                _ => (),
            }
        }
        Self {
            text,
            title,
            metadata,
            anchors,
            links,
        }
    }

    fn field(&self, key: &str) -> &str {
        self.metadata
            .get(key)
            .map(String::as_str)
            .unwrap_or("not declared")
    }

    fn revision(&self) -> &str {
        ["Contract revision", "Revision", "Contract"]
            .iter()
            .find_map(|key| self.metadata.get(*key))
            .map(String::as_str)
            .unwrap_or("not declared")
    }

    fn traversable(&self) -> Result<(), String> {
        let lines = self.text.lines().count();
        if self.metadata.contains_key("Node type") && lines > 100 {
            return Err(format!(
                "declared node has {lines} physical lines; maximum is 100; use read to inspect source"
            ));
        }
        Ok(())
    }
}

enum Target {
    Local { path: PathBuf, fragment: String },
    Remote(String),
}

fn decode(value: &str) -> Result<String, String> {
    let mut bytes = Vec::new();
    let mut iter = value.bytes();
    while let Some(byte) = iter.next() {
        if byte == b'%' {
            let high = iter.next().and_then(|b| (b as char).to_digit(16));
            let low = iter.next().and_then(|b| (b as char).to_digit(16));
            match (high, low) {
                (Some(h), Some(l)) => bytes.push((h * 16 + l) as u8),
                _ => return Err(format!("invalid percent encoding: {value}")),
            }
        } else {
            bytes.push(byte);
        }
    }
    String::from_utf8(bytes).map_err(|_| format!("invalid UTF-8 in path/fragment: {value}"))
}

pub struct Project {
    root: PathBuf,
}

impl Project {
    pub fn new(root: &Path) -> Result<Self, String> {
        Ok(Self {
            root: root
                .canonicalize()
                .map_err(|e| format!("{}: {e}", root.display()))?,
        })
    }

    fn display(&self, path: &Path) -> String {
        path.strip_prefix(&self.root)
            .unwrap_or(path)
            .display()
            .to_string()
    }

    fn target(&self, base: &Path, value: &str) -> Result<Target, String> {
        let scheme = value.split_once(':').map(|(s, _)| s);
        if value.starts_with("//")
            || scheme.is_some_and(|s| {
                !s.is_empty()
                    && s.starts_with(|c: char| c.is_ascii_alphabetic())
                    && s.chars()
                        .all(|c| c.is_ascii_alphanumeric() || matches!(c, '+' | '-' | '.'))
            })
        {
            return Ok(Target::Remote(value.to_string()));
        }
        let (file, fragment) = value.split_once('#').unwrap_or((value, ""));
        let file = decode(file.split('?').next().unwrap())?;
        let candidate = if file.is_empty() {
            base.to_path_buf()
        } else {
            base.parent().unwrap().join(file)
        };
        let mut path = PathBuf::new();
        for part in candidate.components() {
            match part {
                Component::ParentDir => {
                    path.pop();
                }
                Component::CurDir => (),
                other => path.push(other.as_os_str()),
            }
        }
        if !path.starts_with(&self.root) {
            return Err(format!("path escapes project: {value}"));
        }
        Ok(Target::Local {
            path,
            fragment: decode(fragment)?,
        })
    }

    fn argument(&self, node: &str) -> Result<Target, String> {
        self.target(&self.root.join(".command-base"), node)
    }

    fn local(&self, target: &Target) -> Result<(PathBuf, String), String> {
        match target {
            Target::Remote(url) => Err(format!("remote target is not opened: {url}")),
            Target::Local { path, fragment } => {
                let canonical = path
                    .canonicalize()
                    .map_err(|e| format!("{}: {e}", self.display(path)))?;
                if !canonical.starts_with(&self.root) {
                    return Err(format!("symlink escapes project: {}", self.display(path)));
                }
                if path.extension().is_none_or(|extension| extension != "md")
                    || canonical
                        .extension()
                        .is_none_or(|extension| extension != "md")
                {
                    return Err(format!("not a Markdown file: {}", self.display(path)));
                }
                Ok((canonical, fragment.clone()))
            }
        }
    }

    fn load(&self, path: &Path) -> Result<Document, String> {
        std::fs::read_to_string(path)
            .map(Document::parse)
            .map_err(|e| format!("{}: {e}", self.display(path)))
    }

    fn fragment(&self, doc: &Document, path: &Path, fragment: &str) -> Result<(), String> {
        if !fragment.is_empty() && !doc.anchors.contains(fragment) {
            return Err(format!(
                "{}: missing heading #{fragment}",
                self.display(path)
            ));
        }
        Ok(())
    }

    fn selected(&self, node: &str) -> Result<(PathBuf, Document), String> {
        let (path, fragment) = self.local(&self.argument(node)?)?;
        let doc = self.load(&path)?;
        self.fragment(&doc, &path, &fragment)?;
        Ok((path, doc))
    }

    pub fn read(&self, node: &str) -> Report {
        match self.selected(node) {
            Ok((_, doc)) => Report {
                output: doc.text,
                errors: vec![],
            },
            Err(error) => Report::error(error),
        }
    }

    pub fn map(&self, node: &str) -> Report {
        let (path, doc) = match self.selected(node) {
            Ok(selected) => selected,
            Err(error) => return Report::error(error),
        };
        if let Err(error) = doc.traversable() {
            return Report::error(format!("{}: {error}", self.display(&path)));
        }
        let mut report = Report::default();
        let out = &mut report.output;
        writeln!(
            out,
            "Document: {}\nTitle: {}",
            self.display(&path),
            doc.title
        )
        .unwrap();
        for key in ["Node type", "Status", "Read when", "Do not read when"] {
            writeln!(out, "{key}: {}", doc.field(key)).unwrap();
        }
        writeln!(out, "Revision: {}\n", doc.revision()).unwrap();
        let mut section = String::new();
        for link in &doc.links {
            if section != link.section {
                section = link.section.clone();
                writeln!(out, "## {section}").unwrap();
            }
            let target = self.target(&path, &link.destination);
            let destination = match target {
                Ok(Target::Local { path, fragment }) => format!(
                    "{}{}",
                    self.display(&path),
                    if fragment.is_empty() {
                        String::new()
                    } else {
                        format!("#{fragment}")
                    }
                ),
                Ok(Target::Remote(url)) => format!("{url} (remote; not fetched)"),
                Err(error) => {
                    report
                        .errors
                        .push(format!("{}:{}: {error}", self.display(&path), link.line));
                    link.destination.clone()
                }
            };
            if link.unresolved {
                report.errors.push(format!(
                    "{}:{}: unresolved reference [{}]",
                    self.display(&path),
                    link.line,
                    link.destination
                ));
            }
            writeln!(
                out,
                "- {}\n  Target: {destination}\n  Source: {}:{}\n  Original:\n{}\n",
                link.label,
                self.display(&path),
                link.line,
                link.context
                    .lines()
                    .map(|line| format!("    {line}"))
                    .collect::<Vec<_>>()
                    .join("\n")
            )
            .unwrap();
        }
        if doc.links.is_empty() {
            writeln!(out, "No outgoing links.").unwrap();
        }
        writeln!(
            out,
            "Navigation only; targets not opened. Full contract: spec-nav read {}",
            self.display(&path)
        )
        .unwrap();
        report
    }

    pub fn deps(&self, node: &str) -> Report {
        let mut walk = Walk {
            project: self,
            docs: HashMap::new(),
            visiting: Vec::new(),
            visited: HashSet::new(),
            entries: Vec::new(),
            errors: Vec::new(),
        };
        match self.argument(node) {
            Ok(target) => {
                walk.visit(target);
            }
            Err(error) => walk.errors.push(error),
        }
        let mut output = format!("Dependencies of: {node}\n\n");
        for entry in &walk.entries {
            writeln!(
                output,
                "- {}\n  Revision: {}",
                self.display(&entry.path),
                walk.docs
                    .get(&entry.path)
                    .map(Document::revision)
                    .unwrap_or("unavailable")
            )
            .unwrap();
            for reason in &entry.reasons {
                writeln!(output, "  Required by: {reason}").unwrap();
            }
        }
        if walk.entries.is_empty() {
            writeln!(output, "No declared local dependencies discovered.").unwrap();
        }
        writeln!(output, "\nUnique dependency documents: {}\nDeclared dependency traversal: {}\nBodies not included. This is not a proof of semantic completeness.", walk.entries.len(), if walk.errors.is_empty() { "complete" } else { "INCOMPLETE" }).unwrap();
        Report {
            output,
            errors: walk.errors,
        }
    }
}

struct Entry {
    path: PathBuf,
    reasons: Vec<String>,
}

struct Walk<'a> {
    project: &'a Project,
    docs: HashMap<PathBuf, Document>,
    visiting: Vec<PathBuf>,
    visited: HashSet<PathBuf>,
    entries: Vec<Entry>,
    errors: Vec<String>,
}

impl Walk<'_> {
    fn visit(&mut self, target: Target) {
        let result = self.project.local(&target).and_then(|(path, fragment)| {
            if !self.docs.contains_key(&path) {
                self.docs.insert(path.clone(), self.project.load(&path)?);
            }
            let doc = &self.docs[&path];
            self.project.fragment(doc, &path, &fragment)?;
            doc.traversable()
                .map_err(|e| format!("{}: {e}", self.project.display(&path)))?;
            Ok(path)
        });
        let path = match result {
            Ok(path) => path,
            Err(error) => {
                self.errors.push(error);
                return;
            }
        };
        if self.visiting.contains(&path) {
            let mut chain: Vec<_> = self
                .visiting
                .iter()
                .map(|p| self.project.display(p))
                .collect();
            chain.push(self.project.display(&path));
            self.errors
                .push(format!("dependency cycle: {}", chain.join(" -> ")));
            return;
        }
        if !self.visited.insert(path.clone()) {
            return;
        }
        self.visiting.push(path.clone());
        // Own the small edge list so recursive reads can populate the document cache.
        let edges: Vec<_> = self.docs[&path]
            .links
            .iter()
            .filter(|l| l.dependency)
            .map(|l| {
                (
                    l.destination.clone(),
                    l.section.clone(),
                    l.line,
                    l.unresolved,
                )
            })
            .collect();
        for (destination, section, line, unresolved) in edges {
            let reason = format!(
                "{}:{line} [{section}] -> {destination}",
                self.project.display(&path)
            );
            let target = if unresolved {
                Err(format!("unresolved reference [{destination}]"))
            } else {
                self.project.target(&path, &destination)
            };
            match target {
                Ok(target) => match self.project.local(&target) {
                    Ok((dependency, _)) => {
                        if let Some(entry) = self.entries.iter_mut().find(|e| e.path == dependency)
                        {
                            entry.reasons.push(reason.clone());
                        } else {
                            self.entries.push(Entry {
                                path: dependency,
                                reasons: vec![reason.clone()],
                            });
                        }
                        let before = self.errors.len();
                        self.visit(target);
                        for error in &mut self.errors[before..] {
                            *error = format!("{reason}: {error}");
                        }
                    }
                    Err(error) => self.errors.push(format!("{reason}: {error}")),
                },
                Err(error) => self.errors.push(format!("{reason}: {error}")),
            }
        }
        self.visiting.pop();
    }
}
