use std::fs;
use std::path::PathBuf;
use std::process::{Command, Output};
use std::sync::atomic::{AtomicUsize, Ordering};

static NEXT: AtomicUsize = AtomicUsize::new(0);

struct Fixture(PathBuf);
impl Fixture {
    fn new() -> Self {
        let root = std::env::temp_dir().join(format!(
            "spec-nav-test-{}-{}",
            std::process::id(),
            NEXT.fetch_add(1, Ordering::Relaxed)
        ));
        fs::create_dir(&root).unwrap();
        Self(root)
    }
    fn write(&self, name: &str, text: &str) {
        let path = self.0.join(name);
        fs::create_dir_all(path.parent().unwrap()).unwrap();
        fs::write(path, text).unwrap();
    }
    fn run(&self, args: &[&str]) -> Output {
        Command::new(env!("CARGO_BIN_EXE_spec-nav"))
            .current_dir(&self.0)
            .args(args)
            .output()
            .unwrap()
    }
}
impl Drop for Fixture {
    fn drop(&mut self) {
        // These fixtures contain only text created by this test.
        fs::remove_dir_all(&self.0).unwrap();
        assert!(!self.0.exists());
    }
}
fn stdout(out: &Output) -> String {
    String::from_utf8(out.stdout.clone()).unwrap()
}
fn stderr(out: &Output) -> String {
    String::from_utf8(out.stderr.clone()).unwrap()
}
fn success(out: &Output) {
    assert!(out.status.success(), "{}", stderr(out));
}
fn failed(out: &Output, text: &str) {
    assert_eq!(out.status.code(), Some(1));
    assert!(stderr(out).contains(text), "{}", stderr(out));
}

#[test]
fn map_defaults_to_root_and_never_reads_targets() {
    let f = Fixture::new();
    f.write("docs/specs/README.md", "# Root\n\n- Node type: root\n- Status: Active\n- Read when: choosing\n  a branch.\n- Revision: `root@1`\n\n## Choose\n\n- [Branch](branch.md) — description\n  continues here.\n");
    // branch.md deliberately does not exist: map must not open it.
    let out = f.run(&["map"]);
    success(&out);
    let text = stdout(&out);
    for expected in [
        "Title: Root",
        "Node type: root",
        "Status: Active",
        "Read when: choosing a branch.",
        "Revision: `root@1`",
        "Do not read when: not declared",
        "Target: docs/specs/branch.md",
        "## Choose",
        "Source: docs/specs/README.md:11",
        "continues here.",
        "targets not opened",
    ] {
        assert!(text.contains(expected), "missing {expected}: {text}");
    }
}

#[test]
fn map_preserves_reference_table_and_inline_context() {
    let f = Fixture::new();
    f.write("root.md", "# Root\n\nA [reference][target] in a paragraph.\n\n[target]: leaf.md#rule\n\n| Name | Meaning |\n| --- | --- |\n| [Leaf](leaf.md) | whole row |\n\n[Remote](https://example.com)\n\n![Ignored](image.png)\n\n```md\n[Example](missing.md)\n## Dependencies\n```\n");
    let out = f.run(&["map", "root.md"]);
    success(&out);
    let text = stdout(&out);
    assert!(text.contains("Target: leaf.md#rule"));
    assert!(text.contains("A [reference][target] in a paragraph."));
    assert!(text.contains("| [Leaf](leaf.md) | whole row |"));
    assert!(text.contains("remote; not fetched"));
    assert!(!text.contains("missing.md"));
    assert!(!text.contains("image.png"));
}

#[test]
fn read_is_byte_exact_including_crlf_unicode_and_missing_final_newline() {
    let f = Fixture::new();
    let original = "# Заголовок\r\n\r\nТочный **текст** — é";
    f.write("source.md", original);
    let out = f.run(&["read", "source.md"]);
    success(&out);
    assert_eq!(out.stdout, original.as_bytes());
    assert!(out.stderr.is_empty());
}

#[test]
fn fragment_selects_whole_document_and_handles_duplicate_headings() {
    let f = Fixture::new();
    let text = "# Root\n\n## **Rule**\nfirst\n\n## Rule\nsecond\n\n## Привет мир\n";
    f.write("a b.md", text);
    for node in [
        "a%20b.md#rule-1",
        "a%20b.md#%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82-%D0%BC%D0%B8%D1%80",
    ] {
        let out = f.run(&["read", node]);
        success(&out);
        assert_eq!(out.stdout, text.as_bytes());
    }
    failed(
        &f.run(&["read", "a%20b.md#missing"]),
        "missing heading #missing",
    );
}

#[test]
fn deps_diamond_deduplicates_documents_and_keeps_all_reasons() {
    let f = Fixture::new();
    f.write("a.md", "# A\n\n## Dependencies\n- [B](b.md)\n- [C](c.md#rule)\n\n## Other\n[Do not follow](missing.md)\n");
    f.write(
        "b.md",
        "# B\n\n- Contract: `b@1`\n\n## Dependency notes\n[B needs C][c]\n\n[c]: c.md#rule\n",
    );
    f.write("c.md", "# C\n\n## Rule\nSECRET BODY\n");
    let out = f.run(&["deps", "a.md"]);
    success(&out);
    let text = stdout(&out);
    assert_eq!(text.matches("- c.md\n").count(), 1);
    assert!(text.contains("Required by: b.md:6 [Dependency notes] -> c.md#rule"));
    assert!(text.contains("Required by: a.md:5 [Dependencies] -> c.md#rule"));
    assert!(text.contains("Revision: `b@1`"));
    assert!(text.contains("Unique dependency documents: 2"));
    assert!(text.contains("traversal: complete"));
    assert!(!text.contains("SECRET BODY"));
    assert!(!text.contains("missing.md"));
    assert_eq!(out.stdout, f.run(&["deps", "a.md"]).stdout);
}

