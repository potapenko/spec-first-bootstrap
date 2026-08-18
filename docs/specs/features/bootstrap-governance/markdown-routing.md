# Markdown-First Routing Contract

- Node type: leaf
- Contract: `bootstrap.governance.markdown-routing@1`
- Clause: `BOOTSTRAP.ROUTING`
- Read when: installing, traversing, authoring, or validating specification nodes.
- Do not read when: the current task has a recorded complete Markdown path and does not change routing.
- Maximum size: 100 physical lines.

## Required behavior

- The specification entrypoint is a Markdown root document.
- Every branch describes children briefly and links with ordinary Markdown.
- Agents read one node, choose one matching child, and continue by link.
- Leaf and branch are roles; one Markdown file may be a hybrid.
- Branch summaries navigate and never define child product behavior.
- Selected nodes link explicit dependencies required for their meaning.
- Completeness is the selected path plus dependencies, not every sibling.
- The traversal receipt records Markdown paths, revisions, dependencies,
  excluded siblings, and approximate resolved size.
- No JSON manifest, resolver, generated registry, or tool output is authority
  or a required input to traversal.

## Size boundary

Every node declares `Node type` and contains at most 100 physical lines,
including blanks. Target 50–80 lines; keep routing-only branches near 50.
Oversized nodes are split by independently selectable responsibility.

## Technical support

Optional tools may check Markdown links, reachability, cycles, duplicates, and
line counts. Agents must be able to traverse correctly without reading tool
state or understanding its implementation.

## Failure policy

A broken link, ambiguous child, missing dependency, duplicate responsibility,
or oversized selected node blocks only the affected path. Record the gap and
repair the Markdown tree; do not compensate by reading the whole corpus.
