from __future__ import annotations

import re
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.check_spec_markdown import validate


ROOT = Path(__file__).resolve().parents[2]
PROJECT_SPEC_SECTION = re.compile(
    r"## Project: product specifications\s+~~~markdown\n(.*?)\n~~~",
    re.DOTALL,
)


def node(kind: str, body: str) -> str:
    return (
        f"# Installed fixture\n\n"
        f"- Node type: {kind}\n"
        "- Status: Active\n"
        "- Read when: selected for the fixture product task.\n"
        "- Do not read when: another product branch governs the task.\n"
        "- Maximum size: 100 physical lines.\n\n"
        f"{body}\n"
    )


class InstalledLayoutFixtureTests(unittest.TestCase):
    def test_project_install_is_markdown_only_and_preserves_agents_text(self) -> None:
        source = (ROOT / "docs/agent-governance/agents-sections.md").read_text(
            encoding="utf-8"
        )
        match = PROJECT_SPEC_SECTION.search(source)
        self.assertIsNotNone(match)

        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            agents = target / "AGENTS.md"
            agents.write_text("# Existing project rules\n\nPreserve me.\n", encoding="utf-8")
            agents.write_text(
                agents.read_text(encoding="utf-8") + "\n" + match.group(1) + "\n",
                encoding="utf-8",
            )

            governance = target / "docs/agent/product-truth"
            governance.mkdir(parents=True)
            shutil.copy2(
                ROOT / "docs/agent-governance/product-truth-governance.md",
                target / "docs/agent/product-truth-governance.md",
            )
            for leaf in (ROOT / "docs/agent-governance/product-truth").glob("*.md"):
                shutil.copy2(leaf, governance / leaf.name)

            features = target / "docs/specs/features"
            features.mkdir(parents=True)
            (target / "docs/specs/README.md").write_text(
                node("root", "[Features](features/README.md)"), encoding="utf-8"
            )
            (features / "README.md").write_text(
                node("branch", "[Sample](sample.md)"), encoding="utf-8"
            )
            (features / "sample.md").write_text(
                node("leaf", "The sample behavior remains explicit."), encoding="utf-8"
            )

            result = validate(
                [
                    target / "docs/specs/README.md",
                    target / "docs/agent/product-truth-governance.md",
                ],
                [target / "docs/specs", target / "docs/agent"],
            )

            self.assertIn("Preserve me.", agents.read_text(encoding="utf-8"))
            self.assertIn("docs/specs/README.md", agents.read_text(encoding="utf-8"))
            self.assertEqual(result["nodes"], 10)
            self.assertEqual(list((target / "docs").rglob("*.json")), [])


if __name__ == "__main__":
    unittest.main()
