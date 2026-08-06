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

1. Read this file, `docs/specs/README.md`, the project spec index when one
   exists, and the smallest active contract set governing the task.
2. Classify work as Restore, Reconcile, Evolve, Discover, or
   Behavior-neutral.
3. Establish a Contract Change Envelope with authorized and protected domains,
   evidence requirements, allowed spec delta, release baseline, and contract
   revision.
4. State a provisional Spec Basis.
5. Inspect the smallest complete applicable source, design, QA, runtime,
   history, upstream, and release evidence set.
6. Classify every material discrepancy.
7. Accept only a legitimate Contract Delta and update the spec first when
   meaning changes.
8. State the final reconciled Spec Basis with a pinned revision or epoch.
9. Only then implement and verify the authorized slice.

The specification system is canonical intended behavior but is not infallible
or self-authorizing. Spec-first is not spec-only. Current code, stale tests,
implementation convenience, or agent preference cannot be written into a spec
and then cited as authority.

Explicit brownfield discovery is the narrow exception. Record the missing or
unreliable contract first, inspect source and runtime only as evidence,
separate observed from intended behavior, and create first-pass specs without
changing product implementation.

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
