# Optional Codex Lifecycle Enforcement

- Node type: leaf
- Status: Active
- Contract ID: `bootstrap.codex-lifecycle`
- Domain ID: `bootstrap.codex-lifecycle`
- Authority: Active
- Stability: Evolving
- Contract revision: `bootstrap.codex-lifecycle@3`
- Clauses: `CODEX.LIFECYCLE.ROOT`, `CODEX.LIFECYCLE.WORKER`,
  `CODEX.LIFECYCLE.COMPACTION`, `CODEX.LIFECYCLE.INSTALL`
- Read when: changing the optional Codex lifecycle adapter.
- Do not read when: changing portable Markdown routing without adapter mechanics.
- Maximum size: 100 physical lines.

## Goal and scope

Reinforce the active instruction hierarchy after startup, resume, clear,
compaction, and worker-start events. Cover project/global templates,
installation, trust, deduplication, and fixtures.

The adapter does not install other governance layers, inject full specs or
conversations, change model/application defaults, or prove that files were read.

## Required behavior

- Root events inject a concise checklist to restore instructions, objective,
  envelope, latest Markdown traversal path, selected nodes, and next evidence.
- Worker events require the finite packet and only its linked contract nodes.
- Compaction restores context before the immediate continuation request.
- Root traversal restarts at the Markdown root only when the task changed or
  the prior path is missing or ambiguous.
- Existing hooks are preserved and equivalent hooks are reconciled.
- Setup reports any required trust-review step.

## Invariants and failure policy

The adapter is optional and Codex-specific. It reinforces `AGENTS.md` and
never replaces it. Global and project hooks are not both installed for one
scope without explicit choice. Output stays concise and contains no secrets.

Malformed input produces a conservative root response. Unsupported events fall
back to root context. Setup stops when the active Codex home or trusted project
root cannot be resolved.

## Evidence and verification

Evidence: Codex hook documentation, lifecycle integration README, templates,
implementation script, and fixtures.

Verify all four root sources, worker startup, malformed input, template parsing,
event-specific context, Markdown-path restoration, sibling exclusion, and
absence of mandatory JSON routing state.
