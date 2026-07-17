# Strict Spec-First Workflow

This document is the canonical workflow for projects that use
`spec-first-bootstrap`.

Its purpose is simple: intended product behavior must be established from the
active specs before implementation code is used to design, diagnose, or change
that behavior.

## Three Separate Layers

1. `docs/specs/` defines intended product behavior.
2. Implementation code realizes that contract.
3. Tests, QA, runtime output, screenshots, and history verify or explain the
   implementation.

The second and third layers may expose a missing, stale, or contradictory spec.
They must not silently replace the first layer as product truth.

## Tasks Covered By The Gate

The Mandatory Spec Gate applies to:

- new product features;
- observable behavior changes;
- behavioral bugs and regressions;
- behavioral investigations and product-behavior planning;
- route, state, persistence, permission, eligibility, or data-contract changes;
- multi-step user flows;
- refactors whose behavioral impact is possible or uncertain.

It normally does not require a feature spec for formatting, comments,
copy-only work, documentation-only maintenance, or proven behavior-neutral
internal cleanup. If impact is uncertain, the gate applies.

## Required Start Order

Before opening implementation source for a covered task:

1. Read the project's active instruction files, starting with `AGENTS.md`.
2. Read `docs/specs/README.md` and the project spec index when one exists.
3. Select and read every active spec that governs the task.
4. State a compact **Spec Basis** in the plan or first progress update.
5. Resolve missing or conflicting behavior in the specs.
6. Only then inspect implementation source, tests, runtime evidence, or Git
   history.

Use this template:

```text
Spec Basis
- Task:
- Authoritative specs:
- Expected behavior:
- Invariants and edge cases:
- Gaps or conflicts:
- Required spec impact:
- Implementation authorized: yes / no
```

The Spec Basis is deliberately observable. It lets the user verify that the
agent found the right contract before code begins shaping the answer.

## Missing Or Conflicting Specs

When no adequate spec exists:

1. state the gap;
2. create a first-pass spec or update the correct existing spec;
3. settle behavior that follows directly from the user's request;
4. ask the user only when a material product choice remains ambiguous;
5. do not edit implementation until the contract is explicit.

When active specs conflict:

- follow explicit `canonical`, `governs`, `wins`, or `supersedes` language;
- treat historical, legacy, and deferred specs as evidence only;
- if precedence is not explicit, update the index or specs before proceeding;
- never use current code to choose which product rule should win.

## Behavioral Diagnosis

Behavioral investigation has a fixed order:

1. derive expected behavior from the active specs;
2. derive actual behavior from code, tests, runtime evidence, and history;
3. state the exact discrepancy;
4. decide whether the spec is already correct or needs a product change;
5. only then propose or implement the fix.

A bug fix that restores an already explicit contract may not require new
product behavior, but the agent must still name the governing spec before
reading code. If the fix changes the contract, edit the spec first.

## Implementation Ordering

For a behavior change, the spec edit must happen before the first
implementation edit. Spec and code may share one checkpoint commit; the rule is
about reasoning and working order, not mandatory commit separation.

High-risk or cross-cutting changes may use a separate spec checkpoint when that
makes review, approval, or restartability clearer.

Planning-only and investigation-only requests are hard boundaries. Reading a
spec or discovering a plausible fix does not authorize implementation.

## Brownfield Discovery

Brownfield projects may not yet have reliable specs. This is the narrow
exception to source-after-spec ordering.

Before source inspection, record that the relevant contract is absent or
unreliable. Then:

1. inspect code, routes, state, tests, docs, and UI flows as evidence;
2. separate observed behavior from intended behavior;
3. create a product map and active-spec backlog;
4. write first-pass specs with unknowns and conflicts called out;
5. do not modify product implementation during the discovery pass.

Once first-pass specs exist, ordinary work returns to the Mandatory Spec Gate.

## Spec Index And Lifecycle

Mature projects should keep a small authority registry, normally
`docs/specs/index.md`, that identifies:

- active specs and when to read them;
- explicit precedence between overlapping contracts;
- historical, legacy, deferred, or superseded material;
- the smallest active slice needed for a task.

Historical material may remain in the repository, but it must not look equally
authoritative. Use explicit status metadata, a separate archive directory, or
both.

## Repository Enforcement

Put the compact Mandatory Spec Gate near the top of `AGENTS.md`, before
lower-priority build and workflow detail. Repeat only routing, not competing
versions of the rule, in onboarding and prompt files.

For stronger enforcement, projects may add a hook or preflight that blocks
implementation edits until the task records its Spec Basis. Review and CI can
also require a declared spec impact for behavior-changing diffs.

At minimum, an agent's first progress update for a covered task should make the
Spec Basis visible, and the final response should identify the governing specs
and any spec changes.

## Migration Audit

When repairing an existing project's spec-first workflow:

1. read all applicable `AGENTS.md` and onboarding files;
2. preserve project-specific safety, build, test, and Git rules;
3. move the Mandatory Spec Gate close to the top-level entry point;
4. replace phrases such as `before or alongside implementation` with explicit
   spec-before-implementation ordering;
5. require a visible Spec Basis before implementation source is opened;
6. make behavioral diagnosis spec-first, evidence-second;
7. make planning-only wording a hard implementation stop;
8. establish or repair the active spec index and lifecycle labels;
9. update day-to-day and brownfield prompts to match the same contract;
10. do not change product implementation during the workflow-migration task;
11. verify the resulting docs for contradictions and broken links;
12. create a scoped checkpoint according to the target repository's Git rules.

Use `prompts/repair-spec-first-workflow.md` as the ready-to-send migration
prompt for another project.
