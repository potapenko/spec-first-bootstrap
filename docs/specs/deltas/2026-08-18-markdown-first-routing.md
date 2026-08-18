# Markdown-First Routing Correction

- Change ID: `bootstrap.delta.2026-08-18.markdown-first-routing`
- Change mode: Evolve
- Authorized by: explicit user correction, 2026-08-18
- Domain: `bootstrap.governance`, `bootstrap.legacy-spec-migration`
- Previous behavior: mandatory JSON route manifests and resolver selected nodes.
- New behavior: agents traverse only Markdown roots, branches, leaves, and
  explicit Markdown dependency links.
- Node limit: 100 physical lines; target 50–80.
- Compatibility: workflow correction; no target product behavior change.
- Supersedes:
  `bootstrap.delta.2026-08-18.hierarchical-spec-routing` routing mechanism and
  `bootstrap.delta.2026-08-18.legacy-spec-migration` JSON state mechanism.
- Protected layers: product-truth semantics, task framing, worktree safety,
  optional lifecycle behavior, agent coordination, and browser QA.
- QA impact: replace JSON-route fixtures with Markdown traversal, reachability,
  link, and line-limit checks.
- New revisions: `bootstrap.governance@7`,
  `bootstrap.legacy-spec-migration@2`, `bootstrap.codex-lifecycle@3`,
  `bootstrap.markdown-routing@1`.

## Decision

The specification system contains Markdown nodes only. Its required navigation
is ordinary Markdown links beginning at `docs/specs/README.md`. Technical
tools may validate the tree but are not authority and do not create committed
routing registries.

## Evidence

The user restated the intended root → branch → leaf workflow and rejected JSON
as outside the requested scope. The prior implementation had not split any
target legacy contract and therefore had not tested the requested approach.

## Verification

- all declared Markdown nodes are reachable from an approved root;
- every declared node contains at most 100 physical lines;
- every local link from a node resolves;
- no required spec or governance JSON manifest remains;
- setup and migration prompts install the Markdown protocol only.
