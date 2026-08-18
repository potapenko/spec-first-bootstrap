# Set Up Spec-First Development In This Project

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Set up specification-first product work in the current project. Keep every
change inside this repository. Do not modify the user's global Codex, Claude,
or other agent configuration.

This is a workflow, specification, and discovery task. It does not authorize
product implementation.

## Read first

From the bootstrap repository, resolve and read the applicable routed closure:

- `docs/spec-first-workflow.md`;
- `docs/agent-governance/product-truth-governance.md` and
  `docs/agent-governance/product-truth/route.json` using the `evolve` profile;
- the Project: product specifications section in
  `docs/agent-governance/agents-sections.md`;
- `docs/specs/README.md`, `docs/specs/routing.md`, and the route, contract,
  receipt, and envelope templates;
- `prompts/greenfield-bootstrap.md`;
- `prompts/brownfield-discovery.md`;
- `prompts/generate-first-specs.md`;
- `prompts/migrate-legacy-spec-library.md` when the target already has a large
  specification corpus.

In the target project, resolve and read the complete active instruction chain,
including `AGENTS.override.md`, nested instruction files, configured fallback
names, and instruction-size limits. Then read every applicable onboarding
document, spec registry, active contract, directly linked plan, runbook,
operator handoff, accepted baseline, design contract, QA guide, release rule,
and worktree status before editing. Preserve unrelated changes.

Before inspecting target implementation sources or runtime evidence, state the
Route Receipt, selected contracts read completely, and a provisional Spec Basis that
separates specified expectation, protected behavior, established flow, and
evidence still needed. If no governing specification exists, record the gap and
use Discover before consulting implementation evidence.

## Install the project layer

1. Merge the compact project product-truth section into the repository's
   existing root agent instruction file. Never replace the whole file.
2. Install the compact governance router as
   `docs/agent/product-truth-governance.md` and its routed leaves and manifest
   under `docs/agent/product-truth/`.
3. Add or reconcile `docs/spec-first-workflow.md`.
4. Add or reconcile the project's `docs/specs/README.md`, root `route.json`,
   human-readable index, routing guide, neutral templates, and
   `scripts/spec_route.py`. Also install `scripts/spec_migration.py` and the
   legacy migration plan template so an existing mature spec system can be
   converted without creating a competing one or loading its whole corpus.
5. Add only specification-related follow-up prompts. Do not install or copy
   persistent-goal agent architecture, browser-QA prompts, or browser-QA
   artifacts in this step.
6. Keep project-specific framework, safety, build, test, Git, database,
   storage, and release rules intact.
7. Do not install the optional Codex lifecycle adapter unless the user
   explicitly requested that adapter. If it is already installed, preserve it
   and keep its compact restart gate consistent with the strengthened product
   gate.

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

If the existing project already has a substantial specification library, do
not treat it as missing documentation and do not read it wholesale during
setup. Install the migration prompt and tools, perform only a bounded census,
and leave corpus conversion to a separately approved run of
`prompts/migrate-legacy-spec-library.md`.

The specification system is canonical intended behavior but is not infallible
or self-authorizing. Source and runtime evidence may reveal a missing or stale
spec; current code must not silently become product intent.

## Verification

Verify that:

- only the target project changed;
- existing instructions and unrelated work remain intact;
- the compact gate appears once and routes to an existing manifest and leaves;
- route validation and one representative closure resolution pass;
- the gate is present in the instruction file Codex or the detected agent
  actually loads, is not shadowed by an override, and remains inside the
  configured instruction-size limit;
- Markdown, local links, and whitespace pass;
- no product implementation changed;
- no product behavior was invented merely to populate a template;
- the migration inventory tool can produce compact status without emitting
  corpus bodies;
- no persistent-goal agent or browser-QA layer was installed or modified;
- no Codex hook or agent application configuration was installed or modified
  without explicit adapter scope;
- any unresolved product decision is described with its evidence and impact.

Follow the target repository's checkpoint policy. Report installed paths,
created or updated product artifacts, verification, and exact residuals.
