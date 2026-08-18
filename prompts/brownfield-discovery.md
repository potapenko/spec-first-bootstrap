Use https://github.com/potapenko/spec-first-bootstrap as the spec-first
reference.

Read its `docs/spec-first-workflow.md`, `AGENTS.md`, `docs/specs/README.md`,
spec template, and `examples/favorites-spec.md` as an example only.

This is an existing project that needs a spec-first migration.

Use Discover mode. Record that reliable specs are missing or incomplete and
establish a bounded Contract Change Envelope before inspecting source.
Do not change implementation code during this discovery pass.

Before source or runtime evidence, state the Route Receipt, selected contracts,
linked plan/runbook/design/QA/release leaves, and provisional Spec Basis. If no
node governs the domain, record that absence explicitly; do not infer intent
from the first implementation artifact found.

Analyze the smallest complete applicable evidence set:

- source and ownership;
- routes, state transitions, persistence, permissions, and public contracts;
- design and UI flows;
- tests and QA action-state-result chains;
- runtime behavior;
- history and released behavior.

Produce:

1. a hierarchical product-domain route with leaf, branch, or hybrid nodes;
2. observed behavior separated from intended behavior;
3. a spec backlog;
4. authority, stability, clause IDs, revisions, dependencies, and context budgets;
5. the top product areas that need first-pass specs;
6. unknowns, conflicts, and assumptions requiring confirmation;
7. legacy-released behavior that must be protected until reconciled.
