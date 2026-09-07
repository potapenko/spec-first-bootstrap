# Minimum-Sufficient Work Acceptance Scenarios

Contracts: `bootstrap.governance.restart-delivery@5`, `BOOTSTRAP.ECONOMY`,
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
| MW-09: model choice | A packet ranges from deterministic editing to ambiguous high-risk reasoning. | Inherit the user settings by default. Optional overrides need a concrete task justification and must honor user constraints and host/tool restrictions; recommendations do not assign fixed tiers or role mappings. |
| MW-10: review repeat | Review is proposed after no relevant change and no new evidence. | Do not repeat. Repeat only for changed implementation, a remaining mandatory failure, or newly available required evidence. |
| MW-11: no budget theater | An ordinary task starts or reports progress. | Do not create token ledgers, numerical budgets, percentage mixes, checkpoint quotas, or routine economy reports. |
| MW-12: protected evidence | The smallest cheap check would omit required security, data-loss, irreversible-action, released-compatibility, or claimed-outcome evidence. | Keep the required evidence; minimum-sufficient work does not mean under-verification. |
| MW-13: persistent goal | A required approved-plan item remains while another item waits or optional support is available. | Continue dependency-ready required work. Economy routing never completes, pauses, or voluntarily blocks the goal. |
| MW-14: selected flagship | User selected a high-capability model and effort; dispatch a routine worker without a justified override. | Preserve both settings through inheritance; do not downgrade or demand a separate selection justification. |
| MW-15: permitted override | A concrete risk or latency need justifies changing model or effort, and user/host rules permit it. | Explain the override, resolve supported values, and treat model capability and effort separately. |
| MW-16: constrained override | Host supports inherited settings but disallows an override, or the desired override is unavailable. | Keep usable inherited settings; report the exact limitation if they cannot meet the task. Never invent aliases or silently substitute an unsupported setting. |
| MW-17: generation change | Available models change and the user selects a new default. | Ordinary workers inherit the selection without editing portable governance; no model generation or fixed tier table is required. |
| MW-18: installation | Install the policy into a project or global layout with existing application defaults. | Both layouts carry inheritance and advisory recommendations; application defaults remain unchanged. `inherit` is never sent as a model ID. |

## Verification method

Trace each case through the canonical root contract, compact project/global
sections, setup prompts, and installed global copies. Structural tests verify
the policy vocabulary, mirrored sections, active revisions, and removal of the
superseded numerical and fixed-cycle rules. Actual token savings and agent
adherence remain empirical and are not claimed from documentation checks alone.
