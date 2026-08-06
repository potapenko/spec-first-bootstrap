# Prompt Pack

The repository-root [`README.md`](../README.md) contains exactly two prompts a
person can copy into Codex, Claude Code, or another coding agent.

The files in this directory contain the detailed contracts that the selected
agent reads and executes.

## Human entry prompts

1. [`setup-project.md`](setup-project.md) configures all three layers inside the
   current project.
2. [`setup-global.md`](setup-global.md) configures all three layers in the
   current user's global agent environment.

The project prompt is the recommended default. The global prompt requires
permission to write outside the current repository and can affect every future
project.

## Layer contracts used by the entry prompts

Project phases:

- [`setup-project-spec-first.md`](setup-project-spec-first.md)
- [`setup-project-agents.md`](setup-project-agents.md)
- [`optional-web-qa.md`](optional-web-qa.md)

Global phases:

- [`setup-global-spec-first.md`](setup-global-spec-first.md)
- [`setup-global-agents.md`](setup-global-agents.md)
- [`setup-global-browser-qa.md`](setup-global-browser-qa.md)

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
