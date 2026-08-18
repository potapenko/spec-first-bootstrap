# Semantic Batches and Safety

- Node type: leaf
- Contract: `bootstrap.legacy-spec-migration.batch@1`
- Clauses: `BOOTSTRAP.MIGRATION.BATCH`, `BOOTSTRAP.MIGRATION.SAFETY`
- Read when: selecting, reading, classifying, or splitting one migration batch.
- Do not read when: only checking completed migration status.
- Maximum size: 100 physical lines.

Process one coherent product-domain batch at a time. Read only its Markdown
batch node, linked sources, applicable authority, explicit dependencies, and
required acceptance evidence.

Every source receives one visible disposition: contract, resource, historical,
superseded, duplicate, or deferred. Filenames and headings are insufficient;
semantic review of the selected batch is required.

Keep source paths by default. Moving, merging, deleting, or rewriting requires
explicit selected-batch scope, preserved provenance, updated inbound links, and
semantic-equivalence review.

Split contracts at independently selectable responsibilities. The parent
becomes a small branch or hybrid with short child descriptions and ordinary
Markdown links. Every resulting node is at most 100 physical lines.

Stop only the affected batch on conflicting Active behavior without precedence,
unresolved product meaning, hash drift, broken provenance, or a required
protected-domain change. Preserve completed independent batches.
