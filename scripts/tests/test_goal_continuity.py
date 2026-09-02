from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PERSISTENT_SECTION = re.compile(
    r"## (Project|Global): persistent-goal agents\s+"
    r"~~~markdown\n(.*?)\n~~~",
    re.DOTALL,
)


class GoalContinuityTests(unittest.TestCase):
    def test_project_and_global_sections_share_continuity_contract(self) -> None:
        source = (ROOT / "docs/agent-governance/agents-sections.md").read_text(
            encoding="utf-8"
        )
        matches = PERSISTENT_SECTION.findall(source)
        self.assertEqual({scope for scope, _ in matches}, {"Project", "Global"})
        self.assertEqual(len(matches), 2)

        for scope, payload in matches:
            with self.subTest(scope=scope):
                normalized = " ".join(payload.split())
                self.assertIn("dependency-ready authorized item", normalized)
                self.assertIn("waiting_resource", normalized)
                self.assertIn("waiting_evidence", normalized)
                self.assertIn("awaiting_authority", normalized)
                self.assertIn("every three minutes", normalized)
                self.assertIn("without a fixed attempt ceiling", normalized)
                self.assertIn("goal-level `blocked`", normalized)
                self.assertNotIn("paused or blocked goal", normalized.lower())

    def test_root_uses_waiting_states_instead_of_blocked_packet_status(self) -> None:
        root = (ROOT / "docs/agent-governance/root-orchestration.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Goal continuity and ready-work scheduling", root)
        self.assertIn("no fixed retry or attempt ceiling", root)
        self.assertIn("status: done | waiting_resource", root)
        self.assertNotIn("status: done | blocked | failed", root)
        self.assertNotIn("                  -> blocked", root)

    def test_setup_prompts_require_installed_continuity(self) -> None:
        for relative in (
            "prompts/setup-project-agents.md",
            "prompts/setup-global-agents.md",
        ):
            with self.subTest(path=relative):
                text = (ROOT / relative).read_text(encoding="utf-8")
                self.assertIn("waiting_resource", text)
                self.assertIn("every three minutes without a fixed", text)
                self.assertIn("goal-level `blocked`", text)


if __name__ == "__main__":
    unittest.main()
