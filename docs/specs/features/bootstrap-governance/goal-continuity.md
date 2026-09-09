# Persistent Goal Continuity

- Node type: leaf
- Status: Active
- Contract: `bootstrap.governance.goal-continuity@3`
- Clauses: `BOOTSTRAP.GOAL.ACTIVE`, `BOOTSTRAP.GOAL.READY`,
  `BOOTSTRAP.GOAL.WAIT`, `BOOTSTRAP.GOAL.RECOVER`, `BOOTSTRAP.GOAL.TERMINAL`
- Read when: installing, coordinating, reviewing, or repairing persistent-goal work.
- Do not read when: no persistent goal behavior is involved.
- Maximum size: 100 physical lines.

## Active-until-complete

A persistent goal remains incomplete until its complete definition of done is
verified. Continue authorized work until user pause/clear or a mandatory host
transition. Do not use goal-level `blocked` as a discretionary stopping policy.
When the host requires it after a repeated genuine impasse and no meaningful
independent work remains, follow that transition and preserve the exact resume
condition. Never equate a blocked state with completion or silently resume it.

## Execution mode

Every task and persistent goal defaults to `single-agent` in the current chat,
regardless of size or duration. Only an explicit user request for multi-agent
work authorizes `coordinated` execution within that request's scope. Complexity,
independent work, context isolation, risk, review, available slots, skills, and
project instructions do not authorize delegation or a mode change. Do not
routinely ask to enable it. The primary agent performs authorized work directly.

Preserve scoped user authorization on follow-ups and restart. A recorded mode
or an old automatic choice is not user authorization. Without it, resume as
`single-agent`; reconcile existing worker ownership before taking over, without
new dispatch or losing accepted work. A user revocation stops new dispatch and
returns work safely to the current chat. Coordinator-only restrictions apply
only to user-requested coordinated goals. Installing rules never resumes goals.

Required independent review remains required but cannot authorize another
agent. Use available independent evidence or report the exact acceptance gap;
continue other authorized work. Self-review is not independent acceptance.

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
These item states never imply completion. Mandatory host state rules still apply.

Economic reassessment changes routing, records cost, and removes optional work
without an immediate approved-plan consumer. It does not stop required work
already inside the approved plan. Scope expansion, destructive action, and
other protected operations still require their existing authorization.

## Terminal conditions

`complete` requires every mandatory plan outcome and acceptance condition.
Packet counts, elapsed time, token use, retry count, temporary resource
contention, missing optional polish, or an unfinished plan cannot justify a
completion. Mandatory host impasse transitions remain an exception for blocking.
