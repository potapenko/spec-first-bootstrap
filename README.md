# Spec-First Bootstrap for AI-Assisted Projects

Open your project in Codex, Claude Code, or another coding agent and choose one
of these two prompts.

## 1. Set up the current project

This is the recommended option. It installs all three layers inside the current
project: specifications, coordinated agent work, and optional browser QA.

```text
Use https://github.com/potapenko/spec-first-bootstrap as the canonical reference and fully set up the current project with the Bootstrap.

Follow prompts/setup-project.md from that repository. In one project-local setup, configure all three layers in order: specification-first product work, coordinated agents for long-running goals, and the optional browser-QA layer when this project has a browser UI. Preserve all existing project instructions and product code. Do not modify my global Codex, Claude, or other agent configuration, and do not create or resume a goal during setup.
```

The agent reads the three detailed project contracts, adapts them to the
existing repository, and verifies the result. You do not need to copy files or
run three separate prompts.

## 2. Set up every project globally

Use this only when you deliberately want the same three layers available in
all future projects.

> **Warning:** this prompt modifies your user-level Codex, Claude, or other
> agent configuration outside the current repository. The agent needs
> permission to write there, and some environments may require broad or full
> filesystem access. A mistake can affect every project. Review the exact
> target paths and permission request before allowing the change.

```text
Use https://github.com/potapenko/spec-first-bootstrap as the canonical reference and fully set up the Bootstrap globally for all my projects.

Follow prompts/setup-global.md from that repository. In one global setup, configure all three layers in order: specification-first product governance, coordinated agents for long-running goals, and optional browser-QA guidance. Detect the active agent environment, show me the exact global paths before writing, request the required filesystem permission, preserve all existing global instructions, and do not modify any project repository or create or resume a goal during setup.
```

The global setup installs reusable conditional guidance. It does not copy
specs, agent files, or QA folders into every existing repository.

## What the Bootstrap adds

- **Specifications** keep intended product behavior explicit before code is
  changed. Agents reconcile specs with source, design, runtime behavior, QA,
  and released behavior instead of treating Markdown as an infallible
  substitute for understanding the product.
- **Agent teamwork** keeps the main agent focused on context and coordination
  while bounded workers implement, review, build, test, and perform runtime QA.
- **Browser QA** adds optional real-browser cases and run reports for web UI
  projects. It remains separate from specifications and implementation.

The Bootstrap works for new and existing projects. In an existing project, the
setup agent preserves current instructions, studies the product as evidence,
creates first-pass specifications, and does not change product implementation
during discovery.

Detailed setup and follow-up contracts are listed in
[`prompts/README.md`](prompts/README.md). The specification workflow is in
[`docs/spec-first-workflow.md`](docs/spec-first-workflow.md), and the optional
browser-QA pack is in [`qa/web/`](qa/web/).

This Bootstrap was extracted from several months of work on four internal
projects behind [`playphrase.me`](https://playphrase.me).

The broader idea is described in
[this short article](https://www.patreon.com/posts/spec-first-or-ai-155606468?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link).

## License

MIT
