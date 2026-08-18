# Product Truth Routing And Spec Basis

- Contract: `governance.product-truth.routing@1`
- Clauses: `PT.ROUTE.TRAVERSE`, `PT.ROUTE.CLOSURE`, `PT.ROUTE.RECEIPT`,
  `PT.BASIS.PROVISIONAL`, `PT.BASIS.FINAL`

## PT.ROUTE.TRAVERSE — Mandatory pre-decision traversal

Before a project-specific product answer, diagnosis, hypothesis,
recommendation, source inspection, runtime interpretation, non-reading task
tool, implementation, or verification:

1. re-read applicable instruction layers;
2. start at the project specification root route;
3. use each branch's `summary`, `read_when`, and `do_not_read_when` to descend;
4. select the smallest nodes that govern the named task;
5. resolve their explicit dependency closure;
6. read every selected contract completely;
7. state the Route Receipt and provisional Spec Basis;
8. only then inspect implementation evidence.

A router is non-normative navigation metadata. Its summary cannot replace a
contract or create product intent. A node may have a local contract, child
route, or both; branch and leaf are roles rather than different document types.

When no route matches, record the missing contract and use Discover. When two
Active routes conflict without precedence, stop only the affected slice.

## PT.ROUTE.CLOSURE — Smallest complete contract set

Completeness is measured by the selected contract closure, not by reading
every document in a directory or every sibling domain. The closure contains:

- selected local contracts;
- explicit `requires` dependencies and named clauses;
- directly required plans, runbooks, operator handoffs, design contracts, QA
  workflows, accepted baselines, and release records;
- shared or upstream contracts whose meaning is necessary to decide the task.

Do not load sibling nodes merely because they share a parent or source owner.
Do not omit an explicit dependency to save context. If source or runtime
evidence reveals an unregistered cross-domain dependency, return to the route,
expand the closure, and record the discrepancy before acting.

Task-to-domain selection requires product judgment. After node IDs are
selected, dependency expansion and revision checking should be mechanical.

## PT.ROUTE.RECEIPT — Auditable context provenance

Before evidence inspection, record:

- task and root manifest;
- selected node IDs and traversal path;
- routing manifests read;
- complete contract closure, clause IDs, and revisions;
- cross-domain dependencies;
- explicitly excluded sibling nodes;
- supporting resources and resolved context size;
- ambiguity or revision drift.

The receipt proves routing provenance. It does not replace the contracts. For
long-running work it is durable; for bounded work it may appear in the first
progress update or Contract Change Envelope.

## PT.BASIS.PROVISIONAL — Investigation frame

The provisional basis states:

- change mode and current envelope;
- Route Receipt;
- specified expectation;
- protected behavior and domains;
- established operational flow from governing documents;
- apparent gaps or conflicts;
- evidence still needed;
- whether implementation is authorized.

It frames investigation and does not allow spec-only escalation. A mismatch is
an evidence-reconciliation trigger, not automatically a user decision.

## PT.BASIS.FINAL — Reconciled implementation authority

After inspecting the smallest complete applicable evidence set, classify every
material discrepancy and state:

- pinned contract and route revisions;
- resolved intended behavior;
- evidence inspected and its role;
- discrepancy dispositions;
- accepted Contract Delta, if any;
- remaining protected domains;
- required acceptance scenarios;
- implementation authorization.

Implementation proceeds only against this final pinned basis. When meaning
changes, update the contract first and advance the affected semantic revision.
