# Prompt Pack

The repository-root [`README.md`](../README.md) contains the short prompts a
person can copy into Codex, Claude Code, or another coding agent.

The files in this directory contain the detailed contracts that the selected
agent reads and executes.

## Set up one project

Recommended for most users:

1. [`setup-project-spec-first.md`](setup-project-spec-first.md) installs the
   specification and product-truth layer in the current project.
2. [`setup-project-agents.md`](setup-project-agents.md) installs plan-first task
   framing, approved-scope control, outcome/resource proportionality, and
   coordinator-and-workers rules for persistent goals in the current project.
3. [`optional-web-qa.md`](optional-web-qa.md) installs optional browser QA in a
   web UI project.

Each layer is independently selectable. An installer must not install either
of the other layers as a prerequisite or dependency. Choose any one, any two,
or all three. When all three are wanted, the listed order is recommended.

## Set up every project

Advanced global setup:

1. [`setup-global-spec-first.md`](setup-global-spec-first.md)
2. [`setup-global-agents.md`](setup-global-agents.md) installs the same
   plan-first and scope-controlled agent layer in the active user-level
   instruction chain.
3. [`setup-global-browser-qa.md`](setup-global-browser-qa.md)

These global layers are also independently selectable. Each installer changes
only its named global layer and preserves any selected or unselected layers
already present.

These prompts modify the active user's agent configuration outside the current
repository. They must detect the active agent environment, state exact target
paths, preserve existing global instructions, and request the required
filesystem permission. They change no project during installation.

## Optional Codex lifecycle adapter

The adapter reinforces whichever instruction layers are already installed. It
is Codex-specific and is not a fourth governance dependency.

- [`setup-project-codex-lifecycle.md`](setup-project-codex-lifecycle.md)
  installs it only in one trusted project.
- [`setup-global-codex-lifecycle.md`](setup-global-codex-lifecycle.md) installs
  it only in the active user's Codex home.

Both prompts preserve existing hooks, avoid duplicate global/project coverage,
and include trust and fixture-test verification.

## Follow-up project work

- [`greenfield-bootstrap.md`](greenfield-bootstrap.md): prepare the first spec
  structure and backlog for a new project.
- [`brownfield-discovery.md`](brownfield-discovery.md): map an existing product
  and create first-pass specifications without changing implementation.
- [`brownfield-interview.md`](brownfield-interview.md): prepare the material
  product questions left after evidence inspection.
- [`generate-first-specs.md`](generate-first-specs.md): write prioritized
  first-pass product specs.
- [`day-to-day-spec-first.md`](day-to-day-spec-first.md): execute ordinary
  specification-first product work.
- [`repair-spec-first-workflow.md`](repair-spec-first-workflow.md): repair a
  project whose specification workflow has drifted.
