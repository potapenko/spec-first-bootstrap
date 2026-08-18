# Legacy Specification Library Migration

- Contract ID: `bootstrap.legacy-spec-migration`
- Domain ID: `bootstrap.legacy-spec-migration`
- Authority: Active
- Stability: Accepted
- Governs: migration of large pre-routing specification libraries
- Contract revision or epoch: `bootstrap.legacy-spec-migration@1`
- Clauses: `BOOTSTRAP.MIGRATION.INVENTORY`, `BOOTSTRAP.MIGRATION.BATCH`,
  `BOOTSTRAP.MIGRATION.SAFETY`, `BOOTSTRAP.MIGRATION.RESUME`,
  `BOOTSTRAP.MIGRATION.COMPLETE`
- Release baseline: None

## Goal

Convert an existing flat or inconsistently structured specification library to
hierarchical routing without loading the whole corpus into one agent context,
losing documents, or silently changing product meaning.

## User-visible behavior

### BOOTSTRAP.MIGRATION.INVENTORY

Migration begins with a deterministic mechanical inventory of the legacy
corpus. It records paths, hashes, sizes, word counts, headings, and local links
without emitting document bodies into the agent conversation. Inventory
metadata may suggest batches but never determines product authority or meaning.

### BOOTSTRAP.MIGRATION.BATCH

The agent processes one bounded product-domain batch at a time. Every legacy
document receives exactly one tracked disposition: routed contract, supporting
resource, historical, superseded, duplicate, or deferred. Contract and resource
classification requires semantic review of that batch; filenames and headings
alone are insufficient.

Processed contracts enter the hierarchical route incrementally. Unprocessed
documents remain visible in migration coverage and are never represented as
migrated.

### BOOTSTRAP.MIGRATION.SAFETY

The default migration adds routing and metadata around existing documents. It
does not delete, move, merge, split, or rewrite legacy documents. Those actions
require an explicit approved batch, preserved provenance, link updates, and
verification that no product rule was lost or invented.

Migration changes no product implementation. Existing Active, Accepted,
Released, and legacy-released behavior remains protected until reconciled from
the smallest complete evidence set.

### BOOTSTRAP.MIGRATION.RESUME

Migration state is durable and restartable. A resumed agent reads the migration
plan, compact status, current batch receipt, and only the routed authority for
that batch. It does not reload completed batches or the complete inventory into
conversation context.

Each batch records its source hashes, dispositions, route changes, unresolved
conflicts, verification, and next batch. Hash drift or route-revision drift is
reported before further mutation.

### BOOTSTRAP.MIGRATION.COMPLETE

Migration is complete only when every inventoried document has one terminal,
non-deferred disposition; every routed contract validates; duplicates and
superseded files name their canonical replacement; source drift is resolved;
representative task closures stay within their budgets; and no unresolved
semantic conflict is hidden by structural cleanup.

## Invariants

- Corpus-wide mechanical analysis is not corpus-wide semantic reading.
- A migration manifest or router summary never creates product authority.
- No legacy document disappears from coverage.
- Deferred is visible progress state, not a completion disposition.
- A structural migration does not authorize product implementation.
- Context budgets are enforced per selected closure and per migration batch.

## Failure policy

- Stop the affected batch when two documents claim conflicting Active behavior
  without precedence.
- Stop before moving or rewriting a document when inbound links, provenance, or
  semantic equivalence cannot be established.
- Regenerate or explicitly reconcile the inventory when a source hash changes.
- Split an oversized batch instead of raising its context budget automatically.
- Preserve independently valid completed batches when another batch is blocked.

## Evidence mapping

- `prompts/migrate-legacy-spec-library.md`
- `scripts/spec_migration.py`
- `docs/specs/templates/legacy-migration-plan.md`
- `docs/specs/legacy-migration-routing.md`

## Verification mapping

- deterministic inventory and compact-status unit tests;
- missing, duplicate, deferred, and hash-drift coverage tests;
- a generated thousand-document corpus fixture;
- route validation and representative closure resolution;
- local Markdown-link checks and `git diff --check`.

## Unknowns requiring confirmation

None.
