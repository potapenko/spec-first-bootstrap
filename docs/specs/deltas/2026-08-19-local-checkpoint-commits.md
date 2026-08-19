# Contract Delta: Local Checkpoint Commits

- Change ID: `bootstrap.delta.2026-08-19.local-checkpoint-commits`
- Change mode: Evolve
- Authorized by: explicit user direction and approved implementation plan on
  2026-08-19
- Domain and clause IDs: `bootstrap.governance`, `BOOTSTRAP.SCOPE`
- Previous behavior: checkpoint completion was coupled to commit, push, and
  remote-tracking setup.
- New behavior: work that changes files ends with a local checkpoint commit in
  the currently checked-out branch. The agent commits only the files it changed
  for the task. Unrelated working-tree changes remain untouched and do not block
  the checkpoint. Completion requires the checkpoint commit to succeed.
- Evidence basis: explicit user clarification that a checkpoint is a local save
  of the agent's own completed work, plus the existing task-owned worktree rule.
- Compatibility classification: workflow correction removing remote state from
  checkpoint semantics while preserving current-branch and scoped-file rules.
- Adjacent domains checked: task planning, worktree ownership, portable setup,
  migration prompts, and checkpoint validation.
- QA impact: structural checks require the local-save directive and reject
  commit/push or remote-tracking checkpoint language on active surfaces.
- Specification paths changed: `docs/specs/index.md`;
  `docs/specs/features/bootstrap-governance.md`;
  `docs/specs/features/bootstrap-governance/task-and-scope.md`; this delta.
- Required review: focused self-review and repository structural checks.
- New revisions: `bootstrap.governance@9`,
  `bootstrap.governance.task-scope@3`.

## Discrepancy disposition

- Classification: authorized evolution correcting an over-broad checkpoint
  interpretation.
- Resolution: define checkpoint completion as a local commit of the agent's own
  task files and remove push, remote, upstream, and tracking requirements from
  checkpoint instructions and validation.
