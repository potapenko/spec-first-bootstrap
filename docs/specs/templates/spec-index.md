# Specification Authority Index

- Node type: root | branch
- Status: Active
- Read when: authority, stability, precedence, or release baselines matter.
- Do not read when: the selected contract path already supplies complete authority.
- Maximum size: 100 physical lines.

The specification tree starts at [README.md](README.md). This file is a compact
human authority view.

## Contracts

| Contract | Domain | Authority | Stability | Revision | Read when | Precedence |
| --- | --- | --- | --- | --- | --- | --- |
| [<Contract>](<path.md>) | <domain> | Active | Evolving | <revision> | <condition> | <rule> |

## Shared dependencies

- [<Dependency>](<path.md>) — <why it is required>.

## Accepted deltas

- [<Contract Delta>](<path.md>)

## Unknown precedence

- <conflict or None>

If the table approaches 100 lines, split it into linked domain indexes. The
Markdown root and branch links remain the traversal authority.
