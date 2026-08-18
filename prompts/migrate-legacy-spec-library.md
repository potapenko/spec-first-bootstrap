# Migrate A Large Legacy Specification Library

Use https://github.com/potapenko/spec-first-bootstrap as the canonical workflow
reference. Keep work inside the target repository. Do not change product code,
product behavior, global configuration, or optional agent/browser/lifecycle
layers.

## Read and plan first

Read the active instruction chain; the target spec Markdown root and smallest
applicable linked closure; the Bootstrap migration contract, guidance, prompt,
template, and helper scripts; and target Git/docs/safety/QA/release rules.

Use Reconcile where legacy authority is reliable and Discover where it is
missing or contradictory. Establish an envelope with product implementation
forbidden. Before writes, run a bounded mechanical census: count candidate
files, words, and oversized documents without printing bodies, identify the
current index, and inspect only a representative sample. Present exact source
root, Markdown migration-state path, batches, write set, verification, and
protected behavior before approval when project rules require it.

## Context boundary

- Never place the complete inventory or corpus bodies in the conversation.
- Keep at most one semantic batch active.
- Default limits are 3 documents or 12,000 source words, whichever comes first;
  one larger document forms its own batch.
- Read only the active batch, its applicable authority, direct dependencies,
  and acceptance evidence.
- Every resulting node has at most 100 physical lines; prefer 50–80.

## Markdown migration state

After approval create only Markdown state:

```text
docs/specs/migration/
  README.md
  batches/<batch-id>.md
  receipts/<batch-id>.md
```

`README.md` links every pending, active, and completed batch. Each batch links
its source documents, intended target nodes, disposition, dependencies, and
status. Each receipt records revisions, evidence, semantic disposition,
verification, and next batch. Do not create JSON inventory, mapping, or route
files.

Run a compact census without storing machine authority:

```sh
python3 scripts/spec_migration.py census <legacy-spec-root> \
  --exclude 'migration/**' --max-lines 100
```

## One batch

1. verify source paths and current Markdown links;
2. read one coherent bounded batch completely;
3. state provisional and final Spec Basis and classify discrepancies;
4. give every source one Markdown-recorded disposition: contract, resource,
   historical, superseded, duplicate, or deferred;
5. create or update the smallest root/branch/leaf/hybrid nodes and ordinary
   Markdown dependency links;
6. preserve stable IDs and revisions only after authority is reconciled;
7. preserve legacy paths or leave explicit forwarding links when splitting;
8. review semantic equivalence and inbound links;
9. validate reachability, links, no JSON, and the 100-line maximum;
10. write the compact receipt and checkpoint under repository policy.

On resume, read instructions, `docs/specs/migration/README.md`, the active batch
and latest receipt, then reopen only their linked nodes. Do not reload completed
batches or the full corpus.

Coverage is optional mechanical evidence:

```sh
python3 scripts/spec_migration.py coverage <legacy-spec-root> \
  --batch-root docs/specs/migration/batches --require-complete
python3 scripts/check_spec_markdown.py \
  --root docs/specs/README.md --scan docs/specs --max-lines 100
```

Final completion requires every legacy source to be represented exactly once,
zero deferred items, valid links, no unreachable or oversized node, no JSON
routing state, preserved authority, and no unresolved semantic conflict.
Report compact counts and paths, never corpus bodies.
