# AGENTS.md

This file defines workflow rules for agents maintaining this repository.

It is not the source of truth for detailed product behavior. Product behavior
belongs in `docs/specs/`; portable installer doctrine belongs in
`docs/agent-governance/`.

## Current branch only

Agents must work only in the Git branch that is checked out when the task begins.

Do not create, switch, rename, or publish another branch, and do not create a Git
worktree, unless the user explicitly asks for it. General approval to begin work,
commit, or push is not permission to create a branch.

Before editing, declare the task-owned write set in the plan when one is
required. Existing changes are blockers only where they overlap the planned
edits. Leave all non-overlapping changes untouched and exclude them from staging
and commits.

Work is not complete or accepted while its changes exist only in another branch
or worktree. Task changes must be integrated into the operator-selected current
branch.

At the end of any task that changes files, create a checkpoint commit in the
currently checked-out branch. The checkpoint is the saved state of the work you
completed, so commit only the files you changed for that task. Unrelated changes
elsewhere in the working tree do not block the checkpoint and remain untouched.
Do not report the task as complete until the checkpoint commit succeeds.

## Task framing and scope control

### New-chat first implementation request gate

This gate applies only to the first implementation-bearing request in a new
chat: a request that asks to modify code, task artifacts, or external state.

Questions, explanations, read-only investigations, reviews, diagnoses, status
checks, and Git-history inspection do not require a plan or user approval.
Perform them directly and return the evidence-backed answer.

If a read-only request reveals a possible change, report the findings without
automatically turning the request into an implementation task. Propose an
implementation plan only when the user has asked for a change.

For a request that includes implementation, complete the planning phase before
asking the user to approve implementation.

The planning phase includes all bounded, non-mutating work needed to make the
implementation plan concrete and evidence-based: reading applicable
instructions, specifications, source, tests, documentation, logs,
configuration, and Git history; tracing ownership and dependencies; running
safe read-only checks; and diagnosing or reproducing the reported problem when
needed.

Do not propose a plan to perform this planning work. Perform it first. The plan
presented to the user must report the established findings and describe the
actual implementation: intended outcome, exact scope, relevant owners or files,
required changes, protected behavior, verification, out-of-scope work, and only
those decisions that genuinely cannot be resolved without the user.

Before the user approves that implementation plan, do not modify code or task
artifacts, mutate external state, or delegate implementation work.

The gate does not repeat for every user message. Clarifications, answers to the
agent's questions, additions within the proposed or approved scope, objections,
status questions, and ordinary follow-up requests in the same chat are not a
new-chat first request. A resume, lifecycle restart, context compaction, or
automatic continuation of the same chat also does not reactivate the gate.

After the first implementation plan has been approved, continue within its
boundary without asking for a new plan on every message. For a later task in the
same chat, require a new plan only when it introduces a new feature, initiative,
or other material scope judgment. A plainly bounded, low-risk follow-up that
requires no material scope choice may be executed without another plan.

The plan states the intended outcome, in-scope work, out-of-scope work,
execution steps, verification, and any unresolved decisions. Planning-only,
investigation-only, and review-only requests do not authorize implementation.
Do not delegate execution work before the plan is approved unless the user
explicitly requested that delegation as part of planning.

After the new-chat first implementation gate has been satisfied, immediate
execution is allowed when the user has approved the governing plan or when a
subsequent task or follow-up is plainly bounded, low-risk, and requires no
material scope choice. A generic imperative to build a non-trivial feature is
not by itself an immediate-execution waiver. Immediate execution does not bypass
any applicable safety, specification, approval, or environment gate.

Once approved, the plan is the execution boundary. Make equivalent technical
choices and perform directly necessary supporting edits and verification
without repeated approval, but do not add adjacent features, refactors,
cleanup, tooling, or other helpful extras that are not required by the approved
outcome.

If execution reveals a material dependency outside the approved boundary, stop
the affected slice and return the exact dependency, the minimum proposed scope
addition, expected cost, and risk. Wait for user approval before crossing that
boundary. Continue independent in-scope work when safe.

## Outcome and resource proportionality

This applies to every implementation task, including ordinary single-agent work
and finite workers inside an orchestrated goal.

Measure progress first by the concrete capability requested by the user and
reachable from the product or release path. Tests, diagnostics, Debug harnesses,
models, maps, evidence, documentation, registries, and review are supporting
work. Report them separately and never represent them as delivered product
functionality.

Start an ordinary milestone with a 60/25/15 planning target: 60% shipping
implementation, 25% verification/review/QA, and 15% discovery/diagnostics/
tooling/coordination. This is a tripwire, not a quota or permission to skip work
required by demonstrated risk.

Aim for the smallest release-reachable vertical slice in the first one or two
implementation checkpoints. Every support artifact names the next
dependency-ready implementation decision or capability that will consume it.
Speculative support infrastructure and production-grade hardening of temporary
Debug tooling are forbidden.

