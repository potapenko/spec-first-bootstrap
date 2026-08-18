# Legacy Migration Routing

- Node type: leaf
- Status: Active
- Revision: `bootstrap.legacy-migration-routing@2`
- Read when: planning or resuming migration of a large existing spec library.
- Do not read when: authoring a new small Markdown-first tree.
- Maximum size: 100 physical lines.

Do not begin by reading every legacy document. Perform a mechanical census
without emitting bodies, then create a Markdown migration root whose children
are bounded batch nodes.

Each batch node links to at most the current coherent domain set. Read one batch
completely, split its documents into Markdown nodes no larger than 100 lines,
write a compact Markdown receipt, and then select the next batch.

Durable migration state is Markdown:

- `migration/README.md` — status and links to batch nodes;
- `migration/batches/<batch>.md` — bounded source links and disposition;
- `migration/receipts/<batch>.md` — hashes, changes, checks, and next link.

Technical tools may rescan paths, hashes, links, and line counts. They must not
create a required JSON registry or become an authority layer.

Resume from the migration root, current batch, and latest receipt. Do not reload
completed batches or the complete corpus.
