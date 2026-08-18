# Bootstrap Governance And Installation

- Contract ID: `bootstrap.governance`
- Domain ID: `bootstrap.governance`
- Authority: Active
- Stability: Accepted
- Governs: Bootstrap governance, setup prompts, templates, and layer composition
- Contract revision or epoch: `bootstrap.governance@5`
- Release baseline: `ba891245af7ffa6ffa5463f85af8045b3f6bc75c`

## Goal

Install strict, portable AI-agent workflow guidance without replacing existing
project authority, inventing product behavior, or silently installing unrelated
layers.

## Scope

- specification-first product governance;
- plan-first task framing and approved execution-scope control;
- current-branch and worktree scope control;
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
- The first implementation-bearing request in a new chat begins with a visible,
  evidence-based execution plan and explicit user approval before implementation
  or another state-changing task action.
- Questions, explanations, read-only investigations, reviews, diagnoses, status
  checks, and Git-history inspection proceed without an implementation plan or
  approval. A possible change found during read-only work is reported without
  silently turning the task into implementation.
- Planning performs the bounded non-mutating investigation required to make the
  implementation plan concrete. It does not ask the user to approve a plan for
  performing that planning work.
- The first-request gate runs once per chat. Later new initiatives or tasks that
  require material scope judgment receive a new plan; plainly bounded low-risk
  follow-ups without material scope choice may proceed directly.
- An approved plan becomes the execution boundary. Agents may make equivalent
  implementation choices and perform the verification required by that plan,
  but they do not add adjacent features, cleanup, refactors, tooling, or other
  helpful extras outside it.
- A newly discovered material dependency outside the approved boundary is
  returned as a minimal proposed plan amendment for user approval. Independent
  in-scope work may continue when safe.
- Agents work only in the Git branch selected when the task begins. They do not
  create, switch, rename, or publish another branch or create a worktree unless
  the user explicitly requests it; commit or push permission alone does not
  authorize branch creation.
- Before editing, agents declare the task-owned write set in the plan when one
  is required. Existing changes block implementation only where they overlap
  the planned edits. Non-overlapping changes remain untouched and are
  excluded from staging and commits.
- Worktree state is never bypassed by moving work to another branch or
  worktree. Work is not complete while its changes exist only outside the
  operator-selected branch.
- A persistent goal remains coordinator-and-workers work by default. When the
  user explicitly requires the current chat to complete that goal without
  subagents, workers, or delegation, the primary agent instead works as a
  normal single agent and may perform all in-scope goal actions itself.
- The explicit single-agent exception lasts only while the no-delegation
  instruction is active and never weakens specification, safety, approval,
  destructive-action, framework, or product-authority boundaries.
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
- Read-only work never consumes the first implementation-request gate and never
  authorizes implementation merely because it discovers a possible change.
- Silence, a generic request to create a non-trivial feature, or an agent's
  belief that extra work would be beneficial does not approve a plan or expand
  its scope.
- General approval to implement, commit, or push is not permission to create,
  switch, rename, or publish a branch or create a worktree.
- Repository-wide dirty state is not an implementation eligibility gate.
  Existing staged, unstaged, or untracked changes block only when their paths
  overlap the task-owned write set.
- Non-overlapping existing changes are preserved and excluded from task staging
  and commits.
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
- If an existing change overlaps the task-owned write set, report the exact
  paths and stop before editing them. Do not create or switch branches or
  worktrees to bypass the conflict.
- If existing changes do not overlap the task-owned write set, continue while
  leaving them untouched and excluding them from staging and commits.
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
- The operator-selected branch is the task's Git integration boundary until the
  user explicitly selects another branch or worktree.
- The task-owned write set is the file-level ownership boundary used for
  pre-edit conflict checks and scoped staging.
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
  boundaries, read-only handling, current-branch enforcement, task-owned
  write-set conflict handling, unrelated-change preservation, the explicit
  single-agent exception, and approved-scope enforcement on project and global
  surfaces;
- `git diff --check` and changed-scope review.

## Unknowns requiring confirmation

None.
