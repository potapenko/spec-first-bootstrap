# Compact Instruction Sections

Installer agents merge only the selected section into the selected instruction
file. Never replace an existing instruction file or append an equivalent
duplicate. Full governance documents remain outside automatically loaded
instructions and are read only when their boundary applies.

## Project: product specifications

~~~markdown
## Product truth and specification governance

For work that investigates, defines, changes, implements, or verifies product
behavior, UX, state, data contracts, compatibility, or product QA, the primary
single agent or coordinating `/root` must read
`docs/agent/product-truth-governance.md` before product action.

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
~~~

## Project: persistent-goal agents

~~~markdown
## Persistent-goal coordination

When a persistent goal is running and the current request advances that goal,
the primary agent acts as `/root`: a context-preserving, coordinator-only
agent. Before goal action, `/root` must read
`docs/agent/root-orchestration.md` completely.

There is no direct-execution exception for small, urgent, mechanical, or
supposedly faster work. `/root` delegates finite implementation,
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
this layer. Cases verify pinned product behavior through explicit
action-state-result chains. Browser observations and QA cases are acceptance
evidence; they do not independently create product intent or authorize weaker
expectations.
~~~

## Global: product specifications

~~~markdown
## Product truth and specification governance

For work that investigates, defines, changes, implements, or verifies product
behavior, UX, state, data contracts, compatibility, or product QA, the primary
single agent or coordinating `/root` must read the sibling
`product-truth-governance.md` in the active user-level agent configuration
directory before product action.

The specification system is canonical intended behavior and the primary
product artifact, but no specification is infallible or self-authorizing.
Establish a bounded change mode and envelope, state a provisional basis,
reconcile the smallest complete applicable source/design/QA/runtime/history/
release evidence set, classify discrepancies, and state the final reconciled
basis before implementation. A spec edit cannot create its own authority.

Workers without product-authority, reconciliation, or contract-review
responsibility receive only the finite pinned clauses, evidence paths,
protected boundaries, and acceptance conditions required by their task.
~~~

## Global: persistent-goal agents

~~~markdown
## Persistent-goal coordination

When a persistent goal is running and the current request advances that goal,
the primary agent acts as `/root`: a context-preserving, coordinator-only
agent. Before goal action, `/root` must read the sibling
`root-orchestration.md` in the active user-level agent configuration directory
and follow it completely.

There is no direct-execution exception for small, urgent, mechanical, or
supposedly faster work. Spawned workers receive finite packets and do not read
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

Browser QA remains optional and conditional. It is not installed into every
project automatically. Cases verify pinned product behavior through explicit
action-state-result chains; browser observations and QA cases do not
independently create product intent or authorize weaker expectations.
~~~
