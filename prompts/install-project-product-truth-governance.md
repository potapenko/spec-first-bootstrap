# Install Product-Truth Governance In One Project

Use this prompt when governance should apply to one repository only.

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Install the checked-in product-truth governance into the target project. This
is a project documentation and workflow task, not permission to change product
implementation. Do not launch subagents.

## Deployment scope

The scope is PROJECT_ONLY.

- Change only the target repository.
- Do not write, replace, or install files in the active Codex home.
- Respect global instructions already applicable to the session, but do not
  use this project-only install to duplicate or modify their source files.
- Do not install persistent-goal root architecture in this invocation.

The target project must remain self-contained when no global Codex
customization exists.

## Canonical source

Read completely from the bootstrap repository:

- docs/spec-first-workflow.md;
- docs/agent-governance/README.md;
- docs/agent-governance/agents-sections.md;
- docs/agent-governance/product-truth-governance.md;
- docs/specs/README.md;
- docs/specs/templates/.

If those files cannot be fetched or found, stop and request access or the
package path. Do not reconstruct a shorter substitute from memory.

## Existing project discovery

Before editing:

1. resolve the exact target repository root;
2. read the applicable instruction context and every existing AGENTS.md layer
   in that repository;
3. inspect its worktree and preserve unrelated changes;
4. identify its language, engineering, safety, build, test, QA, release, and
   documentation rules;
5. inspect its specification registry and active contracts, if any;
6. identify whether equivalent product-truth governance already exists.

Do not use this installation pass to rewrite product behavior.

Do not infer first-pass product contracts from implementation unless the task
is separately authorized as Discover.

## Installation

1. Install the canonical full document as
   docs/agent/product-truth-governance.md in the target repository.
2. Merge the exact Project-local product-truth section from
   docs/agent-governance/agents-sections.md into the repository-root
   AGENTS.md.
3. If an older equivalent section exists, reconcile or replace only that
   section. Do not replace the whole file or append a contradictory duplicate.
4. Preserve all project-specific safety, engineering, testing, release, and
   framework instructions.
5. Keep the full governance document outside the automatically loaded
   AGENTS.md.
6. Route project product tasks to the existing spec registry.
7. If no registry exists, create only the minimum neutral scaffold:
   - docs/specs/README.md;
   - docs/specs/index.md from the bootstrap template;
   - docs/specs/templates/feature-spec.md;
   - docs/specs/templates/contract-change-envelope.md;
   - docs/specs/templates/contract-delta.md;
   - docs/specs/templates/release-contract-baseline.md.
8. A new neutral registry must distinguish contract authority
   (Draft/Active/Superseded/Historical) from domain stability
   (Evolving/Accepted/Released/Deprecated), define precedence, and avoid
   claiming unknown product intent.
9. If a mature registry already exists, extend it in place rather than creating
   a competing specification system.

Use apply_patch for edits.

## Required project behavior

The resulting project workflow must require:

- a provisional specification pass before implementation evidence;
- the smallest complete applicable source, design, QA, runtime, and release
  evidence pass before the final reconciled basis;
- a Contract Change Envelope for product work;
- explicit authorized and protected domains;
- legitimate external authority for every semantic spec change;
- stable domain and clause identifiers where the project has mature specs;
- contract revision or epoch pinning for long-running or multi-agent work;
- QA action-state-result mapping;
- exact discrepancy classification;
- user escalation only for a real material fork or authority boundary.

Do not copy generic Rust, Swift, JavaScript, database, UI, or platform rules
unless they already belong to the target project.

## Verification and checkpoint

Verify:

- target paths and scope are exact;
- the canonical full document is complete;
- the local gate appears exactly once;
- existing AGENTS.md content remains present;
- no Codex-home file changed;
- Markdown links, fences, headings, and whitespace pass;
- no product contract was silently invented;
- unrelated worktree changes remain untouched.

Run the target repository's docs-only checks.

If its instructions require a checkpoint commit, stage and commit only the
installer-owned paths. Otherwise report the exact changed paths without
inventing a commit requirement.

Report complete, blocked, and residual state.
