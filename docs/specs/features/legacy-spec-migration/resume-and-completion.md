# Migration Resume and Completion

- Node type: leaf
- Contract: `bootstrap.legacy-spec-migration.resume@1`
- Clauses: `BOOTSTRAP.MIGRATION.RESUME`, `BOOTSTRAP.MIGRATION.COMPLETE`
- Read when: resuming, reviewing, or completing a legacy migration.
- Do not read when: initially selecting a new current batch.
- Maximum size: 100 physical lines.

On resume, read applicable instructions, `migration/README.md`, the linked
current batch, its latest receipt, and only the authority needed for the next
action. Do not reload completed batches or the complete corpus.

Before mutation, rescan current-batch hashes and verify parent/child Markdown
links. Record drift explicitly instead of refreshing evidence silently.

A batch receipt records source links and hashes, dispositions, created or
updated nodes, protected meaning, validation, unresolved conflicts, and the
next batch link.

Migration completes only when:

- every legacy source is represented by one terminal non-deferred disposition;
- every Active contract is reachable from the Markdown root;
- every node and migration batch stays within 100 physical lines;
- child and dependency links resolve;
- duplicate and superseded sources name canonical Markdown targets;
- no source drift or semantic conflict is hidden;
- product implementation did not change.

Report compact counts and links rather than embedding corpus bodies.
