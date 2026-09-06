# Minimum-Sufficient Work

- Node type: leaf
- Status: Active
- Read when: choosing tools, context, models, delegation, checks, or evidence.
- Do not read when: the current packet already pins these rules.
- Maximum size: 100 physical lines.

This applies to every implementation task, including ordinary single-agent work
and finite workers inside an orchestrated goal.

Measure progress first by the concrete capability requested by the user and
reachable from the product or release path. Tests, diagnostics, Debug harnesses,
models, maps, evidence, documentation, registries, and review are supporting
work. Report them separately and never represent them as delivered product
functionality.

Choose the reading, reasoning, tools, agents, and verification that minimize
expected total token use while still delivering a reliable result. Expected
cost includes duplicated context, coordination, tool output, retries, and
rework; the cheapest individual step is not always the cheapest complete path.
Ordinary tasks do not create token ledgers, numerical budgets, percentage mixes,
or routine economy reports.

Start with the most direct path likely to deliver the requested outcome or
resolve the next material uncertainty. Every support action names its immediate
implementation, decision, or acceptance consumer. Expand only when observed
evidence shows the current path is insufficient, a real dependency or shared
owner appears, a governing contract requires more, or a concrete risk needs
broader proof. Stop expanding when the result and mandatory acceptance criteria
have sufficient evidence. Do not production-harden temporary tooling or expand
diagnostics speculatively.

Verification is change-driven. Select the smallest check that can detect a
plausible regression from the actual change. Presentation-only edits do not run
logic test suites when actions, state, persistence, services, and business rules
are unchanged. Local logic receives focused checks; shared or high-risk changes
receive affected-consumer or risk-mapped checks. A full suite requires concrete
cross-cutting evidence or an explicit governing requirement. Re-run a check only
when its inputs, environment, or relevant implementation changed.

Use compact, decision-relevant command output and worker receipts rather than
raw logs or complete reasoning transcripts. Parallelism is justified only when
independent work's time or context-isolation benefit outweighs duplicated
context and coordination. Choose model and reasoning strength to minimize
expected total work, including likely rework, rather than from role names or
maximum capability.

This policy never weakens required evidence for data loss, privacy, security,
irreversible actions, released compatibility, or the claimed user outcome. It
never creates a discretionary stop for required approved-plan work; mandatory
host impasse transitions still apply. A
residual cannot hide a known acceptance failure or missing capability claimed
as delivered.

## Independent acceptance in either execution mode

Small low-risk deterministic changes may use focused self-review. Independent
review is required for user-data ownership or deletion, privacy/security,
permissions, irreversible actions, shared released owners, compatibility,
persistence, complex concurrency, or another explicit governing requirement.
Use a non-author with fresh context: first provide neutral criteria and the
artifact, obtain observations, then provide the builder's receipt for
reconciliation. Verify the integrated scenario on the relevant revision.
`not_verified` is missing proof; `reject` is an observed failed criterion.
Neither permits acceptance. User no-delegation instructions remain binding;
unavailable independent evidence remains an acceptance gap, not self-approval.
