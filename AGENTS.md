# AGENTS.md

This file defines workflow rules for agents working in this repository.

It is not the source of truth for detailed feature behavior.
Detailed feature behavior must live in `docs/specs/`.

## Global and project-local instruction scopes

Global Codex-home AGENTS.md rules apply across repositories. This
repository-root AGENTS.md owns project-specific workflow and bootstrap
maintenance.

Read every applicable instruction layer. Preserve the stronger compatible
constraint. Never promote project-specific product, framework, safety, build,
test, database, storage, or release rules into the global layer merely because
one repository needs them.

Reusable global and project-local installation sources live under
`docs/agent-governance/`. Installer prompts live under `prompts/`.

## Product Truth Gate

Follow `docs/spec-first-workflow.md` for the compact canonical workflow.
For product-truth or governance work in this repository, also read
`docs/agent-governance/product-truth-governance.md`.

The gate applies to every product feature, behavioral bug or investigation,
product-behavior plan, UX/state/data-contract change, transfer, migration,
product QA task, and refactor that may affect observable behavior.

1. Read applicable global and project-local instructions, the spec README and
   index, and the smallest active contract set governing the task.
2. Classify the task as Restore, Reconcile, Evolve, Discover, or
   Behavior-neutral.
3. Establish a Contract Change Envelope naming authorized and protected
   domains, required evidence, permitted spec delta, release baseline, and
   contract revision.
4. State a provisional Spec Basis before implementation evidence.
5. Inspect the smallest complete applicable source, design, QA, runtime,
   history, upstream, and release evidence set.
6. Classify every material discrepancy.
7. Accept any legitimate Contract Delta and update the spec first.
8. State the final reconciled Spec Basis with a pinned revision.
9. Only then implement and verify the authorized slice.

The specification system is canonical product intent but is not infallible or
self-authorizing. Spec-first is not spec-only. Current code, stale tests,
implementation convenience, or agent preference cannot be written into a spec
and then cited as authority.

The user's request opens only the domain and behavior it actually names.
Adjacent Accepted, Released, and shared-consumer contracts remain protected.

Explicit brownfield discovery is the narrow exception. When no reliable spec
exists, record that gap first, inspect the complete applicable evidence as
evidence, separate observed from intended behavior, and create first-pass specs
without changing implementation.

## When a spec is required

Create or update a spec when a task:

- introduces a new feature
- changes observable behavior
- introduces or modifies route, state, or data contracts
- affects multi-step user flows
- changes gating, permissions, or eligibility logic
- changes an Accepted or Released compatibility contract
- introduces behavior that could be misunderstood later

A new spec is usually not required for:

- pure refactors
- formatting-only changes
- comments-only edits
- behavior-neutral internal cleanup

## Separation of concerns

- `AGENTS.md` defines workflow and agent rules.
- `docs/specs/` defines product behavior.
- `docs/agent-governance/` defines reusable workflow source artifacts.
- `qa/` or tests define verification and evidence.

Do not merge these layers into one file.

## Implementation rule

Implement against the final pinned Spec Basis, not ad-hoc chat memory. If
behavior changes under legitimate Evolve or Reconcile authority, update the
spec first and record the Contract Delta. If evidence reveals an unapproved
contract discrepancy, stop that slice and return the evidence rather than
rewriting intent or creating a workaround.

An accepted semantic change advances the affected contract revision or epoch.
Open packets using affected clauses must be revalidated or retired.

## Verification rule

If a task changes behavior, update or add appropriate verification artifacts.
Verification can be browser-based, backend-based, API-based, or otherwise project-appropriate.

QA verifies pinned action-state-result contracts. It does not independently
authorize product intent or weaken expectations solely to obtain a green
result.

## Writing style for specs

Specs should be:

- short
- explicit
- product-level
- behavior-oriented

Avoid deep implementation detail unless it is necessary to preserve the product contract.
