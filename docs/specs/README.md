# Feature Specs

This directory is the product behavior layer.

It captures expected user-visible behavior for complex features before
implementation begins.

Specs are lightweight and product-oriented.
They define **what the system must do**, not how it is implemented.

QA cases are separate verification artifacts.
They provide evidence but do not replace the product contract.

## Product truth system

The specification system is the canonical statement of intended product
behavior and the primary product artifact. It is not infallible,
self-authorizing, or a replacement for all other evidence.

- User requests and accepted decisions define what may change now.
- Active specs define intended behavior.
- Design and source define current structure, mechanics, and ownership.
- Runtime establishes actual executable behavior.
- QA defines repeatable action-state-result acceptance evidence.
- Release baselines protect behavior on which users or consumers may rely.

Spec-first means the spec frames the investigation first. It does not mean
spec-only. Before final implementation authority, reconcile the smallest
complete applicable evidence set and classify every discrepancy.

## Authority, stability, and evidence

Active specs define intended product behavior. Source code, tests, runtime
output, screenshots, and Git history establish current behavior and ownership.
They may reveal a missing or stale contract, but they do not silently override
product intent.

Keep authority and stability separate.

Authority:

- Draft
- Active
- Superseded
- Historical

Stability:

- Evolving
- Accepted
- Released
- Deprecated

An Active contract may be Evolving or already Released.

Use a project spec index to record both dimensions, select the smallest
governing contract set, define precedence, and link Accepted or Released
domains to their baseline.

A public deployment is not inferred from an Active label or a green suite.

## Change Envelope and Spec Basis

For every product feature, behavioral bug, behavioral investigation,
product-behavior plan, transfer, or potentially behavioral refactor:

1. classify the task as Restore, Reconcile, Evolve, Discover, or
   Behavior-neutral;
2. establish a Contract Change Envelope;
3. state a provisional Spec Basis before implementation evidence;
4. inspect the smallest complete applicable evidence set;
5. classify discrepancies;
6. accept any legitimate Contract Delta;
7. state the final reconciled Spec Basis with a pinned revision;
8. only then implement.

The envelope and bases identify:

- authorized and protected domains;
- authoritative paths and clause IDs;
- expected user-visible behavior;
- invariants and edge cases;
- gaps or conflicts;
- required evidence;
- required spec impact;
- stability or release baseline;
- contract revision or epoch;
- whether implementation is authorized.

The full gate is defined in `docs/spec-first-workflow.md`.

A specification edit cannot authorize itself. It requires a user decision,
accepted Evolve envelope, accepted Reconcile result, explicit contract
precedence, or a proven non-inventive contradiction correction.

## What lives here

- product goals for complex features
- scope and non-goals
- user-visible behavior
- invariants that must not regress
- important thresholds and state or route implications
- failure policy and edge cases
- optional links to representative verification coverage
- evidence mappings to source, design, runtime, history, upstream contracts,
  and releases
- stable acceptance scenario identifiers

In this bootstrap repository, production-style example specs live under
`examples/`, not under `docs/specs/features/`.

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

1. Read the project spec index when one exists.
2. Read every active spec relevant to the task.
3. Establish the Change Envelope and provisional Spec Basis.
4. Inspect the smallest complete applicable evidence set.
5. Classify discrepancies and accept any legitimate Contract Delta.
6. Update the spec before implementation when intent changes or reconciliation
   is authorized.
7. Pin the final basis to a contract revision or epoch.
8. Keep the normative spec short and product-level.
9. Put source paths, hashes, captures, and mechanical proof in evidence
   artifacts.

Explicit brownfield discovery is the exception. Record that the contract is
missing, inspect source/design/QA/runtime/release state as evidence, separate
observed from intended behavior, and do not change implementation.

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
    <feature-name>.md
```

## Spec philosophy

- Specs are contracts, not documentation.
- Specs should be short but precise.
- Authorized behavior changes update the spec before implementation.
- Reconciliation corrects stale or incomplete specs only from a complete
  accepted evidence basis.
- Specs should reflect what users experience, not internal structure.
- Spec edits do not create their own product authority.

## Relationship with other layers

- `AGENTS.md` defines workflow and rules for agents.
- `docs/specs/` defines product behavior.
- `docs/agent-governance/` defines reusable workflow source artifacts.
- `qa/` or tests define verification and evidence.

These layers must stay separate.

## Goal

Make product behavior explicit before code begins.
