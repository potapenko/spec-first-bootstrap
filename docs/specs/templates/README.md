# Specification Templates

These templates belong only to the optional specification-first layer. Copy
or adapt the files a project actually needs; installing agent coordination or
browser QA does not require this directory.

- [`feature-spec.md`](feature-spec.md) — product behavior and acceptance
  contract for one feature.
- [`route.json`](route.json) — machine-readable branch/leaf/hybrid routing,
  authority, dependencies, revisions, and context budgets.
- [`route-receipt.md`](route-receipt.md) — selected path and contract-closure
  provenance for one task.
- [`spec-index.md`](spec-index.md) — optional human-readable view of the routed
  authority registry.
- [`contract-change-envelope.md`](contract-change-envelope.md) — bounded
  authority and protected-domain record for a change.
- [`contract-delta.md`](contract-delta.md) — accepted semantic change record.
- [`release-contract-baseline.md`](release-contract-baseline.md) — released
  behavior and compatibility baseline.

The route manifest is the machine-readable selection authority. The receipt
and envelope carry selected nodes, clauses, revisions, excluded siblings,
specified expectation, protected behavior, established flow, and evidence
still needed.

Return to the [`specification documentation`](../README.md) or the main
[`documentation index`](../../README.md).
