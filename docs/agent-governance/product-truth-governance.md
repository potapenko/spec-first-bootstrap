# Product Truth Governance

- Node type: root
- Status: Active
- Read when: work investigates, defines, changes, implements, reviews, or verifies product behavior.
- Do not read when: work is proven mechanical, infrastructure-only, or behavior-neutral.
- Maximum size: 100 physical lines.

This Markdown file is the governance entrypoint. Follow only the links matching
the current task; do not preload every leaf.

## Always begin with

1. [Core authority and truth layers](product-truth/core.md)
2. [Markdown traversal and Spec Basis](product-truth/routing-and-basis.md)

## Then choose only what applies

- [Change control](product-truth/change-control.md) — planning implementation,
  changing a specification, or protecting adjacent domains.
- [Evidence and profiles](product-truth/evidence-and-profiles.md) — inspecting
  source, design, QA, runtime, history, transfers, defects, or brownfield work.
- [Delivery and acceptance](product-truth/delivery-and-acceptance.md) —
  implementation, design, QA, proportionality, or completion.
- [Coordination and lifecycle](product-truth/coordination-and-lifecycle.md) —
  worker packets, epochs, restart, or context compaction.

## Common paths

- Product question: core → routing → evidence.
- Restore/Reconcile/Evolve: core → routing → change → evidence → delivery.
- Discover: core → routing → evidence.
- Product worker: coordination plus the pinned product nodes in its packet.
- Restart: routing → coordination, then the previously selected product path.

## Invariants

The specification tree is canonical intended behavior but is not infallible or
self-authorizing. Current code, tests, runtime, screenshots, history, and chat
memory do not silently create intent.

Completeness means the selected Markdown path plus explicit dependency links,
not every sibling. Branch summaries are navigation only. Semantic changes need
legitimate authority and advance affected revisions.

After compaction, reopen only the recorded path and required next evidence.
Every governance node follows the same 100-physical-line maximum as product
nodes.
