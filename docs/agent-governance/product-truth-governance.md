# Product Truth Governance Router

This is the compact compatibility entry point for product-truth governance.
Normative clauses live in the routed contract leaves under
[`product-truth/`](product-truth/); this file is navigation, not a product
contract.

## Activation

Use this router for work that investigates, defines, changes, implements,
reviews, or verifies product behavior, UX, state, routes, public data,
permissions, persistence, compatibility, behavioral defects, QA, release
behavior, transfers, ports, or migrations.

Proven mechanical, infrastructure-only, and behavior-neutral work does not
need the product-truth tree.

## Start here

1. Read [`product-truth/route.json`](product-truth/route.json).
2. Select the applicable task profile or node IDs.
3. Resolve the explicit dependency closure with the installed route resolver.
   In this Bootstrap repository the command is:

   ```sh
   python3 scripts/spec_route.py resolve \
     docs/agent-governance/product-truth/route.json \
     --profile <product-question|restore|reconcile|evolve|discover|product-worker|restart>
   ```

4. Read every contract in the resulting closure completely.
5. Record the Route Receipt and provisional Spec Basis before implementation
   source, runtime evidence, diagnosis, recommendation, or non-reading action.

Installers adapt the resolver path to the active project or user-level
configuration. If the resolver is genuinely unavailable, follow the same
`children` and `requires` fields manually and report that validation residual.
Do not read every sibling leaf as a substitute for routing.

## Universal invariants

- The specification system is canonical intended behavior but is not
  infallible or self-authorizing.
- Current code, tests, runtime, screenshots, history, and chat memory do not
  silently create product intent.
- Completeness means the smallest complete selected contract closure, not all
  documents in the tree.
- Router summaries are non-normative and cannot replace contract clauses.
- Semantic changes require legitimate external authority and advance affected
  revisions or epochs.
- Protected adjacent domains remain outside the change envelope.
- Evidence reconciliation, implementation, and QA use the pinned routed basis.
- After context compaction, restore the latest Route Receipt and selected
  closure, check revision drift, and do not reload unselected siblings.

## Contract leaves

- [`core.md`](product-truth/core.md) — authority, truth layers, domains,
  stability, and release baselines.
- [`routing-and-basis.md`](product-truth/routing-and-basis.md) — traversal,
  closure, Route Receipt, and provisional/final Spec Basis.
- [`change-control.md`](product-truth/change-control.md) — modes, envelope,
  semantic authority, deltas, and protected scope.
- [`evidence-and-profiles.md`](product-truth/evidence-and-profiles.md) —
  reconciliation, discrepancy classes, defects, transfers, and brownfield work.
- [`delivery-and-acceptance.md`](product-truth/delivery-and-acceptance.md) —
  implementation order, design, QA, proportionality, and completion.
- [`coordination-and-lifecycle.md`](product-truth/coordination-and-lifecycle.md)
  — worker packets, epochs, restart, compaction, and receipts.

The route manifest is the machine-readable authority for selection,
dependencies, revisions, and context budgets. Stable clause IDs, not headings
or line numbers, identify the governing slice.
