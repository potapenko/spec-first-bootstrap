# Set Up Agent Work Governance Globally

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Install only the agent-work layer: current-branch protection, plan-first work,
approval continuity, bounded scope, minimum-sufficient work, and goal execution.
Change only the explicitly selected user-level configuration. Change no
project repository. Detect the active configuration and state its exact paths.
Do not create, resume, pause, block, or complete a persistent goal during setup.
Do not change product code or install specification or browser-QA layers.

## Read first

Read the following canonical sources completely:

- `docs/agent-governance/README.md`;
- the Global current-branch, task-framing, minimum-sufficient-work, and
  persistent-goal sections in `docs/agent-governance/agents-sections.md`;
- `docs/agent-governance/work-governance.md` and every node under its `work/`
  directory (installation carries the whole work layer);
- `docs/agent-governance/root-orchestration.md`.

Resolve the target's active instruction hierarchy, overrides, fallback names,
size limit, local checkpoint policy, existing changes, and goal state. Read
existing target files before editing. Preserve unrelated instructions and
already-installed layers. Request permissions only when actually required by
the environment and not already authorized. Never expose secrets or providers.

## Install

1. Install `work-governance.md`, the complete `work/` directory, and
   `root-orchestration.md` beside the active global instruction file, preserving relative links.
2. Merge the four compact sections into the active instruction chain. Adjust
   their paths for the target. Existing equivalent rules become routing gates,
   not another full copy. Do not replace the complete target instruction file.
3. Record deliberate local overrides with their owner, scope, and precedence.
   The global default is a local checkpoint commit; automatic push is project
   opt-in. Preserve explicit commit-and-push projects. For those projects,
   before committing verify a safe writable upstream and that the push publishes
   no unrelated local commits; completion requires both commit and push.
4. Preserve the first implementation-plan approval gate and explicit execute-now
   exception. Approval persists across follow-ups, skills, and compaction.
   A requested plan artifact does not trigger a meta-plan. Omitted authority
   defaults to `bounded`; both `bounded` and `task-wide` protect unrelated
   behavior, including other content inside writable files.
5. Install mode selection: bounded sequential goals use `single-agent`;
   worthwhile independent work or context isolation uses `coordinated`. Honor
   user choice and retain the recorded mode on restart. Only coordinated goals
   activate coordinator-only restrictions; finite workers use pinned packets.
6. Preserve dependency-ready scheduling and `waiting_resource`,
   `waiting_evidence`, and `awaiting_authority`. Recheck temporary contention
   every three minutes without a fixed attempt ceiling, subject to mandatory
   host impasse transitions. Goal-level `blocked` is never completion and is
   used only when the current host contract requires it after genuine impasse.
7. Preserve independent review for the named high-risk classes in either mode.
   Independent observation precedes builder-receipt reconciliation. Missing
   mandatory proof is `not_verified`; a failed criterion is `reject`. Neither
   can be accepted as a residual. Preserve integrated user-scenario acceptance.
8. Keep product-truth and optional QA compatible without installing them.
   Product workers receive their finite traversal receipt and pinned closure
   when that layer applies. Keep root orchestration conditional on coordinated
   goal work. Model, reasoning, permissions, providers, concurrency, plugin
   configuration, and existing lifecycle adapters remain unchanged.

Use `apply_patch` for edits. Skill/plugin conflict repair is a separate explicit
configuration scope, never a hidden part of installing this portable layer.

## Verification

Verify one active gate per responsibility, complete linked sources, valid links,
node-size limits, preserved overrides, and exact changed-path scope. Verify no
shadowed gate, goal change, hidden layer installation, or unrelated config edit.

Trace first-request planning, direct plan delivery, execute-now exception,
approved follow-up without reapproval, both authority modes, same-file scope,
current-branch protection, dirty-path handling, and checkpoint-policy selection.
Trace both goal modes, mode retention on compaction, independent ready work,
resource waits, mandatory host blocking, and required independent acceptance.
Use change-driven verification without numerical budgets or percentage mixes;
full suites require concrete cross-cutting risk or an explicit requirement.

Run the relevant cases in `qa/cases/workflow-compatibility.md` against the
installed closure. Structural checks establish wiring; actual model observations
must be identified separately and never claimed from text assertions alone.

Follow the target checkpoint policy. Report exact paths, preserved overrides,
verification, and residuals. Do not install this full layer both globally and
locally unless that duplication was explicitly requested.
