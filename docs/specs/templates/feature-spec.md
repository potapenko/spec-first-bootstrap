# <Feature or responsibility>

- Node type: leaf | hybrid
- Contract ID: <stable-id>
- Domain ID: <stable-domain>
- Status: Draft | Active | Superseded | Historical
- Stability: Evolving | Accepted | Released | Deprecated
- Contract revision: <revision-or-epoch>
- Read when: <task-selection condition>
- Do not read when: <sibling or excluded condition>
- Maximum size: 100 physical lines.

## Goal and scope

Describe the product outcome and the bounded responsibility of this node.

## Non-goals

- <explicit exclusion>
- <protected adjacent behavior>

## User-visible behavior

- <stable clause ID>: <required behavior>
- <stable clause ID>: <required behavior>

## Invariants and failure policy

- <invariant>
- <edge case or recovery behavior>

## Route, state, and data implications

- <product-significant implication>

## Children

For a hybrid only:

- [<Child responsibility>](<relative-path.md>) — <when to read it>.

## Dependencies

- [<Required contract>](<relative-path.md>) — <exact required meaning>.

## Verification mapping

- <scenario or QA evidence>

## Unknowns

- <real unresolved product decision>

Split by responsibility before this node exceeds 100 physical lines. Product
rules belong in selected contract nodes, never in branch summaries.
