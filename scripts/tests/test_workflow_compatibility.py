from __future__ import annotations

import re
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.check_spec_markdown import validate


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/agent-governance"
SECTION = re.compile(r"## (Project|Global): ([^\n]+)\n\n~~~markdown\n(.*?)\n~~~", re.S)
WORK_SECTIONS = {
    "current branch only", "task framing and scope control",
    "minimum-sufficient work", "persistent-goal agents",
}


class WorkflowInstallTests(unittest.TestCase):
    def test_both_install_layouts_resolve_shared_rules_and_preserve_overrides(self) -> None:
        sections = SECTION.findall((SOURCE / "agents-sections.md").read_text())
        for scope in ("Global", "Project"):
            with self.subTest(scope=scope), tempfile.TemporaryDirectory() as raw:
                target = Path(raw)
                owner = target if scope == "Global" else target / "docs/agent"
                owner.mkdir(parents=True, exist_ok=True)
                for name in ("work-governance.md", "root-orchestration.md"):
                    shutil.copy2(SOURCE / name, owner / name)
                shutil.copytree(SOURCE / "work", owner / "work")
                override = "## Local override\nOwner: operator; scope: this project.\nCheckpoint: commit and push.\n"
                installed = override + "\n" + "\n\n".join(
                    text for selected, name, text in sections
                    if selected == scope and name in WORK_SECTIONS
                )
                (target / "AGENTS.md").write_text(installed)
                self.assertTrue(installed.startswith(override))
                self.assertEqual(installed.count("## Task framing and scope control"), 1)
                refs = re.findall(r"`([^`]*work-governance\.md)`", installed)
                self.assertEqual(len(refs), 4)
                self.assertTrue(all((target / ref).is_file() for ref in refs))
                result = validate([owner / "work-governance.md"], [owner / "work-governance.md", owner / "work"])
                self.assertEqual(result["nodes"], 5)
                self.assertIn("automatic push is project opt-in", installed)

    def test_shared_owners_cover_approval_modes_and_host_precedence(self) -> None:
        framing = (SOURCE / "work/task-framing.md").read_text()
        scope = (SOURCE / "work/scope-and-checkpoints.md").read_text()
        goal = (SOURCE / "work/goal-execution.md").read_text()
        economy = (SOURCE / "work/minimum-sufficient-work.md").read_text()
        for text, required in (
            (framing, ("Approval persists", "User instructions and existing authorization", "Silence is not consent")),
            (scope, ("An omitted mode defaults to `bounded`", "project opt-in", "no unrelated local commits")),
            (goal, ("`single-agent`", "`coordinated`", "no meaningful independent work remains", "Never evade", "Preserve the mode")),
            (economy, ("Independent acceptance in either execution mode", "shared released owners", "unavailable independent evidence")),
        ):
            for clause in required:
                self.assertIn(clause, " ".join(text.split()))
        self.assertNotIn("three consecutive", goal)  # Host-specific thresholds are not portable defaults.


if __name__ == "__main__":
    unittest.main()
