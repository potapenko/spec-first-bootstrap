# Set Up Agent Work Governance In This Project

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Set up current-branch discipline, plan-first task framing, strict execution-
scope control, implementation economics, and the coordinator-and-workers
architecture inside the current project only. Do not modify the user's global
Codex, Claude, or other agent configuration.

This is an instruction and documentation setup task. Do not create, resume,
pause, block, or complete a persistent goal. Do not change product code.

Install only the agent-work layer described here. Do not install specification-
first governance or browser QA as a prerequisite or dependency. Preserve and
interoperate with either layer when it is already present.

## Read first

Read completely from the bootstrap repository:

- the Project: current branch only section in
  `docs/agent-governance/agents-sections.md`;
- the Project: task framing and scope control section in
  `docs/agent-governance/agents-sections.md`;
- `docs/agent-governance/root-orchestration.md`;
- the Project: outcome and resource proportionality section in
  `docs/agent-governance/agents-sections.md`;
- the Project: persistent-goal agents section in
  `docs/agent-governance/agents-sections.md`.

Resolve and read the target project's active instruction hierarchy, including
overrides, nested files, fallback names, and instruction-size limits. Read its
coordination rules, worktree state, and any current goal state before editing.
Preserve unrelated content.

## Install

1. Merge the compact Project: current branch only and Project: task framing and
   scope control sections into the existing project-root instruction file.
2. Install the full root contract as
   `docs/agent/root-orchestration.md`.
3. Merge the compact Project: outcome and resource proportionality and Project:
   persistent-goal agents sections into the existing project-root instruction
   file. Never replace the complete file.
4. Reconcile equivalent existing sections instead of appending
   a conflicting duplicate.
5. Do not add, remove, or rewrite specification, product-truth, browser-QA, or
   other unrelated workflow layers. If they already exist, preserve them and
   keep the agent layer compatible with their established authority paths.
6. Do not change model defaults, reasoning defaults, concurrency limits,
   custom agent profiles, provider settings, or application configuration.
   Apply the root contract's role-based model policy using models actually
   supported by the active agent environment; do not hardcode another
   platform's model names.
7. Do not install or modify the optional Codex lifecycle adapter unless the
   user explicitly requested it. Preserve an existing adapter and keep its
   worker-start wording aligned with finite packet authority.

Use `apply_patch` for edits.

## Required result

The resulting project must preserve these rules:

- the first implementation-bearing request presents a bounded execution plan
  and waits for explicit user approval before implementation; later new
  features, initiatives, and tasks with material scope judgment do the same;
- questions, explanations, read-only investigations, reviews, diagnoses, status
  checks, and Git-history inspection proceed directly and do not consume the
  first implementation-request gate;
- planning performs the bounded non-mutating investigation needed to produce a
  concrete implementation plan instead of asking approval for a plan whose
  output would merely be another plan;
- when the requested result is itself a plan, including a plan saved in a file
  for a future goal, the agent produces or saves it directly without first
  proposing a meta-plan; this does not authorize the described implementation;
- the plan names the outcome, in-scope and out-of-scope work, steps,
  verification, and unresolved decisions;
- explicit direction to execute now or without a plan waives the planning-
  approval gate even on the first implementation-bearing request, without
  bypassing other applicable gates or expanding scope;
- after the first implementation-request gate is satisfied, an approved plan
  and plainly bounded low-risk follow-up work without material scope judgment
  may proceed directly;
- the approved plan remains the execution boundary, and material additions are
  returned as minimal proposed amendments rather than performed silently;
- agents stay in the branch selected when the task begins and do not create,
  switch, rename, or publish another branch or create a worktree without an
  explicit user request; commit or push permission alone is insufficient;
- before editing, a required plan declares the task-owned write set; existing
  changes block only where their paths overlap that set;
- non-overlapping existing changes remain untouched and are
  excluded from staging and commits; worktree conflicts are not bypassed
  through another branch or worktree;
- at the end of any task that changes files, the agent creates a checkpoint
  commit in the currently checked-out branch containing only the files it
  changed for that task; unrelated working-tree changes do not block the
  checkpoint, and the task is not complete until the commit succeeds;
- `/root` is coordinator-only when a running persistent goal is being
  advanced;
- when the user explicitly requires the current chat to complete a persistent
  goal without subagents, workers, or delegation, the primary agent works as a
  normal single agent and performs in-scope goal work itself without weakening
  any other governing boundary;
- absent that explicit no-delegation instruction, no small-task exception
  permits `/root` to implement, inspect broadly, build, test, run, browse, or
  perform visual QA itself;
- ordinary work remains single-agent when no persistent goal is active;
- ordinary implementation and persistent goals measure progress by concrete
  release-path capability and separate it from supporting work;
- the first one or two implementation checkpoints target a smallest
  release-reachable vertical slice;
- workers receive classified finite packets with authority, scope, owners,
  forbidden actions, release-path consumer, effort bound, economic stop,
  checks, stopping conditions, and a terminal receipt;
- product packets carry a Markdown traversal receipt, exact pinned contract closure,
  specified expectation, protected behavior, assigned evidence, and contract
  epoch when product-truth governance applies;
- model strength follows risk and judgment needs, with quality ahead of token
  savings;
- only independent ownership is parallelized;
- shipping changes receive risk-proportional review, with
  independent review mandatory for the named high-risk classes or when another
  governing contract requires it;
- a third consecutive support-only implementation checkpoint, second
  repair/re-review cycle, or material diagnostic/tooling expansion triggers a
  delivery-and-cost reassessment and the required user-approval gate;
- one restart-safe registry carries packet state, applicable authority
  revision, work classification, support depth, budget variance, next
  capability, receipts, and residuals;
- a paused or blocked goal stays idle until explicitly resumed;
- context compaction resumes from the traversal receipt, selected closure, and
  durable state rather than chat memory or every sibling document.

## Verification

Verify exact project-only scope, one merged copy of each compact section,
complete canonical document, preserved existing instructions, valid Markdown,
no product-code change, no goal-state change, no model/configuration change,
and no installation or modification of the specification or browser-QA layers.

Also verify that the merged gate is active rather than shadowed, stays within
the configured instruction-size limit, and that no lifecycle hook changed
without explicit adapter scope. Verify that read-only work does not require an
implementation plan, a requested plan artifact does not trigger a meta-plan,
explicit execute-now or no-plan direction waives only planning approval,
planning does not mutate task state, the current-branch boundary is active,
required plans declare the task-owned write set, only overlapping changes block
editing, non-overlapping changes stay outside staging and commits, work that
changes files ends with a successful checkpoint commit containing only the
agent's task files, the single-agent exception requires an explicit no-
delegation instruction, and the approved-plan boundary rejects unapproved
adjacent work.

Follow the project's checkpoint policy and report changed paths, coexistence
with any already installed layers, verification, and exact residuals.
