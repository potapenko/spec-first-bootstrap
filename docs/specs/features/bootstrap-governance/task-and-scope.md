# Task Framing and Work Scope

- Node type: leaf
- Status: Active
- Contract: `bootstrap.governance.task-scope@7`
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

Approval persists across follow-ups and compaction. A complete brief or an
approved plan is not reopened by a skill's generic confirmation workflow.
Ask only for a material unresolved decision or genuinely new authority.

## Authority modes

Every approved implementation plan declares one authority mode. `bounded`
permits only the named paths, operations, and behavior; everything else is
protected. `task-wide` permits any repository file reasonably necessary for
the approved outcome without an exact write set, but it does not by itself
authorize unrelated work, destructive action, external-state changes, or work
beyond that outcome. Explicit protected paths or behavior override either mode.
When the mode is absent, use `bounded`.

Path authority never enlarges semantic authority. Permission to edit a file or
change a parent or container does not permit unrelated symbols, behavior,
content, children, data, actions, or accepted layout in that file to change.
Existing accepted behavior outside the named outcome remains protected in both
modes. Every changed diff hunk must map to the authorized outcome; otherwise it
is a scope violation. A required protected-behavior change is returned as a
scope amendment rather than used as a workaround.

## Git and worktree

Use only the branch selected when the task begins. Do not create or switch a
branch or worktree without explicit permission. Existing changes block only
the task-owned bounded paths, or any path a `task-wide` task must modify.
Preserve and exclude every unrelated change.

The global default is a task-owned local checkpoint commit. Automatic push
requires project opt-in. This Bootstrap repository retains commit and push.
Preserve explicit project policy during installation and record its precedence.
For commit-and-push projects, before committing verify a safe, writable upstream
and that the push will not publish unrelated local commits; otherwise do not
create the checkpoint. Completion requires both the checkpoint commit and push
to succeed. Commit-only projects need no upstream. Never include unrelated work.

## Invariants

Writable paths never enlarge product authority. General permission to
implement, commit, or push is not permission to rewrite history, force-push,
change branches, or publish unrelated local commits.
