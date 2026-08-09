# Product Specifications

This directory is the product behavior layer.

It captures expected user-visible behavior for complex features before
implementation begins.

Specs are lightweight and product-oriented.
They define **what the system must do**, not how it is implemented.

QA cases are separate verification artifacts.
They provide evidence but do not replace the product contract.

The specification system is the canonical product artifact, but it is not
infallible or self-authorizing. Source, design, runtime behavior, QA, history,
and release records answer different questions and must be reconciled before
final implementation authority. Spec-first does not mean spec-only.

## Authority and evidence

Active specs define intended product behavior. Source code, tests, runtime
output, screenshots, and Git history establish current behavior and ownership.
They may reveal a missing or stale contract, but they do not silently override
product intent.

Use a project spec index to record both contract authority
(Draft/Active/Superseded/Historical) and domain stability
(Evolving/Accepted/Released/Deprecated). Resolve conflicts and precedence in
the specification system instead of choosing a winner from current code.

## Provisional and final Spec Basis

For every product feature, behavioral bug, behavioral investigation,
product-behavior plan, transfer, or potentially behavioral refactor:

1. start at the spec index and read the complete directly applicable governing
   set before implementation evidence;
2. classify the work and establish a bounded Contract Change Envelope;
3. state the exact documents read and a provisional Spec Basis separating
   specified expectation, protected behavior, established flow, and evidence
   still needed;
4. inspect the smallest complete applicable evidence set;
5. classify discrepancies;
6. accept only a legitimately authorized Contract Delta;
7. state the final reconciled Spec Basis with a pinned revision or epoch;
8. only then implement.

The full gate is defined in `docs/spec-first-workflow.md`.

## What lives here

- product goals for complex features
- scope and non-goals
- user-visible behavior
- invariants that must not regress
- important thresholds and state or route implications
- failure policy and edge cases
- optional links to representative verification coverage
- stable domain, clause, and QA scenario identifiers in mature projects
- evidence mappings when a behavior needs source, design, runtime, upstream, or
  release reconciliation

In this bootstrap repository, [`index.md`](index.md) and `features/` govern the
observable behavior of the Bootstrap itself. Production-style target-product
examples live under `examples/` and remain non-authoritative reference
material.

When this workflow is installed in a real project, `docs/specs/features/`
should contain that project's own specs only.

## What does not live here

- agent workflow and operational rules
  - keep those in `AGENTS.md`
- step-by-step selector-level validation
  - keep those in `qa/` or test directories
- styling system rules
  - keep those in styling docs
- deep implementation notes that are only useful at code level
  - keep those near the source

## How to use this directory

1. Read the project spec index.
2. Read every active spec and directly linked governing document relevant to
   the task completely.
3. Establish the change mode and envelope.
4. State the exact documents read and the provisional Spec Basis.
5. Inspect the smallest complete applicable source, design, QA, runtime,
   history, upstream, and release evidence set.
6. Classify discrepancies and accept only a legitimate Contract Delta.
7. Update the contract before implementation when intended meaning changes.
8. Pin the final basis to a revision or epoch.
9. Keep normative contracts short and product-level; put hashes, captures, and
   mechanical proof in evidence artifacts.

Explicit brownfield discovery is the exception. Record that the contract is
missing, inspect source only as evidence for first-pass specs, and do not change
implementation during the discovery pass.

## Reading guide

- **User-visible behavior** defines expected behavior.
- **Invariants** define rules that must never break.
- **Edge cases** define how the system behaves under imperfect input.
- This document is a contract, not an explanation.

## Scope rule

Create or update a spec when a task:

- introduces a new feature
- changes observable behavior
- introduces or modifies route, state, or data contracts
- affects multi-step user flows
- changes gating, permissions, or eligibility logic
- touches onboarding, search, filtering, playback, publishing, or similar flows
- introduces behavior that could be misunderstood later

Skip new specs for:

- pure refactors
- formatting-only changes
- comments-only edits
- behavior-neutral internal cleanups

## Structure

```text
docs/specs/
  README.md
  index.md
  templates/
    feature-spec.md
    spec-index.md
    contract-change-envelope.md
    contract-delta.md
    release-contract-baseline.md
  features/
    bootstrap-governance.md
    codex-lifecycle-enforcement.md
```

## Spec philosophy

- Specs are contracts, not documentation.
- Specs should be short but precise.
- Authorized semantic changes update specs before implementation.
- A spec edit cannot create its own product authority.
- Specs should reflect what users experience, not internal structure.

## Relationship with other layers

- `AGENTS.md` defines workflow and rules for agents.
- `docs/specs/` defines product behavior.
- `qa/` or tests define verification and evidence.

These layers must stay separate.

## Goal

Make product behavior explicit before code begins.
