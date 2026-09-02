# Persistent Goal Continuity Acceptance Scenarios

Contract: `bootstrap.governance.goal-continuity@1`, all `BOOTSTRAP.GOAL.*`
clauses. Consumer: Bootstrap validation and future persistent-goal reviews.

| Case | Setup and action | Required result |
| --- | --- | --- |
| GC-01: independent work | One plan item waits for a busy simulator while another is dependency-ready. | Record `waiting_resource`, release the lane, and run the ready item. The goal stays active. |
| GC-02: repeated contention | The simulator remains busy for more than three rechecks. | Recheck at three-minute intervals with no fixed attempt ceiling and no voluntary goal-level `blocked`. |
| GC-03: only waiting work | Every unfinished item needs the same busy resource. | Use nonblocking continuation or bounded waits until the next three-minute recheck; do not busy-loop or complete the goal. |
| GC-04: failed packet | A worker or implementation attempt fails. | Classify and repair, strengthen, replace the method, or decompose the packet while independent work continues. |
| GC-05: missing evidence | Required runtime proof is temporarily unavailable. | Record `waiting_evidence`, retain the acceptance requirement, and continue independent work. |
| GC-06: missing authority | One protected operation needs user authority. | Record `awaiting_authority`; do not perform it, invent permission, block the goal voluntarily, or stop independent work. |
| GC-07: economic reassessment | An approved persistent goal reaches a support or repair tripwire with required plan work remaining. | Report cost and reroute work without making approval a prerequisite for already-authorized required work. |
| GC-08: user pause | The user explicitly pauses or clears the goal. | Stop new work and preserve the exact resume state. |
| GC-09: completion | All required plan items and acceptance checks are verified. | Mark complete exactly once; elapsed time, retries, packet closure, or partial work never substitute. |

## Verification method

Trace each case through the canonical root contract, compact project/global
sections, setup prompts, and installed global files. Structural tests verify
required wording and reject the former idle-on-blocked rule. Real-run adherence
remains empirical and must not be claimed from documentation checks alone.
