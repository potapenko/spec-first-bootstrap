# Agent Setup Sources

The repository-root `README.md` is the human entrypoint. Installer agents use
these portable sources for three independently selectable layers: product
specifications, agent work, and optional browser QA. Each can be installed in
one named project or the explicitly selected global configuration.

## Agent-work owners

- [Work governance](work-governance.md) routes to the shared definitions for
  task framing, scope/checkpoints, minimum-sufficient work, and goal execution.
- [Root orchestration](root-orchestration.md) owns the detailed coordinator
  packet, ownership, review, and registry protocol only for coordinated goals.
- [Compact sections](agents-sections.md) provide instruction-chain gates.
  Adapt paths at installation; do not duplicate the full shared definitions.

## Other independent layers

- [Product truth](product-truth-governance.md) routes to the selected contract
  authority, evidence, and acceptance rules.
- [Browser QA](web-qa-governance.md) is optional.
- The [Codex lifecycle adapter](../../integrations/codex-lifecycle/) is optional
  and must not be installed or changed without its own explicit scope.

## Installation invariants

Detect the active instruction mechanism and resolve overrides and size limits.
Read before merging. Project setup touches only that project; global setup
changes no project. Preserve safety, framework, product, build, data, Git,
release, and operator rules. Never replace the whole target instruction file.

Install the complete linked work tree and conditionally loaded coordinator
contract. Preserve explicit local overrides with their owner and scope. Global
checkpoint default is local commit; automatic push is project opt-in. This
Bootstrap repository retains commit and push. Never publish unrelated commits.

Honor user authorization across follow-ups and skills without weakening the
first substantive planning gate or protected scope. Select and retain goal
execution mode from the work; only coordinated mode restricts the root to
coordination. Required independent review remains required in either mode.

Continue ready work across resource waits, preserve exact resume conditions,
and follow mandatory host impasse transitions. A blocked goal is incomplete.

Do not change model, reasoning, permissions, providers, concurrency, plugins,
product code, or goal state during installation. Do not launch workers merely
to install documents. Do not copy project-specific rules into global defaults
or reinstall a full global layer locally without explicit duplication scope.

Verify active routing, links, node sizes, preserved overrides, installed
scenario behavior, and changed-file boundaries. The setup prompts in `prompts/`
are the executable installation instructions for the selected scope.
