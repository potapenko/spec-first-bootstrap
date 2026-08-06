Use https://github.com/potapenko/spec-first-bootstrap as the spec-first
reference.

Read its `docs/spec-first-workflow.md`, `AGENTS.md`, `docs/specs/README.md`,
spec template, and `examples/favorites-spec.md` as an example only.

This is an existing project that needs a spec-first migration.

Use Discover mode. Record that reliable specs are missing or incomplete before
inspecting source. Establish a bounded Contract Change Envelope with
implementation unauthorized.

Do not change implementation code during this discovery pass.

Analyze the smallest complete relevant evidence set:

- source and ownership;
- routes, state, persistence, permissions, and public data contracts;
- design and UI flows;
- tests and QA action-state-result chains;
- runtime behavior;
- history and release evidence.

Produce:

1. a product-domain map;
2. observed behavior separated from intended behavior;
3. a spec backlog;
4. authority and stability classifications;
5. the top domains needing first-pass specs;
6. real conflicts, unknowns, and assumptions requiring confirmation;
7. legacy-released behavior that must be protected until reconciled.
