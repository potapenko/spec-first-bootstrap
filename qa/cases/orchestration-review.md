# Orchestration Review Acceptance Scenarios

Contract: `bootstrap.governance.review@1`, all `BOOTSTRAP.REVIEW.*` clauses.
Consumer: the Bootstrap and global audit update; subsequent reviewer packets
use these cases to check protocol adherence without changing product scope.
These are verification cases, not new product authority or generated run logs.

## Scenario checks

| Case | Setup and action | Required result |
| --- | --- | --- |
| OR-01: independent first observation | Builder claims success. Dispatch the reviewer against the artifact. | Initial packet has criteria, revision and safe access facts, not builder claims or old review conclusions. Initial observations precede receipt reconciliation. |
| OR-02: misleading author summary | Initial inspection finds a mandatory scenario fails; builder receipt says it passed. | Evidence and the pinned criterion decide; `reject` names impact, repair owner and recheck. The summary cannot override the failure. |
| OR-03: unavailable proof | Mandatory runtime check cannot run; no failure is otherwise established. | `not_verified`, exact missing evidence and owner, blocked verification. No acceptance or implementation-defect claim from absence alone. |
| OR-04: failure plus missing proof | One mandatory criterion fails and another cannot be checked. | `reject` includes both the proven failure and the evidence gap. Repair does not automatically close the missing verification. |
| OR-05: optional reference | Mandatory criteria pass; output trails a reference explicitly designated aspirational. | May accept with the optional gap recorded. Do not invent a blocking threshold or weaken an existing mandatory quality criterion. |
| OR-06: integration seam | Parts pass locally but the composed user scenario fails. | Integrated capability is not accepted. Assign the seam finding to the responsible owner and verify the composed revision. |
| OR-07: stale evidence | Artifact changes after initial observation or QA. | Revalidate affected criteria. Missing current mandatory proof blocks acceptance; unaffected valid evidence can be reused. |
| OR-08: repair loop | A focused repair is reviewed with fresh initial observation, then previous findings are disclosed. | Check closure and affected regressions. A fresh critic does not reset the one-repair normal limit or reopen unrelated accepted work. |
| OR-09: low-risk delta | A small deterministic change has no independent-review trigger. | Focused self-review remains admissible; no mandatory fan-out or misleading claim of independent review. |
| OR-10: unsafe blindness | Runtime evidence needs safety restrictions or approved operation boundaries. | Include those facts before action; independence never hides safety information or grants additional permissions. |
| OR-11: unsupported critique | Critic dislikes style but cannot tie it to a mandatory criterion and impact. | Nonblocking preference, not an invented defect or authorization for a rewrite. |
| OR-12: scope and installation | Apply the audit update to project/global instruction copies with unrelated differences. | Audit sections agree; goal activation, coordinator-only rules, review risk triggers, repair limits, unrelated settings and existing differences remain unchanged. |
| OR-13: independence unavailable | Independent review is required but the host cannot provide fresh reviewer context. | The gate stays blocked. Self-review or a reviewer inheriting implementation claims cannot be labeled independent. |

## Verification method

For OR-01, verify that the initial observations are an intermediate message;
only afterward does the root supply the receipt and prior findings to the same
reviewer. The intermediate message cannot close the review packet.

For this instruction-only change, trace each setup through the canonical
orchestration text and compare the installed audit sections. Run the existing
Bootstrap validator and Markdown/test suite to check routing and installation
structure. A textual scenario walkthrough is not a live multi-agent experiment.

When observing future authorized runs, record whether criteria coverage,
initial-observation ordering, findings and final acceptance match these cases.
Use existing task receipts; do not add a separate telemetry system. Model
adherence, missed defects, false positives and cost benefits remain empirical
questions, not claims established by structural checks.
