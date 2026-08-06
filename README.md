# Spec-First Bootstrap for AI-Assisted Projects

Open your project in Codex, Claude Code, or another coding agent. Copy only the
prompts for the layers you want. Each layer is independent: choose any one,
any two, or all three.

## Set up this project

This is the recommended option. Everything stays inside the current project.

No prompt installs either of the other layers. If you choose all three, the
recommended order is specifications, agents, then browser QA.

### 1. Add specification-first development

```text
Use https://github.com/potapenko/spec-first-bootstrap as the reference and set up this project for specification-first development.

Follow prompts/setup-project-spec-first.md from that repository. Keep the setup inside this project, preserve its existing instructions and product code, and do not add global configuration, persistent-goal agent architecture, or browser QA in this step.
```

### 2. Add agent teamwork

Use this when the project will have long-running work handled by a coordinator
and multiple focused agents. It does not require the specification or browser-
QA layers.

```text
Use https://github.com/potapenko/spec-first-bootstrap as the reference and set up coordinated multi-agent work for long-running goals in this project.

Follow prompts/setup-project-agents.md from that repository. Keep the setup inside this project. Do not create or resume a goal, change agent application settings, or change product code during setup.
```

### 3. Add optional browser QA

Use this only for a project with a browser UI. It can be installed on its own;
it does not require the specification or agent layers.

```text
Use https://github.com/potapenko/spec-first-bootstrap as the reference and add the optional browser-QA layer to this web UI project.

Follow prompts/optional-web-qa.md from that repository. Install only the browser-QA layer. Do not install specification-first governance or persistent-goal agent architecture. Keep browser QA optional and do not change product code.
```

Each selected prompt is a complete installer for that one layer. You do not
need to copy files manually or install an unselected layer first.

## Set up every project at once

This is an advanced and less common option. Prefer project-only setup unless
you deliberately want the same rules in every future project.

> **Warning:** these prompts modify your user-level Codex, Claude, or other
> agent configuration outside the current repository. The agent will need
> permission to write there, and some environments may require broad or full
> filesystem access. A mistake can affect every project. Review the exact
> target paths and permission request before allowing the change.

Run only the prompts for the global layers you want. Each prompt changes only
its named layer. If you want all three, the listed order is recommended but
not required as a dependency.

### 1. Add specifications globally

```text
Use https://github.com/potapenko/spec-first-bootstrap as the reference and set up specification-first product governance globally for all my projects.

Follow prompts/setup-global-spec-first.md from that repository. Install only the specification layer. Do not install persistent-goal agent architecture or browser-QA guidance. Detect the active agent environment, show me the exact global paths before writing, preserve all existing global instructions, and do not modify any project repository.
```

### 2. Add agent teamwork globally

```text
Use https://github.com/potapenko/spec-first-bootstrap as the reference and set up coordinated multi-agent work for long-running goals globally for all my projects.

Follow prompts/setup-global-agents.md from that repository. Install only the persistent-goal agent layer. Do not install specification governance or browser-QA guidance. Detect the active agent environment, show me the exact global paths before writing, preserve all existing global instructions, and do not create or resume a goal or modify any project repository.
```

### 3. Add optional browser QA globally

```text
Use https://github.com/potapenko/spec-first-bootstrap as the reference and set up optional browser-QA guidance globally for all my web projects.

Follow prompts/setup-global-browser-qa.md from that repository. Install only the optional browser-QA layer. Do not install specification governance or persistent-goal agent architecture. Detect the active agent environment, show me the exact global paths before writing, keep browser QA optional, preserve all existing global instructions, and do not modify any project repository.
```

Global setup installs reusable guidance. It does not automatically add specs,
agent files, or QA folders to every existing repository.

## What the three layers do

- **Specifications** keep intended product behavior explicit before code is
  changed. The agent still reconciles specs with source, design, runtime
  behavior, QA, and released behavior instead of treating Markdown as an
  infallible substitute for understanding the product.
- **Agents** keep the main agent focused on coordination and
  context continuity while bounded workers implement, review, build, test, and
  perform runtime QA.
- **Browser QA** adds optional real-browser cases and run reports for web UI
  projects. It remains separate from product specifications and implementation.

The Bootstrap works for both new and existing projects. When the specification
layer is selected for an existing project, the setup agent preserves current
instructions, studies the product as evidence, creates first-pass
specifications, and does not change product implementation during discovery.

## What is included

- a minimal project `AGENTS.md` example;
- the canonical specification-first workflow;
- reusable product-spec templates and a Favorites example;
- project and global setup prompts;
- optional browser-QA files;
- detailed governance sources read by installer agents under
  `docs/agent-governance/`.

More detailed working prompts are listed in
[`prompts/README.md`](prompts/README.md). The specification workflow is in
[`docs/spec-first-workflow.md`](docs/spec-first-workflow.md), and the optional
browser-QA pack is in [`qa/web/`](qa/web/).

This Bootstrap was extracted from several months of work on four internal
projects behind [`playphrase.me`](https://playphrase.me).

The broader idea is described in
[this short article](https://www.patreon.com/posts/spec-first-or-ai-155606468?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link).

## License

MIT
