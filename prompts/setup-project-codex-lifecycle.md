# Set Up The Optional Codex Lifecycle Adapter In This Project

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Install only the optional Codex lifecycle adapter in the current project. Do
not install specification-first governance, persistent-goal coordination, or
browser QA as a prerequisite. Preserve and reinforce any of those layers that
are already installed.

Do not change product code, global Codex configuration, model or reasoning
defaults, providers, permissions, concurrency, or goal state.

## Read first

Read completely:

- `docs/specs/index.md`;
- `docs/specs/features/codex-lifecycle-enforcement.md`;
- `integrations/codex-lifecycle/README.md`;
- `integrations/codex-lifecycle/lifecycle_restart.py`;
- `integrations/codex-lifecycle/project-hooks.json.template`;
- the Project: Codex lifecycle restart adapter section in
  `docs/agent-governance/agents-sections.md`;
- the adapter fixture tests.

Resolve the project's active Codex instruction chain and all active hook
sources before editing. Inspect the effective hooks feature state without
changing global configuration. State the exact target paths, any existing
matching hooks, project trust status, and whether `hooks.json` or inline
`[hooks]` is already used in the project layer. If hooks are globally or
administratively disabled, report that exact blocker instead of changing
out-of-scope configuration.

## Install

1. Install the script as `.codex/hooks/lifecycle_restart.py`.
2. Merge the template behavior into `.codex/hooks.json` or the existing inline
   project hook representation. Use one representation in this layer.
3. Resolve commands from the Git root on macOS/Linux and substitute an exact
   project path for Windows.
4. Merge the compact Project: Codex lifecycle restart adapter section into the
   active project instruction file. Reconcile an equivalent section instead of
   duplicating it.
5. Preserve all existing hooks. If an equivalent global or plugin hook already
   covers the project, report the overlap and avoid duplicate installation.
6. Keep root/single-agent and worker messages event-specific.

Use `apply_patch` for edits.

## Verification

- parse the resulting hook configuration;
- run the lifecycle fixture tests;
- verify `startup`, `resume`, `clear`, `compact`, and `SubagentStart` routing;
- verify root context restores the Route Receipt and detects revision drift
  without requiring unselected sibling contracts;
- verify the compact restart gate is active and not shadowed;
- verify only one matching adapter covers the selected scope;
- verify the effective hooks feature is enabled without a global configuration
  change;
- report Codex trust-review requirements and confirm the project hook is not
  silently skipped;
- run `git diff --check` and the project's documentation checks;
- verify no product, global configuration, unselected governance layer, model,
  goal, or unrelated hook changed.

Follow the project's checkpoint policy and report exact residuals.
