# Compact Instruction Sections

Installer agents merge only the selected section into the selected instruction
file. Never replace an existing instruction file or append an equivalent
duplicate. Full governance documents remain outside automatically loaded
instructions and are read only when their boundary applies.

## Project: current branch only

~~~markdown
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

At the end of any task that changes files, create a checkpoint commit and push
it from the currently checked-out branch. Before committing, verify that a safe,
writable upstream exists and that the push will not publish unrelated local
commits. If either condition cannot be established, do not create the checkpoint
commit. Commit only the files you changed for the task, and leave unrelated
working-tree changes untouched. Do not report the task as complete until both
the checkpoint commit and push succeed.
~~~

## Project: task framing and scope control

~~~markdown
## Task framing and scope control

### New-chat first implementation request gate

This gate applies only to the first implementation-bearing request in a new
chat: a request that asks to modify code, task artifacts, or external state.

A request whose requested result is itself a plan is planning-only, including
when the user asks to save that plan in a file for a future goal. Perform the
bounded planning work and produce or save the requested plan directly. Do not
first propose a meta-plan or ask for approval merely to create the plan. This
does not authorize implementation of the work described by that plan.

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

Absent an applicable planning-deliverable or explicit immediate-execution
exception, before the user approves that implementation plan, do not modify
code or task artifacts, mutate external state, or delegate implementation work.

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

Immediate execution is allowed when the user explicitly directs the agent to
execute now or without a plan, including on the first implementation-bearing
request; when the user has already approved the governing plan; or, after the
new-chat gate has been satisfied, when a subsequent task or follow-up is plainly
bounded, low-risk, and requires no material scope choice. A generic imperative
to build a non-trivial feature is not by itself an immediate-execution waiver.
Immediate execution does not bypass any applicable safety, specification,
approval, destructive-action, or environment gate.

Once approved, the plan is the execution boundary. Make equivalent technical
choices and perform directly necessary supporting edits and verification
without repeated approval, but do not add adjacent features, refactors,
cleanup, tooling, or other helpful extras that are not required by the approved
outcome.

If execution reveals a material dependency outside the approved boundary, stop
the affected slice and return the exact dependency, the minimum proposed scope
addition, expected cost, and risk. Wait for user approval before crossing that
boundary. Continue independent in-scope work when safe.
~~~

## Project: product specifications

~~~markdown
## Product truth and specification governance

For work that investigates, defines, changes, implements, or verifies product
behavior, UX, state, data contracts, compatibility, or product QA, the primary
single agent or coordinating `/root` must read
`docs/agent/product-truth-governance.md`, follow only applicable Markdown
links, and read the selected governance nodes before product action.

Before any project-specific answer, diagnosis, hypothesis, investigation,
recommendation, decision, plan, source inspection, non-reading task tool,
runtime action, implementation, or verification:

1. re-read every applicable instruction layer;
2. start at `docs/specs/README.md`;
3. follow matching branch summaries and ordinary Markdown links, select the
   smallest governing nodes, follow explicit dependencies, and read the
   selected closure completely;
4. record a Markdown traversal receipt with paths, clauses, revisions, dependencies,
   excluded siblings, and resolved context size;
5. classify the change mode, establish the Contract Change Envelope, and state
   a provisional Spec Basis separating specified expectation, protected
   behavior, established flow, and evidence still needed;
6. explicitly record a missing or ambiguous route and use Discover before
   consulting implementation evidence.

Until that gate is complete, do not inspect implementation sources, interpret
runtime evidence, form a failure hypothesis, recommend a repair, infer product
intent, or call a non-reading task tool. There is no urgency, debugging,
read-only-investigation, or one-command exception.

Every specification node is Markdown and has at most 100 physical lines;
50–80 is preferred. A node may be a root, branch, leaf, or hybrid. Branch
summaries navigate only. JSON manifests and generated routing registries are
not part of the specification system.

The specification system is the canonical statement of intended behavior and
the project's primary product artifact, but no specification is infallible or
self-authorizing. Applicable source, design, QA, runtime, history, and release
evidence must be reconciled with it; those layers expose realization,
ownership, observed behavior, acceptance, and compatibility without silently
inventing intent.

Classify covered work as `restore`, `reconcile`, `evolve`, `discover`, or
`behavior-neutral`, establish a bounded Contract Change Envelope, state a
provisional Spec Basis, inspect the smallest complete applicable evidence set,
classify discrepancies, and state the final reconciled Spec Basis before
implementation. A spec edit cannot grant itself product authority.

Ask the user only after evidence reconciliation leaves a material product fork,
a protected cross-domain or compatibility change, or missing external
authority. A semantic contract change advances its revision or epoch; affected
stale worker packets must be revalidated or retired.

Router summaries are non-normative. A node may be a leaf, branch, or both, and
complete authority means the selected contract closure rather than every
document under the specification root.
~~~

## Project: outcome and resource proportionality

~~~markdown
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
~~~

## Project: persistent-goal agents

~~~markdown
## Persistent-goal coordination

