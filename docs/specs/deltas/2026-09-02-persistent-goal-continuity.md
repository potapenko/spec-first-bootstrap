# Contract Delta: Persistent Goal Continuity

- Change ID: `bootstrap.delta.2026-09-02.persistent-goal-continuity`
- Change mode: Evolve
- Authorized by: explicit user request and approval on 2026-09-02
- Domain and clauses: `bootstrap.governance`; `BOOTSTRAP.GOAL.*`;
  `BOOTSTRAP.PROPORTIONALITY`
- Previous behavior: packets could report `blocked`, goal governance left
  goal-level blocking available after repeated inability to progress, resource
  waits had no required revisit cadence, and economic thresholds could pause an
  approved goal while dependency-ready plan work remained.
- New behavior: local governance keeps persistent goals active until verified
  completion or user pause/clear, schedules any dependency-ready plan item
  regardless of list order, models temporary contention as a waiting item,
  rechecks resources every three minutes without a fixed attempt ceiling, and
  treats economic thresholds as nonblocking routing reassessments for approved
  plan work.
- Evidence basis: explicit user report of overnight goals stopping early;
  current Bootstrap and installed agent-work governance; OpenAI Goal mode and
  configuration documentation; active Codex goal-tool contract.
- Compatibility: behavioral governance evolution. Safety, destructive-action,
  product-authority, scope, branch, checkpoint, review, and per-call external
  timeout rules remain protected.
- Adjacent domains checked: product-truth governance, optional lifecycle hooks,
  browser QA, model/provider settings, concurrency, and operator safety.
- Specification paths: `features/bootstrap-governance.md`,
  `features/bootstrap-governance/goal-continuity.md`,
  `features/bootstrap-governance/installation.md`,
  `features/bootstrap-governance/restart-and-delivery.md`, `index.md`, this delta.
- QA: structural validator plus goal-continuity scenarios for independent work,
  repeated contention, failure recovery, evidence waits, authority waits, user
  pause, and verified completion.
- New revisions: `bootstrap.governance@14`;
  `bootstrap.governance.goal-continuity@1`;
  `bootstrap.governance.restart-delivery@2`;
  `bootstrap.governance.review@2`.
- Residual: local instructions cannot remove host-owned goal states or add an
  undocumented Codex configuration key. They prevent voluntary local blocking
  whenever approved work or a meaningful wait/retry path exists.