#[test]
fn deps_heading_boundaries_and_code_examples() {
    let f = Fixture::new();
    f.write("a.md", "# A\n\n```md\n## Dependencies\n[Fake](missing.md)\n```\n\n## DEPENDENCIES: required\n### Detail\n[Real](b.md)\n\n# Stop\n[Other](missing.md)\n\n## DependenciesElse\n[Other](missing.md)\n");
    f.write("b.md", "# B\n");
    let out = f.run(&["deps", "a.md"]);
    success(&out);
    assert!(stdout(&out).contains("Unique dependency documents: 1"));
}

#[test]
fn deps_reports_cycle_and_still_visits_independent_edge() {
    let f = Fixture::new();
    f.write("a.md", "# A\n\n## Dependencies\n[B](b.md)\n[C](c.md)\n");
    f.write("b.md", "# B\n\n## Dependency\n[A](a.md)\n");
    f.write("c.md", "# C\n");
    let out = f.run(&["deps", "a.md"]);
    failed(&out, "dependency cycle: a.md -> b.md -> a.md");
    assert!(stdout(&out).contains("- c.md"));
    assert!(stdout(&out).contains("traversal: INCOMPLETE"));
    assert!(stderr(&out).contains("b.md:4"));
}

#[test]
fn normal_navigation_cycle_is_not_a_dependency_cycle() {
    let f = Fixture::new();
    f.write("a.md", "# A\n[B](b.md)\n");
    f.write("b.md", "# B\n[A](a.md)\n");
    let out = f.run(&["deps", "a.md"]);
    success(&out);
    assert!(stdout(&out).contains("No declared local dependencies discovered"));
}

#[test]
fn deps_accumulates_missing_fragment_file_and_remote_errors() {
    let f = Fixture::new();
    f.write("a.md", "# A\n\n## Dependencies\n- [Missing](missing.md)\n- [Broken](b.md#absent)\n- [Remote](https://example.com)\n- [Text](note.txt)\n- [Good](c.md)\n");
    f.write("b.md", "# B\n");
    f.write("note.txt", "not Markdown");
    f.write("c.md", "# C\n");
    let out = f.run(&["deps", "a.md"]);
    for expected in [
        "missing.md",
        "missing heading #absent",
        "remote target is not opened",
        "not a Markdown file",
        "a.md:4",
    ] {
        failed(&out, expected);
    }
    assert!(stdout(&out).contains("- c.md"));
    assert!(stdout(&out).contains("traversal: INCOMPLETE"));
}

#[test]
fn missing_root_is_incomplete() {
    let f = Fixture::new();
    let out = f.run(&["deps", "absent.md"]);
    failed(&out, "absent.md");
    assert!(stdout(&out).contains("traversal: INCOMPLETE"));
}

#[test]
fn unresolved_reference_is_visible_in_map_and_fails_dependency_closure() {
    let f = Fixture::new();
    f.write(
        "a.md",
        "# A\n\n## Dependencies\n[Lost][missing-definition]\n",
    );
    for command in ["map", "deps"] {
        failed(
            &f.run(&[command, "a.md"]),
            "unresolved reference [missing-definition]",
        );
    }
}

#[test]
fn rereads_edited_files_between_invocations() {
    let f = Fixture::new();
    f.write("a.md", "# Before\n");
    assert!(stdout(&f.run(&["map", "a.md"])).contains("Title: Before"));
    f.write("a.md", "# After\n");
    assert!(stdout(&f.run(&["map", "a.md"])).contains("Title: After"));
}

#[test]
fn oversized_node_cannot_be_traversed_but_source_remains_readable() {
    let f = Fixture::new();
    let text = format!("# A\n- Node type: leaf\n{}", "line\n".repeat(99));
    f.write("a.md", &text);
    for command in ["map", "deps"] {
        failed(&f.run(&[command, "a.md"]), "101 physical lines");
    }
    let out = f.run(&["read", "a.md"]);
    success(&out);
    assert_eq!(out.stdout, text.as_bytes());
}

#[test]
fn invalid_utf8_and_malformed_percent_encoding_fail_without_panicking() {
    let f = Fixture::new();
    fs::write(f.0.join("a.md"), [255, 254]).unwrap();
    failed(&f.run(&["read", "a.md"]), "a.md");
    failed(&f.run(&["map", "bad%ZZ.md"]), "invalid percent encoding");
}

#[test]
fn project_boundary_is_enforced() {
    let f = Fixture::new();
    failed(&f.run(&["read", "../outside.md"]), "escapes project");
    f.write("a.md", "# A\n\n## Dependencies\n[Outside](../outside.md)\n");
    failed(&f.run(&["deps", "a.md"]), "escapes project");
}

#[cfg(unix)]
#[test]
fn symlink_escape_is_rejected_when_opening_but_map_does_not_open_it() {
    let f = Fixture::new();
    let other = Fixture::new();
    other.write("outside.md", "# Outside\n");
    std::os::unix::fs::symlink(other.0.join("outside.md"), f.0.join("link.md")).unwrap();
    f.write("a.md", "# A\n\n## Dependencies\n[Link](link.md)\n");
    success(&f.run(&["map", "a.md"]));
    failed(&f.run(&["read", "link.md"]), "symlink escapes project");
    failed(&f.run(&["deps", "a.md"]), "symlink escapes project");
}

#[test]
fn usage_errors_have_exit_two() {
    let f = Fixture::new();
    for args in [vec![], vec!["unknown"], vec!["read"], vec!["deps"]] {
        assert_eq!(f.run(&args).status.code(), Some(2));
    }
}
