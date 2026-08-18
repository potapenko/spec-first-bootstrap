# Bootstrap Specification Tree

- Node type: root
- Status: Active
- Read when: any task may affect Bootstrap behavior, setup, governance, migration, or lifecycle integration.
- Do not read when: using a copied template as a non-authoritative example.
- Maximum size: 100 physical lines.

This Markdown file is the only required entrypoint. Follow ordinary Markdown
links one node at a time. Do not scan sibling directories or load every linked
document in advance.

## Choose the next node

- [Bootstrap contracts](features/README.md) — choose installation/governance,
  legacy-library migration, or optional Codex lifecycle behavior.
- [Markdown routing contract](routing.md) — read when changing the node
  protocol, traversal rules, link semantics, or size limit.
- [Human authority index](index.md) — read when authority, stability,
  precedence, or accepted deltas matter.
- [Specification templates](templates/README.md) — read only when authoring or
  installing nodes.
- [Legacy migration operating guide](legacy-migration-routing.md) — read when
  planning or resuming bounded conversion of a large existing spec library.

## Traversal contract

1. Read this root node.
2. Match the task to one child description.
3. Open only that linked Markdown node.
4. Repeat until the selected leaf or hybrid node fully governs the task.
5. Follow dependency links declared by the selected node.
6. Record the Markdown path and selected contract revisions in the Spec Basis.
7. Do not read unselected siblings.

A branch summary is navigation only. Product meaning lives in the selected
contract nodes. A file may be a branch, leaf, or hybrid.

## Size contract

Every Markdown node declares `Node type` and must contain at most 100 physical
lines. Authors should target 50–80 lines and keep routing-only branches closer
to 50. Split an oversized node by independently selectable responsibility;
never raise the limit to preserve an oversized document.

Templates, historical deltas, raw evidence, generated reports, and ordinary
non-node documentation are not nodes unless they declare `Node type`.

## Authority and evidence

Active contract nodes define intended behavior but cannot authorize their own
semantic changes. Source, tests, runtime, screenshots, history, and release
records remain evidence. Establish the selected Spec Basis before using those
layers to decide product behavior.

Product maps and backlogs are discovery aids, not behavior contracts.
