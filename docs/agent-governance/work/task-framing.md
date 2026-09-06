# Task Framing and Approval Continuity

- Node type: leaf
- Status: Active
- Read when: classifying requests, planning implementation, or resolving approval.
- Do not read when: the current packet already pins these rules.
- Maximum size: 100 physical lines.

## First implementation request

Questions, explanations, read-only investigations, reviews, diagnoses, status
checks, and Git-history inspection proceed directly and do not authorize edits.
A finding does not turn read-only work into implementation.

For the first implementation-bearing request in a chat, complete the bounded
read-only investigation first. Inspect the applicable instructions, contracts,
source, tests, configuration, history, and safe reproductions needed to produce
an evidence-based implementation plan. Do not ask for approval to do planning.

Present the actual outcome, in-scope and out-of-scope work, owners, protected
behavior, execution steps, verification, authority mode, and unresolved material
decisions. Wait for approval before implementation unless the user explicitly
directs execution now or without a plan. A generic imperative is not a waiver.
Do not delegate implementation before approval.

A request whose result is itself a plan is planning-only. Produce or save the
requested plan directly without a meta-plan or asking for approval to create it.
That permission does not authorize the implementation described by the plan.

## Approval persists

After approval, continue inside that boundary. Routine technical choices and
necessary supporting verification do not require repeated approval. A later
new feature, initiative, or material scope choice needs a new plan; a bounded
low-risk follow-up does not. Follow-ups, answers, objections, status questions,
resume, and context compaction do not reset the first-request gate.

Explicit execute-now instructions waive only planning approval, not safety,
protected behavior, external authority, or other applicable environment gates.
Use context to resolve routine gaps. Ask only when the unresolved answer would
materially affect the outcome or new authority is actually required. Continue
independent authorized work while waiting. Silence is not consent.

## Skills and overlapping instructions

User instructions and existing authorization take precedence over skill
guidelines. A generic brief-confirmation workflow does not reopen an approved
plan or a complete user-supplied brief. State routine assumptions and continue
within scope. Do not invent approval gates from hypothetical risk.

If a skill explicitly requires a pause that still applies, identify the exact
file and clause, explain the concrete unresolved decision, and ask only that
question. A skill cannot grant authority to change protected behavior.

Conflicting duplicate skills are a configuration discrepancy. Do not alternate
between incompatible workflows or edit an installed cache as a lasting repair.
When configuration repair is authorized, resolve the source or active plugin
selection and preserve required local additions.
