# Canonical AGENTS.md Sections

Use these sections as merge sources. Do not replace an existing AGENTS.md. If
equivalent rules already exist, reconcile them into one non-contradictory
section instead of appending a duplicate.

## Global product-truth section

Install this section in the active Codex-home AGENTS.md.

~~~markdown
## Product truth and specification governance

For any task that investigates, defines, changes, implements, or verifies
product behavior, UX, state, data contracts, compatibility, or product QA, the
primary single agent or coordinating `/root` must read the sibling
`product-truth-governance.md` in the active Codex home before product action.

That document is conditional role guidance. Workers that do not own product
authority, specification reconciliation, or contract review must not read the
whole document unless their packet explicitly requires it. They receive the
finite change envelope, pinned contract basis, evidence paths, protected
boundaries, and acceptance clauses needed for their task.

The specification system is the canonical statement of intended product
behavior and the project's primary product artifact, but no specification file
is infallible or self-authorizing. Applicable source, design, QA, runtime, and
release evidence must be reconciled with it. Those evidence layers establish
current realization, ownership, observed behavior, acceptance, and
compatibility; they do not silently invent intent.

Before implementation, classify the task as `restore`, `reconcile`,
`evolve`, `discover`, or `behavior-neutral` and establish a Contract
Change Envelope. It must name the authorized domains or clauses, protected
adjacent domains, stability or release baseline, required evidence, permitted
specification delta, material decisions that still require the user, and the
pinned contract revision.

The user's request authorizes semantic change inside the domain and behavior it
actually names. It does not silently open neighboring domains, shared-consumer
behavior, or unrelated released contracts. A specification edit cannot grant
itself authority and must never be used to launder an agent preference,
implementation convenience, current bug, or stale test into product intent.

Spec-first means the specification frames the investigation first; it does not
mean spec-only. Establish a provisional basis, inspect the smallest complete
applicable source/design/QA/runtime evidence set, classify discrepancies, and
then establish the final reconciled basis before implementation. Ask the user
only when that evidence pass leaves a material product fork, a protected
cross-domain or compatibility change outside the envelope, or missing external
authority.

When a semantic specification change is accepted, advance its contract
revision or epoch. Every open worker packet based on an older affected revision
must be revalidated or retired before its result can be accepted.
~~~

## Project-local product-truth section

Install this section in the target repository's AGENTS.md when the user chooses
project-only deployment.

~~~markdown
## Product truth and specification governance

For any task that investigates, defines, changes, implements, or verifies
product behavior, UX, state, data contracts, compatibility, or product QA, the
primary single agent or coordinating `/root` must read
`docs/agent/product-truth-governance.md` before product action.

That document is conditional role guidance. Workers that do not own product
authority, specification reconciliation, or contract review must not read the
whole document unless their packet explicitly requires it. They receive the
finite change envelope, pinned contract basis, evidence paths, protected
boundaries, and acceptance clauses needed for their task.

The specification system is the canonical statement of intended product
behavior and the project's primary product artifact, but no specification file
is infallible or self-authorizing. Applicable source, design, QA, runtime, and
release evidence must be reconciled with it. Those evidence layers establish
current realization, ownership, observed behavior, acceptance, and
compatibility; they do not silently invent intent.

Before implementation, classify the task as `restore`, `reconcile`,
`evolve`, `discover`, or `behavior-neutral` and establish a Contract
Change Envelope. It must name the authorized domains or clauses, protected
adjacent domains, stability or release baseline, required evidence, permitted
specification delta, material decisions that still require the user, and the
pinned contract revision.

The user's request authorizes semantic change inside the domain and behavior it
actually names. It does not silently open neighboring domains, shared-consumer
behavior, or unrelated released contracts. A specification edit cannot grant
itself authority and must never be used to launder an agent preference,
implementation convenience, current bug, or stale test into product intent.

Spec-first means the specification frames the investigation first; it does not
mean spec-only. Establish a provisional basis, inspect the smallest complete
applicable source/design/QA/runtime evidence set, classify discrepancies, and
then establish the final reconciled basis before implementation. Ask the user
only when that evidence pass leaves a material product fork, a protected
cross-domain or compatibility change outside the envelope, or missing external
authority.

When a semantic specification change is accepted, advance its contract
revision or epoch. Every open worker packet based on an older affected revision
must be revalidated or retired before its result can be accepted.
~~~

## Global persistent-goal section

Install this section in the active Codex-home AGENTS.md.

~~~markdown
## Persistent-goal coordination

A persistent goal does not make every agent a coordinator.

When a persistent goal is running and the current request directly or
indirectly advances that goal, the primary agent acts as `/root`: a
context-preserving, coordinator-only agent. This boundary has no exception for
small, simple, urgent, or supposedly faster-to-do-directly work.

Before taking goal action, `/root` must read the sibling
`root-orchestration.md` in the active Codex home directory and follow it
completely.

Spawned workers, explorers, reviewers, build agents, and runtime-QA agents are
not `/root`. They must not read `root-orchestration.md` unless the user
explicitly assigns them the primary coordinator role. They receive only their
finite worker packet and the instructions required by that packet.

A paused or blocked goal remains idle until the user explicitly resumes it. An
explicitly identified side task may be handled as ordinary single-agent work
only when it does not inspect, change, decide, verify, unblock, or advance any
goal-owned artifact or acceptance condition.

If no persistent goal is running, work as a normal single agent unless the user
explicitly requests delegation.
~~~

## Project-local persistent-goal section

Install this section in the target repository's AGENTS.md when the user chooses
project-only architecture deployment.

~~~markdown
## Persistent-goal coordination

A persistent goal does not make every agent a coordinator.

When a persistent goal is running and the current request directly or
indirectly advances that goal, the primary agent acts as `/root`: a
context-preserving, coordinator-only agent. This boundary has no exception for
small, simple, urgent, or supposedly faster-to-do-directly work.

Before taking goal action, `/root` must read
`docs/agent/root-orchestration.md` and follow it completely.

Spawned workers, explorers, reviewers, build agents, and runtime-QA agents are
not `/root`. They must not read `docs/agent/root-orchestration.md` unless
the user explicitly assigns them the primary coordinator role. They receive
only their finite worker packet and the instructions required by that packet.

A paused or blocked goal remains idle until the user explicitly resumes it. An
explicitly identified side task may be handled as ordinary single-agent work
only when it does not inspect, change, decide, verify, unblock, or advance any
goal-owned artifact or acceptance condition.

If no persistent goal is running, work as a normal single agent unless the user
explicitly requests delegation.
~~~
