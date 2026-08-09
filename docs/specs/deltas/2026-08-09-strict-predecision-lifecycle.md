# Contract Delta: Strict Pre-Decision And Lifecycle Enforcement

- Change ID: `bootstrap.delta.2026-08-09.predecision-lifecycle`
- Change mode: Evolve
- Authorized by: explicit user approval on 2026-08-09
- Domain and clause IDs: `bootstrap.governance`;
  `bootstrap.codex-lifecycle`
- Previous behavior: Bootstrap required specification reconciliation before
  implementation, but several compact and setup surfaces did not explicitly
  block project conclusions, source inspection, runtime interpretation, or
  non-reading task actions before a visible Spec Basis. Restart guidance lived
  only in conditional full governance and no portable Codex hook adapter was
  provided.
- New behavior: the specification gate is a mandatory pre-decision gate; the
  agent names complete governing documents and separates specified expectation,
  protected behavior, established flow, and evidence still needed before
  implementation evidence. Lifecycle restart is represented in compact
  routing, and an optional Codex adapter provides distinct root and worker
  context with setup, trust, deduplication, and fixture-test contracts.
- Evidence basis: current global Codex instruction and governance behavior;
  official Codex AGENTS.md and hooks documentation; Bootstrap baseline
  `ba891245af7ffa6ffa5463f85af8045b3f6bc75c`.
- Compatibility classification: additive workflow hardening; no target-product
  behavior change; existing three-layer independence preserved.
- Adjacent domains checked: persistent-goal agents; optional browser QA;
  project/global scope; model and application defaults.
- QA and design impact: documentation validator, JSON checks, and lifecycle
  fixtures added; no visual design impact.
- Specification paths changed: `docs/specs/index.md`;
  `docs/specs/features/bootstrap-governance.md`;
  `docs/specs/features/codex-lifecycle-enforcement.md`.
- Independent review: separate multi-agent review was not requested for this
  single-agent change; repository-wide contract/diff self-review and automated
  structural checks are required, with an independent review recommended
  before release.
- New contract revision or epoch: `bootstrap.governance@1`;
  `bootstrap.codex-lifecycle@1`.

## Discrepancy disposition

- Classification: authorized evolution
- Resolution: synchronize portable doctrine without copying environment-
  specific model names or making governance layers depend on the adapter.
- Exact residual: release baseline remains unchanged until a release is made.
