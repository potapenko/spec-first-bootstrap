# Single-Chat Default and Explicit Delegation

- Change ID: `2026-09-09-explicit-delegation`
- Mode: Evolve
- Authority: user requested single-chat execution for every task and goal,
  with additional agents only on explicit request, then approved implementation.
- Domain: `bootstrap.governance`
- Clauses: `BOOTSTRAP.INSTALL`, `BOOTSTRAP.GOAL.*`, `BOOTSTRAP.RESTART`,
  `BOOTSTRAP.ECONOMY`, `BOOTSTRAP.REVIEW.INDEPENDENCE`

## Change

Previously, Bootstrap allowed the agent to select coordinated execution for
independent work, context isolation, or new risks. The installed global rules
required coordination for goals unless the user explicitly forbade delegation.

Every task and goal now defaults to direct execution in the current chat.
Only a scoped, explicit user request authorizes additional agents. Complexity,
skills, local project rules, independent review, and tool availability are not
authorization. Approval to implement or resume a goal is not a delegation request.
The same boundary covers reviewer sessions, nested workers, and equivalent
delegation through another tool or model invocation.

Restore explicit authorization across follow-ups and compaction. An old recorded
mode alone is insufficient. Reconcile existing ownership before resuming direct
work; preserve accepted results and do not dispatch new workers without authority.
No existing goals are resumed or modified during installation.

## Evidence, compatibility, and verification

Evidence: project/global instruction gates, shared work rules, coordinator
activation, installation prompts, README examples, and installation fixtures.
This deliberately changes the execution default and removes automatic
delegation overrides. Explicit user-requested coordinated execution remains.

Protected: goal continuity, specification authority, review evidence standards,
current-branch/checkpoint policy, models, tool availability, lifecycle mechanics,
unrelated global configuration, and other project repositories.

Verification: updated installed-layout fixtures, delegation authorization and
restart scenarios, negative regression checks, and Markdown/Bootstrap validation.
Focused self-review applies to this instruction change; no reviewer agents are
authorized. Structural checks do not establish empirical model obedience.

Revisions: aggregate @18; installation @4; goal-continuity @3;
restart-delivery @6; review @5. Task-and-scope remains @7.
