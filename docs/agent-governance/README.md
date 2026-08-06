# Reusable Agent Governance Sources

This directory contains canonical source documents for the installer prompts
under prompts/.

They are separate from this repository's own AGENTS.md. The local file governs
work in this repository; these sources are portable artifacts for installing
the same product-truth and persistent-goal discipline elsewhere.

## Canonical artifacts

- product-truth-governance.md defines specification authority, evidence
  reconciliation, Change Envelopes, domain stability, release baselines,
  Contract Deltas, contract epochs, agent roles, and QA integration.
- root-orchestration.md defines the coordinator-only primary /root contract for
  running persistent goals.
- agents-sections.md contains compact global and project-local routing
  sections. Only these compact sections belong in an automatically loaded
  AGENTS.md; the full documents remain conditionally loaded.

The canonical documents were synchronized from the accepted global Codex
governance on 2026-08-06.

## Deployment choices

| Need | Prompt | Changes Codex home | Changes target project |
| --- | --- | --- | --- |
| Product-truth governance for every project | prompts/install-global-product-truth-governance.md | yes | no |
| Product-truth governance for one project | prompts/install-project-product-truth-governance.md | no | yes |
| Coordinator-only persistent-goal architecture | prompts/install-persistent-goal-agent-architecture.md | selected explicitly | selected explicitly |

One installer invocation uses one deployment scope. Installing both global and
project-local copies requires an explicit user request and a reason; duplicate
full documents are not created merely for reassurance.

## Installation invariants

- Read every existing instruction layer before editing it.
- Merge; never replace an existing AGENTS.md.
- Preserve unrelated user rules and local safety boundaries.
- Keep full governance documents outside automatically loaded instruction
  files.
- Do not copy project-specific language, framework, database, storage, build,
  or product rules into the global layer.
- A project-only install must work without any global Codex customization.
- A global install must not mutate a project repository.
- Architecture installation must not create, resume, pause, or complete a
  persistent goal.
- Do not launch subagents merely to install governance documents.
- Verify Markdown, paths, duplicate headings, instruction-size limits, and
  changed-file scope.
- When repository files change, follow that repository's scoped checkpoint
  policy.

## Maintenance

When governance changes:

1. update the canonical full document;
2. update only the compact routing section that exposes the change;
3. update installer acceptance checks;
4. update docs/spec-first-workflow.md and reusable templates;
5. verify that global and project-only semantics remain equivalent;
6. preserve the conditional-reading boundary for ordinary workers.

Prompt files are execution contracts, not alternate copies of the governance
doctrine.
