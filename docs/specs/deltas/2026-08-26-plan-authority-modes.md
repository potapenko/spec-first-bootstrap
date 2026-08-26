# Contract Delta: Plan Authority Modes And Semantic Boundaries

- Change ID: `bootstrap.delta.2026-08-26.plan-authority-modes`
- Change mode: Evolve
- Authorized by: explicit user approval on 2026-08-26
- Domain and clause IDs: `bootstrap.governance`; `BOOTSTRAP.SCOPE`
- Previous behavior: required plans declared task-owned paths and treated the
  approved plan as the execution boundary, but did not distinguish tightly
  bounded mature-product work from task-wide greenfield work. File permission
  also did not explicitly protect unrelated behavior inside the same file.
- New behavior: every approved implementation plan declares `bounded` or
  `task-wide` authority. Bounded work is allowlisted; task-wide work may change
  any repository file necessary for the approved outcome. In both modes,
  explicit protections and accepted behavior outside the outcome remain
  protected, and every diff hunk must map to authorized behavior. Permission
  for a container or parent never silently opens its content or descendants.
- Evidence basis: explicit reports of agents rewriting accepted child UI while
  fixing a container; the current compact agent sections, installer prompts,
  worker packet contract, structural validator, and green baseline checks.
- Compatibility classification: additive workflow evolution. Existing product,
  specification, browser-QA, lifecycle, provider, and release behavior remain
  unchanged.
- Adjacent domains checked: current-branch worktree ownership, persistent-goal
  worker concurrency, product-truth semantic authority, installer scope, and
  instruction-size limits.
- QA impact: structural validation pins both authority modes, default-bounded
  behavior, semantic boundaries, mirrored project/global sections, and updated
  contract revisions.
- Specification paths changed: `docs/specs/index.md`;
  `docs/specs/features/bootstrap-governance.md`;
  `docs/specs/features/bootstrap-governance/task-and-scope.md`; this delta.
- Independent review: focused diff review and full Bootstrap checks are
  proportional for this governance-only change.
- New contract revisions: `bootstrap.governance@12`;
  `bootstrap.governance.task-scope@6`.

## Policy choices

- `bounded` is the fail-closed default when a plan omits its mode.
- `task-wide` removes path-by-path permission friction but remains bounded by
  the approved outcome and explicit protections.
- Writable paths grant filesystem authority, not blanket semantic authority.
- Existing accepted behavior outside the outcome is protected in both modes;
  greenfield work has no fictional legacy baseline to preserve.
- Parent or container permission does not open child content, layout, actions,
  state, or data unless the plan explicitly says so.
- A protected dependency is reported with evidence and a minimal amendment; it
  is not changed as a workaround.
- Writable task-wide worker packets serialize against other writable packets
  unless narrower disjoint ownership is explicitly established.

## Discrepancy disposition

- Classification: authorized product evolution.
- Resolution: update the canonical contracts, installed compact sections,
  worker packet rules, installer prompts, documentation, and validator.
- Residual: this is instruction and structural enforcement; target projects may
  add stronger diff tooling when their build systems expose stable boundaries.
