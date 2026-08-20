# Contract Delta: Planning Deliverables And Explicit Waiver

- Change ID: `bootstrap.delta.2026-08-20.planning-deliverables-and-waiver`
- Change mode: Reconcile
- Authorized by: explicit user request and plan approval on 2026-08-20
- Domain and clause IDs: `bootstrap.governance`, `BOOTSTRAP.SCOPE`
- Previous behavior: the accepted plan-first delta allowed explicit direction
  to execute now or without a plan, and the universal-work-guards delta barred
  approval requests for planning whose result would merely be another plan.
  Later compact instruction wording no longer preserved the first exception
  and did not state clearly that a requested plan file is itself the planning
  deliverable.
- Reconciled behavior: a request whose result is a plan produces or saves that
  plan directly without a meta-plan or planning-approval request. Explicit
  operator direction to execute now or without a plan skips the
  planning-approval gate. Neither case authorizes planned implementation,
  expands scope, or bypasses other applicable gates.
- Evidence basis: accepted deltas
  `bootstrap.delta.2026-08-11.plan-first-scope-control` and
  `bootstrap.delta.2026-08-14.universal-work-guards`; their originating Git
  history; current portable project/global instruction sections; current setup
  prompts; and the active user-level `AGENTS.md`.
- Compatibility classification: additive workflow reconciliation. Planning
  remains the default for ordinary implementation-bearing requests.
- Adjacent domains checked: product-truth gates, persistent-goal coordination,
  approved-scope control, current-branch policy, checkpoint commits, and
  project/global installation boundaries.
- QA impact: structural validation requires both the planning-deliverable rule
  and the explicit no-plan waiver on project, global, and installed surfaces.
- Specification paths changed: `docs/specs/index.md`;
  `docs/specs/features/bootstrap-governance.md`;
  `docs/specs/features/bootstrap-governance/task-and-scope.md`; this delta.
- Required review: focused self-review and repository structural checks.
- New revisions: `bootstrap.governance@10`,
  `bootstrap.governance.task-scope@4`.

## Protected behavior

- A generic imperative does not waive planning.
- Producing a plan does not authorize the implementation described by it.
- Explicit no-plan direction waives only the planning-approval gate.
- Specification, safety, authorization, destructive-action, environment,
  scope, branch, and checkpoint requirements remain active.

## Discrepancy disposition

- Classification: specification omission and installed-instruction regression.
- Resolution: reconcile the contract, portable sections, installer prompts,
  active global instruction file, and validation around the accepted behavior.
- Exact residual: no released Bootstrap baseline is advanced by this change.