When a persistent goal is running and the current request advances that goal,
the primary agent acts as `/root`: a context-preserving, coordinator-only
agent, unless the user explicitly requires the current chat to complete the
goal without subagents, workers, or delegation.

Under that explicit single-agent exception, the primary agent works as a normal
single agent for the goal and must not spawn workers. It may inspect, implement,
build, test, launch, and perform other in-scope goal actions itself. The
exception lasts only while the explicit no-delegation instruction is active and
does not weaken specification, safety, approval, destructive-action, framework,
or product-authority boundaries.

Without that explicit exception, `/root` remains coordinator-only. Before goal
action, `/root` must read
`docs/agent/root-orchestration.md` completely.

That orchestration remains outcome-first and economically proportional. It
classifies work, tracks support-only checkpoint depth and budget variance, and
requires a delivery-and-cost reassessment before preparation or repair expands
beyond the compact proportionality gate above.

There is no coordinator direct-execution exception merely for small, urgent,
mechanical, or supposedly faster work. `/root` delegates finite implementation,
investigation, review, build, test, runtime, browser, device, and visual
packets; workers receive only their bounded packet and do not read the full
root manual unless assigned the coordinator role.

A paused or blocked goal remains idle until the user explicitly resumes it. A
separate side task may be single-agent only when it does not inspect, change,
decide, verify, unblock, or advance goal-owned work. Without a running goal,
work normally as a single agent unless delegation is explicitly requested.
~~~

## Project: optional browser QA

~~~markdown
## Optional browser QA

When the task installs, creates, runs, diagnoses, or reviews browser QA, read
`qa/README.md` and the applicable files under `qa/web/` before action.

Browser QA is optional and applies only to browser-facing projects that use
this layer. It does not require the product-specification or persistent-goal
agent layers. Cases verify the best available named product authority through
explicit action-state-result chains and link stable contract identifiers when
they exist. Browser observations and QA cases are acceptance evidence; they do
not independently create product intent or authorize weaker expectations.
~~~

## Global: product specifications

~~~markdown
## Product truth and specification governance

For work that investigates, defines, changes, implements, or verifies product
behavior, UX, state, data contracts, compatibility, or product QA, the primary
single agent or coordinating `/root` must read the sibling
`product-truth-governance.md` in the active user-level agent configuration
directory, follow only applicable Markdown links, and read the selected
governance nodes before product action.

Before any project-specific answer, diagnosis, hypothesis, investigation,
recommendation, decision, plan, source inspection, non-reading task tool,
runtime action, implementation, or verification:

1. re-read every applicable instruction layer;
2. start at `docs/specs/README.md`;
3. follow matching branch summaries and ordinary Markdown links, select the
   smallest governing nodes, follow explicit dependencies, and read the
   selected closure completely;
4. record a Markdown traversal receipt with paths, clauses, revisions, dependencies,
   excluded siblings, and resolved context size;
5. classify the change mode, establish the Contract Change Envelope, and state
   a provisional Spec Basis separating specified expectation, protected
   behavior, established flow, and evidence still needed;
6. explicitly record a missing or ambiguous route and use Discover before
   consulting implementation evidence.

Until that gate is complete, do not inspect implementation sources, interpret
runtime evidence, form a failure hypothesis, recommend a repair, infer product
intent, or call a non-reading task tool. There is no urgency, debugging,
read-only-investigation, or one-command exception.

Every specification node is Markdown and has at most 100 physical lines;
50–80 is preferred. A node may be a root, branch, leaf, or hybrid. Branch
summaries navigate only. JSON manifests and generated routing registries are
not part of the specification system.

The specification system is canonical intended behavior and the primary
product artifact, but no specification is infallible or self-authorizing.
Establish a bounded change mode and envelope, state a provisional basis,
reconcile the smallest complete applicable source/design/QA/runtime/history/
release evidence set, classify discrepancies, and state the final reconciled
basis before implementation. A spec edit cannot create its own authority.

Workers without product-authority, reconciliation, or contract-review
responsibility receive only the finite traversal receipt, pinned contract closure,
evidence paths, protected boundaries, and acceptance conditions required by
their task. Branch summaries cannot create product intent.
~~~

## Global: task framing and scope control

~~~markdown
## Task framing and scope control

### New-chat first implementation request gate

This gate applies only to the first implementation-bearing request in a new
chat: a request that asks to modify code, task artifacts, or external state.

A request whose requested result is itself a plan is planning-only, including
when the user asks to save that plan in a file for a future goal. Perform the
bounded planning work and produce or save the requested plan directly. Do not
first propose a meta-plan or ask for approval merely to create the plan. This
does not authorize implementation of the work described by that plan.

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

Absent an applicable planning-deliverable or explicit immediate-execution
exception, before the user approves that implementation plan, do not modify
code or task artifacts, mutate external state, or delegate implementation work.

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

Immediate execution is allowed when the user explicitly directs the agent to
execute now or without a plan, including on the first implementation-bearing
request; when the user has already approved the governing plan; or, after the
new-chat gate has been satisfied, when a subsequent task or follow-up is plainly
bounded, low-risk, and requires no material scope choice. A generic imperative
to build a non-trivial feature is not by itself an immediate-execution waiver.
Immediate execution does not bypass any applicable safety, specification,
approval, destructive-action, or environment gate.

