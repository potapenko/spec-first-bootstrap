# Feature Specs

This directory is the product behavior layer.

It captures expected user-visible behavior for complex features before
implementation begins.

Specs are lightweight and product-oriented.
They define **what the system must do**, not how it is implemented.

QA cases are separate verification artifacts.
They provide evidence but do not replace the product contract.

## Authority and evidence

Active specs define intended product behavior. Source code, tests, runtime
output, screenshots, and Git history establish current behavior and ownership.
They may reveal a missing or stale contract, but they do not silently override
product intent.

Use a project spec index to distinguish active contracts from historical,
legacy, deferred, or superseded evidence. Resolve conflicts in specs or their
index instead of choosing a winner from current code.

## Mandatory Spec Basis

For every product feature, behavioral bug, behavioral investigation,
product-behavior plan, or potentially behavioral refactor, state the Spec Basis
before opening implementation source:

- authoritative spec paths;
- expected user-visible behavior;
- invariants and edge cases;
- gaps or conflicts;
- required spec impact;
- whether implementation is authorized.

The full gate is defined in `docs/spec-first-workflow.md`.

## What lives here

- product goals for complex features
- scope and non-goals
- user-visible behavior
- invariants that must not regress
- important thresholds and state or route implications
- failure policy and edge cases
- optional links to representative verification coverage

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
3. State the Spec Basis before opening implementation source.
4. If the contract exists but must change, update it before editing code.
5. If it is missing, create a new spec using the template before implementation.
6. Keep the spec short and product-level.
7. Use existing behavior, tests, and documentation as evidence after the Spec
   Basis, but write the contract in clear product language.

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
  templates/
    feature-spec.md
  features/
    <feature-name>.md
```

## Spec philosophy

- Specs are contracts, not documentation.
- Specs should be short but precise.
- Specs should be updated before implementation changes to behavior.
- Specs should reflect what users experience, not internal structure.

## Relationship with other layers

- `AGENTS.md` defines workflow and rules for agents.
- `docs/specs/` defines product behavior.
- `qa/` or tests define verification and evidence.

These layers must stay separate.

## Goal

Make product behavior explicit before code begins.
