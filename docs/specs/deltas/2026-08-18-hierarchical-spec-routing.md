# Contract Delta: Hierarchical Specification Routing

- Change ID: `bootstrap.delta.2026-08-18.hierarchical-spec-routing`
- Change mode: Evolve
- Authorized by: explicit user approval on 2026-08-18
- Domain and clause IDs: `bootstrap.governance` (`BOOTSTRAP.ROUTING`,
  `BOOTSTRAP.RESTART`); `bootstrap.codex-lifecycle`
  (`CODEX.LIFECYCLE.COMPACTION`, `CODEX.LIFECYCLE.WORKER`)
- Previous behavior: agents started at a flat index and were repeatedly
  required to read complete large governance documents and linked sets, even
  though the doctrine also requested the smallest governing slice by stable ID.
- New behavior: non-normative route manifests form a traversal tree; nodes may
  be leaves, branches, or hybrids; selected nodes expand through explicit
  dependency edges into the smallest complete contract closure. Agents record
  a Route Receipt, contracts have clause IDs and context budgets, and restart
  or compaction restores the pinned closure instead of unrelated siblings.
- Evidence basis: current Bootstrap contracts, prompts, lifecycle fixtures,
  measured governance word counts, user-approved architecture, and official
  [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model)
  favoring lean, non-repeated prompts with representative evals.
- Compatibility classification: governance evolution. Existing product-truth
  authority, evidence reconciliation, scope protection, layer independence,
  and hook trust behavior remain protected. Existing installations require the
  repair prompt to migrate; they are not modified automatically.
- Adjacent domains checked: agent-work orchestration, optional browser QA,
  target-product behavior, models/providers, and global configuration.
- QA and design impact: add route graph validation, resolver fixtures, context
  budget checks, lifecycle revision-drift wording, and Route Receipt output. No
  target-product visual behavior changes.
- Specification paths changed: `docs/specs/route.json`,
  `docs/specs/features/route.json`, both Active feature contracts, routed
  product-truth governance, templates, prompts, and lifecycle adapter.
- Independent review: focused contract/diff self-review plus structural,
  resolver, and lifecycle tests; no high-risk product boundary changes.
- New contract revision or epoch: `bootstrap.governance@6`;
  `bootstrap.codex-lifecycle@2`

## Discrepancy disposition

- Classification: authorized evolution plus resolution of an internal
  implementation omission in the existing smallest-slice doctrine.
- Resolution: preserve complete applicable authority while changing the unit
  of completeness from whole documentation sets to an explicit routed closure.
- Exact residual: target projects already using an older Bootstrap are not
  migrated until their operator runs the updated repair or setup workflow.
