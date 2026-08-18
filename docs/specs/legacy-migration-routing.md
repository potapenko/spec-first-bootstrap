# Legacy Specification Migration Routing

- Revision: `bootstrap.legacy-spec-migration.routing@1`

Do not begin a large migration by reading every legacy specification. Generate
a mechanical inventory first, then use its compact status to select one bounded
product-domain batch. Inventory metadata may cluster candidates, but only
semantic review can classify a document as a contract, supporting resource,
historical record, superseded source, or duplicate.

Add routes incrementally around documents in their existing locations. Moving,
splitting, merging, or rewriting source documents is a later explicit step, not
the default routing operation. Track every source path until it has one terminal
disposition, and keep deferred documents visible.

Resume from the migration plan, compact coverage status, and current batch
receipt. Do not reload completed batches or the full inventory into the agent
conversation. Validate source hashes and route revisions before continuing.
