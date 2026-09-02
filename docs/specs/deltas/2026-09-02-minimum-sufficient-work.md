# Contract Delta: Minimum-Sufficient Work

- Change ID: `bootstrap.delta.2026-09-02.minimum-sufficient-work`
- Change mode: Evolve
- Authorized by: explicit user request and plan approval on 2026-09-02
- Domain and clauses: `bootstrap.governance`; `BOOTSTRAP.PROPORTIONALITY`;
  `BOOTSTRAP.ECONOMY`; `BOOTSTRAP.REVIEW.LIMITS`
- Previous behavior: active governance used a 60/25/15 planning mix, counted
  support-only checkpoints and repair cycles, and selected strong reasoning by
  role. Verification was risk-proportional but lacked a portable change-driven
  rule, so agents could run broad tests or supporting work without showing how
  the result served the actual change.
- New behavior: agents choose the minimum-sufficient complete path by expected
  total token cost, expand only from evidence, stop expansion when mandatory
  proof is sufficient, select tests from changed behavior and plausible risk,
  and justify parallelism by net time or context-isolation benefit.
- Superseded policy: the numerical planning mix, checkpoint-depth trigger,
  fixed repair-cycle limit, and mandatory budget-variance accounting from the
  2026-08-10 proportionality delta no longer govern active work. That delta
  remains unchanged as historical evidence.
- Compatibility: workflow evolution without token caps, numerical quotas,
  forced model downgrades, concurrency limits, or reduced safety and acceptance.
- Evidence basis: explicit user correction; the PlayPhrase Mac change-driven
  test rule; active Bootstrap governance; official OpenAI guidance on smallest
  relevant tests, lean prompts, task-fit reasoning, and compact subagent returns.
- Adjacent domains checked: persistent-goal continuity, review independence,
  product truth, installation layers, model/provider settings, lifecycle hooks,
  project-specific test rules, and operator safety.
- Specification paths: `features/bootstrap-governance.md`,
  `features/bootstrap-governance/installation.md`,
  `features/bootstrap-governance/restart-and-delivery.md`,
  `features/bootstrap-governance/review-and-acceptance.md`, `index.md`, this delta.
- QA: minimum-sufficient-work scenarios plus focused installation, goal
  continuity, and structural validation.
- New revisions: `bootstrap.governance@15`;
  `bootstrap.governance.installation@2`;
  `bootstrap.governance.restart-delivery@3`;
  `bootstrap.governance.review@3`.
- Residual: instruction and structural checks cannot measure actual token savings
  or guarantee model adherence; effectiveness must be evaluated from real runs.
