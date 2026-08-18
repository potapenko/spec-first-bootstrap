from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.check_spec_markdown import CheckError, validate


def node(kind: str, body: str = "") -> str:
    return (
        f"# Node\n\n- Node type: {kind}\n"
        "- Status: Active\n"
        "- Read when: selected by the parent node.\n"
        "- Do not read when: another sibling governs the task.\n"
        "- Maximum size: 100 physical lines.\n\n"
        f"{body}\n"
    )


class MarkdownTreeTests(unittest.TestCase):
    def test_valid_root_branch_leaf_tree(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "README.md").write_text(
                node("root", "[Branch](branch.md)"), encoding="utf-8"
            )
            (root / "branch.md").write_text(
                node("branch", "[Leaf](leaf.md)"), encoding="utf-8"
            )
            (root / "leaf.md").write_text(node("leaf", "Rule."), encoding="utf-8")
            result = validate([root / "README.md"], [root])
            self.assertEqual(result["nodes"], 3)

    def test_rejects_oversized_node(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            text = node("root") + "\n".join("line" for _ in range(100))
            (root / "README.md").write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(CheckError, r"exceeds (declared )?maximum"):
                validate([root / "README.md"], [root])

    def test_rejects_broken_link(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "README.md").write_text(
                node("root", "[Missing](missing.md)"), encoding="utf-8"
            )
            with self.assertRaisesRegex(CheckError, "broken link"):
                validate([root / "README.md"], [root])

    def test_rejects_orphan_node(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "README.md").write_text(node("root"), encoding="utf-8")
            (root / "orphan.md").write_text(node("leaf"), encoding="utf-8")
            with self.assertRaisesRegex(CheckError, "unreachable"):
                validate([root / "README.md"], [root])

    def test_rejects_json_in_tree(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "README.md").write_text(node("root"), encoding="utf-8")
            (root / "route.json").write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(CheckError, "JSON is forbidden"):
                validate([root / "README.md"], [root])

    def test_rejects_missing_required_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "README.md").write_text(
                "# Root\n\n- Node type: root\n", encoding="utf-8"
            )
            with self.assertRaisesRegex(CheckError, "missing required node metadata"):
                validate([root / "README.md"], [root])

    def test_validates_heading_fragments(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "README.md").write_text(
                node("root", "[Details](leaf.md#required-behavior)"),
                encoding="utf-8",
            )
            (root / "leaf.md").write_text(
                node("leaf", "## Required behavior\n\nRule."), encoding="utf-8"
            )
            result = validate([root / "README.md"], [root])
            self.assertEqual(result["nodes"], 2)

    def test_rejects_broken_heading_fragment(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "README.md").write_text(
                node("root", "[Missing](leaf.md#missing-heading)"),
                encoding="utf-8",
            )
            (root / "leaf.md").write_text(node("leaf", "Rule."), encoding="utf-8")
            with self.assertRaisesRegex(CheckError, "broken heading anchor"):
                validate([root / "README.md"], [root])

    def test_rejects_dependency_cycle(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "README.md").write_text(
                node("root", "[A](a.md)\n\n[B](b.md)"), encoding="utf-8"
            )
            (root / "a.md").write_text(
                node("leaf", "## Dependencies\n\n- [B](b.md)"), encoding="utf-8"
            )
            (root / "b.md").write_text(
                node("leaf", "## Dependency\n\n- [A](a.md)"), encoding="utf-8"
            )
            with self.assertRaisesRegex(CheckError, "dependency cycle"):
                validate([root / "README.md"], [root])

    def test_allows_navigation_cycle_outside_dependency_sections(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "README.md").write_text(
                node("root", "[Index](index.md)"), encoding="utf-8"
            )
            (root / "index.md").write_text(
                node("branch", "[Root](README.md)"), encoding="utf-8"
            )
            result = validate([root / "README.md"], [root])
            self.assertEqual(result["nodes"], 2)


if __name__ == "__main__":
    unittest.main()
