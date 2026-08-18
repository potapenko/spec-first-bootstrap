# Legacy Specification Migration Plan

- Migration ID:
- Status: planned | in_progress | blocked | complete
- Change mode: Reconcile | Discover
- Approved by:
- Source specification root:
- Migration state root:
- Inventory revision or digest:
- Root route revision:
- Maximum documents per batch: 25
- Maximum source words per batch: 12000

## Contract Change Envelope

- User-authorized outcome:
- Authorized specification domains:
- Protected product and adjacent domains:
- Product implementation authorization: forbidden
- Allowed specification delta:
- Forbidden specification delta:
- Stability or release baseline:
- Evidence required:
- Material decisions requiring the user:

## Corpus baseline

- Total documents:
- Total words:
- Existing routed documents:
- Existing unregistered documents:
- Known authority conflicts:
- Legacy-released behavior requiring protection:

## Migration strategy

- Initial domain and batch order:
- Documents that must stay in place:
- Optional normalization deferred until after routing:
- Route and context-budget verification:
- Checkpoint policy:

## Durable state

- Inventory: `inventory.json`
- Batch mappings: `batches/`
- Batch receipts: `receipts/`
- Compact status command:
- Drift verification command:

## Current batch

- Batch ID:
- Selected domain:
- Source documents and words:
- Governing routed closure:
- Dependencies:
- Expected dispositions:
- Stop conditions:

## Completion contract

- Every inventory path has one terminal disposition.
- Deferred, unclassified, duplicate-mapped, and hash-drift counts are zero.
- Duplicate and superseded documents name canonical paths.
- Every routed contract and representative task closure validates.
- No document was moved, deleted, or semantically rewritten without explicit
  approved scope and provenance verification.
- Product implementation did not change.

## Next action

- Next batch or decision:
- Exact files and authority required:
