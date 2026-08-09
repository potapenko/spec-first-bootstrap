# AGENTS.md

This file defines workflow rules for agents maintaining this repository.

It is not the source of truth for detailed product behavior. Product behavior
belongs in `docs/specs/`; portable installer doctrine belongs in
`docs/agent-governance/`.

## Product Truth Gate

Follow `docs/spec-first-workflow.md` for the compact workflow. For product-truth
or installer-governance changes, also read
`docs/agent-governance/product-truth-governance.md`.

The gate applies to every product feature, behavioral bug or investigation,
product-behavior plan, UX/state/data-contract change, migration, product QA
task, and refactor that may affect observable behavior.

### Mandatory pre-action specification gate

Before any project-specific answer, diagnosis, hypothesis, investigation,
recommendation, interpretation, decision, plan, source inspection, non-reading
task tool, implementation, runtime action, or verification:

1. Re-read every applicable global and project instruction layer.
2. Read `docs/specs/README.md`, `docs/specs/index.md`, and the complete directly
   applicable governing set routed by the index, including linked plans,
   registries, runbooks, operator handoffs, accepted reusable baselines, design
   contracts, and QA workflows.
3. Classify work as Restore, Reconcile, Evolve, Discover, or Behavior-neutral.
4. Establish a Contract Change Envelope with authorized and protected domains,
   evidence requirements, allowed spec delta, release baseline, and contract
   revision.
5. State the exact documents read completely and provide a provisional Spec
   Basis that separates specified expectation, protected behavior, established
   flow, and evidence still needed.
6. If no governing specification exists after bounded discovery, record that
   absence explicitly and use Discover mode before consulting other evidence.
7. Only after that basis exists, inspect the smallest complete applicable
   source, design, QA, runtime,
   history, upstream, and release evidence set.
8. Classify every material discrepancy.
9. Accept only a legitimate Contract Delta and update the spec first when
   meaning changes.
10. State the final reconciled Spec Basis with a pinned revision or epoch.
11. Only then implement and verify the authorized slice.

Until steps 1-6 are complete, do not inspect implementation sources, interpret
runtime evidence, form a failure hypothesis, recommend a repair, infer product
or operational intent, or call a non-reading task tool. This has no exception
for urgency, apparent simplicity, debugging, read-only investigation, or “just
one command.”

The specification system is canonical intended behavior but is not infallible
or self-authorizing. Spec-first is not spec-only. Current code, stale tests,
implementation convenience, or agent preference cannot be written into a spec
and then cited as authority.

Explicit brownfield discovery is the narrow exception. Record the missing or
unreliable contract first, inspect source and runtime only as evidence,
separate observed from intended behavior, and create first-pass specs without
changing product implementation.

## Lifecycle restart gate

When a lifecycle hook reports startup, resume, clear, context compaction, or a
worker start, take no task action until the applicable instruction hierarchy
and every action-specific governing document have been re-read. Re-establish
the current goal state, Contract Change Envelope, spec index, governing clauses,
contract epoch, accepted deltas, unresolved discrepancies, and next-action QA
instructions as applicable.

State the exact documents re-read in the next progress update. Chat summaries,
memory, worker lists, previous receipts, green builds, tests, screenshots, and
raw configuration do not replace the current governing documents. Workers use
their pinned packet and do not reconstruct authority from the root conversation.

## When a spec is required

Create or update a spec when a task:

- introduces a new feature;
- changes observable behavior;
- introduces or modifies route, state, or data contracts;
- affects multi-step user flows;
- changes gating, permissions, or eligibility logic;
- changes accepted or released compatibility;
- introduces behavior that could be misunderstood later.

A new spec is usually unnecessary for formatting, comments, or proven
behavior-neutral cleanup.

## Separation of concerns

- `AGENTS.md` defines workflow and agent rules.
- `docs/specs/` defines product behavior.
- `docs/agent-governance/` defines portable setup sources for installer agents.
- `qa/` or tests define verification and evidence.

Do not merge these layers into one file.

## Implementation rule

Implement against the final pinned Spec Basis, not ad-hoc chat memory. A spec
edit requires legitimate user or reconciliation authority and cannot authorize
itself. If evidence reveals an unresolved product fork, stop only the affected
slice and return the evidence rather than inventing behavior.

## Verification rule

If a task changes behavior, update appropriate verification artifacts. QA
verifies pinned action-state-result contracts; it does not independently define
intent or weaken expectations solely to obtain a green result.

## Writing style for specs

Specs should be short, explicit, product-level, and behavior-oriented. Avoid
deep implementation detail unless it is necessary to preserve the product
contract.
