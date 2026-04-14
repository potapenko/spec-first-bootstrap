# Feature Specs

This directory is the product behavior layer.

It captures expected user-visible behavior for complex features before or
alongside implementation.

Specs are lightweight and product-oriented.
They define **what the system must do**, not how it is implemented.

QA cases are separate verification artifacts.
They provide evidence but do not replace the product contract.

## What lives here

- product goals for complex features
- scope and non-goals
- user-visible behavior
- invariants that must not regress
- important thresholds and state or route implications
- failure policy and edge cases
- optional links to representative verification coverage

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

1. Check whether the feature already has a spec.
2. If yes, update it before or alongside the code change.
3. If not, create a new spec using the template.
4. Keep the spec short and product-level.
5. Use existing behavior, tests, and documentation as evidence, but write the contract in clear product language.

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
- Specs should be updated together with behavior changes.
- Specs should reflect what users experience, not internal structure.

## Relationship with other layers

- `AGENTS.md` defines workflow and rules for agents.
- `docs/specs/` defines product behavior.
- `qa/` or tests define verification and evidence.

These layers must stay separate.

## Goal

Make product behavior explicit before code begins.
