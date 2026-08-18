# Legacy Specification Library Migration

- Node type: hybrid
- Contract ID: `bootstrap.legacy-spec-migration`
- Domain ID: `bootstrap.legacy-spec-migration`
- Authority: Active
- Stability: Accepted
- Contract revision: `bootstrap.legacy-spec-migration@2`
- Clauses: `BOOTSTRAP.MIGRATION.INVENTORY`, `BOOTSTRAP.MIGRATION.BATCH`,
  `BOOTSTRAP.MIGRATION.SAFETY`, `BOOTSTRAP.MIGRATION.RESUME`,
  `BOOTSTRAP.MIGRATION.COMPLETE`
- Read when: migrating a large flat or inconsistently structured spec library.
- Do not read when: creating a small new Markdown-first tree.
- Maximum size: 100 physical lines.

## Goal

Convert legacy documents into bounded Markdown nodes without corpus-wide
reading, lost rules, or silent product changes.

## Choose the governing child

- [Census and Markdown state](legacy-spec-migration/census-and-state.md) —
  mechanical discovery and bounded migration indexes.
- [Semantic batches and safety](legacy-spec-migration/batches-and-safety.md) —
  one-domain reading, dispositions, splitting, and protected meaning.
- [Resume and completion](legacy-spec-migration/resume-and-completion.md) —
  restart context, drift, receipts, and terminal coverage.

## Shared invariants

Corpus-wide mechanical analysis is not corpus-wide semantic reading. A branch
summary or migration table never creates product authority. No legacy document
disappears from coverage.

Migration changes no product implementation. Existing Active, Accepted,
Released, and legacy-released behavior remains protected until reconciled.
Every migrated node must stay within 100 physical lines.

## Dependency

This contract depends on [Markdown-first routing](bootstrap-governance/markdown-routing.md)
and [task scope](bootstrap-governance/task-and-scope.md).
