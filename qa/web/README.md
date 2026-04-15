# Optional Web QA Starter Pack

This directory is an optional QA addon for browser-based products.

Use it when your project has a web UI and you want a simple structure for:

- smoke cases
- regression cases
- experimental cases
- browser run reports
- bug reports

Do **not** treat this as mandatory for every project.

If your product is a backend service, CLI tool, pipeline, desktop app, or any
other non-browser system, use a verification layer that fits that product
instead.

## What this pack includes

- `AGENTS.snippet.md` — small block to paste into a project's `AGENTS.md`
  so the agent loads browser QA instructions automatically
- `AGENTS.run.md` — runner instructions for browser QA runs
- `AGENTS.cases.md` — author instructions for QA case creation
- `create-cases-prompt.md` — reusable prompt for generating browser cases
- `templates/report.template.md` — run report template
- `templates/bug.template.md` — bug report template
- `templates/case.template.md` — QA case template

## Suggested structure in a real project

```text
qa/
  README.md
  cases/
    smoke/
    regression/
    experimental/
  runs/
  templates/
```

## Principle

Keep these layers separate:

- specs define the product contract
- QA cases verify representative behavior
- run reports capture execution evidence
