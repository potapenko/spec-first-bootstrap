# Migrate A Large Legacy Specification Library

Use https://github.com/potapenko/spec-first-bootstrap as the canonical workflow
reference.

Migrate this project's existing specification library to hierarchical routing.
Keep the work inside the target repository. Do not change product
implementation, product behavior, global agent configuration, or optional
agent/browser/lifecycle layers.

This prompt is for a project that already has many specification documents. It
is not a substitute for brownfield discovery when reliable specifications do
not exist.

## Read and plan first

Read completely:

1. the active global and project instruction chain;
2. the target spec README or index and the smallest applicable routed closure;
3. from the Bootstrap, the `legacy-spec-migration` profile, its complete
   contract closure, its routed migration guidance, this prompt, the
   migration-plan template, `scripts/spec_route.py`, and
   `scripts/spec_migration.py`;
4. target-project Git, documentation, safety, QA, and release rules required to
   preserve authority and history.

Classify the Bootstrap change as installed workflow and the target corpus work
as Reconcile when existing authority is reliable, or Discover where authority
is missing or contradictory. Establish a Contract Change Envelope with product
implementation forbidden.

Before any write, perform only a bounded read-only census: locate candidate
spec roots, count files and words mechanically, identify existing indexes or
routes, and inspect a small representative sample. Do not read the corpus
wholesale. Present an evidence-based migration plan with the exact source root,
migration-state path, batch limits, task-owned paths, verification, and
protected behavior. Wait for explicit approval when the target instructions
require it.

## Context boundary

- Never place the complete inventory or corpus bodies in the conversation.
- Use mechanical tools for counting, hashing, headings, links, filtering,
  coverage, and drift detection.
- Keep at most one semantic batch active.
- Default batch limits are 25 documents and 12,000 source words; stop at the
  first limit. A single larger document forms its own batch.
- Read only the current batch's applicable authority, documents, direct
  dependencies, and acceptance evidence.
- Split an oversized batch instead of raising its budget automatically.

## Durable migration state

After approval, create:

```text
docs/specs/migrations/<migration-id>/
  plan.md
  inventory.json
  batches/
    <batch-id>.json
  receipts/
    <batch-id>.md
```

Adapt the root only when the target project uses another canonical spec path.
The plan follows `docs/specs/templates/legacy-migration-plan.md`.

Generate the inventory without printing document bodies:

```sh
python3 scripts/spec_migration.py inventory <legacy-spec-root> \
  --output docs/specs/migrations/<migration-id>/inventory.json \
  --exclude 'migrations/**'
```

Use `status` to select work and `verify` before and after every batch. Do not
open the full inventory merely to count or filter it.

## Inventory and classification

The inventory records sorted source paths, SHA-256 hashes, byte and word counts,
Markdown headings, local links, and declared contract metadata. These are
routing evidence only.

Each batch file uses this shape:

```json
{
  "schema_version": 1,
  "batch_id": "account-access",
  "documents": [
    {
      "path": "legacy/account/login.md",
      "disposition": "contract",
      "node_id": "product.account.login",
      "target": "legacy/account/login.md"
    }
  ]
}
```

Allowed dispositions are:

- `contract`: normative product behavior; requires `node_id`;
- `resource`: required evidence, plan, runbook, design, QA, or baseline;
  requires `node_id`;
- `historical`: retained context that is not current authority;
- `superseded`: replaced by `canonical_path`;
- `duplicate`: duplicates `canonical_path`;
- `deferred`: unresolved and explicitly incomplete.

Do not classify from a filename, title, heading, date, or current code alone.
For each semantic batch, read the smallest complete applicable evidence, state
the provisional and final Spec Basis, and classify discrepancies. Stop only the
affected batch on a real product fork.

## Incremental route migration

For each approved batch:

1. verify inventory hashes and current route revisions;
2. select one coherent product domain within both batch limits;
3. read that batch and its explicit dependencies completely;
4. assign every document in the batch exactly one disposition;
5. add or update the smallest branch, leaf, or hybrid route nodes;
6. add stable contract, domain, clause, and revision IDs only after authority is
   reconciled;
7. keep existing document paths by default;
8. when an approved batch changes a source document, record its pre-change
   hash, review the semantic diff, regenerate the inventory with the same
   command, and record the new digest; never refresh inventory to hide
   unexplained drift;
9. validate the route and a representative task closure;
10. write a compact receipt and name the next batch;
11. follow the target repository's scoped checkpoint policy.

Do not delete, move, merge, split, or rewrite a legacy document as part of
ordinary route classification. Such normalization needs an explicitly approved
batch, preserved provenance, updated inbound links, and semantic-equivalence
verification.

## Resume

On resume or after context compaction, re-read instructions, the migration
plan, compact status, current batch receipt, current route revisions, and only
the current batch closure. Do not reload completed batches or the full corpus.

```sh
python3 scripts/spec_migration.py status \
  docs/specs/migrations/<migration-id>/inventory.json \
  --mapping-dir docs/specs/migrations/<migration-id>/batches
```

## Verification and completion

Before completing a batch:

```sh
python3 scripts/spec_migration.py verify \
  docs/specs/migrations/<migration-id>/inventory.json \
  --mapping-dir docs/specs/migrations/<migration-id>/batches
python3 scripts/spec_route.py validate docs/specs/route.json
```

For final completion add `--require-complete`. Completion requires zero
unclassified or deferred documents, no duplicate mappings or hash drift,
canonical targets for duplicate/superseded records, valid route closures, and
no hidden semantic conflict. Report counts and paths, not the full inventory.
