# Compact Instruction Sections

Installer agents merge only the selected section into the selected instruction
file. Never replace an existing instruction file or append an equivalent
duplicate. Full governance documents remain outside automatically loaded
instructions and are read only when their boundary applies.

## Project: current branch only

~~~markdown
## Current branch only

Use only the branch selected when the task begins. Do not create, switch,
rename, or publish another branch or create a worktree without explicit user
permission. Declare bounded task-owned paths or task-wide authority before
editing; preserve unrelated changes and exclude them from checkpoints.
Follow scope-and-checkpoints through `docs/agent/work-governance.md`.

Global default: local checkpoint commit. Preserve explicit project checkpoint
policy; automatic push is project opt-in.
~~~

## Project: task framing and scope control

~~~markdown
## Task framing and scope control

Before implementation, read the task-framing and scope rules through
`docs/agent/work-governance.md`. Complete bounded investigation before presenting the first
implementation-bearing plan; wait for approval unless the user explicitly
requests immediate execution. A requested plan is produced directly.
Approval persists across follow-ups, skills, and compaction. Use `bounded` or
`task-wide` authority; neither opens protected adjacent behavior.
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

## Project: minimum-sufficient work

~~~markdown
## Minimum-sufficient work

Use the minimum-sufficient-work rules through `docs/agent/work-governance.md`.
Choose the smallest complete path and change-driven verification. Expand only
from concrete evidence or required acceptance, not available tools or capacity.
~~~

## Project: persistent-goal agents

~~~markdown
## Persistent-goal coordination

Before goal action, read goal-execution through `docs/agent/work-governance.md`.
Record `single-agent` for bounded sequential work or `coordinated` when
independent packets or context isolation justify delegation. Honor user choice
and preserve the mode on restart. Only coordinated goals load `docs/agent/root-orchestration.md`;
finite workers use their packets and pinned contracts.
Continue independent ready work while preserving exact waiting conditions.
Follow mandatory host impasse transitions; blocked never means complete.
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

Before implementation, read the task-framing and scope rules through
`work-governance.md`. Complete bounded investigation before presenting the first
implementation-bearing plan; wait for approval unless the user explicitly
requests immediate execution. A requested plan is produced directly.
Approval persists across follow-ups, skills, and compaction. Use `bounded` or
`task-wide` authority; neither opens protected adjacent behavior.
~~~

## Global: current branch only

~~~markdown
## Current branch only

Use only the branch selected when the task begins. Do not create, switch,
rename, or publish another branch or create a worktree without explicit user
permission. Declare bounded task-owned paths or task-wide authority before
editing; preserve unrelated changes and exclude them from checkpoints.
Follow scope-and-checkpoints through `work-governance.md`.

Global default: local checkpoint commit. Preserve explicit project checkpoint
policy; automatic push is project opt-in.
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

## Global: minimum-sufficient work

~~~markdown
## Minimum-sufficient work

Use the minimum-sufficient-work rules through `work-governance.md`.
Choose the smallest complete path and change-driven verification. Expand only
from concrete evidence or required acceptance, not available tools or capacity.
~~~

## Global: persistent-goal agents

~~~markdown
## Persistent-goal coordination

Before goal action, read goal-execution through `work-governance.md`.
Record `single-agent` for bounded sequential work or `coordinated` when
independent packets or context isolation justify delegation. Honor user choice
and preserve the mode on restart. Only coordinated goals load `root-orchestration.md`;
finite workers use their packets and pinned contracts.
Continue independent ready work while preserving exact waiting conditions.
Follow mandatory host impasse transitions; blocked never means complete.
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
