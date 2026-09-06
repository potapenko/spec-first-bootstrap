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

Before editing, a required plan declares either a bounded task-owned write set
or task-wide repository authority. Existing changes are blockers only where
they overlap paths the task must modify. Leave all other changes untouched and
exclude them from staging and commits.

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

## Task framing and scope control

Before implementation, read the task-framing and scope rules through
`docs/agent-governance/work-governance.md`. Complete bounded investigation before presenting the first
implementation-bearing plan; wait for approval unless the user explicitly
requests immediate execution. A requested plan is produced directly.
Approval persists across follow-ups, skills, and compaction. Use `bounded` or
`task-wide` authority; neither opens protected adjacent behavior.

## Minimum-sufficient work

Use the minimum-sufficient-work rules through `docs/agent-governance/work-governance.md`.
Choose the smallest complete path and change-driven verification. Expand only
from concrete evidence or required acceptance, not available tools or capacity.

## Persistent-goal continuity

Before goal action, read goal-execution through `docs/agent-governance/work-governance.md`.
Record `single-agent` for bounded sequential work or `coordinated` when
independent packets or context isolation justify delegation. Honor user choice
and preserve the mode on restart. Only coordinated goals load `docs/agent-governance/root-orchestration.md`;
finite workers use their packets and pinned contracts.
Continue independent ready work while preserving exact waiting conditions.
Follow mandatory host impasse transitions; blocked never means complete.

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
