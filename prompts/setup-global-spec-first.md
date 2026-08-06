# Set Up Spec-First Governance Globally

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Install specification and product-truth governance in the current user's
global agent configuration so it applies across future projects.

This is an advanced global configuration task. Change no project repository.
Do not install persistent-goal agent architecture or browser QA in this step.

## Resolve the environment safely

1. Detect the active agent environment and its supported user-level
   instruction entry point. It may be Codex, Claude Code, or another compatible
   agent. Do not assume another user's path or silently target both systems.
2. Resolve the exact global configuration directory and instruction file from
   the active environment.
3. Read the existing global instruction file completely if it exists.
4. Before writing outside the current project, state the exact target paths.
   If filesystem permission is required, request only the narrow permission
   needed for those paths.
5. Stop if the supported global instruction mechanism or target scope is
   ambiguous.

Do not expose credentials, tokens, environment values, or unrelated global
configuration while inspecting the setup.

## Canonical source

Read completely:

- `docs/agent-governance/README.md`;
- `docs/agent-governance/product-truth-governance.md`;
- the Global: product specifications section in
  `docs/agent-governance/agents-sections.md`.

## Install

1. Install the full product-truth document beside the active user-level
   instruction entry point as `product-truth-governance.md`.
2. Merge the compact global product-specification section into the existing
   global instruction file. Never replace the complete file.
3. Reconcile or replace only an older equivalent section; do not append a
   contradictory duplicate.
4. Keep project-specific framework, product, safety, build, test, database,
   storage, Git, and release rules out of the global layer.
5. Keep the full document conditionally loaded so ordinary workers receive
   only their finite product contract and evidence packet.

Use `apply_patch` for edits.

## Verification

Verify that the full document matches the canonical source, the compact gate
appears once, existing global instructions remain intact, instruction-size
limits are respected, Markdown and whitespace pass, and no project repository
changed.

Report the detected agent environment, exact global paths, merge decision,
permission used, verification, and residuals. Do not create a Git commit for
files outside a Git repository.
