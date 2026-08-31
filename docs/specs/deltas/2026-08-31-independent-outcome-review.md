# Contract Delta: Independent Outcome Review

- Change ID: `bootstrap.delta.2026-08-31.independent-outcome-review`
- Change mode: Evolve
- Authorized by: explicit user approval to implement the agreed audit changes
  in Bootstrap and the active global orchestration instructions on 2026-08-31.
- Domain and clauses: `bootstrap.governance`; `BOOTSTRAP.REVIEW.*`.
- Previous behavior: reviewers received the builder's terminal receipt at the
  outset; review used three verdicts and did not explicitly separate an
  independent first observation, missing proof, and composed outcome coverage.
- New behavior: pin mandatory criteria and optional quality references; inspect
  the actual result in fresh reviewer context before reading builder claims;
  reconcile claims afterward; require evidence-backed findings; distinguish
  `not_verified` from `reject`; verify integrated user scenarios.
- Evidence basis: the existing acceptance pipeline and installation prompts,
  the user's approval of the critical comparison with Gauntlet Loop, and the
  active global root contract. The video demonstration was not independently
  verified; it does not establish effectiveness or implementation authority.
- Compatibility: additive workflow evolution with a fourth review verdict.
  Worker execution statuses remain unchanged. Unaffected accepted work stays
  accepted; pending reviews receive the revised criteria and verdict mapping.
- Protected behavior: risk-based review admission, low-risk self-review,
  coordinator-only root activation, finite ownership, scope and safety rules,
  cost and repair limits, pause/resume, independent installation layers.
- Global scope: only `root-orchestration.md` in the active Codex home receives
  the same audit changes. Existing unrelated differences from Bootstrap remain;
  this is not a full global reinstallation or application-settings migration.
- Specification paths: `features/bootstrap-governance.md`,
  `features/bootstrap-governance/review-and-acceptance.md`, `index.md`, this delta.
- Review and QA: focused semantic diff review; existing Bootstrap structural
  checks; [acceptance scenarios](../../../qa/cases/orchestration-review.md);
  equality of changed audit sections across project/global copies and
  preservation of all unrelated global content.
- New revisions: `bootstrap.governance@13`; `bootstrap.governance.review@1`.
- Residual: instruction and structural checks cannot guarantee model adherence
  or quantify defect reduction. Real-run efficacy remains unmeasured.
