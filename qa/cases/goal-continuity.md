# Persistent Goal Continuity Acceptance Scenarios

Contract: `bootstrap.governance.goal-continuity@3`, all `BOOTSTRAP.GOAL.*`
clauses. Consumer: Bootstrap validation and future persistent-goal reviews.

| Case | Setup and action | Required result |
| --- | --- | --- |
| GC-01: independent work | One plan item waits for a busy simulator while another is dependency-ready. | Record `waiting_resource`, release the lane, and run the ready item. The goal stays active. |
| GC-02: repeated contention | The simulator remains busy for more than three rechecks. | Recheck at three-minute intervals with no fixed attempt ceiling, subject to mandatory host impasse transitions. |
| GC-03: only waiting work | Every unfinished item needs the same busy resource. | Use nonblocking continuation or bounded waits until the next three-minute recheck; do not busy-loop or complete the goal. |
| GC-04: failed packet | A worker or implementation attempt fails. | Classify and repair, strengthen, replace the method, or decompose the packet while independent work continues. |
| GC-05: missing evidence | Required runtime proof is temporarily unavailable. | Record `waiting_evidence`, retain the acceptance requirement, and continue independent work. |
| GC-06: missing authority | One protected operation needs user authority. | Record `awaiting_authority`; do not perform it, invent permission, stop independent work; follow mandatory host impasse transitions if all meaningful work is exhausted. |
| GC-07: economic routing | An approved persistent goal has required plan work remaining while optional support or repeated checks are proposed. | Continue dependency-ready required work, omit support without an immediate consumer, and expand only from evidence; do not invent a budget stop or approval prerequisite. |
| GC-08: user pause | The user explicitly pauses or clears the goal. | Stop new work and preserve the exact resume state. |
| GC-09: completion | All required plan items and acceptance checks are verified. | Mark complete exactly once; elapsed time, retries, packet closure, or partial work never substitute. |
| GC-10: default execution | Start a large goal without an explicit multi-agent request. | Execute directly in the current chat; do not load coordinator-only restrictions or launch workers. |
| GC-11: scoped opt-in | User explicitly requests multi-agent execution for the goal. | Record request and scope with coordinated mode; delegate only within that scope and preserve it on restart. |
| GC-12: old automatic mode | Resume an old coordinated goal without user delegation authorization. | Reconcile ownership without new dispatch, preserve accepted results, and continue single-agent. |

## Verification method

Trace each case through the canonical root contract, compact project/global
sections, setup prompts, and installed global files. Structural tests verify
required wording and reject the former idle-on-blocked rule. Real-run adherence
remains empirical and must not be claimed from documentation checks alone.
