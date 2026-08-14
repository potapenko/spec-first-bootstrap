# Agent Setup Sources

This directory is for the agents that install the Bootstrap. The human entry
point is the repository-root `README.md`.

The six setup prompts expose three independent layers:

1. product specifications and product-truth governance;
2. current-branch, plan-first, scope-controlled agent work, including
   persistent-goal multi-agent coordination and an explicit single-agent
   exception when the user forbids delegation;
3. optional browser QA.

Each layer can be installed in one project or, by explicit advanced request,
in the current user's global agent configuration.

The layers are composable but independent. No setup prompt may install another
layer as a prerequisite or hidden dependency. A user may install any one, any
two, or all three in either scope.

## Files

- `product-truth-governance.md` is the full specification and product-evidence
  contract.
- `root-orchestration.md` is the full outcome-first, economically proportional,
  coordinator-only-by-default `/root` contract for persistent goals, with the
  explicit user-required no-delegation activation exception.
- `web-qa-governance.md` is the full optional browser-QA contract.
- `agents-sections.md` contains compact current-branch, task-framing,
  scope-control, routing, and proportionality blocks to merge into a project or
  global instruction file.

## Installation invariants

- Project-only setup is the default and changes only the named repository.
- Global setup is advanced, explicit, and changes no project during install.
- Detect the active agent environment and its supported user-level instruction
  entry point; do not assume another user's path.
- Read and merge existing instructions. Never replace the complete instruction
  file.
- Keep full governance documents conditionally loaded. Ordinary workers receive
  only the finite rules and evidence required by their task.
- Install the compact task-framing and scope-control gate with the agent layer
  so the first implementation-bearing request and later materially ambiguous
  work pause at an approved execution plan and stay inside it, while questions
  and read-only work proceed directly.
- Install the current-branch gate with the agent layer so branch or worktree
  changes require an explicit user request and dirty or diverged state is not
  bypassed by moving work elsewhere.
- Install the compact outcome/resource gate with the agent-work layer so
  ordinary implementation and orchestrated goals share the same release-path
  progress measure and economic stop conditions.
- Preserve project-specific product, framework, safety, build, test, database,
  storage, Git, and release rules.
- Preserve coordinator-only persistent-goal behavior by default, while honoring
  an explicit user requirement to complete the current goal chat without
  subagents, workers, or delegation as bounded single-agent work.
- Do not copy project-specific rules into global configuration.
- Do not change product implementation while installing workflow layers.
- Do not create, resume, pause, block, or complete a persistent goal during
  setup.
- Do not launch subagents merely to install these documents.
- Do not install the same full layer both globally and locally unless the user
  explicitly requests that duplication.
- Verify exact scope, Markdown, links, duplicate sections, instruction-size
  limits, and unrelated-file preservation.

The detailed prompt files under `prompts/` are the executable installation
contracts. This directory is their canonical source, not an additional human
setup flow.

The optional Codex lifecycle adapter lives under
[`../../integrations/codex-lifecycle/`](../../integrations/codex-lifecycle/).
It reinforces installed instruction layers but does not make any of the three
governance layers depend on Codex or on the adapter.
