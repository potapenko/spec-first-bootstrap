# Bootstrap Governance And Installation

- Contract ID: `bootstrap.governance`
- Domain ID: `bootstrap.governance`
- Authority: Active
- Stability: Evolving
- Governs: Bootstrap governance, setup prompts, templates, and layer composition
- Contract revision or epoch: `bootstrap.governance@2`
- Release baseline: `ba891245af7ffa6ffa5463f85af8045b3f6bc75c`

## Goal

Install strict, portable AI-agent workflow guidance without replacing existing
project authority, inventing product behavior, or silently installing unrelated
layers.

## Scope

- specification-first product governance;
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

- The specification, persistent-goal agent, and browser-QA layers are
  independently selectable.
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
- Product-truth, persistent-goal agents, and browser QA remain independently
  installable.
- Environment-specific model names are not copied into portable governance.
- Planning-only, discovery-only, and installation-only requests do not
  authorize product implementation.
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
- `git diff --check` and changed-scope review.

## Unknowns requiring confirmation

None.
