# Contract Delta: Outcome And Resource Proportionality

- Change ID: `bootstrap.delta.2026-08-10.outcome-resource-proportionality`
- Change mode: Evolve
- Authorized by: explicit user request on 2026-08-10
- Domain and clause IDs: `bootstrap.governance`
- Previous behavior: persistent-goal governance prioritized correctness,
  architecture, context preservation, and independent review, but did not make
  release-path capability the primary progress measure or bound consecutive
  preparation, diagnostics, tooling, and repair/re-review cycles.
- New behavior: implementation progress is reported by concrete user capability
  reachable from the product or release path. Supporting work has an explicit
  next consumer, default planning budget, durable classification, and economic
  stop conditions. The first one or two implementation checkpoints target a
  release-reachable vertical slice. Review and verification remain proportional
  to demonstrated risk, with stronger independent review and safety gates for
  high-risk boundaries. Residuals cannot hide failed acceptance or missing
  claimed capability.
- Evidence basis: accepted global Codex `AGENTS.md` and root-orchestration
  working-tree direction; repository agent governance, setup prompts, compact
  instruction sections, and structural validator; explicit user confirmation
  to transfer the doctrine and make the concrete policy choices in this delta.
- Compatibility classification: additive workflow evolution. Existing project
  scope, layer independence, model neutrality, lifecycle behavior, browser QA,
  and product code remain unchanged.
- Adjacent domains checked: product-truth governance; Codex lifecycle adapter;
  optional browser QA; project/global installation scope; model and provider
  configuration.
- QA and design impact: structural validation gains outcome/economic consistency
  checks. No visual design or target-product behavior changes.
- Specification paths changed: `docs/specs/index.md`;
  `docs/specs/features/bootstrap-governance.md`; this delta.
- Independent review: risk-proportional self-review is sufficient for this
  documentation-only bootstrap evolution; independent review remains required
  for the high-risk classes named by the portable root contract and is
  recommended before a release baseline is advanced.
- New contract revision or epoch: `bootstrap.governance@2`

## Policy choices

- Default planning mix: 60% shipping implementation, 25% verification/review/
  QA, and 15% discovery/diagnostics/tooling/coordination. The values sum to
  100% and may move when demonstrated risk requires it.
- Economic depth is counted by implementation checkpoint or integration wave,
  not by raw parallel packet count.
- Low-risk shipping work receives proportional review that may be focused
  self-review. Independent review is mandatory for user-data ownership or
  deletion, privacy or security, permissions, irreversible actions, shared
  released owners, compatibility, persistence, and complex concurrency, or
  when another governing contract requires it.
- Portable governance remains conditional on installed layers and uses no
  environment-specific model names.

## Discrepancy disposition

- Classification: authorized evolution
- Resolution: transfer the outcome-first economic doctrine into the portable
  Bootstrap while correcting review-pipeline, percentage, checkpoint-counting,
  residual, and layer-independence ambiguities before implementation.
- Exact residual: release baseline remains
  `ba891245af7ffa6ffa5463f85af8045b3f6bc75c` until a release is made.
