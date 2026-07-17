# Prompt Pack

Use these prompts as a starting point when you point Codex or Claude Code at
this bootstrap repository.

Step 1: set up spec-first development

```text
Use https://github.com/potapenko/spec-first-bootstrap as the reference and set up this project for spec-first development.

Read the bootstrap repository and docs/spec-first-workflow.md first. Add or adapt the needed AGENTS.md, the docs/specs README and template layer, and prompts. Require a visible Spec Basis before implementation source is opened. If this is an existing project, do brownfield discovery and create project-specific first-pass specs before changing implementation code.
```

Optional step 2: add browser QA for a web UI project

```text
Use https://github.com/potapenko/spec-first-bootstrap as the reference and add the optional browser-QA layer to this web UI project.

Assume the spec-first bootstrap from step 1 is already installed. Read qa/README.md, qa/web/README.md, and qa/web/AGENTS.snippet.md from the bootstrap repository. Add or adapt the qa/web files for this project, and merge the qa/web/AGENTS.snippet.md routing block into the project's AGENTS.md so browser-QA instructions load automatically. Keep browser QA optional and do not change product code.
```

The files below are follow-up prompts for specific situations.

Available prompts:

- [`greenfield-bootstrap.md`](greenfield-bootstrap.md)
- [`brownfield-discovery.md`](brownfield-discovery.md)
- [`brownfield-interview.md`](brownfield-interview.md)
- [`generate-first-specs.md`](generate-first-specs.md)
- [`optional-web-qa.md`](optional-web-qa.md)
- [`day-to-day-spec-first.md`](day-to-day-spec-first.md)
- [`repair-spec-first-workflow.md`](repair-spec-first-workflow.md)
