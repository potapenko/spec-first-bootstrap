# Restart and Delivery Proportionality

- Node type: leaf
- Status: Active
- Contract: `bootstrap.governance.restart-delivery@6`
- Clauses: `BOOTSTRAP.RESTART`, `BOOTSTRAP.PROPORTIONALITY`,
  `BOOTSTRAP.ECONOMY`
- Read when: recovering after lifecycle events or planning implementation support work.
- Do not read when: neither restart nor delivery economics affects the task.
- Maximum size: 100 physical lines.

## Restart

After startup, resume, clear, or compaction, re-read applicable instructions,
the current objective and envelope, the latest Markdown traversal receipt, and
only nodes on the selected path plus the next required evidence.

Restart from the root only when the task changed or the recorded path is
missing or ambiguous. Chat memory, summaries, old tests, and screenshots do not
replace current nodes. Finite workers restart from their pinned packet.
Restore the approved boundary and scoped user authorization without requesting
the same approval again. A recorded coordinated mode without an explicit user
request is not authorization; use the current chat after reconciling ownership.
Load shared work rules once through their linked owner.

## Delivery proportionality

Measure implementation progress first by release-path user capability.
Specifications, evidence, diagnostics, tooling, coordination, and review are
supporting work and must be reported separately.

Start with the most direct path likely to implement the requested outcome or
resolve the next material uncertainty. Every support action names its immediate
implementation, decision, or acceptance consumer. Do not production-harden
temporary tooling or expand diagnostics speculatively.

## Minimum-sufficient work

Choose the reading, reasoning, tools, agents, and verification that minimize
expected total token use while still delivering a reliable result. Expected
cost includes duplicated context, coordination, tool output, retries, and
rework; the cheapest individual step is not always the cheapest complete path.
Ordinary tasks do not create token ledgers, numerical budgets, percentage mixes,
or economy reports.

Expand the initial path only when observed evidence shows it is insufficient,
a real dependency or shared owner appears, a governing contract requires more,
or a concrete risk needs broader proof. Stop expanding when the requested
result and mandatory acceptance criteria have sufficient evidence.

Verification is change-driven. Select the smallest check that can detect a
plausible regression from the actual change. Presentation-only edits do not run
logic test suites when actions, state, persistence, services, and business rules
are unchanged. Local logic receives focused checks; shared or high-risk changes
receive the affected consumer or risk-mapped checks. A full suite requires
concrete cross-cutting evidence or an explicit governing requirement. Re-run a
check only when its inputs, environment, or relevant implementation changed.

Use compact, decision-relevant command output and worker receipts instead of raw
logs or complete reasoning transcripts. Additional agents require an explicit
user request first; only then weigh independent work's time or context-isolation
benefit against duplicated context and coordination. Task complexity, skills,
review requirements, or project instructions cannot grant that authorization.
Concurrent tool calls within the current chat do not create additional agents.

Inherit the user's current model and reasoning settings by default, including
an explicitly selected high-capability model. Worker packets may say `inherit`;
explicit model and effort assignments are optional. Omit override parameters
when the host supports inheritance; `inherit` is a policy label, not a model ID.
Honor explicit user constraints and host/tool restrictions. Override only when
permitted and justified by a concrete task property, such as ambiguity, risk,
latency, or expected total work including retries and rework. Explain only an
override; routine inheritance needs no separate justification.

Recommendations describe task needs, not mandatory model tiers or role mappings.
Complex or high-risk work may benefit from stronger reasoning; mechanical work
may benefit from an efficient tool-capable model. Model capability and reasoning
effort are separate choices. Resolve any override from the host's currently
supported models and effort values; never infer capability from generation names
or invent a model alias. If an override is unavailable, retain a usable inherited
setting or report the exact limitation. Keep concrete model IDs in environment
settings or explicit run overrides, not portable governance. Installation never
changes application defaults.

Minimum-sufficient work never weakens required evidence for data loss, privacy,
security, irreversible actions, released compatibility, or the claimed user
outcome. It never creates a discretionary stop for approved-plan work; mandatory
host impasse transitions still apply.

A residual may preserve bounded uncertainty but cannot hide a known acceptance
failure or missing capability claimed as delivered.
