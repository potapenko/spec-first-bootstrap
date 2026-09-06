# Workflow Compatibility and Local Overrides

- Change ID: `bootstrap.delta.2026-09-06.workflow-compatibility`
- Mode: Evolve
- Authority: user approved the audit's implementation plan on 2026-09-06.
- Domain: `bootstrap.governance`
- Revision: `bootstrap.governance@15` → `bootstrap.governance@16`.

## Authorized change

Install linked shared work rules instead of repeated full definitions. Preserve
the first substantive implementation planning gate and approval across follow-ups,
skills, and compaction. Preserve local overrides explicitly; use local commits
globally and project opt-in for automatic push. This repository still pushes.

Select and retain single-agent or coordinated goal execution from actual work,
honoring user choice. Coordinator-only boundaries apply in coordinated mode.
Follow mandatory host impasse transitions after independent work is exhausted.
Blocked never means complete. Required independent acceptance remains unchanged.

The separate local deployment removes conflicting Product Design routing through
plugin configuration, without copying model names into portable governance.

## Evidence and compatibility

The approved audit compared installed instructions with Bootstrap and the
[official model guide](https://developers.openai.com/api/docs/guides/latest-model).
It found conflicting skill gates, repeated rules, checkpoint policy differences,
and unconditional delegation/host-state rules. These justify the named changes;
the model guide does not itself authorize removing operator safeguards.

Revisions: installation @3, task-scope @7, restart-delivery @4, goal-continuity @2,
review @4. Markdown routing, product truth, current-branch protection, safety,
independent-review risk triggers, and model/application defaults remain protected.

Acceptance: structural routing/install checks and the scenarios in
[workflow compatibility](../../../qa/cases/workflow-compatibility.md).
Model observations are bounded evidence, not a guarantee of future compliance.
