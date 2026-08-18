Generate first-pass product specs for the highest-priority named domains.

Use this Bootstrap as the reference:

https://github.com/potapenko/spec-first-bootstrap

Read `docs/spec-first-workflow.md` first. Use Discover or Reconcile as justified
and do not change product implementation.

Start at the project's `docs/specs/README.md` and follow only relevant Markdown
links. Before implementation evidence, record the traversal receipt and
provisional Spec Basis. If no governing node exists, record the absence rather
than treating the first source file or test as product authority.

Inspect the smallest complete applicable source, design, QA, runtime, history,
and release evidence set. Keep authority (Draft/Active/Superseded/Historical)
separate from stability (Evolving/Accepted/Released/Deprecated).

Each contract node should include stable domain and clause IDs, goal, scope,
non-goals, user-visible behavior, invariants, edge cases, state/data/route
implications, verification, evidence, dependencies, revision, and unknowns.

Create short Markdown branch nodes when subdomains can be selected
independently. Link branches, leaves, and dependencies with ordinary Markdown
links. Every node must contain at most 100 physical lines; prefer 50–80. Do not
create JSON manifests or generated routing state.

Keep the specs explicit and product-level. Do not turn them into technical
design documents or fill a real product fork with agent preference.
