# Spec-First Bootstrap for AI-Assisted Projects

## Start here

Open your real project in Codex, Claude Code, or another coding agent and paste
this prompt first:

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

That is the normal setup path. Start with step 1. Run step 2 only when the
project has a browser UI and you want browser QA artifacts.

The canonical strict workflow is
[`docs/spec-first-workflow.md`](docs/spec-first-workflow.md). Use
[`prompts/repair-spec-first-workflow.md`](prompts/repair-spec-first-workflow.md)
to repair an existing project whose agents have started reading code before
specs or updating specs only after implementation decisions.

## Why this exists

A lot of AI coding failures are not coding failures.
They happen earlier, when product behavior was never made explicit.
This repo gives the agent a simple place to keep that truth before code starts.

**Do not start with code. Start with a spec.**

## What the agent should do

The agent should:

- read this bootstrap repository first
- preserve existing project-specific agent instructions
- add or adapt `AGENTS.md`
- install the Mandatory Spec Gate from `docs/spec-first-workflow.md`
- add the `docs/specs/` README and template layer
- add useful prompts from `prompts/`
- add `qa/web` only in the optional browser-QA step
- create a product map, spec backlog, or project-specific first-pass specs
  before implementation work starts

This is not just for browser apps. The same model works for web, backend, API,
CLI, data pipelines, internal tools, and other software projects. Browser QA is
optional.

This bootstrap did not come out of theory. It was extracted from several
months of work on four internal projects behind
[`playphrase.me`](https://playphrase.me), then cleaned up into a small public
setup.

If you want the broader context behind this workflow, the main ideas are also
written up in a short article
[here](https://www.patreon.com/posts/spec-first-or-ai-155606468?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link).

## What this is for

Use this repository in either of these situations:

- you are starting a new project and want spec-first work from day one
- you already have a working project and want to migrate it to a spec-first
  workflow

Included:

- a minimal public `AGENTS.md`
- a product-spec layer under `docs/specs/`
- a reusable feature spec template
- an example spec under `examples/`
- prompt files for greenfield and brownfield adoption
- an optional browser-QA starter pack for web UI projects

## Three layers

Instead of keeping product truth scattered across code and chat history, this
workflow keeps three separate layers:

1. `docs/specs/` - product truth
2. implementation - code that follows the contract
3. `qa/` - verification evidence when the project needs it

The rules are simple:

- context should live in specs, not only in code
- code should implement the contract
- QA should verify the contract when the project needs QA artifacts

## Two common scenarios

### Greenfield project

Use this when the project is new or mostly empty.

The agent should:

- set up the spec-first workflow in the new project
- create the initial product-spec structure
- propose the first specs that should exist before feature code

Reference prompt:

- [`prompts/greenfield-bootstrap.md`](prompts/greenfield-bootstrap.md)

### Brownfield project

Use this when the project already exists and you want to retrofit specs.

The agent should:

- analyze the current codebase
- extract product behavior from code, routes, state, tests, UI flows, and docs
- ask for clarification where product intent is unclear
- generate first-pass specs for the most important product areas

In practice, brownfield migration usually means:

1. record where reliable active specs are missing
2. inspect implementation as evidence without changing it
3. map the product
4. build a spec backlog
5. generate first-pass specs
6. review unknowns and conflicts
7. only then start changing code

Reference prompts:

- [`prompts/brownfield-discovery.md`](prompts/brownfield-discovery.md)
- [`prompts/brownfield-interview.md`](prompts/brownfield-interview.md)
- [`prompts/generate-first-specs.md`](prompts/generate-first-specs.md)

## Minimal workflow

Use this workflow for non-trivial work:

1. Read the active specs.
2. State the Spec Basis before opening implementation source.
3. Clarify the product goal.
4. Create or update the spec before implementation edits.
5. Review behavior, invariants, and edge cases.
6. Inspect implementation and implement against the Spec Basis.
7. Add or update verification artifacts if the project needs them.

## Optional web QA layer

Browser QA is **optional**.

Use it if your project has a browser UI and you want a lightweight structure
for smoke checks, regression cases, and run reports.

The optional web QA pack assumes Playwright-style real-browser checks.

Do not treat browser QA as mandatory for every project. Many projects are
better served by API verification, CLI verification, integration testing,
operator runbooks, or other project-specific checks.

If you do have a browser UI, this repo includes a compact starter pack under:

- [`qa/web/README.md`](qa/web/README.md)
- [`qa/web/AGENTS.snippet.md`](qa/web/AGENTS.snippet.md)

And a matching prompt:

- [`prompts/optional-web-qa.md`](prompts/optional-web-qa.md)

## Prompt pack

The default setup prompt above is usually enough.

The files under [`prompts/`](prompts/) are follow-up prompts for specific
situations:

- `greenfield-bootstrap.md`
- `brownfield-discovery.md`
- `brownfield-interview.md`
- `generate-first-specs.md`
- `optional-web-qa.md`
- `day-to-day-spec-first.md`
- `repair-spec-first-workflow.md`

<details>
<summary>Manual install fallback</summary>

Use this only if your agent cannot fetch or inspect the GitHub repository.

Copy these into the target project:

Required:

- `AGENTS.md`
- `docs/spec-first-workflow.md`
- `docs/specs/README.md`
- `docs/specs/templates/`

Recommended:

- `prompts/`

Optional:

- `qa/`

Reference only, not installed as project specs:

- `examples/`

If you copy `qa/`, also add the optional browser-QA routing block from:

- `qa/web/AGENTS.snippet.md`

Without that extra block in the project's `AGENTS.md`, the agent may not load
the QA instructions automatically.

After copying, ask the agent to work from the files already inside the project:

```text
Read AGENTS.md and docs/specs/README.md in this project first.

This is a brownfield project. Generate project-specific first-pass specs before changing implementation code.
```

</details>

## Suggested repository structure

```text
.
├── AGENTS.md
├── README.md
├── docs/
│   ├── spec-first-workflow.md
│   └── specs/
│       ├── README.md
│       ├── templates/
│       │   └── feature-spec.md
│       └── features/
│           └── <project-feature>.md
├── examples/
│   └── favorites-spec.md
├── prompts/
│   ├── README.md
│   └── *.md
└── qa/
    ├── README.md
    └── web/
        └── ...
```

## Included files

- `AGENTS.md` - minimal workflow rules for agents
- `docs/spec-first-workflow.md` - canonical strict gate and migration audit
- `docs/specs/README.md` - how the spec layer works
- `docs/specs/templates/feature-spec.md` - reusable template
- `examples/favorites-spec.md` - example production-style spec for reference
- `prompts/` - ready-to-send prompts for setup and migration
- `qa/web/` - optional browser-QA starter pack for web UI projects

## License

MIT
