# Strict Spec-First Workflow

This document is the compact canonical workflow for projects that use
`spec-first-bootstrap`.

Its purpose is to make intended product behavior explicit before implementation
choices begin shaping it. The active specification system frames the work
first; applicable source, design, QA, runtime, history, and release evidence
then complete the product picture before implementation.

The full reusable contract is in
`docs/agent-governance/product-truth-governance.md` in this Bootstrap. An
installed project normally keeps its copy under `docs/agent/`.

## Three Separate Layers

1. `docs/specs/` defines intended product behavior.
2. Design and implementation realize that contract and establish current
   structure and ownership.
3. Tests, QA, runtime output, screenshots, history, and release records establish
   observed behavior, acceptance, and compatibility.

The specification system is the canonical product artifact, but it is not
infallible or self-authorizing. The other layers may expose a missing, stale,
ambiguous, or contradictory spec. They do not silently replace it, and a spec
edit cannot turn an agent preference or current defect into product intent.

Spec-first therefore does not mean spec-only.

## Tasks Covered By The Gate

The gate applies to:

- new product features;
- observable behavior changes;
- behavioral bugs and regressions;
- behavioral investigations and product-behavior planning;
- UX, state, route, persistence, permission, eligibility, compatibility, or
  data-contract changes;
- multi-step user flows;
- product transfers, ports, rewrites, and migrations;
- refactors whose behavioral impact is possible or uncertain;
- product QA and release behavior.

It normally does not require a product-contract change for formatting,
comments, documentation-only maintenance, or proven behavior-neutral internal
cleanup. If impact is uncertain, the gate applies.

## Change Mode And Envelope

Classify every covered task before implementation:

- **Restore**: bring implementation back to an established contract.
- **Reconcile**: recover or faithfully transfer one existing product truth
  into a complete current contract.
- **Evolve**: implement a semantic change the user requested in a named domain.
- **Discover**: understand a product whose contract is missing or unreliable,
  without changing implementation.
- **Behavior-neutral**: make a proven non-behavioral change.

Establish a bounded Contract Change Envelope. For a small task it may be in the
first progress update; for long-running, multi-agent, accepted, released, or
cross-domain work it should be durable.

```text
Contract Change Envelope
- Task and change mode:
- User-authorized outcome:
- Authorized domains or clauses:
- Protected adjacent domains:
- Stability or release baseline:
- Required evidence:
- Allowed and forbidden spec delta:
- Material decisions requiring the user:
- Current contract revision or epoch:
- Required review and QA:
```

The user's request opens only the product domain and behavior it actually
names. A writable source path does not open every product contract implemented
by that file.

## Required Start Order

Before implementation for a covered task:

1. Read every applicable global and project instruction layer.
2. Read `docs/specs/README.md`, the authority index when one exists, and the
   smallest active contract set that governs the task.
3. Classify the change mode and establish the Contract Change Envelope.
4. State a provisional Spec Basis.
5. Inspect the smallest complete applicable source, design, QA, runtime,
   history, upstream, and release evidence set.
6. Classify every material discrepancy.
7. Accept only a legitimately authorized Contract Delta and update the spec
   before implementation when meaning changes.
8. State the final reconciled Spec Basis with a pinned revision or epoch.
9. Only then implement and verify the authorized slice.

Use this provisional form:

```text
Provisional Spec Basis
- Task and change mode:
- Authoritative specs and clauses:
- Expected behavior:
- Invariants and protected domains:
- Apparent gaps or conflicts:
- Required evidence:
- Allowed spec impact:
- Implementation authorized: yes / no
```

Use this final form:

```text
Final Reconciled Spec Basis
- Contract revision or epoch:
- Governing clauses:
- Resolved intended behavior:
- Evidence inspected and its role:
- Discrepancy dispositions:
- Accepted Contract Delta:
- Protected adjacent domains:
- Required acceptance scenarios:
- Implementation authorized: yes / no
```

The provisional basis frames the investigation. It is not permission to stop
at Markdown or turn the first mismatch into a user decision.

## Evidence And Discrepancies

Use the smallest complete evidence set that can settle the task. Do not sample
only the artifact that supports the easiest conclusion, and do not create a
broad audit when a bounded slice is sufficient.

Classify each material mismatch as:

