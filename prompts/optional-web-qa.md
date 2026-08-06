This project has a browser UI.

Use this bootstrap repository as the reference:

https://github.com/potapenko/spec-first-bootstrap

Assume the spec-first bootstrap is already installed in this project.

Keep every change inside the current project. Do not modify global Codex,
Claude, or other agent configuration. Preserve any mature QA system instead of
creating a competing one.

Add the optional browser-QA layer for this project.

Read these files from the bootstrap repository first:

- `qa/README.md`
- `qa/web/README.md`
- `qa/web/AGENTS.snippet.md`
- `docs/agent-governance/web-qa-governance.md`

Add or adapt:

1. the minimal QA folder structure
2. smoke vs regression vs experimental guidance
3. report and bug templates
4. rules for when a browser QA case is required
5. a simple spec-to-QA mapping approach
6. the `qa/web/AGENTS.snippet.md` routing block in this project's `AGENTS.md`

Keep this QA layer optional.

Do not change product code.

Do not assume browser QA is appropriate for non-web projects.

QA cases verify the governing product behavior through explicit
action-state-result chains. Browser observations and existing cases are
evidence; they do not independently create product intent or authorize weaker
expectations.

Verify exact project-only scope, preserved existing instructions, valid
Markdown and links, and the absence of product-code changes. Follow the target
repository's checkpoint policy and report exact residuals.