A third consecutive support-only implementation checkpoint, a second
repair/re-review cycle, or material diagnostic/tooling expansion is an economic
stop. Before continuing, report capability delivered, capability being
unlocked, expected additional time or token cost, why a truthful residual is
insufficient, the cheapest safe alternative, and the stop condition. Continue
only with explicit user approval unless stopping would leave a demonstrated
data-loss, privacy, security, irreversible-action, or released-compatibility
risk unsafe.

A residual must not hide a known acceptance failure or missing capability that
is being claimed as delivered. Progress updates separate shipping capability
and files from verification, diagnostics/tooling/coordination cost, elapsed
effort, budget variance, and the next user-visible milestone.

## Product Truth Gate

Follow `docs/spec-first-workflow.md` for the compact workflow. For covered
product work, start at the compact router
`docs/agent-governance/product-truth-governance.md`, follow only the
applicable Markdown links, and read the selected governance nodes completely.

The gate applies to every product feature, behavioral bug or investigation,
product-behavior plan, UX/state/data-contract change, migration, product QA
task, and refactor that may affect observable behavior.

### Mandatory pre-action specification gate

Before any project-specific answer, diagnosis, hypothesis, investigation,
recommendation, interpretation, decision, plan, source inspection, non-reading
task tool, implementation, runtime action, or verification:

1. Re-read every applicable global and project instruction layer.
2. Start at `docs/specs/README.md`. Follow ordinary Markdown links through
   only the matching branch summaries.
3. Select the smallest governing Markdown nodes and follow their explicit
   dependency links. Read each selected node completely; do not load siblings
   merely because they share a parent.
4. Record a traversal receipt with the Markdown path, selected clauses,
   revisions, dependencies, excluded siblings, and resolved context size.
5. Classify work as Restore, Reconcile, Evolve, Discover, or Behavior-neutral
   and establish the Contract Change Envelope.
6. State a provisional Spec Basis separating specified expectation, protected
   behavior, established flow, and evidence still needed. Record a missing or
   ambiguous Markdown path explicitly and use Discover before implementation evidence.
7. Only then inspect the smallest complete applicable source, design, QA,
   runtime, history, upstream, and release evidence set.
8. Classify discrepancies, accept only a legitimate Contract Delta, pin the
   final reconciled basis, and only then implement and verify.

Until steps 1-6 are complete, do not inspect implementation sources, interpret
runtime evidence, form a failure hypothesis, recommend a repair, infer product
or operational intent, or call a non-reading task tool. This has no exception
for urgency, apparent simplicity, debugging, read-only investigation, or “just
one command.”

Branch summaries are navigation only and never define intended behavior. A
Markdown node may be a leaf, branch, or both. Every node is limited to 100
physical lines, with 50–80 preferred. Completeness means the selected path and
explicit dependencies, not every document under the specification root.

The specification system is canonical intended behavior but is not infallible
or self-authorizing. Spec-first is not spec-only. Current code, stale tests,
implementation convenience, or agent preference cannot be written into a spec
and then cited as authority.

Explicit brownfield discovery is the narrow exception. Record the missing or
unreliable contract first, inspect source and runtime only as evidence,
separate observed from intended behavior, and create first-pass specs without
changing product implementation.

## Lifecycle restart gate

When a lifecycle hook reports startup, resume, clear, context compaction, or a
worker start, take no task action until the applicable instruction hierarchy
and current linked authority have been re-established. Re-read the current
goal, envelope, latest traversal receipt, selected Markdown nodes, pinned contract
closure, epochs, deltas, discrepancies, and only the next-action QA evidence.
Reopen the recorded path to detect revision drift. Traverse from the root again
only when the task changed or the receipt is missing or ambiguous; do not reload
unselected siblings merely because context was compacted.

State the Markdown path and contracts re-read in the next progress update. Chat
summaries, memory, worker lists, previous receipts, green builds, tests,
screenshots, and raw configuration do not replace current contracts. Workers
use their pinned packet and linked closure rather than the root conversation.

## When a spec is required

Create or update a spec when a task:

- introduces a new feature;
- changes observable behavior;
- introduces or modifies route, state, or data contracts;
- affects multi-step user flows;
- changes gating, permissions, or eligibility logic;
- changes accepted or released compatibility;
- introduces behavior that could be misunderstood later.

A new spec is usually unnecessary for formatting, comments, or proven
behavior-neutral cleanup.

## Separation of concerns

- `AGENTS.md` defines workflow and agent rules.
- `docs/specs/` defines product behavior.
- `docs/agent-governance/` defines portable setup sources for installer agents.
- `qa/` or tests define verification and evidence.

Do not merge these layers into one file.

## Implementation rule

Implement against the final pinned Spec Basis, not ad-hoc chat memory. A spec
edit requires legitimate user or reconciliation authority and cannot authorize
itself. If evidence reveals an unresolved product fork, stop only the affected
slice and return the evidence rather than inventing behavior.

## Verification rule

If a task changes behavior, update appropriate verification artifacts. QA
verifies pinned action-state-result contracts; it does not independently define
intent or weaken expectations solely to obtain a green result.

## Writing style for specs

Specs should be short, explicit, product-level, and behavior-oriented. Avoid
deep implementation detail unless it is necessary to preserve the product
contract.
