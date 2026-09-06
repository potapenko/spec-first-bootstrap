# Bootstrap Spec Index

- Node type: branch
- Status: Active
- Read when: authority, stability, precedence, or accepted contract deltas matter.
- Do not read when: a selected leaf already supplies the complete pinned authority.
- Maximum size: 100 physical lines.

The Markdown tree starts at [README.md](README.md). This index is a compact
human authority view, not a second routing system.

## Active contracts

| Contract | Authority | Stability | Revision | Read when |
| --- | --- | --- | --- | --- |
| [Bootstrap governance](features/bootstrap-governance.md) | Active | Accepted | `bootstrap.governance@16` | Setup, governance, Markdown routing, prompts, templates, scope, minimum-sufficient work, goal continuity, or review |
| [Legacy spec migration](features/legacy-spec-migration.md) | Active | Accepted | `bootstrap.legacy-spec-migration@2` | Migrating a large existing spec library |
| [Codex lifecycle](features/codex-lifecycle-enforcement.md) | Active | Evolving | `bootstrap.codex-lifecycle@3` | Optional Codex lifecycle adapter |

## Precedence

- Bootstrap governance controls portable installation and Markdown-node rules.
- Legacy migration is more specific for corpus conversion and depends on the
  governance routing and scope clauses.
- Codex lifecycle is more specific only for optional Codex hook mechanics.
- Persistent-goal and browser-QA layers remain independently selectable.

## Accepted deltas

- [Strict predecision lifecycle](deltas/2026-08-09-strict-predecision-lifecycle.md)
- [Outcome/resource proportionality](deltas/2026-08-10-outcome-resource-proportionality.md)
- [Plan-first scope control](deltas/2026-08-11-plan-first-scope-control.md)
- [Universal work guards](deltas/2026-08-14-universal-work-guards.md)
- [Task-owned worktree state](deltas/2026-08-18-task-owned-worktree-state.md)
- [Superseded JSON routing change](deltas/2026-08-18-hierarchical-spec-routing.md)
- [Superseded JSON migration change](deltas/2026-08-18-legacy-spec-migration.md)
- [Markdown-first correction](deltas/2026-08-18-markdown-first-routing.md)
- [Current-branch checkpoint policy](deltas/2026-08-19-current-branch-checkpoint-policy.md)
- [Local checkpoint commits](deltas/2026-08-19-local-checkpoint-commits.md)
- [Planning deliverables and explicit waiver](deltas/2026-08-20-planning-deliverables-and-waiver.md)
- [Checkpoint commit and push](deltas/2026-08-24-checkpoint-commit-and-push.md)
- [Plan authority modes and semantic boundaries](deltas/2026-08-26-plan-authority-modes.md)
- [Independent outcome review](deltas/2026-08-31-independent-outcome-review.md)
- [Persistent goal continuity](deltas/2026-09-02-persistent-goal-continuity.md)
- [Minimum-sufficient work](deltas/2026-09-02-minimum-sufficient-work.md)

- [Workflow compatibility and local overrides](deltas/2026-09-06-workflow-compatibility.md)

## Unknown precedence

None.
