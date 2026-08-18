# Set Up The Optional Codex Lifecycle Adapter Globally

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Install only the optional Codex lifecycle adapter in the current user's active
Codex home. Do not modify any project repository or install specification-first
governance, persistent-goal coordination, or browser QA as a prerequisite.
Preserve and reinforce any of those layers that are already installed.

Do not change model or reasoning defaults, providers, permissions, concurrency,
unrelated application configuration, or goal state.

## Read first

Read completely:

- `docs/specs/index.md`;
- `docs/specs/features/codex-lifecycle-enforcement.md`;
- `integrations/codex-lifecycle/README.md`;
- `integrations/codex-lifecycle/lifecycle_restart.py`;
- `integrations/codex-lifecycle/global-hooks.json.template`;
- the Global: Codex lifecycle restart adapter section in
  `docs/agent-governance/agents-sections.md`;
- the adapter fixture tests.

Resolve the active Codex home, global instruction entry point, override
precedence, configured instruction-size limit, hooks feature state, and every
active global, project, session, managed, and plugin hook source visible for the
current scope. State exact target paths before writing. Do not expose tokens,
credentials, provider settings, or unrelated configuration.

## Install

1. Install the script under the resolved Codex home as
   `hooks/lifecycle_restart.py`.
2. Substitute exact platform commands and the resolved Codex-home path in the
   global template.
3. Merge the hook behavior into `hooks.json` or the existing inline global hook
   representation. Use one representation in this layer.
4. Merge the compact Global: Codex lifecycle restart adapter section into the
   active global instruction entry point. Reconcile equivalent wording instead
   of duplicating it.
5. Preserve all existing hooks. If an equivalent project, managed, session, or
   plugin hook already covers the intended scope, report the overlap and avoid
   duplicate installation.
6. Keep root/single-agent and worker messages event-specific.
7. If hooks are explicitly disabled, report the exact setting. Change only the
   canonical hooks feature when the user's adapter request authorizes it and no
   managed policy forbids it.

Use `apply_patch` for edits.

## Verification

- parse the resulting hook configuration;
- run the lifecycle fixture tests before copying and test the installed script;
- verify `startup`, `resume`, `clear`, `compact`, and `SubagentStart` routing;
- verify root context restores the Route Receipt and detects revision drift
  without requiring unselected sibling contracts;
- verify the compact restart gate is active, not shadowed, and inside the
  configured instruction-size limit;
- verify only one matching adapter covers the selected scope;
- report the required Codex `/hooks` trust review and confirm the definition is
  not silently skipped;
- verify no project repository, product behavior, unselected governance layer,
  model, goal, provider, permission, concurrency, or unrelated hook changed.

Do not create a Git commit for files outside a Git repository. Report exact
paths, merge decisions, trust state, verification, and residuals.
