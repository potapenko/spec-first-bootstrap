# Bootstrap Spec Index

This human-readable index summarizes the observable Bootstrap contracts. The
machine-readable authority and traversal root is [`route.json`](route.json).
Templates and examples are reference material, not Active contracts.

## Selection and precedence

1. Start at `route.json` before changing Bootstrap setup behavior, governance,
   prompts, adapters, or verification artifacts.
2. Select the smallest applicable nodes and resolve their explicit dependency
   closure before inspecting implementation evidence.
3. Draft, Superseded, and Historical contracts are evidence only.
4. A more specific contract wins only when this index or the contracts state
   explicit precedence.
5. Stop the affected slice when Active contracts conflict without precedence.

## Contracts

| Contract | Domain | Authority | Stability | Revision | Read when | Precedence | Baseline |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [`features/bootstrap-governance.md`](features/bootstrap-governance.md) | `bootstrap.governance` | Active | Accepted | `bootstrap.governance@6` | Changing setup scope, governance, routing, prompts, templates, layer composition, task-scope control, Git work boundaries, or outcome/resource proportionality | Governs all portable Bootstrap installation surfaces | `ba891245af7ffa6ffa5463f85af8045b3f6bc75c` |
| [`features/legacy-spec-migration.md`](features/legacy-spec-migration.md) | `bootstrap.legacy-spec-migration` | Active | Accepted | `bootstrap.legacy-spec-migration@1` | Migrating a large existing flat or inconsistently structured specification library | Depends on `BOOTSTRAP.ROUTING` and `BOOTSTRAP.SCOPE`; more specific for corpus migration | None |
| [`features/codex-lifecycle-enforcement.md`](features/codex-lifecycle-enforcement.md) | `bootstrap.codex-lifecycle` | Active | Evolving | `bootstrap.codex-lifecycle@2` | Changing the optional Codex lifecycle adapter, routed restart context, prompts, or tests | More specific than `bootstrap.governance` only for Codex hook mechanics | None |

## Resolved closure support

| Domain | Routed supporting leaves |
| --- | --- |
| `bootstrap.governance` | Route profile `bootstrap-governance`; routed product-truth profile matching the task; affected setup/work prompt and template leaves |
| `bootstrap.legacy-spec-migration` | Route profile `legacy-spec-migration`; migration prompt, routing guide, inventory and batch coverage artifacts |
| `bootstrap.codex-lifecycle` | Route profile `codex-lifecycle`; lifecycle README, hook templates, script, fixture tests, and applicable setup prompt |

## Shared dependencies

- Persistent-goal coordination is independently selectable. Product-truth
  packet fields apply only when product behavior or another protected contract
  is in scope.
- Browser QA is independently selectable and must remain optional.
- The Codex lifecycle adapter reinforces installed instruction layers but does
  not install or silently require any of them.

## Accepted Contract Deltas

- [`deltas/2026-08-09-strict-predecision-lifecycle.md`](deltas/2026-08-09-strict-predecision-lifecycle.md)
- [`deltas/2026-08-10-outcome-resource-proportionality.md`](deltas/2026-08-10-outcome-resource-proportionality.md)
- [`deltas/2026-08-11-plan-first-scope-control.md`](deltas/2026-08-11-plan-first-scope-control.md)
- [`deltas/2026-08-14-universal-work-guards.md`](deltas/2026-08-14-universal-work-guards.md)
- [`deltas/2026-08-18-task-owned-worktree-state.md`](deltas/2026-08-18-task-owned-worktree-state.md)
- [`deltas/2026-08-18-hierarchical-spec-routing.md`](deltas/2026-08-18-hierarchical-spec-routing.md)
- [`deltas/2026-08-18-legacy-spec-migration.md`](deltas/2026-08-18-legacy-spec-migration.md)

## Unknown precedence

None.
