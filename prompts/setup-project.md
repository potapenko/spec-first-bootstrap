# Set Up The Complete Bootstrap In This Project

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Configure the current repository with all three Bootstrap layers. Keep every
change inside this project. Do not modify user-level Codex, Claude, or other
agent configuration.

This is one setup task with three ordered phases. Read and execute each detailed
contract completely:

1. **Specifications:** `prompts/setup-project-spec-first.md`.
2. **Agents:** `prompts/setup-project-agents.md`.
3. **QA:** inspect whether the project has a browser UI. If it does, execute
   `prompts/optional-web-qa.md`. If it does not, leave browser QA uninstalled
   and report that the optional layer is not applicable.

Do not ask the user to copy files or run the three phase prompts separately.
Reconcile shared `AGENTS.md` edits into one coherent result without duplicate
sections.

Preserve all existing project instructions, product behavior, implementation,
QA systems, unrelated worktree changes, and repository-specific safety, build,
test, Git, database, storage, and release rules.

Do not create, resume, pause, block, or complete a persistent goal during
setup. Do not change product implementation. Brownfield discovery may inspect
source, design, QA, runtime, history, and releases as evidence only under the
specification setup contract.

Use `apply_patch` for edits. Follow the target repository's checkpoint policy.

Before finishing, verify:

- exact project-only scope;
- all three phase dispositions;
- one non-duplicated instruction hierarchy;
- valid Markdown, local links, and whitespace;
- preserved unrelated files and existing rules;
- no product implementation or global configuration change;
- no goal-state or agent-application configuration change.

Report installed layers, changed paths, browser-QA applicability, verification,
checkpoint state, and exact residuals.
