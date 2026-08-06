# Spec Index

This file is the authority and stability registry for product contracts.

## Selection and precedence

1. Read the smallest contract set that governs the task.
2. Only Active contracts define current intended behavior.
3. Draft, Superseded, and Historical contracts are evidence only.
4. A more specific contract wins only when this index or the contracts state
   explicit precedence.
5. Stop before implementation when Active contracts conflict without
   precedence.

## Contracts

| Contract | Domain | Authority | Stability | Read when | Precedence | Baseline |
| --- | --- | --- | --- | --- | --- | --- |
| <path> | <domain-id> | Draft | Evolving | <task routing> | <overlap rule> | None |

Authority values:

- Draft
- Active
- Superseded
- Historical

Stability values:

- Evolving
- Accepted
- Released
- Deprecated

## Shared and upstream dependencies

Record cross-domain contracts, upstream product contracts, and which target
contract resolves each dependency.

## Release baselines

Link every Accepted or Released domain to its latest baseline or record why no
baseline exists yet.

## Unknown precedence

List unresolved overlaps here. An unknown precedence is not implementation
authority.
