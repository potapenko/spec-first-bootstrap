# Work Governance

- Node type: root
- Status: Active
- Read when: planning, implementing, installing agent work, or advancing a goal.
- Do not read when: a bounded read-only answer needs no work-policy decision.
- Maximum size: 100 physical lines.

Read only the linked rules needed for the current action. These are the shared
definitions for ordinary tasks and persistent goals; compact AGENTS gates route
here instead of repeating them.

- [Task framing](work/task-framing.md): first implementation request, approval
  continuity, clarifications, and skill conflicts.
- [Scope and checkpoints](work/scope-and-checkpoints.md): authority modes,
  current branch, existing changes, and local/project checkpoint policy.
- [Minimum-sufficient work](work/minimum-sufficient-work.md): proportionate
  reading, tools, delegation, verification, and completion evidence.
- [Goal execution](work/goal-execution.md): execution mode, readiness, waits,
  host-required transitions, and restart.

Implementation requires task framing, scope, and minimum-sufficient work.
Goal work also requires goal execution. Only coordinated goals load the full
[coordinator contract](root-orchestration.md). Finite workers read their packet
and pinned rules, not the coordinator's complete context.

## Installation and local overrides

Install this root and the `work/` directory together. Resolve all relative links.
Preserve independently installed product-truth, safety, and QA layers.
Host/system instructions take precedence; local text cannot override tool gates.

Keep deliberate target overrides in a named section of the active instruction
chain with their scope, owner, and precedence. Global defaults are inherited;
explicit project rules govern that project. Never convert a local preference
into a portable default or erase it during synchronization.

Update the shared definitions once, then reconcile compact routing gates.
Do not reinstall a full global layer locally merely to repeat the same rules.
Report preserved overrides and any unresolved conflict rather than silently
choosing a new policy. Installing governance does not change model, reasoning,
permissions, concurrency, plugin configuration, or goal state.
