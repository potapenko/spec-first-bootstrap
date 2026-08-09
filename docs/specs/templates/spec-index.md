# Spec Index

Use this file as the authority and stability registry for product contracts.

## Selection and precedence

1. Read the smallest complete active contract set that governs the task and
   every directly linked document required to decide it.
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

## Required reading graph

Route each domain to the complete plans, registries, runbooks, operator
handoffs, accepted reusable baselines, design contracts, QA workflows, and
release records that must be read with its governing contract.

| Domain | Complete governing set |
| --- | --- |
| <domain-id> | <direct links> |

## Unknown precedence

List unresolved overlaps here. Unknown precedence is not implementation
authority.
