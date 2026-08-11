# Contract Delta: Plan-First Task Framing And Scope Control

- Change ID: `bootstrap.delta.2026-08-11.plan-first-scope-control`
- Change mode: Evolve
- Authorized by: explicit user request and plan approval on 2026-08-11
- Domain and clause IDs: `bootstrap.governance`
- Previous behavior: Bootstrap constrained product authority, persistent-goal
  packets, and implementation economics, but its ordinary agent layer did not
  require a visible approved plan for new or materially ambiguous tasks and did
  not make that plan the durable execution boundary.
- New behavior: new features, initiatives, and tasks requiring material scope
  judgment pause after a bounded non-mutating planning pass, present an
  execution plan, and wait for explicit user approval. Explicit immediate-
  execution direction, an already approved plan, and obvious bounded low-risk
  tasks that need no material scope judgment may proceed immediately. During
  execution, agents remain inside the approved plan and return material
  out-of-scope dependencies as minimal proposed amendments instead of silently
  adding work.
- Evidence basis: explicit user report that agents have become overly
  proactive; current Bootstrap agent sections and project/global setup prompts;
  current repository and user-level `AGENTS.md` files; green structural
  validation before the change.
- Compatibility classification: additive agent-workflow evolution. Existing
  specification, persistent-goal, browser-QA, lifecycle, model, provider, and
  target-product behavior remain unchanged.
- Adjacent domains checked: product-truth pre-decision gate; persistent-goal
  coordinator authority; outcome/resource proportionality; project/global
  installation scope; lifecycle adapter independence.
- QA and design impact: structural validation gains project/global plan-first
  and scope-control assertions. No visual design or target-product impact.
- Specification paths changed: `docs/specs/index.md`;
  `docs/specs/features/bootstrap-governance.md`; this delta.
- Independent review: focused self-review and repository structural checks are
  proportional for this documentation-only governance change. No named
  high-risk product boundary is modified.
- New contract revision or epoch: `bootstrap.governance@3`

## Policy choices

- Planning permits only the minimum non-mutating instruction, specification,
  and evidence reading required to state a credible plan.
- A generic imperative to build a non-trivial feature is not an implicit waiver
  when material scope judgment remains. Immediate execution requires an
  explicit direction, an approved plan, or a task that is plainly bounded,
  low-risk, and free of material scope choices.
- The plan names the intended outcome, in-scope and out-of-scope work, execution
  steps, verification, and unresolved decisions. Approval freezes those bounds.
- Equivalent technical choices and directly necessary supporting work do not
  require repeated approval when they preserve the approved outcome and
  protected adjacent behavior.
- A material boundary expansion requires the dependency, minimum addition,
  expected cost, and risk to be presented for approval. Work that is both
  independent and still in scope may continue.

## Discrepancy disposition

- Classification: authorized evolution
- Resolution: add one compact task-framing and scope-control section to the
  project and global agent installation surfaces, then install those sections
  into the Bootstrap repository and the active user-level instructions.
- Exact residual: the release baseline remains
  `ba891245af7ffa6ffa5463f85af8045b3f6bc75c` until a release is made.
