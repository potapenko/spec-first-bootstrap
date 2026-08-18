# Bootstrap Spec Index

This index governs the observable installation and enforcement behavior of the
Bootstrap itself. Templates under `templates/` and the Favorites example are
reference material, not Active contracts.

## Selection and precedence

1. Read this index before changing Bootstrap setup behavior, governance,
   prompts, adapters, or verification artifacts.
2. Read every Active contract and directly linked document named for the
   affected domain before inspecting implementation evidence.
3. Draft, Superseded, and Historical contracts are evidence only.
4. A more specific contract wins only when this index or the contracts state
   explicit precedence.
5. Stop the affected slice when Active contracts conflict without precedence.

## Contracts

| Contract | Domain | Authority | Stability | Revision | Read when | Precedence | Baseline |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [`features/bootstrap-governance.md`](features/bootstrap-governance.md) | `bootstrap.governance` | Active | Accepted | `bootstrap.governance@5` | Changing setup scope, governance, prompts, templates, layer composition, task-scope control, Git work boundaries, or outcome/resource proportionality | Governs all Bootstrap installation surfaces | `ba891245af7ffa6ffa5463f85af8045b3f6bc75c` |
| [`features/codex-lifecycle-enforcement.md`](features/codex-lifecycle-enforcement.md) | `bootstrap.codex-lifecycle` | Active | Evolving | `bootstrap.codex-lifecycle@1` | Changing the optional Codex lifecycle adapter, its prompts, or tests | More specific than `bootstrap.governance` only for Codex hook mechanics | None |

## Required reading graph

| Domain | Complete governing set |
| --- | --- |
| `bootstrap.governance` | `AGENTS.md`; `docs/spec-first-workflow.md`; `docs/agent-governance/product-truth-governance.md`; `docs/agent-governance/agents-sections.md`; affected setup or work prompts; affected templates |
| `bootstrap.codex-lifecycle` | `features/codex-lifecycle-enforcement.md`; `integrations/codex-lifecycle/README.md`; hook templates; lifecycle script; fixture tests; applicable setup prompts |

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

## Unknown precedence

None.
