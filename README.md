# Spec-First Bootstrap for AI-Assisted Projects

A lightweight bootstrap for teams and solo builders who want AI to produce reliable product work.

The core idea is simple:

**Do not start with code. Start with a spec.**

When working with AI, most failures do not come from weak code generation. They come from weak problem framing, missing behavior contracts, and unclear edge cases. This repository provides a practical starting point for a spec-first workflow that can be embedded directly into `AGENTS.md` and used from day one.

## What this repository contains

- a minimal public `AGENTS.md`
- a product-spec layer under `docs/specs/`
- a reusable feature spec template
- a real example spec
- a simple repository structure that can be copied into a live project

## The problem

A common workflow today looks like this:

1. You have an idea.
2. You ask the AI to build it.
3. The AI starts coding immediately.
4. The task drifts.
5. You discover missing cases, broken assumptions, and behavior mismatches later.

The usual mistake is treating specification as optional overhead. In practice, specification is the cheapest place to find mistakes.

## The principle

**Code is no longer the most expensive part. Misunderstanding is.**

So the workflow becomes:

Idea → Discussion → Specification → Implementation → Verification

The specification is not documentation for later. It is the behavioral contract the implementation must follow.

## Layer model

A reliable setup separates three kinds of truth.

### 1. Product truth
This is the actual feature behavior.

Examples:
- what users can do
- what must always remain true
- route, state, and data contracts
- edge cases
- failure behavior

Store this in specs, not in `AGENTS.md`.

### 2. Workflow truth
This is how the agent should operate.

Examples:
- what files must be read first
- when specs are required
- what order work happens in
- what can and cannot be changed

Store this in `AGENTS.md`.

### 3. Verification truth
This is how you check that the work matches reality.

Examples:
- QA cases
- test scenarios
- verification scripts
- acceptance checks

This can be browser-based or non-browser-based depending on the project.

## Minimal workflow

Use this workflow for non-trivial work:

1. Clarify the product goal.
2. Write or update a spec.
3. Review the behavior, invariants, and edge cases.
4. Implement against the spec.
5. Add or update verification artifacts if needed.

## Adoption path

### Level 1 — Minimal
Add a spec-first rule to `AGENTS.md`.

### Level 2 — Structured
Create `docs/specs/` and use a standard feature spec template.

### Level 3 — Operational
Add role routing, verification rules, and more explicit implementation discipline.

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
└── qa/
    └── README.md
```

## Included files

- `AGENTS.md` — minimal public workflow rules
- `docs/specs/README.md` — how the spec layer works
- `docs/specs/templates/feature-spec.md` — reusable template
- `docs/specs/features/favorites-spec.md` — example production-style spec
- `examples/favorites-spec.md` — same example in a simpler discovery path
- `qa/README.md` — placeholder for later verification strategy

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

## Anti-pattern

Do not start implementation from a vague request like:

> Add feature X.

Instead:

1. Turn the request into a spec.
2. Confirm behavior and edge cases.
3. Only then implement.

Skipping this step usually leads to rework.

## Positioning

This project is not claiming to invent specification-driven development.
Its goal is more practical:

**make spec-first AI development easy to adopt in real repositories.**

## License

MIT
