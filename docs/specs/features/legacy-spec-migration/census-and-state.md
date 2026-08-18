# Census and Markdown Migration State

- Node type: leaf
- Status: Active
- Contract: `bootstrap.legacy-spec-migration.census@1`
- Clause: `BOOTSTRAP.MIGRATION.INVENTORY`
- Read when: starting or measuring a legacy-library migration.
- Do not read when: working inside an already selected current batch.
- Maximum size: 100 physical lines.

Begin with a bounded mechanical census of paths, sizes, line counts, headings,
links, and hashes without printing document bodies.

Durable state remains Markdown:

- `migration/README.md` links the current and completed batch nodes;
- each batch node lists a bounded set of ordinary Markdown source links;
- each receipt records hashes, dispositions, node links, checks, and next work.

Do not create a required JSON inventory, machine authority registry, or hidden
routing format. Optional tools may rescan the filesystem and compare it against
Markdown links, but their state is disposable technical evidence.

A census may suggest candidate batches from size and links. It cannot classify
authority or meaning from filenames, headings, dates, or current code.

The migration root must stay small. Put large coverage lists into multiple
linked batch nodes, each within the 100-line node limit.
