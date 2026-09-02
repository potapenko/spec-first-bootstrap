# Persistent Goal Continuity

- Node type: leaf
- Status: Active
- Contract: `bootstrap.governance.goal-continuity@1`
- Clauses: `BOOTSTRAP.GOAL.ACTIVE`, `BOOTSTRAP.GOAL.READY`,
  `BOOTSTRAP.GOAL.WAIT`, `BOOTSTRAP.GOAL.RECOVER`, `BOOTSTRAP.GOAL.TERMINAL`
- Read when: installing, coordinating, reviewing, or repairing persistent-goal work.
- Do not read when: no persistent goal behavior is involved.
- Maximum size: 100 physical lines.

## Active-until-complete

A persistent goal remains active until its complete definition of done is
verified, or the user pauses or clears it. Local governance must not voluntarily
set goal-level `blocked`. Host-enforced termination is reported as a platform
constraint, not reinterpreted as completion or a local policy choice.

## Dependency-ready scheduling

Plan order is not execution order. On every coordination pass, select any
dependency-ready authorized work. A waiting, failed, rejected, or unavailable
packet does not stop independent work and does not block the goal. When one
slice cannot proceed, preserve its exact state and continue every safe
independent slice before waiting.

## Resource waits

Temporary resource contention uses `waiting_resource`, with the resource,
owner when known, last observation, and `recheck_at` recorded. Release the
worker slot and shared lane, run other ready work, and revisit after the next
completed packet or after three minutes, whichever makes the item ready sooner.

If only resource-waiting work remains, use the host's nonblocking continuation,
scheduler, or bounded wait mechanism and recheck every three minutes. Each
external call retains an explicit timeout, but the goal has no fixed retry or
attempt ceiling. Do not use a long shell sleep or busy loop.

## Recovery and authority

Implementation failure triggers classification, focused repair, stronger
reasoning, alternative execution, or narrower decomposition. Missing evidence
uses `waiting_evidence`; required user or external authority uses
`awaiting_authority`. Continue all independent authorized work in either case.
These item states never imply goal completion or local goal-level blocking.

Economic reassessment changes routing, records cost, and removes optional work
without an immediate approved-plan consumer. It does not stop required work
already inside the approved plan. Scope expansion, destructive action, and
other protected operations still require their existing authorization.

## Terminal conditions

`complete` requires every mandatory plan outcome and acceptance condition.
Packet counts, elapsed time, token use, retry count, temporary resource
contention, missing optional polish, or an unfinished plan cannot justify a
terminal goal state.
