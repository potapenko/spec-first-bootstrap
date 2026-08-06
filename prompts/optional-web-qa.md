This project has a browser UI.

Use this bootstrap repository as the reference:

https://github.com/potapenko/spec-first-bootstrap

Keep every change inside the current project. Do not modify global Codex,
Claude, or other agent configuration. Preserve any mature QA system instead of
creating a competing one.

Add only the optional browser-QA layer for this project. Do not install
specification-first governance or persistent-goal agent architecture as a
prerequisite or dependency. Preserve and interoperate with either layer when
it is already present.

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
5. a simple behavior-authority-to-QA mapping approach, using stable spec IDs
   when a specification layer already exists
6. the `qa/web/AGENTS.snippet.md` routing block in this project's `AGENTS.md`

Keep this QA layer optional.

Do not change product code.

If the project has active product specifications, link cases to them. If it
does not, do not create or install a specification system: identify the
existing source of expected behavior and record material authority gaps in the
QA artifact instead of inventing intent.

Do not assume browser QA is appropriate for non-web projects.

QA cases verify the governing product behavior through explicit
action-state-result chains. Browser observations and existing cases are
evidence; they do not independently create product intent or authorize weaker
expectations.

Verify exact project-only scope, preserved existing instructions, valid
Markdown and links, the absence of product-code changes, and no installation
or modification of specification or persistent-goal agent layers. Follow the
target repository's checkpoint policy and report exact residuals.
