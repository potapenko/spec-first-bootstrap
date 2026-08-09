# Set Up Persistent-Goal Agent Work In This Project

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Set up the coordinator-and-workers architecture inside the current project
only. Do not modify the user's global Codex, Claude, or other agent
configuration.

This is an instruction and documentation setup task. Do not create, resume,
pause, block, or complete a persistent goal. Do not change product code.

Install only the persistent-goal agent layer. Do not install specification-
first governance or browser QA as a prerequisite or dependency. Preserve and
interoperate with either layer when it is already present.

## Read first

Read completely from the bootstrap repository:

- `docs/agent-governance/root-orchestration.md`;
- the Project: persistent-goal agents section in
  `docs/agent-governance/agents-sections.md`.

Resolve and read the target project's active instruction hierarchy, including
overrides, nested files, fallback names, and instruction-size limits. Read its
coordination rules, worktree state, and any current goal state before editing.
Preserve unrelated content.

## Install

1. Install the full root contract as
   `docs/agent/root-orchestration.md`.
2. Merge the compact Project: persistent-goal agents section into the existing
   project-root instruction file. Never replace the complete file.
3. Reconcile an equivalent existing coordination section instead of appending
   a conflicting duplicate.
4. Do not add, remove, or rewrite specification, product-truth, browser-QA, or
   other unrelated workflow layers. If they already exist, preserve them and
   keep the agent layer compatible with their established authority paths.
5. Do not change model defaults, reasoning defaults, concurrency limits,
   custom agent profiles, provider settings, or application configuration.
   Apply the root contract's role-based model policy using models actually
   supported by the active agent environment; do not hardcode another
   platform's model names.
6. Do not install or modify the optional Codex lifecycle adapter unless the
   user explicitly requested it. Preserve an existing adapter and keep its
   worker-start wording aligned with finite packet authority.

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
- product packets carry an exact pinned Spec Basis, complete governing
  documents, specified expectation, protected behavior, assigned evidence, and
  contract epoch when product-truth governance applies;
- model strength follows risk and judgment needs, with quality ahead of token
  savings;
- only independent ownership is parallelized;
- product changes receive independent review;
- one restart-safe registry carries packet state, applicable authority
  revision, receipts, and residuals;
- a paused or blocked goal stays idle until explicitly resumed;
- context compaction resumes from governing documents and durable state rather
  than chat memory.

## Verification

Verify exact project-only scope, one merged gate, complete canonical document,
preserved existing instructions, valid Markdown, no product-code change, no
goal-state change, no model/configuration change, and no installation or
modification of the specification or browser-QA layers.

Also verify that the merged gate is active rather than shadowed, stays within
the configured instruction-size limit, and that no lifecycle hook changed
without explicit adapter scope.

Follow the project's checkpoint policy and report changed paths, coexistence
with any already installed layers, verification, and exact residuals.
