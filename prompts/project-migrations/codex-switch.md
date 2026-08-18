# Start CodexSwitch Specification Migration

Target repository:
`/Users/eugenepotapenko/Projects/potapenko-github/codex-switch`

Canonical workflow repository:
`/Users/eugenepotapenko/Projects/potapenko-github/spec-first-bootstrap`

## Objective

Create the missing Markdown specification root and convert the small legacy
library into bounded linked nodes without changing CodexSwitch behavior or
implementation.

## Mandatory pre-action boundary

1. Work only in the target repository and current `master`. Do not create a
   branch or worktree.
2. Re-read active global instructions and target `AGENTS.md`.
3. Read `docs/specs/index.md` as the legacy entrypoint. A
   `docs/specs/README.md` root was absent in the planning snapshot; recheck it.
4. Read only the Bootstrap migration contract,
   `docs/specs/legacy-migration-routing.md`,
   `prompts/migrate-legacy-spec-library.md`, referenced templates, and helper
   usage.
5. Do not inspect Swift/AppKit/SwiftUI source, tests, Xcode configuration,
   runtime, or visual UI during census and checkpoint-0 planning.
6. Do not change product code, behavior, credentials, global configuration, or
   unrelated files.

## Revalidate the snapshot

The planning snapshot was 5 Markdown documents, 5,446 words, 693 lines, with
2 oversized contracts: `features/codex-account-status.md` at 400 lines and
`features/account-card.md` at 218 lines. It had no declared Markdown nodes,
JSON spec state, or migration directory. Repeat the mechanical census without
printing bodies.

The repository was clean but `master` was four commits ahead of its upstream.
Recheck this before planning. Read-only census may continue, but never push foreign local commits.
If the ahead commits are not explicitly accepted for
the migration push, identify the integration blocker before any write
checkpoint and ask the user to disposition it.

## Checkpoint 0 — plan and stop

Before writes, present current Git/upstream state, exact write set, the new
`docs/specs/README.md` root, a compact branch/index structure, preserved
contract meaning, and batches limited to 3 documents or 12,000 source words.
Plan the two oversized contracts as independently selectable responsibilities,
not arbitrary line chunks. Include verification and the safe commit/push path.
Wait for explicit approval.

## After approval

Create only Markdown state under `docs/specs/migration/`: `README.md`, one
active batch node, and one receipt. Do not create JSON routing, inventory,
mapping, or authority files.

Process only the approved batch. Read its sources and direct dependencies,
preserve privacy/account/removal/distribution boundaries and provenance, and
record each source disposition. Every node must be at most 100 physical lines,
preferably 50–80. Validate links, reachability, coverage, drift, and absence of
JSON routing state. Do not start a second batch in the same checkpoint.

Finish only when the target checkpoint can follow scoped commit and push
discipline without publishing foreign commits. Report compact counts, node
links, preserved behavior, residuals, and the next batch.
