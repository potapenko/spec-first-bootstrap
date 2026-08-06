# Set Up Persistent-Goal Agent Work In This Project

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Set up the coordinator-and-workers architecture inside the current project
only. Do not modify the user's global Codex, Claude, or other agent
configuration.

This is an instruction and documentation setup task. Do not create, resume,
pause, block, or complete a persistent goal. Do not change product code.

## Read first

Read completely from the bootstrap repository:

- `docs/agent-governance/root-orchestration.md`;
- `docs/agent-governance/product-truth-governance.md`;
- the two Project sections for product specifications and persistent-goal
  agents in `docs/agent-governance/agents-sections.md`.

Read the target project's existing instruction hierarchy, coordination rules,
worktree state, and any current goal state before editing. Preserve unrelated
content.

## Install

1. Install the full root contract as
   `docs/agent/root-orchestration.md`.
2. Merge the compact Project: persistent-goal agents section into the existing
   project-root instruction file. Never replace the complete file.
3. If the matching project product-truth dependency is absent, also install
   `docs/agent/product-truth-governance.md` and its compact project section.
   Do not create project specs or change product behavior during this setup.
4. Reconcile an equivalent existing coordination section instead of appending
   a conflicting duplicate.
5. Do not change model defaults, reasoning defaults, concurrency limits,
   custom agent profiles, provider settings, or application configuration.
   Apply the root contract's role-based model policy using models actually
   supported by the active agent environment; do not hardcode another
   platform's model names.

Use `apply_patch` for edits.

## Required result

The resulting project must preserve these rules:

- `/root` is coordinator-only when a running persistent goal is being
  advanced;
- no small-task exception permits `/root` to implement, inspect broadly,
  build, test, run, browse, or perform visual QA itself;
- ordinary work remains single-agent when no persistent goal is active;
- workers receive finite packets with authority, scope, owners, forbidden
  actions, checks, stopping conditions, and a terminal receipt;
- model strength follows risk and judgment needs, with quality ahead of token
  savings;
- only independent ownership is parallelized;
- product changes receive independent review;
- one restart-safe registry carries packet state, contract epoch, receipts,
  and residuals;
- a paused or blocked goal stays idle until explicitly resumed;
- context compaction resumes from governing documents and durable state rather
  than chat memory.

## Verification

Verify exact project-only scope, one merged gate, complete canonical document,
preserved existing instructions, valid Markdown, no product-code change, no
goal-state change, and no model/configuration change.

Follow the project's checkpoint policy and report changed paths, dependency
handling, verification, and exact residuals.
