# Decision Provenance and Optional Context Reminder

- Change ID: `2026-09-23-decision-provenance-reminder`
- Mode: Evolve
- Authority: the user approved reviewed Draft v3 and requested implementation
  globally in Codex and in Bootstrap, with the same four reviewers, 2026-09-23.
- Approved proposal: `spec-first-execution-control`, revision `8b49a5036` in
  the originating PlayPhrase.me site repository; that project is read-only here.
- Execution: root implements; the four requested reviewers inspect wording,
  practicality and the adapter. No additional workers or goals are authorized.

## Intended delta

Before the first and each new material choice, distinguish its basis in a read
contract, explicit user authority or an agent proposal. An agent-authored plan
cannot establish a contract requirement. Preserve the accepted plan content and
actual approval source without new per-task registries or repeated approvals.

Keep selective recovery. Add a separately selected, short Codex SessionStart
reminder; do not restore the old mandatory-rereading payload. Ordinary setup
does not install this optional integration. Existing unrelated hooks and local
overrides remain protected. The reminder is not an enforcement barrier.

## Bounded write set

- Bootstrap routing-and-basis, work/scope-and-checkpoints, work/context-recovery,
  work-governance and agent-governance README.
- Affected governance aggregate/installation/task-scope/lifecycle contracts,
  specification root/features routers, index and this delta;
  public README and prompt index/notices.
- integrations/codex-lifecycle README and new context_reminder.py;
  one opt-in setup prompt; explicit preservation note in legacy migration.
- Existing context/workflow cases, context tests, affected revision expectations
  in validate_bootstrap.py and test_minimum_sufficient_work.py.
- Active ~/.codex: AGENTS.md, implementation-governance.md,
  product-truth-governance.md, product-truth/routing-and-basis.md,
  hooks.json and hooks/context_reminder.py. Preserve dirty config.toml.

No product code, database, model/provider/permission defaults, SSH setup,
new state store, universal guard, branch switch or whole-layer reinstall.
Use existing master branches. Bootstrap requires checkpoint/push after safe
upstream verification; the global configuration requires a local checkpoint.

## Verification

Run relevant structural/fixture tests, adapter subprocess tests and peer review
of the actual diff. Preserve CR-01–04 selective recovery and ordinary autonomy.
Add the initial false-plan case and the misleading-summary variant, paired with
an explicitly approved delta. Distinguish observed decisions from text checks.

Check installed routing, source/installed script identity, hook registration,
configuration preservation and actual host delivery where supported. Normal
hook trust is required; do not bypass it or claim delivery from a subprocess.
Record any host-delivery or behavioral-proof gap without inventing a new system.

## Implementation evidence

Bootstrap validation and 14 focused adapter/installation/workflow tests passed.
The technical critic independently ran the six context/adapter tests. All four
reviewers accepted their wording/code/consistency scope after correcting the
distinction between accepted content and approval, and between an agent-written
plan and self-created authority. A prose case walkthrough is not a runtime test.

The installed routing, governance router and script match canonical source.
Existing config.toml content was preserved and excluded from the checkpoint;
one SessionStart registration was added. The direct installed-script wire test
passed. The AGENTS pointer appeared in the current thread's instruction refresh.

Computer Use refused control of the Codex app; the restriction was not bypassed.
The user completed normal hook trust in the app. A management-only hooks/list
request through the same bundled Codex binary confirmed the exact command,
global source, enabled=true, trustStatus=trusted and no discovery errors.
No thread, model run or new task was created for that check. Activation
prerequisites are satisfied. Actual lifecycle delivery and model-behavior effect
remain unobserved; neither discovery nor direct script tests prove them.
