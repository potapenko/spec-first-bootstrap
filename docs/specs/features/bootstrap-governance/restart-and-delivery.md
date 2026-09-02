# Restart and Delivery Proportionality

- Node type: leaf
- Status: Active
- Contract: `bootstrap.governance.restart-delivery@2`
- Clauses: `BOOTSTRAP.RESTART`, `BOOTSTRAP.PROPORTIONALITY`
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

## Delivery proportionality

Measure implementation progress first by release-path user capability.
Specifications, evidence, diagnostics, tooling, coordination, and review are
supporting work and must be reported separately.

Aim for a smallest release-reachable vertical slice in the first one or two
implementation checkpoints. Every support artifact names its next consumer.
Do not production-harden temporary tooling or expand diagnostics speculatively.

A third consecutive support-only checkpoint, second repair/re-review cycle, or
material tooling expansion requires a delivery-and-cost reassessment. For an
active persistent goal executing an approved plan, the reassessment is a
nonblocking routing decision: continue dependency-ready plan work and convert
noncritical uncertainty to an explicit residual when safe. Additional approval
is required only for work outside the approved envelope, an otherwise
unauthorized action, or optional expansion that has no immediate plan consumer.
Stronger safety gates remain for demonstrated data-loss, privacy, security,
irreversible-action, or released-compatibility risk.

A residual may preserve bounded uncertainty but cannot hide a known acceptance
failure or missing capability claimed as delivered.
