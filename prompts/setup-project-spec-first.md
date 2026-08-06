# Set Up Spec-First Development In This Project

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Set up specification-first product work in the current project. Keep every
change inside this repository. Do not modify the user's global Codex, Claude,
or other agent configuration.

This is a workflow, specification, and discovery task. It does not authorize
product implementation.

## Read first

From the bootstrap repository, read completely:

- `docs/spec-first-workflow.md`;
- `docs/agent-governance/product-truth-governance.md`;
- the Project: product specifications section in
  `docs/agent-governance/agents-sections.md`;
- `docs/specs/README.md` and `docs/specs/templates/`;
- `prompts/greenfield-bootstrap.md`;
- `prompts/brownfield-discovery.md`;
- `prompts/generate-first-specs.md`.

In the target project, read every applicable instruction file, onboarding
document, existing spec registry, active contract, QA guide, release rule, and
worktree status before editing. Preserve unrelated changes.

## Install the project layer

1. Merge the compact project product-truth section into the repository's
   existing root agent instruction file. Never replace the whole file.
2. Install the full governance document as
   `docs/agent/product-truth-governance.md`.
3. Add or reconcile `docs/spec-first-workflow.md`.
4. Add or reconcile the project's `docs/specs/README.md`, spec index, and
   neutral templates. Extend an existing mature spec system instead of
   creating a competing one.
5. Add only the useful follow-up prompts. Do not install persistent-goal agent
   architecture or browser QA in this step.
6. Keep project-specific framework, safety, build, test, Git, database,
   storage, and release rules intact.

Use `apply_patch` for edits.

## Establish product understanding

For a new project, create a small domain map and spec backlog without inventing
requirements that the user has not supplied.

For an existing project, use explicit brownfield Discover mode:

1. record which product contracts are missing or unreliable;
2. inspect the smallest complete applicable source, design, routes, state,
   tests, QA, runtime, history, and release evidence set;
3. separate observed behavior from intended behavior;
4. create a product-domain map and prioritized spec backlog;
5. write first-pass project specs with unknowns and conflicts visible;
6. do not change product implementation.

The specification system is canonical intended behavior but is not infallible
or self-authorizing. Source and runtime evidence may reveal a missing or stale
spec; current code must not silently become product intent.

## Verification

Verify that:

- only the target project changed;
- existing instructions and unrelated work remain intact;
- the compact gate appears once and routes to an existing full document;
- Markdown, local links, and whitespace pass;
- no product implementation changed;
- no product behavior was invented merely to populate a template;
- any unresolved product decision is described with its evidence and impact.

Follow the target repository's checkpoint policy. Report installed paths,
created or updated product artifacts, verification, and exact residuals.
