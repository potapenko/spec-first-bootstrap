# Start HoldType Swift Specification Migration

Target repository:
`/Users/eugenepotapenko/Projects/potapenko-github/holdtype-swift`

Canonical workflow repository:
`/Users/eugenepotapenko/Projects/potapenko-github/spec-first-bootstrap`

## Objective

Convert the existing HoldType specification library into a selective
Markdown-first root/branch/leaf/hybrid tree without changing product behavior
or implementation and without loading the corpus into one context.

## Mandatory pre-action boundary

1. Work only in the target repository and its current branch. Do not create a
   branch or worktree.
2. Re-read the active global and target `AGENTS.md` files.
3. Read `docs/specs/README.md` and `docs/specs/index.md` only as the initial
   legacy entrypoints. Do not follow every registry row yet.
4. Read the Bootstrap migration contract, `docs/specs/legacy-migration-routing.md`,
   `prompts/migrate-legacy-spec-library.md`, and the referenced templates and
   helper usage. Do not load unrelated Bootstrap branches.
5. Do not inspect Swift/product code, tests, runtime, backlog bodies, or all spec
   bodies during census and checkpoint-0 planning.
6. Do not change product code, product behavior, global configuration, optional
   QA/lifecycle layers, or unrelated repository files.

## Revalidate the snapshot

The planning snapshot was 54 Markdown documents, 146,123 words, 18,498 lines,
and 45 documents over 100 lines. It contained no declared Markdown nodes, no
JSON spec state, and no migration directory. Treat this only as drift evidence.

Run the Bootstrap `scripts/spec_migration.py census` against `docs/specs` with
`migration/**` excluded and a 100-line maximum. Report only compact totals and
at most the largest 12 paths; never print document bodies or a full inventory.

## Checkpoint 0 — plan and stop

Before any write, present an evidence-based plan containing:

- current branch and exact task-owned paths;
- proposed small root/branch structure and preserved legacy entrypoints;
- bounded domain batches selected from registry meaning, not filenames alone;
- one pilot batch, limited to 3 documents or 12,000 source words; one larger
  document may form its own batch;
- protected Active, Accepted, Released, legacy-released, historical, deferred,
  and iOS/macOS precedence rules;
- verification, checkpoint commit and push, exclusions, and real blockers.

Wait for explicit approval. Planning does not authorize conversion.

## After approval

Create only Markdown state under `docs/specs/migration/`: `README.md`, one
active `batches/<id>.md`, and its `receipts/<id>.md`. Do not create JSON routing,
inventory, mapping, or authority files.

Process only the approved pilot batch. Read its sources completely, reconcile
meaning, preserve provenance/inbound links, and give every source a visible
disposition. Resulting nodes must be at most 100 physical lines, preferably
50–80. Validate links, reachability, coverage, source drift, and absence of JSON
routing state. Do not start the second batch in the same checkpoint.

Before committing, verify a safe, writable upstream and that no unrelated local
commits would be pushed. Then create the task-owned checkpoint commit and push it
from the currently checked-out branch. Do not report the batch complete until
both commit and push succeed. Report compact counts, created links, protected
meaning, residuals, and the next batch link; never return corpus bodies.
