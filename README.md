# Spec-First Bootstrap for AI-Assisted Projects

This repository installs two related but separate capabilities:

1. **Product-truth governance** — specifications remain the canonical product
   contract, while source, design, runtime behavior, QA, and release baselines
   are reconciled as distinct evidence layers.
2. **Persistent-goal agent architecture** — an optional orchestration contract
   for long-running work in which the primary `/root` preserves context and
   coordinates finite workers instead of becoming another implementation
   worker.

Both capabilities can be installed globally for every Codex project or only
inside one repository. Browser QA remains a separate optional layer.

## Choose an installation scope

Do not install the same full governance document in both scopes by default.

| Scope | Use it when | Where the rules live |
| --- | --- | --- |
| `GLOBAL` | You want the same product-truth or persistent-goal discipline in every Codex project. | The active Codex home and its global `AGENTS.md`. |
| `PROJECT_ONLY` | You want one repository to be self-contained or to use different governance. | The target repository and its project-root `AGENTS.md`. |

Global rules provide reusable doctrine. Project-local rules add product,
framework, safety, build, test, database, storage, and release constraints.
Installers merge existing `AGENTS.md` files; they must not replace unrelated
instructions.

## Start here

### Option A: install product-truth governance globally

Open [`prompts/install-global-product-truth-governance.md`](prompts/install-global-product-truth-governance.md),
copy its prompt, and send it to Codex.

This option:

- changes only the active Codex home;
- adds the compact global Product Truth gate to global `AGENTS.md`;
- installs the full governance document as conditionally loaded guidance;
- does not mutate the current project;
- preserves project-local rules.

### Option B: install product-truth governance in one project

Open [`prompts/install-project-product-truth-governance.md`](prompts/install-project-product-truth-governance.md),
replace the target-repository placeholder, and send the prompt to Codex.

This option:

- changes only the named repository;
- installs a complete project-local Product Truth gate and governance document;
- adds or reconciles the spec registry and neutral templates;
- preserves existing product behavior and project instructions;
- does not write to the Codex home.

### Optional: add persistent-goal agent architecture

After product-truth governance is available in the chosen scope, use
[`prompts/install-persistent-goal-agent-architecture.md`](prompts/install-persistent-goal-agent-architecture.md).
Set exactly one deployment scope in the prompt:

```text
Deployment scope: GLOBAL
```

or:

```text
Deployment scope: PROJECT_ONLY
Target repository: /absolute/path/to/repository
```

The installer adds orchestration rules; it does not create, resume, pause,
block, or complete a persistent goal. It also does not change model defaults,
reasoning defaults, concurrency limits, or provider configuration unless that
is separately requested.

### Optional: add browser QA to a web project

Use [`prompts/optional-web-qa.md`](prompts/optional-web-qa.md) after the
project-local spec-first layer exists. Browser QA verifies pinned product
contracts; it does not define product intent or weaken a contract to obtain a
green result.

## The product-truth model

The specification system is the primary product artifact and the canonical
statement of intended behavior. Canonical does not mean infallible, and a spec
edit cannot authorize itself.

Different artifacts answer different questions:

| Layer | Primary question |
| --- | --- |
| User objective or decision | What product change is authorized now? |
| Active product contract | How should the product behave? |
| Design and product model | How is the behavior expressed structurally and visually? |
| Implementation source | How is it currently realized, and who owns it? |
| Runtime behavior | What does the product actually do in the relevant state? |
| QA and acceptance evidence | Which action-state-result chains have been verified? |
| Release baseline | Which behavior may users or consumers already rely on? |

These layers are not a flat vote. The active contract defines intent; the
other layers expose ownership, realization, observed behavior, acceptance,
compatibility, omissions, and stale assumptions.

Spec-first therefore means:

1. classify the task as Restore, Reconcile, Evolve, Discover, or
   Behavior-neutral;
2. establish a bounded Contract Change Envelope;
3. state a provisional Spec Basis;
4. inspect the smallest complete applicable evidence set;
5. classify discrepancies;
6. accept only a legitimately authorized Contract Delta;
7. update the contract first when meaning changes;
8. pin the final reconciled Spec Basis;
9. implement and verify that exact basis.

It does **not** mean reading only Markdown, treating current code as automatic
intent, or changing a spec after the fact to make an implementation look
compliant.

The compact workflow is
[`docs/spec-first-workflow.md`](docs/spec-first-workflow.md). The complete
reusable contract is
[`docs/agent-governance/product-truth-governance.md`](docs/agent-governance/product-truth-governance.md).

## Persistent-goal architecture

A persistent goal is different from an ordinary bounded task because the
primary model's context must survive many implementation, review, build, QA,
pause, and restart cycles.

When a request advances a running persistent goal:

- the primary agent acts as `/root` and remains coordinator-only;
- `/root` preserves the objective, authority, dependency graph, contract
  epochs, accepted receipts, blockers, and next ready work;
- workers receive finite packets with exact authority, scope, owners,
  invariants, checks, and stopping conditions;
- implementation receives independent review before acceptance;
- one restart-safe registry records packet state and exact residuals;
- pause and resume are explicit and durable;
- context quality and correctness outrank maximum fan-out or token savings.

