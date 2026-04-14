# Spec-First Bootstrap for AI-Assisted Projects

A lightweight bootstrap for teams and solo builders who want AI to work from
product contracts instead of jumping straight into code.

The core idea is simple:

**Do not start with code. Start with a spec.**

This repository is meant to be pointed at by an agent such as CodeX or Codex.
The agent reads the bootstrap, applies the workflow to your real project, and
generates the first draft of the product specs for you.

## What this is for

Use this repository in either of these situations:

- you are starting a new project and want spec-first work from day one
- you already have a working project and want to migrate it to a spec-first workflow

This repo gives you:

- a minimal public `AGENTS.md`
- a product-spec layer under `docs/specs/`
- a reusable feature spec template
- a real example spec
- prompt files for greenfield and brownfield adoption
- an optional browser-QA starter pack for web UI projects

## Three layers

Instead of keeping product truth scattered across code and chat history, this
workflow keeps three separate layers:

1. `docs/specs/` — product truth
2. implementation — code that follows the contract
3. `qa/` — verification evidence when the project needs it

The point is simple:

- context should live in specs, not only in code
- code should implement the contract
- QA should verify the contract

## Important: this is chat-driven

The user does not need to write specs manually.

The practical workflow is:

1. put this bootstrap into the project
2. point the agent at it
3. explain the goal in chat
4. let the agent generate or update the specs
5. let the agent implement against those specs

The goal is to keep the process automated and simple.
The user mainly works through chat with the agent.

## Quick start

1. Clone this repository from GitHub.
2. Put it into or next to your real project.
3. Open your real project locally.
4. In CodeX or Codex, give the agent the local path to this bootstrap repo.
5. Tell the agent whether your project is:
   - greenfield
   - brownfield
6. Use one of the prompts from [`prompts/`](prompts/README.md).

The local path matters. In practice it is usually better to point the agent at
the real local folder than to rely on a repo summary from memory.

Example:

```text
Use this bootstrap repository as the reference:
/absolute/path/to/spec-first-bootstrap

This is a brownfield project.
Start with the brownfield discovery workflow and do not write code yet.
```

## Two common scenarios

### 1. Greenfield project

Use this when the project is new or mostly empty.

The agent should:

- read this bootstrap first
- set up the spec-first workflow in the new project
- create the initial product-spec structure
- propose the first specs that should exist before feature code

Start with:

- [`prompts/greenfield-bootstrap.md`](prompts/greenfield-bootstrap.md)

### 2. Brownfield project

Use this when the project already exists and you want to retrofit specs.

The agent should:

- analyze the current codebase
- extract product behavior from code, routes, state, tests, UI flows, and docs
- ask the user for clarification where the product intent is still unclear
- generate first-pass specs for the most important product areas

In practice, brownfield migration usually means:

1. map the product
2. build a spec backlog
3. generate first-pass specs
4. review unknowns and conflicts
5. only then start changing code

Start with:

- [`prompts/brownfield-discovery.md`](prompts/brownfield-discovery.md)
- [`prompts/brownfield-interview.md`](prompts/brownfield-interview.md)
- [`prompts/generate-first-specs.md`](prompts/generate-first-specs.md)

## How brownfield migration works

For an existing product, do not try to write every spec yourself first.

Instead, ask the agent to use the existing project as evidence:

- current code
- routes and state flow
- tests and QA cases
- existing docs
- product interviews with the user or team

The job of the agent is to turn those artifacts into a short product contract.

Good brownfield output usually includes:

- a product map
- a spec backlog
- first-pass specs for risky or important areas
- unknowns that still need confirmation

The user can resolve those unknowns in chat.
The point is still to keep the work agent-driven rather than document-driven.

## Minimal workflow

Use this workflow for non-trivial work:

1. Clarify the product goal.
2. Create or update a spec.
3. Review behavior, invariants, and edge cases.
4. Implement against the spec.
5. Add or update verification artifacts if the project needs them.

## Optional web QA layer

Browser QA is **optional**.

Use it if your project has a browser UI and you want a lightweight structure
for smoke checks, regression cases, and run reports.

Do not treat browser QA as mandatory for every project. Many projects are
better served by API, CLI, integration, or operator-level verification.

If you do have a browser UI, this repo includes a compact starter pack under:

- [`qa/web/README.md`](qa/web/README.md)

And a matching prompt:

- [`prompts/optional-web-qa.md`](prompts/optional-web-qa.md)

## Prompt pack

The easiest way to use this repo is to copy one prompt, replace
`<BOOTSTRAP_PATH>`, and send it to the agent.

Start here:

- [`prompts/README.md`](prompts/README.md)

Included prompt files:

- `greenfield-bootstrap.md`
- `brownfield-discovery.md`
- `brownfield-interview.md`
- `generate-first-specs.md`
- `optional-web-qa.md`
- `day-to-day-spec-first.md`

## Suggested repository structure

```text
.
├── AGENTS.md
├── README.md
├── docs/
│   └── specs/
│       ├── README.md
│       ├── templates/
│       │   └── feature-spec.md
│       └── features/
│           └── favorites-spec.md
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

- `AGENTS.md` — minimal workflow rules for agents
- `docs/specs/README.md` — how the spec layer works
- `docs/specs/templates/feature-spec.md` — reusable template
- `docs/specs/features/favorites-spec.md` — example production-style spec
- `examples/favorites-spec.md` — same example in a simpler discovery path
- `prompts/` — ready-to-send prompts for setup and migration
- `qa/web/` — optional browser-QA starter pack for web UI projects

## Copy-paste starting point

The simplest rule to adopt is this:

```md
## Spec-First Rule

Before implementing any non-trivial feature:

1. Clarify the product goal.
2. Create or update a spec under `docs/specs/`.
3. Confirm user-visible behavior, invariants, and edge cases.
4. Only then begin implementation.

`AGENTS.md` is not the source of truth for detailed feature behavior.
Detailed behavior must live in specs.
```

## License

MIT
