# AGENTS.md

This file defines workflow rules for agents working in this repository.

It is not the source of truth for detailed feature behavior.
Detailed feature behavior must live in `docs/specs/`.

## Mandatory Spec Gate

Follow `docs/spec-first-workflow.md` for the full contract.

The gate applies to every product feature, behavioral bug, behavioral
investigation, product-behavior plan, and refactor that may affect observable
behavior.

1. Read this `AGENTS.md`, `docs/specs/README.md`, the project spec index when it
   exists, and every active spec relevant to the task.
2. Before opening implementation source, state a compact **Spec Basis**:
   authoritative spec paths, expected behavior, invariants, gaps or conflicts,
   required spec impact, and whether implementation is authorized.
3. If the contract is missing or conflicting, create or update the spec first.
4. For a behavior change, edit the spec before the first implementation edit.
5. Only then inspect source, tests, runtime evidence, or history. They establish
   current behavior and ownership; they do not override product intent.
6. For a behavioral bug, derive expected behavior from specs first, actual
   behavior from evidence second, and name the discrepancy before fixing it.
7. Planning-only or investigation-only wording is a hard stop on implementation
   until the user explicitly authorizes code changes.

Explicit brownfield discovery is the narrow exception. When no reliable spec
exists, record that gap first, inspect source only as evidence, and create
first-pass specs before implementation begins.

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

Implement against the Spec Basis, not against ad-hoc chat memory or behavior
inferred from source. If behavior changes, update the spec before the first
implementation edit.

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
