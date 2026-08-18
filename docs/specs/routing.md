# Markdown-First Specification Routing

- Node type: leaf
- Status: Active
- Revision: `bootstrap.markdown-routing@1`
- Read when: authoring, installing, reviewing, or repairing the specification tree.
- Do not read when: the selected task already has a complete node path and does not alter routing.
- Maximum size: 100 physical lines.

## Node model

Every node is a Markdown file with ordinary Markdown links. A node declares:

- `Node type: root | branch | leaf | hybrid`;
- `Status`, `Read when`, and `Do not read when`;
- `Maximum size: 100 physical lines`;
- child links when it is a branch;
- dependency links when another contract is required.

A hybrid node contains both local normative rules and child links. Branch
summaries are navigation only and never define child behavior.

## Traversal

1. Start at the root `README.md`.
2. Read child descriptions in the current node.
3. Open only the matching Markdown link.
4. Continue until the smallest governing leaf or hybrid node is reached.
5. Open only dependencies explicitly linked by selected nodes.
6. Record the ordered Markdown path, selected revisions, dependencies, and
   excluded siblings in the Spec Basis.

Completeness means the selected Markdown path plus explicit dependencies, not
every file below the specification root.

## Size rule

One node may contain at most 100 physical lines, including blank lines.
Target 50–80 lines; keep pure branch nodes closer to 50. Split at stable
responsibility boundaries. Never solve overflow by shrinking prose until rules
become ambiguous or by moving product meaning into branch summaries.

## Technical checks

A checker may verify links, reachability, duplicates, cycles, and line limits.
It is optional implementation support: agents do not read its private state,
and its format is not part of specification authority.

## Failure policy

Stop the affected traversal when a link is broken, two Active nodes conflict
without precedence, a dependency is ambiguous, or a selected node exceeds 100
lines. Record missing authority and use Discover rather than reading the
repository broadly.
