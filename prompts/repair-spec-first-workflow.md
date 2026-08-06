# Repair An Existing Spec-First Workflow

Use https://github.com/potapenko/spec-first-bootstrap as the canonical source.

Repair this project's product-truth and specification-first workflow. This is a
workflow and documentation migration only. Do not change product
implementation.

Use PROJECT_ONLY deployment unless the user explicitly requested a GLOBAL
installation. For global installation, use
prompts/install-global-product-truth-governance.md instead of copying project
rules into the Codex home.

Do not launch subagents merely to install or repair governance.

## Read first

Read completely:

1. every applicable global and project-local AGENTS.md, AGENTS.override.md, or
   equivalent instruction file;
2. project onboarding, planning, development, Git, safety, build, test, QA, and
   release docs;
3. docs/specs/README.md, the spec index, and the smallest active and historical
   contract set needed to audit authority, stability, and precedence;
4. existing day-to-day, greenfield, brownfield, implementation, and repair
   prompts;
5. from the bootstrap repository:
   - docs/spec-first-workflow.md;
   - docs/agent-governance/README.md;
   - docs/agent-governance/agents-sections.md;
   - docs/agent-governance/product-truth-governance.md;
   - docs/specs/templates/.

If canonical sources cannot be fetched or found, stop and request access. Do
not reconstruct a shorter doctrine from memory.

## Change Envelope

Create a workflow-migration Contract Change Envelope:

- Mode: Evolve.
- Authorized domain: project agent workflow, specification routing, governance
  docs, and neutral templates.
- Protected domains: all product behavior, implementation, data, release
  behavior, and unrelated project instructions.
- Implementation authorized: no.

Preserve all project-specific safety, permissions, build, test, release, Git,
operator, framework, and language rules.

Never replace the complete instruction system with the bootstrap template.

## Required repair

Make the smallest coherent changes needed so that:

1. a compact Product Truth gate appears near the top of the project agent entry
   point;
2. the full canonical document is installed at
   docs/agent/product-truth-governance.md;
3. full governance remains conditionally loaded rather than copied into
   AGENTS.md;
4. product tasks are classified as Restore, Reconcile, Evolve, Discover, or
   Behavior-neutral;
5. a Contract Change Envelope names authorized and protected domains, required
   evidence, allowed spec delta, release baseline, and contract revision;
6. the agent reads the registry and governing specs first and states a
   provisional Spec Basis;
7. the provisional basis is followed by the smallest complete applicable
   source, design, QA, runtime, history, upstream, and release evidence pass;
8. every material mismatch is classified as implementation defect,
   specification defect or omission, stale evidence, authorized evolution, real
   product fork, or external authority blocker;
9. the final reconciled Spec Basis is pinned before implementation;
10. semantic spec edits require external authority and happen before
    implementation;
11. a specification edit cannot authorize itself;
12. the user's request opens only the domain and behavior it names;
13. adjacent Accepted and Released domains remain protected;
14. authority (Draft/Active/Superseded/Historical) is separate from stability
    (Evolving/Accepted/Released/Deprecated);
15. mature projects use stable domain and clause IDs;
16. public releases use explicit release contract baselines;
17. semantic contract changes advance the affected contract epoch;
18. stale worker packets are revalidated or retired;
19. behavioral diagnosis uses the active contract for expected behavior and
    evidence for actual behavior before classifying the discrepancy;
20. planning-only and investigation-only requests remain hard implementation
    boundaries;
21. brownfield discovery records missing authority before source inspection,
    separates observed from intended behavior, and changes no product code;
22. QA maps pinned clauses to action-state-result chains and does not rewrite
    expectations solely to obtain a green result;
23. day-to-day, greenfield, brownfield, and implementation prompts repeat the
    same routing without creating weaker doctrine.

Remove or repair wording that permits:

- code-first product decisions;
- spec updates after implementation choices;
- before-or-alongside specification changes;
- implementation evidence to self-authorize a contract edit;
- spec-only escalation before source and QA reconciliation;
- an Active label to imply Released;
- current tests to define product intent;
- project-specific rules to be promoted globally.

Do not invent or rewrite product decisions merely to make documentation
consistent.

If active contracts still conflict after the evidence pass and precedence is
not established, record the exact conflict. Ask the user only when a material
product fork genuinely remains.

## Minimum neutral templates

When absent and appropriate, add or reconcile:

- docs/specs/index.md;
- docs/specs/templates/feature-spec.md;
- docs/specs/templates/contract-change-envelope.md;
- docs/specs/templates/contract-delta.md;
- docs/specs/templates/release-contract-baseline.md.

Do not populate these templates with invented product behavior.

## Verification

Verify the migration by:

- searching for contradictory spec-only, code-first,
  before-or-alongside, or self-authorizing instructions;
- checking every changed Markdown file for balanced fences, duplicate gates,
  internal consistency, valid local links, and trailing whitespace;
- proving the existing AGENTS.md content and safety rules remain present;
- proving no Codex-home file changed during PROJECT_ONLY repair;
- proving no product implementation file changed;
- running the repository's lightweight docs checks and git diff --check;
- following the target repository's checkpoint and branch rules.

In the final response, report:

1. deployment scope;
2. files changed;
3. where the compact gate and full governance document live;
4. how authority, stability, precedence, release baselines, and epochs are
   represented;
5. unresolved product-contract conflicts;
6. verification performed;
7. checkpoint commit when required.
