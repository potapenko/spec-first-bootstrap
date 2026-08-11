# Bootstrap Governance And Installation

- Contract ID: `bootstrap.governance`
- Domain ID: `bootstrap.governance`
- Authority: Active
- Stability: Accepted
- Governs: Bootstrap governance, setup prompts, templates, and layer composition
- Contract revision or epoch: `bootstrap.governance@3`
- Release baseline: `ba891245af7ffa6ffa5463f85af8045b3f6bc75c`

## Goal

Install strict, portable AI-agent workflow guidance without replacing existing
project authority, inventing product behavior, or silently installing unrelated
layers.

## Scope

- specification-first product governance;
- plan-first task framing and approved execution-scope control;
- persistent-goal coordinator-and-workers governance;
- outcome and resource proportionality for implementation work;
- optional browser QA;
- setup and repair prompts;
- neutral specification and verification templates;
- optional environment-specific enforcement adapters.

## Non-goals

- changing target-project product behavior during workflow installation;
- changing model, reasoning, concurrency, provider, or application defaults;
- making one workflow layer a hidden prerequisite of another;
- treating an environment-specific adapter as portable product authority.

## User-visible behavior

- The specification, agent-work, and browser-QA layers are
  independently selectable.
- A new feature, initiative, or materially ambiguous task begins with a visible
  execution plan and explicit user approval before implementation or other
  state-changing task action.
- A bounded, obvious, low-risk task may proceed immediately when it requires no
  material scope judgment. Explicit user direction to execute immediately, or
  approval of an existing plan, also authorizes immediate execution.
- An approved plan becomes the execution boundary. Agents may make equivalent
  implementation choices and perform the verification required by that plan,
  but they do not add adjacent features, cleanup, refactors, tooling, or other
  helpful extras outside it.
- A newly discovered material dependency outside the approved boundary is
  returned as a minimal proposed plan amendment for user approval. Independent
  in-scope work may continue when safe.
- Project setup changes only the named repository. Global setup changes only
  the explicitly selected user-level agent configuration.
- Installers resolve the active instruction chain, including overrides and
  size limits, before editing it.
- Installers merge one compact routing gate and keep full governance outside
  automatically loaded instructions.
- Product work uses a mandatory pre-decision specification gate before any
  project-specific conclusion, source inspection, runtime interpretation, or
  non-reading task action.
- The pre-decision receipt names every governing document read completely and
  separates specified expectation, protected behavior, established flow, and
  evidence still needed.
- If bounded discovery finds no governing specification, the agent records the
  absence and uses Discover instead of inferring intent from code or runtime.
- Restart, resume, clear, and context-compaction recovery re-establishes
  authority from durable documents rather than chat memory.
- Installed agent governance measures progress first by concrete capability
  reachable from the product or release path. Supporting work is reported
  separately and never represented as delivered product functionality.
- Ordinary implementation work and persistent goals aim to produce a smallest
  release-reachable vertical slice in the first one or two implementation
  checkpoints.
- Persistent-goal packets and checkpoints classify shipping, verification,
  diagnostic, tooling, and coordination work. Support-only checkpoints have a
  bounded depth and an explicit delivery-and-cost reassessment before further
  expansion.
- Review, verification, diagnostics, and tooling are proportional to
  demonstrated risk. High-risk boundaries retain stronger independent review
  and safety requirements.

## Invariants

- A specification edit never authorizes itself.
- Current code, tests, logs, runtime, screenshots, or chat memory never define
  intended behavior before the Spec Basis.
- Existing project-specific safety, framework, build, test, database, storage,
  Git, release, and operator rules are preserved.
- Product-truth, agent-work, and browser QA remain independently
  installable.
- Environment-specific model names are not copied into portable governance.
- Planning-only, discovery-only, and installation-only requests do not
  authorize product implementation.
- Preparing a plan permits only the bounded, non-mutating instruction,
  specification, and evidence reading needed to make the plan credible. It
  does not authorize edits, state-changing runtime actions, external writes,
  or execution delegation.
- Silence, a generic request to create a non-trivial feature, or an agent's
  belief that extra work would be beneficial does not approve a plan or expand
  its scope.
- Necessary supporting edits and verification named in the approved plan, or
  unavoidable to complete its stated steps, remain in scope only when they do
  not change user-visible behavior or a protected adjacent contract beyond the
  approved plan.
- A support artifact names the next implementation decision or release-path
  capability that consumes it. Speculative support infrastructure is forbidden.
- A residual may record bounded uncertainty or noncritical hardening, but may
  not hide a known failure of the acceptance contract or an undelivered
  capability being claimed as complete.
- Delivery budgets are planning controls rather than permission to skip
  verification required by demonstrated risk.

## Edge cases and failure policy

- If the active instruction entry point or scope is ambiguous, stop before
  writing.
- If material scope judgment is required before an execution plan can be
  stated, ask the user the smallest necessary question instead of beginning
  implementation.
- If execution exposes a material dependency outside the approved plan, stop
  the affected slice, state the dependency, minimum scope addition, cost, and
  risk, and wait for approval before crossing that boundary.
- If an override shadows the proposed instruction file, update the active
  chain or return the exact blocker instead of claiming installation success.
- If Active contracts conflict without precedence, stop only the affected
  slice.
- If the merged instruction chain exceeds the supported size limit, reduce
  duplication or split conditional guidance rather than allowing silent
  truncation.
- If work would create a third consecutive support-only implementation
  checkpoint, a second repair/re-review cycle, or material diagnostic/tooling
  expansion, stop for a delivery-and-cost reassessment. Continue only with the
  required user approval unless stopping would leave a demonstrated data-loss,
  privacy, security, irreversible-action, or released-compatibility risk unsafe.

## Route / state / data implications

- Compact gates live in the active project or global instruction chain.
- The accepted execution plan is the active task-scope envelope until the user
  approves an amendment or replaces the task.
- Full governance remains conditionally loaded from stable documented paths.
- Semantic contract changes advance the affected revision or epoch.
- Long-running product packets pin the governing clauses and epoch.
- Restart-safe goal state records the current milestone, work classification,
  support-only checkpoint depth, budget variance, and next release-path
  capability.

## Evidence mapping

- `docs/spec-first-workflow.md`
- `docs/agent-governance/product-truth-governance.md`
- `docs/agent-governance/root-orchestration.md`
- `docs/agent-governance/agents-sections.md`
- `prompts/`
- `docs/specs/templates/`

## Verification mapping

- local Markdown-link validation;
- JSON validation for hook templates;
- lifecycle adapter fixture tests;
- consistency search for pre-decision and restart gates;
- consistency checks for outcome-first progress, proportional review, economic
  stop conditions, and portable model-neutral wording;
- consistency checks for plan-first task framing, explicit immediate-execution
  exceptions, and approved-scope enforcement on project and global surfaces;
- `git diff --check` and changed-scope review.

## Unknowns requiring confirmation

None.
