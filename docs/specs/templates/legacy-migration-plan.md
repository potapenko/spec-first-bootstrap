# Legacy Specification Migration

- Node type: root | branch | hybrid
- Migration ID:
- Status: planned | in_progress | blocked | complete
- Change mode: Reconcile | Discover
- Approved by:
- Source specification root:
- Maximum sources per batch:
- Maximum source words per batch:
- Maximum node size: 100 physical lines.

## Contract Change Envelope

- User-authorized outcome:
- Authorized specification domains:
- Protected product and adjacent domains:
- Product implementation authorization: forbidden
- Allowed specification delta:
- Forbidden specification delta:
- Evidence required:
- Material decisions requiring the user:

## Corpus baseline

- Total documents:
- Total words:
- Existing Markdown nodes:
- Unmigrated documents:
- Known authority conflicts:

## Batches

- [Current batch](<migration-root>/batches/<batch>.md) — <domain and status>.
- [Completed batches](<migration-root>/README.md) — <compact linked history>.

## Strategy

- Initial domain order:
- Documents that stay in place:
- Permitted structural splits:
- Link and 100-line verification:
- Checkpoint policy:

## Resume

Read this migration root, the current linked batch, its latest receipt, and only
that batch's authority. Do not reload completed batches or the corpus.

## Completion

Every source has one terminal Markdown disposition; every Active contract is
reachable from the root; every node is at most 100 physical lines; links and
dependencies resolve; drift and conflicts are explicit; product implementation
did not change.
