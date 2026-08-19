# Bootstrap Governance and Installation

- Node type: hybrid
- Status: Active
- Contract ID: `bootstrap.governance`
- Domain ID: `bootstrap.governance`
- Authority: Active
- Stability: Accepted
- Contract revision: `bootstrap.governance@8`
- Clauses: `BOOTSTRAP.INSTALL`, `BOOTSTRAP.ROUTING`, `BOOTSTRAP.SCOPE`,
  `BOOTSTRAP.RESTART`, `BOOTSTRAP.PROPORTIONALITY`
- Read when: changing portable Bootstrap setup, governance, prompts, templates, or workflow.
- Do not read when: changing only optional adapter mechanics.
- Maximum size: 100 physical lines.

## Goal

Install strict portable agent workflow without replacing project authority,
inventing product behavior, or silently installing unrelated layers.

## Choose the governing child

- [Installation and layer composition](bootstrap-governance/installation.md) —
  project/global scope, independent layers, and preservation rules.
- [Task framing and work scope](bootstrap-governance/task-and-scope.md) —
  planning gate, approved boundary, current branch, and task-owned files.
- [Markdown-first routing](bootstrap-governance/markdown-routing.md) —
  root/branch/leaf traversal, Markdown links, dependencies, and node limits.
- [Restart and delivery proportionality](bootstrap-governance/restart-and-delivery.md)
  — context recovery, release-path priority, and support-work limits.

## Shared invariants

A specification edit never authorizes itself. Current source, tests, logs,
runtime, screenshots, or chat memory never silently define intended behavior.

Existing project-specific safety, framework, build, database, storage, Git,
release, and operator rules remain protected. Product-truth, agent-work, browser
QA, and optional adapters remain independently installable.

Planning-only, discovery-only, and installation-only work does not authorize
product implementation. Environment-specific model or application defaults are
not copied into portable governance.

## Failure policy

Stop before writing when the active instruction entrypoint is ambiguous, an
existing change overlaps task-owned paths, or a required semantic change lies
outside the approved envelope. Preserve independent completed work.

## Evidence and verification

Evidence lives in `docs/agent-governance/`, `prompts/`, templates, and
installed-project fixtures. Verify Markdown traversal, node sizes, links,
scope preservation, task gates, restart behavior, and changed-file boundaries.
