# Product Truth Coordination And Lifecycle
- Node type: leaf
- Contract: `governance.product-truth.coordination@1`
- Clauses: `PT.PACKET.CONTEXT`, `PT.PACKET.ROLES`, `PT.EPOCH.PIN`,
  `PT.LIFECYCLE.RESTORE`, `PT.RECEIPT.DISCREPANCY`

## PT.PACKET.CONTEXT — Finite linked worker context

A product worker receives the smallest sufficient packet, not the root
conversation or full governance tree. The packet contains:

- packet ID, finite objective, mode, and authorized node/clause IDs;
- Markdown traversal receipt and pinned contract revisions;
- protected domains, specified expectation, and accepted decisions;
- exact evidence and owner paths;
- permitted specification delta and forbidden inventions;
- writable and forbidden paths;
- checks, stop conditions, and terminal receipt format.

An implementation worker does not reinterpret product intent. Missing linked
authority is returned as a dependency rather than reconstructed from source,
tests, logs, runtime, or chat.

## PT.PACKET.ROLES — Authority separation

The primary single agent may route, reconcile, implement, and verify a bounded
task sequentially. For persistent goals, `/root` preserves the objective,
envelope, traversal receipts, revisions, protected domains, accepted evidence, and
packet state while delegating finite work.

Evidence explorers classify assigned authority and evidence without editing
intent. Specification owners edit named nodes/clauses only. Implementation
owners realize the pinned basis. Reviewers check legitimate change authority,
envelope scope, evidence consistency, implementation fidelity, and protection
of adjacent domains. QA owners verify exact action-state-result chains and do
not weaken them.

## PT.EPOCH.PIN — Revision-safe work

Every product packet pins Markdown paths, contract revisions, and clause IDs.
A semantic change advances the affected contract revision or epoch. After a
change, revalidate or retire open packets using affected clauses; unaffected
packets may continue. Editorial changes need not advance the semantic epoch
when review confirms unchanged meaning.

Paths and line numbers do not replace stable identifiers. For long-running
work, the restart-safe registry records each packet's selected nodes and epoch.

## PT.LIFECYCLE.RESTORE — Restart and context compaction

After startup, resume, clear, or compaction, re-read applicable instruction
layers, the current objective and envelope, the latest traversal receipt,
selected Markdown nodes, pinned contract closure, revisions, accepted deltas,
unresolved discrepancies, and only the evidence/QA instructions needed next.

Reopen the recorded Markdown path. If node or contract revisions differ,
record revision drift and re-establish the Spec Basis before product action. If
the task or domain changed, traverse from the root node again. Do not reread
unselected sibling contracts merely because context was compacted.

Chat summaries, memory, worker lists, old receipts, builds, tests, screenshots,
and raw configuration do not replace current contracts. Workers restart from
their finite packet and pinned closure rather than the root conversation.

## PT.RECEIPT.DISCREPANCY — Compact return

A bounded discrepancy receipt states packet, selected revisions and clauses,
mode, evidence inspected, expected and actual behavior, classification,
authorized resolution, protected domains checked, required spec delta, whether
a user decision is needed, and the exact residual.

A release baseline records release/deployment ID and date, implementation
revision, selected contract revisions, included domains/clauses, QA/runtime
evidence, compatibility notes, and residuals. Receipts preserve decision-grade
facts without returning raw working context.
