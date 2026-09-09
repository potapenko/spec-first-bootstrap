# Goal Execution

- Node type: leaf
- Status: Active
- Read when: starting, advancing, resuming, or installing persistent-goal work.
- Do not read when: no persistent goal or installation decision is involved.
- Maximum size: 100 physical lines.

## Select and retain the mode

Only an explicit user request starts a persistent goal. Installing governance
never creates or resumes one. Every task and goal defaults to `single-agent`
execution in the current chat, regardless of size, duration, or complexity.
Only an explicit user request for multi-agent work authorizes `coordinated`
execution. Record that request and its scope with the mode in existing restart
state. A request to implement, continue, or complete a goal is not delegation
authorization. Honor explicit user mode choice; do not routinely ask to change it.

Skills, project rules, independent review, risk, context isolation, and available
slots cannot authorize additional agents. Apply the same boundary to reviewer
sessions, nested workers, other chats, and equivalent CLI/API model delegation.
Load the full coordinator contract only for user-requested coordinated goals.

In single-agent mode the primary agent may inspect, implement, test, operate,
and verify authorized work. In coordinated mode `/root` only coordinates;
finite workers own implementation and runtime evidence. Required independent
review applies in either mode but does not authorize an agent. If required
independent proof is unavailable, report that acceptance gap and continue any
independent authorized work; self-review is not independent review.

Preserve the mode and scoped user authorization on follow-ups and restart.
Only the user can authorize a switch to coordinated execution. New complexity,
dependencies, risks, or an old recorded mode cannot supply that authorization.
For older goals without evidence of an explicit user request, use single-agent
execution. Before taking over, reconcile running owners without new dispatch,
preserve accepted work, and record the handoff. User revocation likewise stops
new dispatch and safely returns work to the current chat. Do not restart paused
or blocked goals while installing these rules.

## Ready work and waiting

Plan order is not execution order. Continue every dependency-ready authorized
item. A waiting or failed slice does not stop independent work. Preserve its
exact dependency, owner, last observation, and next action.

Temporary contention uses `waiting_resource`. Release the worker slot and
shared lane; revisit after another completed item or every three minutes.
When only waiting work remains, use supported nonblocking continuation or
bounded waits, without a fixed attempt ceiling or a busy loop. Each external
call has an explicit timeout. Mandatory host impasse rules below take precedence.

Missing required proof uses `waiting_evidence`; new user or external authority
uses `awaiting_authority`. Neither state means completion or permission to
weaken acceptance. Classify failed work, repair its cause, and reuse completed
evidence instead of launching duplicate investigation waves.

## Host state and truthful completion

Do not use goal-level `blocked` as a discretionary stopping policy. If the
current host/tool contract requires blocking after repeated genuine impasse,
apply its exact conditions only after no meaningful independent work remains.
Record the blocking cause and resume condition. Do not hardcode one host's
retry threshold into portable governance. Never evade a mandatory transition
with polling or an automation; never create a scheduled task without authority.

An unfinished goal remains incomplete regardless of its host status. Only all
mandatory outcomes and acceptance evidence justify `complete`; elapsed time,
token use, packet count, or temporary contention do not. Follow the host's
supported user action for resuming blocked work; never silently resume it.

On user pause, dispatch no new work; reconcile running ownership and preserve
the next resume action. On resume or compaction, re-read applicable instructions,
the goal, approved plan, recorded mode, registry if needed, selected contract
closure, and next required evidence. Retain prior approval and accepted work;
do not re-read unselected sibling contracts or reconstruct authority from memory.
