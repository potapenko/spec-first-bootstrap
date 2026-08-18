# Hierarchical Specification Routing

The specification tree separates non-normative routing from normative
contracts. Start at `route.json`, select the smallest applicable node IDs, and
resolve their explicit dependencies. Read the resulting contract closure
completely; do not load sibling branches merely because they share a parent.

## Node model

A node may contain:

- `contract`: normative Markdown, revision, clause IDs, authority, stability,
  baseline, and context budget;
- `children`: routing descriptions and links to child contracts or routes;
- both `contract` and `children`, making it a hybrid leaf/branch;
- `requires`: cross-domain dependency edges with exact clause IDs.
- `resources`: directly required plans, runbooks, handoffs, design, QA,
  evidence, or release leaves with roles, revisions, and context budgets.
- root `profiles`: named, repeatedly used sets of node IDs such as Restore,
  Discover, worker, or restart governance.

`summary`, `read_when`, and `do_not_read_when` exist only to select a route.
They cannot replace contract clauses or create product intent.

## Resolution

Task-to-node selection is a semantic agent decision. Dependency closure and
revision checking are mechanical:

```sh
python3 scripts/spec_route.py validate docs/specs/route.json
python3 scripts/spec_route.py resolve docs/specs/route.json --node <domain-id>
```

The resolver emits a Route Receipt naming manifests, selected contracts,
supporting resources, clauses, revisions, excluded siblings, and resolved
context words. Store the
receipt durably for long-running work and re-resolve it after restart or
compaction to detect revision drift.

## Authoring

- Put product rules only in contracts, never router summaries.
- Give every material rule a stable clause ID.
- Add a child route when one contract develops independently selectable
  responsibilities.
- Add `requires` only for meaning required to decide the selected contract.
- Set honest context budgets and split oversized contracts instead of raising
  budgets automatically.
- Update parent routing and semantic revisions with every accepted structural
  or behavioral change.

The route validator rejects missing paths, duplicate IDs, route or dependency
cycles, unresolved dependencies, invalid authority/stability values, and
budget overflow.
