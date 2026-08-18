# Installation and Layer Composition

- Node type: leaf
- Status: Active
- Contract: `bootstrap.governance.installation@1`
- Clause: `BOOTSTRAP.INSTALL`
- Read when: installing or repairing Bootstrap layers in a project or user configuration.
- Do not read when: the task only uses an already installed workflow.
- Maximum size: 100 physical lines.

## Required behavior

- Project setup changes only the named repository.
- Global setup changes only the explicitly selected user-level configuration.
- Installers resolve the active instruction chain, overrides, fallback names,
  and size limits before editing.
- Installers merge a compact routing gate and keep detailed governance in
  linked Markdown nodes.
- Specification, agent-work, browser-QA, and lifecycle layers are independently
  selectable.
- Optional adapters are installed only when explicitly requested.
- Existing project safety, framework, build, test, Git, database, storage,
  release, and operator rules remain intact.
- Target projects receive only their own product contracts, never Bootstrap
  example behavior.

## Non-goals

Installation does not change product implementation, models, provider settings,
reasoning effort, concurrency, permissions, or application defaults.

## Failure policy

If an override shadows the proposed instruction file, update the active chain
or report the exact blocker. If the merged instruction chain exceeds its limit,
remove duplication and route to smaller Markdown nodes rather than relying on
truncation.

## Verification

Confirm the active agent reads the installed gate, every local Markdown link
resolves, all installed nodes stay within 100 physical lines, optional layers
remain absent unless selected, and only task-owned target paths changed.
