# Contract Delta: Universal Work Guards

- Change ID: `bootstrap.delta.2026-08-14.universal-work-guards`
- Change mode: Evolve
- Authorized by: explicit user request and plan approval on 2026-08-14
- Domain and clause IDs: `bootstrap.governance`
- Previous behavior: Bootstrap required plans for new or materially ambiguous
  work, kept persistent goals coordinator-only without exception, and advised
  installers to inspect worktree state, but it did not distinguish the first
  implementation-bearing request from read-only work, did not bind task work to
  the operator-selected Git branch, and could not honor an explicit request to
  complete a persistent goal without delegation.
- New behavior: the first implementation-bearing request in a new chat receives
  an evidence-based plan after bounded read-only planning, while questions,
  diagnoses, reviews, status checks, and Git-history inspection proceed directly
  and do not silently become implementation. Agents remain on the branch active
  when the task begins unless the user explicitly requests another branch or
  worktree. Persistent goals remain coordinator-only by default, but an explicit
  no-subagent or no-delegation instruction activates a bounded single-agent mode
  for that chat without weakening any other authority or safety boundary.
- Evidence basis: accepted global agent-work instructions and root-orchestration
  behavior in the active user configuration; Bootstrap revision
  `bootstrap.governance@3`; explicit user direction to transfer only universal
  project behavior and exclude Codex-specific Computer Use, skill, and screenshot
  rules.
- Compatibility classification: scoped workflow evolution. Product-truth,
  browser QA, Codex lifecycle hooks, models, reasoning defaults, automations, and
  target-product behavior remain unchanged.
- Adjacent domains checked: specification governance; persistent-goal economic
  controls; project/global installation scope; optional Codex lifecycle adapter;
  model and provider neutrality.
- QA and design impact: structural validation gains branch-boundary,
  implementation-request, read-only, and single-agent-exception checks. No visual
  design or target-product behavior changes.
- Specification paths changed: `docs/specs/index.md`;
  `docs/specs/features/bootstrap-governance.md`; this delta.
- Independent review: focused self-review and repository structural checks are
  proportional for this documentation-only governance change. No named high-risk
  product boundary is modified.
- New contract revision or epoch: `bootstrap.governance@4`

## Policy choices

- The first-request gate is consumed only by an implementation-bearing request,
  not by greetings, questions, explanations, read-only investigations, reviews,
  diagnoses, status checks, or Git-history inspection.
- Planning work is performed before the implementation plan is presented. The
  user is not asked to approve a plan whose result would merely be another plan.
- A later task in the same chat receives a new plan only when it introduces a new
  initiative, feature, or material scope judgment. Plainly bounded low-risk
  follow-ups remain eligible for direct execution.
- Branch creation, switching, renaming, publishing, and worktree creation require
  explicit user direction. Commit or push permission is insufficient.
- An explicit no-delegation instruction suspends coordinator-only activation for
  the current chat; it does not suspend the persistent goal or weaken any other
  governing boundary.
- Codex-specific skill discovery, Computer Use startup, screenshot capture,
  lifecycle configuration, models, and automations are outside this delta.

## Discrepancy disposition

- Classification: authorized evolution
- Resolution: synchronize portable project and global agent-work surfaces with
  the accepted universal workflow rules while keeping environment-specific
  operations outside the portable core.
- Exact residual: the release baseline remains
  `ba891245af7ffa6ffa5463f85af8045b3f6bc75c` until a release is made.
