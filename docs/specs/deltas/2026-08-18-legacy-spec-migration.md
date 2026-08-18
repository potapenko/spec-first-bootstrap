# Contract Delta: Legacy Specification Library Migration

- Change ID: `bootstrap.delta.2026-08-18.legacy-spec-migration`
- Change mode: Evolve
- Authorized by: explicit user approval on 2026-08-18
- Domain and clause IDs: `bootstrap.legacy-spec-migration`
  (`BOOTSTRAP.MIGRATION.INVENTORY`, `BOOTSTRAP.MIGRATION.BATCH`,
  `BOOTSTRAP.MIGRATION.SAFETY`, `BOOTSTRAP.MIGRATION.RESUME`,
  `BOOTSTRAP.MIGRATION.COMPLETE`)
- Previous behavior: setup, repair, and brownfield prompts could introduce
  hierarchical routing, but they provided no bounded, restartable conversion
  workflow for a large existing specification corpus.
- New behavior: a dedicated prompt and mechanical tool inventory legacy
  documents without emitting their bodies, track exclusive dispositions in
  bounded batches, validate coverage and hash drift, and resume from compact
  durable state. Existing documents remain in place by default.
- Evidence basis: the accepted hierarchical-routing contract, existing setup
  and repair prompts, the unresolved target-project migration residual in the
  previous routing delta, the user-approved large-corpus use case, and official
  [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model)
  favoring lean prompts and explicit context tracking.
- Compatibility classification: additive governance evolution. Existing route
  schema, product contracts, setup behavior, and installed projects remain
  valid. Migration is opt-in.
- Adjacent domains checked: target-product behavior, product implementation,
  agent-work governance, browser QA, Codex lifecycle hooks, and global setup.
- QA and design impact: add deterministic inventory/coverage tests, including a
  generated thousand-document corpus. No visual behavior changes.
- Specification paths changed: add the migration contract and update Bootstrap
  route manifests, routing guidance, index, prompt surfaces, templates, tooling,
  and structural validation.
- Independent review: focused contract/diff self-review plus structural,
  resolver, migration-tool, and full Bootstrap tests.
- New contract revision or epoch: `bootstrap.legacy-spec-migration@1`;
  `bootstrap.specs.route@2`; `bootstrap.contracts.route@2`;
  `bootstrap.legacy-spec-migration.routing@1`

## Discrepancy disposition

- Classification: authorized evolution closing the explicit residual from the
  hierarchical-routing checkpoint.
- Resolution: distinguish large legacy-library migration from brownfield
  discovery and workflow repair, and make corpus coverage mechanical.
- Exact residual: the Bootstrap supplies the workflow; each target project
  still requires its own approved migration plan and evidence reconciliation.
