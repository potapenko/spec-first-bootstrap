# Task Framing and Work Scope

- Node type: leaf
- Status: Active
- Contract: `bootstrap.governance.task-scope@4`
- Clause: `BOOTSTRAP.SCOPE`
- Read when: planning or executing an implementation-bearing request.
- Do not read when: answering a bounded read-only question with no proposed mutation.
- Maximum size: 100 physical lines.

## First implementation request

Unless a planning-deliverable or explicit-waiver exception below applies,
before the first implementation-bearing action in a chat perform bounded
read-only investigation, present an evidence-based implementation plan, and
wait for explicit approval before editing or mutating external state.

Questions, explanations, reviews, diagnoses, status checks, and Git-history
inspection proceed directly. Findings do not silently turn read-only work into
implementation.

## Planning deliverables and explicit waiver

A request whose requested result is itself a plan is planning-only, including
when the user asks to save that plan in a file for a future goal. Perform the
bounded investigation and produce or save the requested plan directly. Do not
first propose a meta-plan or ask for approval merely to create the plan. This
does not authorize implementation of the work described by that plan.

When the user or operator explicitly directs the agent to execute now or
without a plan, skip the planning-approval gate and begin the authorized task
directly. A generic imperative is not such a waiver. The waiver does not bypass
applicable specification, safety, authorization, destructive-action, or
environment gates and does not expand the requested scope.

## Approved boundary

The approved plan names outcome, exact scope, task-owned paths, protected
behavior, verification, exclusions, and unresolved material decisions.
Equivalent technical choices and directly required verification remain allowed;
adjacent features, cleanup, refactors, or tooling do not.

A newly discovered material dependency outside the plan is returned as the
smallest scope amendment with cost and risk. Independent in-scope work may
continue safely.

## Git and worktree

Use only the branch selected when the task begins. Do not create or switch a
branch or worktree without explicit permission. Existing changes block only
overlapping task-owned paths. Preserve and exclude every unrelated change.

At the end of any task that changes files, create a checkpoint commit in the
currently checked-out branch. The checkpoint is the saved state of the work you
completed, so commit only the files you changed for that task. Unrelated changes
elsewhere in the working tree do not block the checkpoint and remain untouched.
Do not report the task as complete until the checkpoint commit succeeds.

## Invariants

Writable paths never enlarge product authority. General permission to
implement or commit is not permission to rewrite history or change branches.
