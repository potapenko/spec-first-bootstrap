# Contract Delta: Checkpoint Commit and Push

- Change ID: `bootstrap.delta.2026-08-24.checkpoint-commit-and-push`
- Change mode: Evolve
- Authorized by: explicit user direction and approved implementation plan on
  2026-08-24
- Domain and clause IDs: `bootstrap.governance`, `BOOTSTRAP.SCOPE`
- Previous behavior: a successful local checkpoint commit completed file-changing
  work without requiring a push.
- New behavior: a checkpoint requires both a task-owned commit and its push from
  the currently checked-out branch. Before committing, the agent verifies a safe,
  writable upstream and that the push will not publish unrelated local commits.
  If either condition is not established, the agent does not create the commit.
  Completion requires both commit and push to succeed.
- Evidence basis: explicit user direction that checkpoint commits must always be
  pushed and must not be created when a safe push is unavailable.
- Compatibility classification: authorized workflow evolution superseding the
  local-only checkpoint behavior.
- Adjacent domains checked: current-branch discipline, task-owned staging,
  portable setup, migration prompts, and checkpoint validation.
- QA impact: structural checks require commit-and-push completion and safe-push
  preflight language on active surfaces.
- Specification paths changed: `docs/specs/index.md`;
  `docs/specs/features/bootstrap-governance.md`;
  `docs/specs/features/bootstrap-governance/task-and-scope.md`; this delta.
- Required review: focused self-review and repository structural checks.
- New revisions: `bootstrap.governance@11`,
  `bootstrap.governance.task-scope@5`.

## Discrepancy disposition

- Classification: authorized product evolution.
- Resolution: supersede local-only checkpoint completion while preserving the
  current-branch, task-owned-file, and unrelated-change protections.
