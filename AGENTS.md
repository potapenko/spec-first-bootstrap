# AGENTS.md

This file defines workflow rules for agents working in this repository.

It is not the source of truth for detailed feature behavior.
Detailed feature behavior must live in `docs/specs/`.

## Reading order

Before doing implementation work:

1. Read this `AGENTS.md`.
2. Read `docs/specs/README.md`.
3. Read the relevant feature spec if one exists.
4. Only then implement or modify behavior.

## Spec-First Rule

Before implementing any non-trivial feature:

1. Clarify the product goal.
2. Create or update a spec under `docs/specs/`.
3. Confirm user-visible behavior, invariants, and edge cases.
4. Only then begin implementation.

## When a spec is required

Create or update a spec when a task:

- introduces a new feature
- changes observable behavior
- introduces or modifies route, state, or data contracts
- affects multi-step user flows
- changes gating, permissions, or eligibility logic
- introduces behavior that could be misunderstood later

A new spec is usually not required for:

- pure refactors
- formatting-only changes
- comments-only edits
- behavior-neutral internal cleanup

## Separation of concerns

- `AGENTS.md` defines workflow and agent rules.
- `docs/specs/` defines product behavior.
- `qa/` or tests define verification and evidence.

Do not merge these layers into one file.

## Implementation rule

Implement against the spec, not against ad-hoc chat memory.
If behavior changes, update the spec in the same task.

## Verification rule

If a task changes behavior, update or add appropriate verification artifacts.
Verification can be browser-based, backend-based, API-based, or otherwise project-appropriate.

## Writing style for specs

Specs should be:

- short
- explicit
- product-level
- behavior-oriented

Avoid deep implementation detail unless it is necessary to preserve the product contract.
