from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MINIMUM_WORK_SECTION = re.compile(
    r"## (Project|Global): minimum-sufficient work\s+"
    r"~~~markdown\n(.*?)\n~~~",
    re.DOTALL,
)


class MinimumSufficientWorkTests(unittest.TestCase):
    def test_project_and_global_install_the_same_policy(self) -> None:
        source = (ROOT / "docs/agent-governance/agents-sections.md").read_text(
            encoding="utf-8"
        )
        matches = MINIMUM_WORK_SECTION.findall(source)
        self.assertEqual({scope for scope, _ in matches}, {"Project", "Global"})
        self.assertEqual(len(matches), 2)
        self.assertEqual(matches[0][1], matches[1][1])

        payload = matches[0][1]
        installed = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertEqual(installed.count(payload), 1)
        self.assertIn("expected total token use", payload)
        self.assertIn("Presentation-only edits do not run", payload)
        self.assertIn("A full suite requires concrete", payload)
        self.assertIn("Re-run a check only", payload)

    def test_root_uses_evidence_driven_economy(self) -> None:
        root = (ROOT / "docs/agent-governance/root-orchestration.md").read_text(
            encoding="utf-8"
        )
        for required in (
            "Outcome and minimum-sufficient work",
            "expected total token use",
            "economy_basis",
            "Verification is change-driven",
            "expected time or context-isolation benefit outweighs",
            "Repeat review or repair only when relevant implementation changed",
        ):
            self.assertIn(required, root)

        for superseded in (
            "strongest available reasoning model",
            "strongest supported reasoning model",
            "Before a third support-only checkpoint",
            "Before dispatching a second repair cycle",
            "budget_variance:",
        ):
            self.assertNotIn(superseded, root)

    def test_active_instructions_have_no_numerical_economy(self) -> None:
        active_paths = (
            "AGENTS.md",
            "docs/agent-governance/agents-sections.md",
            "docs/agent-governance/root-orchestration.md",
            "prompts/setup-project-agents.md",
            "prompts/setup-global-agents.md",
        )
        for relative in active_paths:
            text = (ROOT / relative).read_text(encoding="utf-8")
            with self.subTest(path=relative):
                self.assertNotIn("60/25/15", text)
                self.assertNotIn("budget_variance:", text)

    def test_contract_revisions_and_cases_are_current(self) -> None:
        expected = {
            "docs/specs/features/bootstrap-governance.md":
                "bootstrap.governance@15",
            "docs/specs/features/bootstrap-governance/installation.md":
                "bootstrap.governance.installation@2",
            "docs/specs/features/bootstrap-governance/restart-and-delivery.md":
                "bootstrap.governance.restart-delivery@3",
            "docs/specs/features/bootstrap-governance/review-and-acceptance.md":
                "bootstrap.governance.review@3",
            "qa/cases/minimum-sufficient-work.md":
                "MW-13: persistent goal",
        }
        for relative, marker in expected.items():
            with self.subTest(path=relative):
                text = (ROOT / relative).read_text(encoding="utf-8")
                self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
