# Contract Delta: Task-Owned Worktree State

- Change ID: `bootstrap.delta.2026-08-18.task-owned-worktree-state`
- Change mode: Evolve
- Authorized by: explicit user request and plan approval on 2026-08-18
- Domain and clause IDs: `bootstrap.governance`
- Previous behavior: Bootstrap treated any dirty or diverged working tree as a
  pre-implementation blocker, even when every existing change was outside the
  files needed by the approved task.
- New behavior: when a plan is required, it declares the task-owned write set
  before editing. Existing staged, unstaged, or untracked changes block only
  when their paths overlap that write set. Non-overlapping changes remain
  untouched and are excluded from task staging and commits. Agents remain on
  the operator-selected branch and may not create or switch branches or
  worktrees to bypass an actual overlap.
- Evidence basis: the user-authorized task-owned worktree policy recorded in
  the active global agent instructions and their 2026-08-17 Git history;
  Bootstrap revision `bootstrap.governance@4`; explicit user direction to
  transfer the universal rule without project-specific automation exceptions.
- Compatibility classification: scoped workflow evolution. The current-branch
  integration boundary remains unchanged; only the repository-wide dirty-state
  eligibility gate becomes path-scoped.
- Adjacent domains checked: task planning and approved scope; scoped staging and
  commits; current-branch enforcement; setup scope; optional lifecycle adapter.
- QA and design impact: structural validation gains task-owned write-set,
  overlapping-change, and unrelated-change-preservation checks. No visual
  design or target-product behavior changes.
- Specification paths changed: `docs/specs/index.md`;
  `docs/specs/features/bootstrap-governance.md`; this delta.
- Independent review: focused self-review and repository structural checks are
  proportional for this documentation-first governance change.
- New contract revision or epoch: `bootstrap.governance@5`

## Policy choices

- A required implementation plan names the files the task expects to edit.
- Dirty state outside that file set is context, not a preflight blocker.
- An overlap is a real ownership conflict and blocks editing of the affected
  paths until it is resolved without discarding or absorbing foreign changes.
- Task staging and commits contain only explicitly identified task-owned files.
- Branch creation, switching, renaming, publishing, and worktree creation still
  require explicit user direction.
- Project-specific automation exceptions remain outside the portable core.

## Discrepancy disposition

- Classification: authorized evolution
- Resolution: replace the blanket dirty-worktree blocker across the active
  contract, compact project and global sections, setup prompts, and structural
  validation while preserving current-branch discipline.
- Exact residual: the release baseline remains
  `ba891245af7ffa6ffa5463f85af8045b3f6bc75c` until a release is made.
