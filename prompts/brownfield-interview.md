Use https://github.com/potapenko/spec-first-bootstrap as the spec-first
reference.

Read `docs/spec-first-workflow.md` from that reference first.

This is an existing project with incomplete or unreliable documentation.

Use Discover mode. First record which product areas lack reliable active specs
and establish a Contract Change Envelope with implementation unauthorized.

Analyze the smallest complete applicable source, design, QA, runtime, history,
and release evidence set. Identify product domains, current owners, observed
behavior, intended behavior already established by authority, and
legacy-released compatibility.

Resolve questions answerable from evidence before preparing a clarification
pass for the user or team.

The clarification should contain only material unresolved items:

- conflicting intended behavior;
- missing business rules;
- meaningful alternative outcomes;
- cross-domain or compatibility consequences;
- missing external authority.

For each item, name the evidence inspected, concrete options, consequences, and
recommended choice.

After that, recommend which specs should be created first and which areas can
wait.

Do not implement anything yet.
Do not ask the user questions that source and QA reconciliation can answer.
