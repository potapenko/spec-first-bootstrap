# Bootstrap Governance And Installation

- Contract ID: `bootstrap.governance`
- Domain ID: `bootstrap.governance`
- Authority: Active
- Stability: Accepted
- Governs: Bootstrap governance, setup prompts, templates, and layer composition
- Contract revision or epoch: `bootstrap.governance@1`
- Release baseline: `ba891245af7ffa6ffa5463f85af8045b3f6bc75c`

## Goal

Install strict, portable AI-agent workflow guidance without replacing existing
project authority, inventing product behavior, or silently installing unrelated
layers.

## Scope

- specification-first product governance;
- persistent-goal coordinator-and-workers governance;
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

## Route / state / data implications

- Compact gates live in the active project or global instruction chain.
- Full governance remains conditionally loaded from stable documented paths.
- Semantic contract changes advance the affected revision or epoch.
- Long-running product packets pin the governing clauses and epoch.

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
- `git diff --check` and changed-scope review.

## Unknowns requiring confirmation

None.
