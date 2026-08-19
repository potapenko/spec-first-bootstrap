# Start Phrases Extractor Specification Migration

Target repository:
`/Users/eugenepotapenko/Projects/playphrase.me/phrases-extractor`

Canonical workflow repository:
`/Users/eugenepotapenko/Projects/potapenko-github/spec-first-bootstrap`

## Objective

Create a selective `docs/specs/README.md` tree for the extractor and migrate
the routed legacy documents under `docs/` without changing pipeline behavior,
data contracts, storage, Mongo state, or product implementation.

## Mandatory pre-action boundary

1. Work only in the target repository and current branch. Do not create a
   branch or worktree.
2. Re-read active global instructions and target `AGENTS.md`.
3. Read `docs/downstream-integration-readme.md` as the legacy entrypoint and
   its `Read In This Order` list as routing only. Do not preload all linked
   documents.
4. Read only the Bootstrap migration contract,
   `docs/specs/legacy-migration-routing.md`,
   `prompts/migrate-legacy-spec-library.md`, referenced templates, and helper
   usage.
5. Do not inspect Clojure source, tests, runtime, logs, MongoDB, object storage,
   remote services, or production during census and checkpoint-0 planning.
6. Do not change code, behavior, data, global configuration, or unrelated
   repository files.

## Revalidate the snapshot

The planning snapshot for `docs/` was 18 Markdown documents, 23,180 words,
5,352 lines, and 15 documents over 100 lines. The largest was
`search-service-migration-plan.md` at 1,049 lines. There was no declared
Markdown node, JSON spec state, migration directory, or `docs/specs/README.md`.
Repeat the mechanical census without printing document bodies.

## Protected authority

Preserve the frozen phrase-document shape, `/<movie-id>/<phrase-id>.mp4`
playback path, `Movie.words.json`/`Movie.words.srt` artifact boundary, segment
timing, site-facing compatibility fields, phrase search correctness, and the
distinction between upstream preparation and downstream extraction. Runbooks,
audits, plans, and operations notes remain resources unless reconciled as
normative contracts. Migration never authorizes direct database access.

## Checkpoint 0 — plan and stop

Before writes, present the current branch, exact write set, the new
root/branch structure, preserved legacy entrypoint, source dispositions, and a
Markdown tree derived from actual meaning. Select one pilot batch of
3 documents or 12,000 source words; one larger document may stand alone.
Include verification. Wait for explicit approval.

## After approval

Create only Markdown state under `docs/specs/migration/`: `README.md`, one
active batch node, and one receipt. Do not create JSON routing, inventory,
mapping, or authority files.

Process only the approved batch. Read its sources and direct dependencies,
preserve provenance and inbound links, and record every source disposition.
Every node must be at most 100 physical lines, preferably 50–80. Validate links,
reachability, coverage, drift, and no JSON routing state. Do not start another
batch in the same checkpoint.

At the end of the batch, create a checkpoint commit in the currently checked-out
branch containing only the files you changed for this task. Unrelated changes do
not block the checkpoint and remain untouched. Do not report the batch complete
until the commit succeeds. Report compact counts, node links, protected contracts,
residuals, and the next batch.
