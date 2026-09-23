# Bootstrap Contract Branch

- Node type: branch
- Status: Active
- Read when: selecting an observable Bootstrap contract.
- Do not read when: the task only consumes templates without changing Bootstrap behavior.
- Maximum size: 100 physical lines.

Choose exactly the smallest matching child. Do not open all contracts.

## Children

- [Bootstrap governance and installation](bootstrap-governance.md) — setup
  scope, Markdown-first routing, task framing, worktree boundaries, restart,
  and delivery proportionality.
- [Legacy specification migration](legacy-spec-migration.md) — converting a
  large existing specification library into bounded Markdown nodes without
  corpus-wide reading.
- [Codex lifecycle](codex-lifecycle-enforcement.md) — optional context reminder,
  legacy entrypoints and explicitly scoped removal of old mandatory hooks.

## Selection rules

The governance contract has precedence for portable setup behavior. Legacy
migration depends on its routing and scope rules. Codex lifecycle retirement
is more specific for the optional reminder, old entrypoints and migration.

For authority status, stability, and accepted deltas, use the
[human authority index](../index.md).