Once approved, the plan is the execution boundary. Make equivalent technical
choices and perform directly necessary supporting edits and verification
without repeated approval, but do not add adjacent features, refactors,
cleanup, tooling, or other helpful extras that are not required by the approved
outcome.

If execution reveals a material dependency outside the approved boundary, stop
the affected slice and return the exact dependency, the minimum proposed scope
addition, expected cost, and risk. Wait for user approval before crossing that
boundary. Continue independent in-scope work when safe.
~~~

## Global: current branch only

~~~markdown
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

At the end of any task that changes files, create a checkpoint commit and push
it from the currently checked-out branch. Before committing, verify that a safe,
writable upstream exists and that the push will not publish unrelated local
commits. If either condition cannot be established, do not create the checkpoint
commit. Commit only the files you changed for the task, and leave unrelated
working-tree changes untouched. Do not report the task as complete until both
the checkpoint commit and push succeed.
~~~

## Project: Codex lifecycle restart adapter

~~~markdown
## Codex lifecycle restart gate

When a trusted Codex lifecycle hook reports startup, resume, clear, context
compaction, or a worker start, take no task action until the applicable
instruction hierarchy and current linked authority have been re-established.

For a root or single-agent session, re-establish current goal state, governing
plan or runbook, registry, Contract Change Envelope, specification index,
latest Markdown traversal receipt, selected nodes and contract closure, contract epoch,
accepted deltas, unresolved discrepancies, and next-action QA instructions.
Reopen the recorded Markdown path to detect revision drift and do not load unselected
siblings merely because context was compacted. A worker reads its finite packet
and pinned Markdown closure; it does not reconstruct authority from the root
conversation or read the root manual unless assigned the coordinator role.

State the route and contracts re-read in the next progress update. Chat
summaries, memory, worker lists, old receipts, builds, tests, screenshots, and
raw configuration never replace current contracts.
~~~

## Global: Codex lifecycle restart adapter

~~~markdown
## Codex lifecycle restart gate

When a trusted Codex lifecycle hook reports startup, resume, clear, context
compaction, or a worker start, take no task action until the applicable global
and project instruction hierarchy and current linked authority have been
re-established.

For a root or single-agent session, re-establish current goal state, governing
plan or runbook, registry, Contract Change Envelope, specification index,
latest Markdown traversal receipt, selected nodes and contract closure, contract epoch,
accepted deltas, unresolved discrepancies, and next-action QA instructions.
Reopen the recorded Markdown path to detect revision drift and do not load unselected
siblings merely because context was compacted. A worker reads its finite packet
and pinned Markdown closure; it does not reconstruct authority from the root
conversation or read the root manual unless assigned the coordinator role.

State the route and contracts re-read in the next progress update. Chat
summaries, memory, worker lists, old receipts, builds, tests, screenshots, and
raw configuration never replace current contracts.
~~~

## Global: outcome and resource proportionality

~~~markdown
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
~~~

## Global: persistent-goal agents

~~~markdown
## Persistent-goal coordination

When a persistent goal is running and the current request advances that goal,
the primary agent acts as `/root`: a context-preserving, coordinator-only
agent, unless the user explicitly requires the current chat to complete the
goal without subagents, workers, or delegation.

Under that explicit single-agent exception, the primary agent works as a normal
single agent for the goal and must not spawn workers. It may inspect, implement,
build, test, launch, and perform other in-scope goal actions itself. The
exception lasts only while the explicit no-delegation instruction is active and
does not weaken specification, safety, approval, destructive-action, framework,
or product-authority boundaries.

Without that explicit exception, `/root` remains coordinator-only. Before goal
action, `/root` must read the sibling
`root-orchestration.md` in the active user-level agent configuration directory
and follow it completely.

That orchestration remains outcome-first and economically proportional. It
classifies work, tracks support-only checkpoint depth and budget variance, and
requires a delivery-and-cost reassessment before preparation or repair expands
beyond the compact proportionality gate above.

There is no coordinator direct-execution exception merely for small, urgent,
mechanical, or supposedly faster work. Spawned workers receive finite packets and do not read
the full root manual unless assigned the coordinator role.

A paused or blocked goal remains idle until explicitly resumed. A separate
side task may be single-agent only when it does not inspect, change, decide,
verify, unblock, or advance goal-owned work. Without a running goal, work
normally as a single agent unless delegation is explicitly requested.
~~~

## Global: optional browser QA

~~~markdown
## Optional browser QA

For a task that installs, creates, runs, diagnoses, or reviews browser QA, read
the sibling `web-qa-governance.md` in the active user-level agent configuration
directory before QA action.

Browser QA remains optional, conditional, and independent. It is not installed
into every project automatically and does not require global product-
specification or persistent-goal agent layers. Cases verify the best available
named product authority through explicit action-state-result chains and link
stable contract identifiers when they exist. Browser observations and QA cases
do not independently create product intent or authorize weaker expectations.
~~~
