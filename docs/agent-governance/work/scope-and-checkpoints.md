# Scope and Checkpoints

- Node type: leaf
- Status: Active
- Read when: editing, assigning ownership, or saving completed work.
- Do not read when: a read-only packet has no ownership or checkpoint question.
- Maximum size: 100 physical lines.

## Authority modes

Every approved implementation plan declares one authority mode:

- `bounded`: only named paths, operations, and behavior may change.
- `task-wide`: any repository file reasonably necessary for the approved
  outcome may change without an exact write set.

An omitted mode defaults to `bounded`. Explicit protected paths and behavior
override either mode. Neither mode authorizes unrelated work, destructive
operations, new external-state actions, or work outside the approved outcome.

Path authority is not semantic authority. Permission to edit a file or change
a parent or container does not authorize unrelated symbols, child content,
actions, data, or accepted layout. Every changed diff hunk must map to the
approved outcome. Do not create adjacent features, refactors, or tooling extras.

For a material dependency outside the boundary, stop the affected slice and
return the exact dependency, minimum scope addition, expected cost, and risk.
Continue independent authorized work; wait before crossing the boundary.

## Current branch and existing work

Use only the branch checked out when the task begins. Do not create, switch,
rename, or publish another branch or create a worktree without explicit user
permission. Permission to implement, commit, or push is not that permission.

Required plans declare bounded paths or task-wide authority before editing.
Existing changes block only paths the task needs to modify. Preserve all other
changes and exclude them from staging and commits. If the user authorizes an
overlay on dirty paths, preserve the original content and checkpoint only the
task's delta; never absorb unrelated edits silently.

## Checkpoint policy and overrides

The global default is a task-owned local checkpoint commit after file changes.
Do not require an upstream for a commit-only policy. Do not report completion
until the applicable checkpoint succeeds.

Automatic push is project opt-in. Preserve a project's explicit checkpoint
policy and record it as a local override; this Bootstrap repository requires
commit and push. For such a policy, before committing establish a safe writable
upstream and that the push publishes no unrelated local commits. If either
cannot be established, do not create the checkpoint. Completion then requires
both commit and push. Never force-push, rewrite history, or publish unrelated
work. Governance installation cannot silently change the target's push policy.
