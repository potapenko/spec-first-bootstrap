# Repair An Existing Spec-First Workflow

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.
Keep the repair inside the target repository unless global setup was explicitly
requested. Do not change product implementation.

Read the active instruction chain, project operating rules, the spec Markdown
root and smallest applicable linked closure, existing workflow prompts, and the
Bootstrap workflow, governance nodes, agent section, and templates. Preserve
project-specific safety, framework, build, test, release, and Git rules.

Before implementation evidence, state the Markdown traversal receipt,
contracts read, provisional Spec Basis, and any missing or ambiguous path.

Use Evolve only for workflow, routing language, governance docs, and neutral
templates. Repair the smallest coherent surface so that:

1. one compact Product Truth gate appears in the active instruction chain;
2. roots and branches use short summaries plus ordinary Markdown links;
3. a node may be root, branch, leaf, or hybrid and has at most 100 physical
   lines, with 50–80 preferred;
4. explicit Markdown links define dependencies and selected closure;
5. a traversal receipt records selected paths, revisions, dependencies,
   exclusions, and context size;
6. Restore/Reconcile/Evolve/Discover/Behavior-neutral, the Contract Change
   Envelope, provisional/final Spec Basis, discrepancy classification,
   legitimate Contract Delta, revision pinning, and QA mappings remain active;
7. startup or compaction reopens the recorded Markdown path without loading
   unrelated siblings;
8. JSON manifests, generated route registries, and resolver requirements are
   removed from the specification and governance trees.

Workflow repair and corpus migration are separate scopes. Repair may install
or reconcile `scripts/check_spec_markdown.py`, `scripts/spec_migration.py`, the
migration plan template, and `prompts/migrate-legacy-spec-library.md`, but it
must not classify or rewrite the corpus without an approved migration plan.

Use `apply_patch`. Verify links, reachability, node sizes, contradictory or
duplicate gates, preserved instructions, project-only scope, no JSON in the
Markdown trees, no product implementation changes, docs checks, and
`git diff --check`. Do not install or modify a lifecycle hook unless explicitly
in scope. Follow the target checkpoint policy and report exact residuals.
