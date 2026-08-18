# Start SwiftUI Semantic Audit Specification Migration

Target repository:
`/Users/eugenepotapenko/Projects/potapenko-github/swiftui-semantic-audit`

Canonical workflow repository:
`/Users/eugenepotapenko/Projects/potapenko-github/spec-first-bootstrap`

## Objective

Convert the compact active specification package into a selective
Markdown-first tree while preserving its complete accepted meaning and keeping
the task entirely documentation-only.

## Mandatory pre-action boundary

1. Work only in the target repository and current branch. Do not create a
   branch or worktree.
2. Re-read active global instructions. The project currently has no root
   `AGENTS.md`; recheck instead of assuming that remains true.
3. Read `docs/specs/README.md` as the legacy registry. Do not preload every
   linked contract.
4. Read only the Bootstrap migration contract,
   `docs/specs/legacy-migration-routing.md`,
   `prompts/migrate-legacy-spec-library.md`, referenced templates, and helper
   usage.
5. Do not inspect Swift source, fixtures, tests, CI logs, or runtime during
   census and checkpoint-0 planning.
6. Do not change product behavior, implementation, global configuration, or
   unrelated repository files.

## Revalidate the snapshot

The planning snapshot was 9 Markdown documents, 10,024 words, 1,027 lines, and
6 documents over 100 lines. It contained no declared Markdown nodes, JSON spec
state, or migration directory. Repeat the bounded mechanical census without
printing bodies; treat the snapshot only as drift evidence.

## Authority that must survive unchanged

Preserve contract epoch `tz-v5`, local revision `spec-6`, the pinned authority
digest, `ROUTER-001`, `INDEXED-SKILLS-001`, `BOUNDARY-001`,
`ARCHITECTURE-001`, `REALISTIC-FIXTURES-001`, and the unreleased baseline.
Markdown splitting and routing are editorial migration, not authority for a new
semantic epoch or a thirtieth rule.

## Checkpoint 0 — plan and stop

Before writes, present current Git state, exact write set, proposed root and
branch nodes, preserved precedence, and a registry-derived batch map. Keep each
batch to 3 documents or 12,000 source words; one larger document may stand
alone. Identify the first pilot batch and explain why its contract closure is
complete without loading siblings. Include verification and checkpoint
commit/push steps, then wait for explicit approval.

## After approval

Create only Markdown state under `docs/specs/migration/`: `README.md`, one
active batch node, and one receipt. Do not create JSON routing, inventory,
mapping, or authority files.

Process only the approved batch. Read its sources and explicit dependencies,
preserve clause IDs, precedence, digest provenance, and accepted addenda, and
record every source disposition. Nodes must be at most 100 physical lines,
preferably 50–80. Validate links, reachability, coverage, drift, and no JSON
routing state. Do not start another batch in the same checkpoint.

Finish under the repository's scoped commit/push policy. Report only compact
counts, node links, preserved authority, residuals, and the next batch.
