# Minimum-Sufficient Work Acceptance Scenarios

Contracts: `bootstrap.governance.restart-delivery@4`, `BOOTSTRAP.ECONOMY`,
and `bootstrap.governance.review@4`, `BOOTSTRAP.REVIEW.LIMITS`.
Consumer: Bootstrap validation and future agent-work installation reviews.

| Case | Setup and action | Required result |
| --- | --- | --- |
| MW-01: presentation only | Change a font, color, spacing, label style, or other presentation detail without changing actions, state, persistence, services, or business rules. | Inspect the diff and relevant rendered surface when required; do not run logic, integration, or full project test suites merely in case. |
| MW-02: local logic | Change one locally owned behavior with focused tests available. | Run the smallest focused check that can detect the plausible regression. |
| MW-03: shared owner | Change a shared owner used by several consumers. | Identify affected consumers and run consumer- or risk-mapped checks; writable ownership does not open unrelated product behavior. |
| MW-04: full suite request | A broad suite is proposed after a bounded change. | Run it only when concrete cross-cutting evidence or a governing requirement justifies it; availability alone is not a reason. |
| MW-05: unchanged rerun | A check already passed and its inputs, environment, and relevant implementation did not change. | Reuse the result instead of rerunning it. |
| MW-06: noisy command | A tool can emit a long log although only a verdict and a few failures affect the next decision. | Request or return compact decision-relevant output and preserve a bounded excerpt only when needed. |
| MW-07: unnecessary fan-out | One agent can complete a bounded task without losing important context. | Keep the task single-agent; spare capacity is not a delegation reason. |
| MW-08: beneficial parallelism | Independent packets have distinct outputs and their elapsed-time or context-isolation benefit exceeds duplicated context and coordination. | Parallelize with disjoint ownership and compact receipts. |
| MW-09: model choice | A packet ranges from deterministic editing to ambiguous high-risk reasoning. | Choose model and reasoning strength by expected total work, including likely retries and rework; neither role name nor maximum capability decides automatically. |
| MW-10: review repeat | Review is proposed after no relevant change and no new evidence. | Do not repeat. Repeat only for changed implementation, a remaining mandatory failure, or newly available required evidence. |
| MW-11: no budget theater | An ordinary task starts or reports progress. | Do not create token ledgers, numerical budgets, percentage mixes, checkpoint quotas, or routine economy reports. |
| MW-12: protected evidence | The smallest cheap check would omit required security, data-loss, irreversible-action, released-compatibility, or claimed-outcome evidence. | Keep the required evidence; minimum-sufficient work does not mean under-verification. |
| MW-13: persistent goal | A required approved-plan item remains while another item waits or optional support is available. | Continue dependency-ready required work. Economy routing never completes, pauses, or voluntarily blocks the goal. |

## Verification method

Trace each case through the canonical root contract, compact project/global
sections, setup prompts, and installed global copies. Structural tests verify
the policy vocabulary, mirrored sections, active revisions, and removal of the
superseded numerical and fixed-cycle rules. Actual token savings and agent
adherence remain empirical and are not claimed from documentation checks alone.
