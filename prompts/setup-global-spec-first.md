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
2. Resolve the exact global configuration directory and active instruction
   entry point, including override precedence and configured instruction-size
   limits. Read the active file completely if it exists.
3. Before writing outside the current project, state the exact target paths.
   If filesystem permission is required, request only the narrow permission
   needed for those paths.
4. Stop if the supported global instruction mechanism or target scope is
   ambiguous.

Do not expose credentials, tokens, environment values, or unrelated global
configuration while inspecting the setup.

## Canonical source

Resolve and read:

- `docs/agent-governance/README.md`;
- `docs/agent-governance/product-truth-governance.md` and the applicable
  closure from `docs/agent-governance/product-truth/route.json`;
- the Global: product specifications section in
  `docs/agent-governance/agents-sections.md`.

## Install

1. Install the compact product-truth router beside the active user-level
   instruction entry point as `product-truth-governance.md`, with its route
   manifest and leaves in a sibling `product-truth/` directory.
2. Install `scripts/spec_route.py` beside the routed package using a stable path
   appropriate to the detected agent environment, and adapt the router's
   example command to that path.
3. Merge the compact global product-specification section into the existing
   global instruction file. Never replace the complete file.
4. Reconcile or replace only an older equivalent section; do not append a
   contradictory duplicate.
5. Keep project-specific framework, product, safety, build, test, database,
   storage, Git, and release rules out of the global layer.
6. Keep governance leaves conditionally routed so ordinary workers receive
   only their finite Route Receipt, product contract closure, and evidence packet.
7. Do not install or change the optional Codex lifecycle adapter unless the
   user explicitly requested it. Preserve an existing adapter and reconcile its
   compact restart wording with the installed product gate.

Use `apply_patch` for edits.

## Verification

Verify that the routed governance package matches the canonical source, the
resolver validates it and emits a representative receipt, the compact gate
appears once, existing global instructions remain intact, instruction-size
limits are respected, Markdown and whitespace pass, no project repository
changed, and no persistent-goal agent or browser-QA layer was installed or
modified. Also verify that no Codex hook or application configuration changed
without explicit adapter scope and that an override does not shadow the merged
gate.

Report the detected agent environment, exact global paths, merge decision,
permission used, verification, and residuals. Do not create a Git commit for
files outside a Git repository.
