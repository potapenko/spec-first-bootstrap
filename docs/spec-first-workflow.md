# Strict Spec-First Workflow

This is the compact canonical workflow for projects using
`spec-first-bootstrap`. Intended behavior is established before implementation
choices shape it, while source, design, QA, runtime, history, and release
evidence still complete the product picture.

Full doctrine is no longer one mandatory monolith. Start at the compact
product-truth router and resolve only the applicable contract closure:

```text
docs/agent/product-truth-governance.md
docs/agent/product-truth/route.json
```

The Bootstrap source keeps those files under `docs/agent-governance/`.

## Separate truth layers

1. Routed specifications define intended product behavior.
2. Design and implementation establish current structure, ownership, and
   realization.
3. Tests, QA, runtime, screenshots, history, and release records establish
   observation, acceptance, and compatibility.

Specifications are canonical but not infallible or self-authorizing. Evidence
may expose a missing, stale, ambiguous, or contradictory contract; it does not
silently replace intent. Spec-first does not mean spec-only.

## Hierarchical routing

The specification tree uses non-normative `route.json` manifests and normative
Markdown contracts. A node may be:

- a leaf with a local contract;
- a branch with children;
- a hybrid with both.

Each branch describes children with `summary`, `read_when`, and
`do_not_read_when`. These fields select a path but cannot define behavior.
Cross-domain `requires` edges form a dependency graph over the navigation tree.

Task-to-node selection requires agent judgment. Once node IDs are selected,
dependency expansion, budget checking, and revision drift detection are
mechanical.

```sh
python3 scripts/spec_route.py validate docs/specs/route.json
python3 scripts/spec_route.py resolve docs/specs/route.json --node <domain-id>
```

Completeness means the smallest complete selected contract closure, not every
document in a directory, every ancestor body, or every sibling domain.

## Mandatory pre-decision order

For product features, behavioral questions or defects, UX/state/data work,
migrations, product QA, release behavior, and refactors with possible
behavioral impact:

1. Re-read applicable instruction layers.
2. Read the product-truth router and select the applicable governance profile.
3. Start at the project specification root route.
4. Traverse matching branches and select the smallest governing node IDs.
5. Resolve explicit dependencies and read every selected contract completely.
6. Record the Route Receipt.
7. Classify the task and establish the Contract Change Envelope.
8. State the provisional Spec Basis.
9. Only then inspect the smallest complete source/design/QA/runtime/history/
   upstream/release evidence set.
10. Classify material discrepancies.
11. Accept only a legitimate Contract Delta and pin the final basis.
12. Only then implement and verify the authorized slice.

Until steps 1–8 are complete, do not inspect implementation source, interpret
runtime evidence, form a failure hypothesis, recommend a repair, infer product
intent, or call a non-reading task tool. There is no urgency, debugging,
read-only-investigation, or one-command exception.

When no route or contract governs the domain, record that absence and use
Discover. Do not promote the first code, test, process, or runtime observation
into intended behavior.

## Route Receipt

The receipt records:

```text
Task:
Root manifest:
Selected node IDs and traversal path:
Routing manifests read:
Contract closure, clause IDs, and revisions:
Cross-domain dependencies:
Explicitly excluded siblings:
Resolved context words:
Revision drift or ambiguity:
```

It establishes context provenance but cannot replace selected contracts or
create product authority.

## Change mode and envelope

Every covered task uses one primary mode:

- **Restore**: implement or repair an established contract.
- **Reconcile**: align the contract with one evidenced existing product truth.
- **Evolve**: implement a user-authorized semantic change in a named domain.
- **Discover**: understand a product whose contract is missing or unreliable,
  without implementation.
- **Behavior-neutral**: make a proven non-behavioral change.

The Contract Change Envelope names the authorized outcome, nodes and clauses,
protected adjacent domains, shared owners, stability/baseline, evidence,
allowed and forbidden spec delta, user decisions, route/contract revisions,
review, QA, and task-owned paths.

Writable files do not enlarge product authority. A newly discovered semantic
dependency outside the envelope is returned rather than silently absorbed.

## Provisional and final Spec Basis

The provisional basis contains the Route Receipt, mode and envelope, specified
expectation, protected behavior, established operational flow, apparent gaps,
evidence still needed, and provisional implementation authorization.

After evidence reconciliation, the final basis pins route and contract
revisions, resolved behavior, evidence roles, discrepancy dispositions,
accepted delta, protected domains, acceptance scenarios, and implementation
authorization.

A provisional mismatch is an evidence trigger, not automatically a user
decision. Ask the user only after complete evidence proves a real product fork,
protected cross-domain change, material compatibility consequence, or missing
external authority.

## Discrepancies and implementation

Classify mismatches as implementation defect, specification defect or omission,
stale evidence, authorized evolution, real product fork, or external authority
blocker. Never edit whichever artifact is easiest merely to obtain consistency.

When meaning changes, update the selected contract and Contract Delta before
implementation and advance the affected semantic revision. Spec and code may
share a checkpoint; the ordering is about authority.

QA verifies pinned action-state-result chains and does not independently define
intent. Runtime and visual evidence remain required when the contract names
observable behavior.

## Restart and compaction

After startup, resume, clear, or context compaction:

1. re-read applicable instructions and current task/goal state;
2. restore the latest Route Receipt and Contract Change Envelope;
3. rerun route resolution to detect manifest or contract revision drift;
4. reread the selected closure and only the next-action evidence/QA guidance;
5. traverse from the root again only when the task changed or the prior route
   is missing or ambiguous.

Do not reload unselected siblings merely because context was compacted. Chat
summaries and old receipts do not replace current contracts; they identify what
must be revalidated.

## Authoring and validation

- Keep product behavior in contracts and routing metadata in manifests.
- Use stable domain and clause IDs.
- Split a node when its responsibilities have different selection conditions.
- Declare cross-domain dependencies explicitly.
- Keep honest context budgets; do not raise them automatically.
- Update parent routing and semantic revisions together.
- Reject orphan nodes, broken paths, duplicate IDs, cycles, invalid statuses,
  unresolved dependencies, and budget overflow.

The goal is decision-complete context, not maximum context.
