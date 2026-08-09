Generate first-pass product specs for the highest-priority named domains.

Use this bootstrap repository as the reference:

https://github.com/potapenko/spec-first-bootstrap

Read `docs/spec-first-workflow.md` from that reference first. Use Discover or
Reconcile mode as justified. Do not change product implementation.

Read the project's existing spec registry and contracts first. Inspect the
smallest complete applicable source, design, QA, runtime, history, and release
evidence set. Treat current implementation as evidence, not automatic product
intent.

Before that evidence inspection, name the complete directly applicable
governing set and state a provisional Spec Basis. If bounded discovery finds no
governing specification, record the absence explicitly instead of treating the
first source or test as product authority.

Do not mark a contract Active merely because implementation exists. Record
authority (Draft/Active/Superseded/Historical) separately from stability
(Evolving/Accepted/Released/Deprecated).

Each spec should include:

- Goal
- Stable contract and domain IDs
- Scope
- Non-goals
- User-visible behavior
- Invariants
- Edge cases and failure policy
- Route / state / data implications
- Verification mapping
- Evidence mapping
- Unknowns requiring confirmation

Keep the specs short, explicit, and product-level.

Do not turn them into technical design docs.
Do not fill a real product fork with agent preference.
