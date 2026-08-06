# Set Up Optional Browser QA Globally

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Install optional browser-QA guidance in the current user's global agent
configuration so it can be reused across future web projects.

This is an advanced global configuration task. Browser QA must remain
conditional. Change no project repository during installation, and do not copy
`qa/` into every project.

Install only the optional browser-QA layer. Do not install specification-first
governance or persistent-goal agent architecture as a prerequisite or hidden
dependency. Preserve and interoperate with either layer when already present.

## Resolve the environment safely

1. Detect the active agent environment and its supported user-level
   instruction entry point. Do not assume another user's path or configure
   multiple agent products silently.
2. Resolve and state the exact global configuration directory and files before
   writing outside the current project.
3. Read the existing global instruction file completely.
4. Request only the narrow filesystem permission required for the stated
   global paths.
5. Stop if the global instruction mechanism or scope is ambiguous.

Do not expose credentials, cookies, sessions, tokens, browser profiles, or
unrelated global settings.

## Canonical source

Read completely:

- `docs/agent-governance/README.md`;
- `docs/agent-governance/web-qa-governance.md`;
- the Global: optional browser QA section in
  `docs/agent-governance/agents-sections.md`;
- `qa/README.md` and `qa/web/README.md` for the project starter-pack model.

## Install

1. Install the full QA contract beside the active user-level instruction entry
   point as `web-qa-governance.md`.
2. Merge the compact global browser-QA section into the existing global
   instruction file. Never replace the complete file.
3. Reconcile an equivalent section rather than creating a duplicate.
4. Keep the full document conditionally loaded only for browser-QA work.
5. Do not make browser QA mandatory and do not install project artifacts until
   the user requests them for a specific web project.
6. Do not add, remove, or rewrite specification, product-truth, persistent-goal
   agent, or other unrelated global layers.

Use `apply_patch` for edits.

## Verification

Verify canonical document identity, one merged conditional gate, preserved
existing global instructions, instruction-size limits, Markdown and
whitespace, no browser/session access, no project-repository change, and no
installation or modification of specification or persistent-goal agent layers.

Report the detected environment, exact paths, permission used, merge decision,
verification, and residuals.
