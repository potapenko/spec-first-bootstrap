# Spec Index

Use this file as the authority and stability registry for product contracts.

## Selection and precedence

1. Read the smallest active contract set that governs the task.
2. Draft, Superseded, and Historical contracts are evidence only.
3. A more specific contract wins only when this index or the contracts state
   explicit precedence.
4. Stop the affected implementation slice when Active contracts conflict
   without precedence.

## Contracts

| Contract | Domain | Authority | Stability | Read when | Precedence | Baseline |
| --- | --- | --- | --- | --- | --- | --- |
| <path> | <domain-id> | Draft | Evolving | <task routing> | <overlap rule> | None |

Authority values: Draft, Active, Superseded, Historical.

Stability values: Evolving, Accepted, Released, Deprecated.

## Shared and upstream dependencies

Record cross-domain contracts, upstream product contracts, and the target
contract that resolves each dependency.

## Unknown precedence

List unresolved overlaps here. Unknown precedence is not implementation
authority.
