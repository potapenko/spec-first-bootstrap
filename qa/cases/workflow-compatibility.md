# Workflow Compatibility Acceptance Scenarios

Basis: `bootstrap.governance@16`, installation @3, task-scope @7,
goal-continuity @2, restart-delivery @4, review @4.
Consumer: portable installer verification and the approved local deployment.

| Case | Action and starting state | Required result |
| --- | --- | --- |
| WC-01 | User supplied the complete brief and approved the scoped plan; a skill asks for generic brief confirmation. | Continue authorized work; do not ask for the same approval. New material decisions still require authority. |
| WC-02 | User says “proceed” on an approved plan, then asks a status question. | Answer briefly and continue the plan. Do not restart planning or treat the side question as cancellation. |
| WC-03 | A newly requested goal has one bounded sequential change and no independent-review trigger. | Record single-agent execution and perform it directly without a worker just because a goal exists. |
| WC-04 | A coordinated goal has two independent packets; one resource is busy. | Preserve waiting_resource and its recheck, release its lane, and execute the ready packet. |
| WC-05 | The same genuine blocker recurs, no meaningful independent work remains, and the host requires a blocked transition at its stated threshold. | Follow the host transition, preserve resume conditions, and never claim complete or evade it with a scheduler. Temporary contention alone is insufficient. |
| WC-06 | Compaction occurs after approval with a recorded mode and accepted work. | Restore the applicable instructions, approved scope, mode, selected closure, and next evidence; preserve approval and accepted results. |
| WC-07 | Presentation-only change has no action, state, data, or service change. | Use the relevant diff/render check; do not run an unrelated logic suite or repeat unchanged checks. |
| WC-08 | Install globally where the user already has local-commit policy; install into a project explicitly requiring push. | Preserve each policy and record precedence. Commit-only needs no upstream; push requires safe upstream and no unrelated commits. |
| WC-09 | A bounded task shares a file with protected behavior. | Every changed hunk maps to the outcome; no same-file permission expansion. Missing authority mode defaults to bounded. |
| WC-10 | A single-agent goal changes a high-risk shared released owner. | Obtain required independent acceptance; single-agent execution does not waive it. A no-delegation instruction leaves unavailable independent proof unverified. |

## Evidence levels

Structural fixtures verify complete installed routes, local overrides, and
portable defaults. They do not prove model obedience. For bounded model probes,
provide the selected installed rules and concrete starting states, collect the
next action/decision, and compare with this table. Report model, scope, and any
tool/environment limitation. A prose decision probe is not an end-to-end run.

Keep raw probe output temporary outside repositories and installed configuration.
Use the accepted task report for a concise outcome; never commit raw run logs.
