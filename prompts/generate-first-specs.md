Generate first-pass product specs for the highest-priority named domains.

Use this bootstrap repository as the reference:

https://github.com/potapenko/spec-first-bootstrap

Read `docs/spec-first-workflow.md` from that reference first.

Use Discover or Reconcile mode as justified. Do not change product
implementation in this prompt.

Read the project's spec registry and existing contracts first. If a governing
spec exists, update it instead of creating a competing contract.

Inspect the smallest complete applicable source, design, QA, runtime, history,
and release evidence set. Separate observed behavior from intended behavior.

Do not mark a contract Active merely because implementation exists.

Record both:

- authority: Draft, Active, Superseded, or Historical;
- stability: Evolving, Accepted, Released, or Deprecated.

Each spec should include:

- stable contract and domain IDs;
- goal and vocabulary;
- scope and non-goals;
- user-visible behavior;
- states, actions, transitions, and effects where product-significant;
- invariants;
- edge cases and failure policy;
- route, state, data, permission, persistence, and compatibility implications;
- cross-domain dependencies and precedence;
- evidence mapping;
- stable QA scenario IDs;
- unknowns requiring confirmation.

Keep the normative specs short, explicit, and product-level. Put source paths,
hashes, captures, and long proof in evidence artifacts.

Do not turn specs into technical design docs.
Do not fill a real product fork with agent preference.