- **implementation defect**: the contract remains correct;
- **specification defect or omission**: accepted evidence and task authority
  establish one existing behavior missing from the contract;
- **stale or inapplicable evidence**: an old test, design, source, or runtime
  observation no longer governs;
- **authorized evolution**: the user requested changed behavior inside the
  open domain;
- **real product fork**: complete evidence leaves materially different valid
  outcomes;
- **external authority blocker**: continuation requires credentials,
  destructive action, policy input, physical access, or another outside
  authority.

Current code alone, a test alone, implementation convenience, platform
convention, or the spec edit itself is not semantic product authority.

Do not invent behavior, write it into a spec, and then cite that edit as
permission to implement it.

## Missing Or Conflicting Specs

When no adequate contract exists, use Discover or Reconcile as justified:

1. record the gap;
2. inspect the complete applicable evidence without changing implementation;
3. separate observed behavior from intended behavior;
4. create or repair the correct contract;
5. ask the user only when a material product decision remains after evidence
   reconciliation.

When active contracts conflict, follow explicit precedence or supersession.
If no precedence exists, stop the affected slice and return the exact conflict.
Never use current code merely to choose which product rule should win.

## Behavioral Diagnosis

For a behavioral defect:

1. establish expected behavior from the active and accepted or released
   contract;
2. establish actual behavior from applicable source, QA, and runtime evidence;
3. name and classify the discrepancy;
4. use Restore when the contract remains correct;
5. use Reconcile only when the contract is proven stale or incomplete;
6. use Evolve only when the user requested new behavior.

Do not convert a bug into a spec change because editing the expectation is
easier than fixing implementation.

## Implementation Ordering

When intended behavior legitimately changes, update the contract before the
first implementation edit and record a compact Contract Delta.

Spec and code may share one checkpoint commit. The rule is about authority and
working order, not mandatory commit separation.

Planning-only and investigation-only requests remain hard implementation
boundaries.

## Brownfield Discovery

Brownfield discovery is the narrow exception to a complete-contract gate.

Before broad source inspection, record that the relevant contract is missing
or unreliable. Then inspect code, routes, state, tests, docs, design, QA,
runtime, history, and released behavior as evidence; create a product map,
spec backlog, first-pass contracts, unknowns, and conflicts; and do not change
product implementation.

Once first-pass contracts exist, later slices use Restore, Reconcile, or
Evolve.

## Spec Index, Stability, And Revisions

Mature projects keep a small authority registry, normally
`docs/specs/index.md`.

It records:

- contract and domain identifiers;
- authority: Draft, Active, Superseded, or Historical;
- stability: Evolving, Accepted, Released, or Deprecated;
- when to read each contract;
- precedence and shared dependencies;
- latest accepted or released baseline.

Authority identifies which contract governs. Stability identifies how strongly
existing behavior is protected.

A semantic contract change advances the affected revision or epoch. Open
multi-agent packets using changed clauses must be revalidated or retired before
their work can be accepted.

## QA And Acceptance

QA verifies a pinned contract through preconditions, actions, state
transitions, intermediate results, final results, and failure or recovery
behavior.

QA does not independently create product intent. A green suite cannot authorize
a product change or prove an unexercised user journey. Runtime and visual
evidence cannot be replaced by unit tests when the contract requires observable
behavior.

## Repository Enforcement

Put a compact routing gate near the top of `AGENTS.md`. Keep the full governance
document outside automatically loaded instructions. Workers without product
authority receive only the finite clauses, evidence paths, protected
boundaries, and acceptance conditions required by their task.

The first progress update for covered work should show the envelope and
provisional basis. The final response should identify the final governing basis,
accepted Contract Delta, verification, and residuals.

## Migration Audit

When repairing an existing project's workflow:

1. read and preserve all existing project instructions;
2. keep project-specific safety, build, test, release, and Git rules;
3. merge the compact gate instead of replacing the instruction file;
4. install the full governance document conditionally;
5. replace code-first and spec-only shortcuts with the provisional-evidence-
   final sequence;
6. establish authority, stability, precedence, revisions, and QA mapping;
7. update day-to-day and brownfield prompts without changing product code;
8. verify Markdown, links, contradictions, and changed-file scope;
9. follow the target repository's checkpoint policy.

Use `prompts/repair-spec-first-workflow.md` for a ready-to-send repair contract.
