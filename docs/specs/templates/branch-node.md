# <Branch name>

- Node type: root | branch | hybrid
- Status: Draft | Active | Superseded | Historical
- Read when: <task-selection condition>
- Do not read when: <sibling or excluded condition>
- Maximum size: 100 physical lines.

<One short paragraph describing only this branch's responsibility.>

## Children

- [<Child name>](<relative-path.md>) — <what is inside and when to read it>.
- [<Child name>](<relative-path.md>) — <what is inside and when to read it>.

## Local contract

<For a hybrid only: shared normative rules that genuinely apply to every child.
Omit this section for a pure branch.>

## Dependencies

- [<Required contract>](<relative-path.md>) — <why its meaning is required>.

Do not put child behavior into navigation summaries. Split this node before it
exceeds 100 physical lines; target 50–80 and keep pure branches closer to 50.
