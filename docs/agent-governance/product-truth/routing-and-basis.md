# Product Truth Routing And Spec Basis
- Node type: leaf
- Status: Active
- Read when: selecting product contracts or establishing a provisional or final Spec Basis.
- Do not read when: work is proven non-product and behavior-neutral.
- Maximum size: 100 physical lines.
- Contract: `governance.product-truth.routing@3`
- Clauses: `PT.ROUTE.TRAVERSE`, `PT.ROUTE.CLOSURE`, `PT.ROUTE.RECEIPT`,
  `PT.BASIS.PROVISIONAL`, `PT.BASIS.FINAL`
## PT.ROUTE.TRAVERSE — Mandatory pre-decision traversal

Before a project-specific product answer, diagnosis, hypothesis,
recommendation, source inspection, runtime interpretation, non-reading task
tool, implementation, or verification:

1. read applicable instruction layers when establishing the task basis;
2. start at the project specification root Markdown node;
3. use each branch's `summary`, `read_when`, and `do_not_read_when` to descend;
4. select the smallest nodes that govern the named task;
5. resolve their explicit dependency closure;
6. read every selected contract completely;
7. state the Markdown traversal receipt and provisional Spec Basis;
8. only then inspect implementation evidence.

Before the first and each new material choice, distinguish its basis in a read
contract, explicit user authority, or an agent proposal. State it briefly in the
existing Spec Basis, plan, or explanation, not before every tool call. An
agent-authored plan, summary, or Active label cannot by itself establish a requirement.
Equivalent implementation and established test mechanisms need no new approval.

For continuing work, reuse a basis whose full required content is available,
applicable, and current. Recovery loads missing, potentially changed, or uncertain
content completely, including dependencies. Summaries cannot replace missing
contracts. Route again when the task/domain changes or the route is uncertain.

A branch summary navigates; it cannot replace a contract or create intent.
A Markdown node may be a branch, leaf, or both.
When no Markdown path matches, record the missing contract and use Discover.
When two Active nodes conflict without precedence, stop only the affected slice.
## PT.ROUTE.CLOSURE — Smallest complete contract set

Completeness means the selected contract closure, not every sibling:

- selected local contracts;
- explicit `requires` dependencies and named clauses;
- directly required plans, runbooks, operator handoffs, design contracts, QA
  workflows, accepted baselines, and release records;
- shared or upstream contracts whose meaning is necessary to decide the task.

Do not load sibling nodes merely because they share a parent or source owner.
Do not omit an explicit dependency to save context. If source or runtime
evidence reveals an unregistered cross-domain dependency, return to the tree,
expand the closure, and record the discrepancy before acting.

Task-to-domain selection requires product judgment. Dependency links and
revision checking may be verified mechanically after the path is selected.
## PT.ROUTE.RECEIPT — Auditable context provenance

Before evidence inspection, record:

- task and root Markdown node;
- selected node paths, traversal order, and branch nodes read;
- complete contract closure, clause IDs, and revisions;
- cross-domain dependencies;
- explicitly excluded sibling nodes;
- supporting resources and resolved context size;
- ambiguity or revision drift.

The receipt proves traversal provenance. It does not replace the contracts. For
long-running work it is durable; for bounded work it may appear in the first
progress update or Contract Change Envelope.
## PT.BASIS.PROVISIONAL — Investigation frame

The provisional basis states:

- change mode, current envelope, and Markdown traversal receipt;
- specified expectation, protected behavior and domains;
- established operational flow from governing documents;
- apparent gaps or conflicts;
- evidence still needed;
- whether implementation is authorized.

It frames investigation and does not allow spec-only escalation. A mismatch is
an evidence-reconciliation trigger, not automatically a user decision.
## PT.BASIS.FINAL — Reconciled implementation authority

After inspecting the smallest complete applicable evidence set, classify every
material discrepancy and state:

- pinned node and contract revisions;
- resolved intended behavior;
- evidence inspected and its role;
- discrepancy dispositions;
- accepted Contract Delta, if any;
- remaining protected domains;
- required acceptance scenarios;
- implementation authorization.

Implementation proceeds only against this final pinned basis. When meaning
changes, update the contract first and advance the affected semantic revision.
