# Spec Index

Use this file as an optional human-readable view. The canonical routing and
authority registry is `route.json`; keep this view consistent with it.

## Selection and precedence

1. Start at `route.json`, select the smallest applicable nodes, and resolve
   their explicit contract dependency closure.
2. Draft, Superseded, and Historical contracts are evidence only.
3. A more specific contract wins only when this index or the contracts state
   explicit precedence.
4. Stop the affected implementation slice when Active contracts conflict
   without precedence.

## Contracts

| Contract | Domain | Authority | Stability | Revision | Read when | Precedence | Baseline |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <path> | <domain-id> | Draft | Evolving | <epoch> | <task routing> | <overlap rule> | None |

Authority values: Draft, Active, Superseded, Historical.

Stability values: Evolving, Accepted, Released, Deprecated.

## Shared and upstream dependencies

Record cross-domain contracts, upstream product contracts, and the target
contract that resolves each dependency.

## Resolved closure support

Represent normative dependencies in `route.json` by node and clause ID. Use
this table only for human explanation of plans, runbooks, handoffs, baselines,
design contracts, QA workflows, and release records in the resolved closure.

| Domain | Routed supporting leaves |
| --- | --- |
| <domain-id> | <direct links> |

## Unknown precedence

List unresolved overlaps here. Unknown precedence is not implementation
authority.
