# Spec Nav CLI

- Node type: leaf
- Status: Active
- Contract ID: `bootstrap.spec-nav`
- Domain ID: `bootstrap.spec-nav`
- Authority: Active
- Stability: Evolving
- Contract revision: `bootstrap.spec-nav@1`
- Read when: using, implementing, or verifying the optional Rust spec navigator.
- Do not read when: ordinary Markdown traversal already suffices.
- Maximum size: 100 physical lines.

## Goal and scope

Provide read-only navigation over current project Markdown without making a
CLI, generated map, or index a source of product authority. The approved first
version has map, read, deps, tests, and current-tree checks; no agent trials.
Run from the project root. Paths identify documents; no generated IDs exist.

## Commands

- `NAV.MAP`: `spec-nav map [node]` defaults to `docs/specs/README.md`.
  Read only that file. Show title, declared type/status/revision, selection
  conditions, and links grouped by their original sections. Each link includes
  its label, original containing item/paragraph/table row, resolved destination,
  and source line. Do not open targets or invent summaries or child roles.
  Missing metadata is explicitly not declared. A map is not full contract text.
- `NAV.READ`: `spec-nav read <node>` writes the entire original UTF-8 Markdown
  to stdout byte-for-byte, without a header, rewriting, or truncation.
  A fragment validates the heading but still returns the entire document.
- `NAV.DEPS`: `spec-nav deps <node>` follows Markdown links only under level-two
  Dependency/Dependencies headings (case-insensitive, allowing a heading suffix),
  including their subsections until the next level-one/two heading. Traverse
  transitively in source order, list each canonical document once, preserve all
  incoming reasons, fragments, source sections/lines and declared revisions.
  Do not print dependency bodies or follow ordinary navigation links.

## Interpretation and failure

- `NAV.SOURCE`: support inline/reference links, table links, relative paths,
  percent-encoded paths/fragments, and duplicate heading anchors. Code examples
  and image destinations are not navigation links. Unresolved reference links
  are diagnosed rather than silently omitted.
- Resolve links against their source file, command arguments against the project
  root. Normalize paths without opening map targets. On opening, canonicalize
  and reject paths or symlinks escaping the project. Only Markdown is opened.
- Read current files on each invocation; no persistent cache or atomic snapshot
  across invocations is promised. Within deps, reuse each loaded document.
- Remote links are displayed but never fetched. A remote or non-Markdown
  dependency makes the closure incomplete. No declared dependencies means only
  that none were found mechanically, not that no semantic dependencies exist.
- `NAV.ERROR`: missing files, invalid UTF-8, broken fragments, unresolved
  dependency references, cycles and unsupported dependencies yield incomplete
  deps output, source-linked stderr diagnostics and exit 1. Continue independent
  edges; never label a partial closure complete. Missing root also yields an
  incomplete report. Map diagnoses unresolved references with exit 1.
- Map/deps reject declared nodes over 100 physical lines; read remains available
  to inspect the complete source. Other structural validation remains with the
  existing Python checker. Map does not validate unopened targets.
- Exit codes: 0 completed, 1 document/traversal error, 2 CLI usage error.
  Normal reports go to stdout; errors go to stderr. Output order is stable.

## Protected behavior and non-goals

No writes, network requests, semantic search, LLM, code analysis, automatic
contract selection, installers, MCP, watcher, persistent index or cache.
Existing governance, node format and Python validator remain unchanged.
Summaries never replace mandatory reading of selected contracts and dependencies.

## Dependencies

- [Markdown routing](../routing.md) — node limits and source authority.
- [Bootstrap routing](bootstrap-governance/markdown-routing.md) — optional tools.

## Verification mapping

[CLI cases and evaluation protocol](../../../qa/spec-nav.md) map these clauses
to executable tests and current-tree checks. Agent efficiency remains unmeasured
until a separately authorized controlled pilot is run.
