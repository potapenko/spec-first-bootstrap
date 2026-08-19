# Contract Delta: Current-Branch Checkpoint Policy

- Change ID: `bootstrap.delta.2026-08-19.current-branch-checkpoint-policy`
- Change mode: Evolve
- Authorized by: explicit user request and plan approval on 2026-08-19
- Domain and clause IDs: `bootstrap.governance`, `BOOTSTRAP.SCOPE`
- Previous behavior: project migration prompts could name a branch or treat
  missing remote tracking as a user-facing checkpoint blocker.
- New behavior: commit and push task-owned changes from the currently checked-out
  branch, configuring remote tracking for that branch automatically when needed.
- Evidence basis: Bootstrap migration prompts, compact agent sections, structural
  validation, and the explicit user decision in the current task.
- Compatibility classification: workflow clarification limited to Git checkpoint
  routing. Foreign commits, task-owned staging, and current-branch protection
  remain unchanged.
- Adjacent domains checked: task planning, worktree ownership, project/global
  installation, migration prompts, and checkpoint validation.
- QA impact: migration-prompt tests reject fixed branch names and tracking
  blockers; structural validation pins the revised governance contract.
- Specification paths changed: `docs/specs/index.md`;
  `docs/specs/features/bootstrap-governance.md`;
  `docs/specs/features/bootstrap-governance/task-and-scope.md`; this delta.
- Required review: focused self-review and repository structural checks.
- New revisions: `bootstrap.governance@8`,
  `bootstrap.governance.task-scope@2`.

## Discrepancy disposition

- Classification: authorized evolution.
- Resolution: remove branch-specific and tracking-blocker language from portable
  prompts and make automatic tracking part of the current-branch contract.
