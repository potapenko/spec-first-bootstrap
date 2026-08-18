# Set Up Spec-First Development In This Project

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.
Keep every change inside the current repository. This workflow task does not
authorize product implementation or global configuration changes.

## Read first

From the Bootstrap, read `docs/spec-first-workflow.md`, the Markdown governance
root and applicable linked leaves, the Project product-specification section
in `docs/agent-governance/agents-sections.md`, the spec root/routing/templates,
and the greenfield, brownfield, generation, and migration prompts that apply.

In the target, read the complete active instruction chain, onboarding, spec
entry point, directly linked contracts and operational docs, and worktree
rules. Preserve unrelated changes. Before implementation evidence, state the
selected Markdown path, documents read, provisional Spec Basis, and missing or
ambiguous contracts.

## Install the project layer

1. Merge the compact project product-truth section into the existing root agent
   instructions; never replace the whole file.
2. Install `docs/agent/product-truth-governance.md` and its linked Markdown
   leaves without a routing manifest.
3. Add or reconcile `docs/spec-first-workflow.md`.
4. Add or reconcile `docs/specs/README.md`, branch nodes, human index, routing
   guide, and neutral Markdown templates. Install
   `scripts/check_spec_markdown.py`, `scripts/spec_migration.py`, and the legacy
   migration plan template as optional validation aids.
5. Every node must be Markdown, reachable from an approved Markdown root, and
   no more than 100 physical lines; prefer 50–80.
6. Keep framework, safety, build, test, Git, database, storage, and release
   rules intact. Do not install persistent-goal, browser-QA, or lifecycle
   layers unless separately requested.

Use `apply_patch` for edits.

## Existing projects

For missing or unreliable contracts, use Discover and keep observed behavior
separate from intended behavior. For a substantial reliable legacy library,
do not read it wholesale during setup. Run only a compact mechanical census
and leave semantic conversion to an approved execution of
`prompts/migrate-legacy-spec-library.md`.

## Verification

Verify project-only scope, preserved instructions, one active non-shadowed
gate, valid Markdown links, node reachability and the 100-line maximum, compact
migration census output, no JSON routing artifacts below the spec or governance
trees, no product implementation change, and no unselected layer or hook
change. Follow the target checkpoint policy and report exact residuals.