Workers do not all read the full orchestration manual. Automatically loaded
`AGENTS.md` contains only a compact routing gate; the full document is read by
the coordinating `/root` when the persistent-goal boundary actually applies.

Model selection is role-based. Strong reasoning is used for coordination,
authority, architecture, risky implementation, and independent review.
Efficient tool-capable models may handle bounded exploration, known-file work,
builds, tests, or mechanical extraction when the packet leaves no product
judgment unresolved. Quality is never downgraded merely to save tokens.

The complete contract is
[`docs/agent-governance/root-orchestration.md`](docs/agent-governance/root-orchestration.md).
Reusable compact `AGENTS.md` sections are in
[`docs/agent-governance/agents-sections.md`](docs/agent-governance/agents-sections.md).

## Greenfield and brownfield projects

### Greenfield

Use [`prompts/greenfield-bootstrap.md`](prompts/greenfield-bootstrap.md) after
choosing project-local deployment. Create the domain registry and initial
contracts before feature implementation begins.

### Brownfield

Use Discover when reliable contracts do not yet exist:

1. record the missing or unreliable contract;
2. inspect code, routes, state, design, tests, QA, runtime, history, and
   released behavior as evidence;
3. separate observed behavior from intended behavior;
4. map domains, owners, compatibility, unknowns, and conflicts;
5. write first-pass contracts without changing product implementation;
6. use Restore, Reconcile, or Evolve for later implementation slices.

Brownfield prompts:

- [`prompts/brownfield-discovery.md`](prompts/brownfield-discovery.md)
- [`prompts/brownfield-interview.md`](prompts/brownfield-interview.md)
- [`prompts/generate-first-specs.md`](prompts/generate-first-specs.md)

## Prompt pack

Installation and architecture:

- [`install-global-product-truth-governance.md`](prompts/install-global-product-truth-governance.md)
- [`install-project-product-truth-governance.md`](prompts/install-project-product-truth-governance.md)
- [`install-persistent-goal-agent-architecture.md`](prompts/install-persistent-goal-agent-architecture.md)

Project work:

- [`greenfield-bootstrap.md`](prompts/greenfield-bootstrap.md)
- [`brownfield-discovery.md`](prompts/brownfield-discovery.md)
- [`brownfield-interview.md`](prompts/brownfield-interview.md)
- [`generate-first-specs.md`](prompts/generate-first-specs.md)
- [`day-to-day-spec-first.md`](prompts/day-to-day-spec-first.md)
- [`repair-spec-first-workflow.md`](prompts/repair-spec-first-workflow.md)
- [`optional-web-qa.md`](prompts/optional-web-qa.md)

See [`prompts/README.md`](prompts/README.md) for ready-to-copy invocation
examples and scope details.

## Included artifacts

- `AGENTS.md` — a self-contained project-local example and maintenance rules
  for this repository.
- `docs/spec-first-workflow.md` — the compact canonical workflow.
- `docs/agent-governance/` — full global/project governance sources, compact
  `AGENTS.md` sections, and deployment guidance.
- `docs/specs/README.md` — the project specification-layer contract.
- `docs/specs/index.md` — this repository's product-contract authority
  registry.
- `docs/specs/templates/` — templates for a feature contract, spec index,
  Change Envelope, Contract Delta, and release baseline.
- `examples/favorites-spec.md` — a historical example contract, not product
  authority for a target project.
- `prompts/` — ready-to-send installers and working prompts.
- `qa/web/` — an optional browser-QA starter pack.

## Manual installation fallback

Use this only when an agent cannot inspect the repository directly.

For a global install:

1. copy the chosen full governance document from `docs/agent-governance/` to
   the active Codex home;
2. merge the matching global gate from `agents-sections.md` into global
   `AGENTS.md`;
3. preserve every unrelated global instruction;
4. do not copy project-specific safety or tooling rules globally.

For a project-only install:

1. copy `docs/spec-first-workflow.md`, `docs/specs/`, and the useful prompts;
2. copy the required full governance document into a project-local
   documentation path;
3. merge the matching project-local gate into the repository's `AGENTS.md`;
4. preserve existing project rules and product behavior;
5. add project-specific contracts through Discover, not by copying the example
   as authority.

If browser QA is installed, also merge the routing block from
[`qa/web/AGENTS.snippet.md`](qa/web/AGENTS.snippet.md).

## Suggested repository structure

```text
.
├── AGENTS.md
├── README.md
├── docs/
│   ├── agent-governance/
│   │   ├── README.md
│   │   ├── agents-sections.md
│   │   ├── product-truth-governance.md
│   │   └── root-orchestration.md
│   ├── spec-first-workflow.md
│   └── specs/
│       ├── README.md
│       ├── index.md
│       ├── templates/
│       │   ├── contract-change-envelope.md
│       │   ├── contract-delta.md
│       │   ├── feature-spec.md
│       │   ├── release-contract-baseline.md
│       │   └── spec-index.md
│       └── features/
│           └── <project-feature>.md
├── examples/
├── prompts/
└── qa/
```

## License

MIT
