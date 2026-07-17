Use https://github.com/potapenko/spec-first-bootstrap as the spec-first
reference.

Read its `docs/spec-first-workflow.md`, `AGENTS.md`, `docs/specs/README.md`,
spec template, and `examples/favorites-spec.md` as an example only.

This is an existing project that needs a spec-first migration.

Record that reliable specs are missing or incomplete before inspecting source.
Do not change implementation code during this discovery pass.

Analyze the current repository and extract product behavior from:

- code
- routes
- state transitions
- tests
- docs
- UI flows

Produce:

1. a product map
2. a spec backlog
3. the top product areas that need first-pass specs
4. unknowns, conflicts, and assumptions that need confirmation
