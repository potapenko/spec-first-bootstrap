# Independent Outcome Review

- Node type: leaf
- Status: Active
- Contract: `bootstrap.governance.review@1`
- Clauses: `BOOTSTRAP.REVIEW.AUTHORITY`, `BOOTSTRAP.REVIEW.INDEPENDENCE`,
  `BOOTSTRAP.REVIEW.EVIDENCE`, `BOOTSTRAP.REVIEW.VERDICT`,
  `BOOTSTRAP.REVIEW.INTEGRATION`, `BOOTSTRAP.REVIEW.LIMITS`
- Read when: installing or changing persistent-goal review and acceptance.
- Do not read when: no orchestration review or acceptance behavior is involved.
- Maximum size: 100 physical lines.

## Dependencies

- [Task and scope](task-and-scope.md): approved outcome and protected boundaries.
- [Delivery proportionality](restart-and-delivery.md): repair and cost limits.

## BOOTSTRAP.REVIEW.AUTHORITY — Establish the bar first

Before implementation, identify mandatory acceptance criteria and any optional
quality references from the approved outcome and available project authority.
If a reference is used, name its applicable dimension and comparison conditions;
an aspirational reference does not become a blocking threshold unless authorized.
An existing approved acceptance condition cannot be relabeled optional.
Reviewers cannot invent requirements, weaken criteria, or expand scope.
Standalone specification governance remains optional for the agent-work layer.

## BOOTSTRAP.REVIEW.INDEPENDENCE — Independent first observation

Where independent review is required or selected, use a non-author reviewer with
fresh context. Its initial packet contains the objective, governing constraints,
criteria, references, artifact revision, neutral access and verification facts.
It excludes the builder's narrative, verdict, terminal receipt, and prior review
conclusions. Send initial observations to the root as an intermediate message;
only then does it provide the receipt and prior findings to the same reviewer
for final reconciliation. The intermediate message is not acceptance.
Unavailable fresh context leaves a required independent-review gate blocked.
Never hide safety restrictions or evidence needed to operate safely for blindness.
Blind A/B comparison is optional and only appropriate for comparable artifacts.

## BOOTSTRAP.REVIEW.EVIDENCE — Inspect the actual result

Review addresses the user outcome separately from implementation correctness.
Inspect the actual artifact and the applicable action-state-result chain;
tests or author summaries cannot replace required runtime or visual evidence.
Evidence must identify the reviewed revision and relevant environment/state.
Use one reviewer for both questions when sufficient; no automatic extra roles.
Each blocking finding names the criterion, observation, impact, repair owner,
and recheck. Stylistic preference or a demand to be harsh is not evidence.

## BOOTSTRAP.REVIEW.VERDICT — Distinguish failure from missing proof

Review verdicts are `accept`, `accept_with_residual`, `reject`, `not_verified`.
Acceptance requires evidence for every mandatory criterion in the review scope.
An observed mandatory failure is `reject`; missing or stale required evidence
is `not_verified` when no mandatory failure is already established. Record all
evidence gaps even when rejecting. Missing evidence is not proof of a defect.
`accept_with_residual` cannot hide a failed or unverified mandatory criterion.
The verdict is distinct from the worker's execution status. `/root` maps
`reject` to repair and `not_verified` to blocked verification, with the exact
missing evidence and responsible owner; neither permits dependent acceptance.

## BOOTSTRAP.REVIEW.INTEGRATION — Verify the whole scenario

Acceptance of separate parts does not establish acceptance of their composition.
Before accepting a multi-part capability, a scoped verifier checks the integrated
user scenario and relevant boundaries on the composed revision. This may share
an existing review/QA wave; no duplicate audit is required.
The root coordinates and evaluates receipts, not raw runtime or visual output.
Revalidate affected criteria after relevant changes; preserve unaffected accepted
work. Critics report findings and do not silently become implementation owners.

## BOOTSTRAP.REVIEW.LIMITS — Preserve proportionate delivery

Existing risk-based independent-review triggers and low-risk self-review remain.
One review and one focused repair/re-review remain the normal limit; further
cycles follow the existing economic and safety gates. Prefer the largest
meaningful in-scope gap without suppressing other mandatory failures.
Neither an unreachable reference nor fresh critics justify indefinite retries,
automatic fan-out, reviewer shopping, or reopening accepted work without evidence.
Installation copies this protocol without changing models, providers, goals,
permissions, concurrency defaults, or unrelated instruction layers.
