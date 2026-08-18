from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.check_spec_markdown import CheckError, validate


def node(kind: str, body: str = "") -> str:
    return (
        f"# Node\n\n- Node type: {kind}\n"
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
            with self.assertRaisesRegex(CheckError, "exceeds maximum"):
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


if __name__ == "__main__":
    unittest.main()
