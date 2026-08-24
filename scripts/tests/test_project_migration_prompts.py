from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROMPT_ROOT = ROOT / "prompts/project-migrations"
PROJECTS = {
    "holdtype-swift.md": {
        "target": "/Users/eugenepotapenko/Projects/potapenko-github/holdtype-swift",
        "specific": ("54 Markdown documents", "146,123 words"),
    },
    "swiftui-semantic-audit.md": {
        "target": "/Users/eugenepotapenko/Projects/potapenko-github/swiftui-semantic-audit",
        "specific": ("contract epoch `tz-v5`", "REALISTIC-FIXTURES-001"),
    },
    "codex-switch.md": {
        "target": "/Users/eugenepotapenko/Projects/potapenko-github/codex-switch",
        "specific": ("5 Markdown documents", "5,446 words"),
    },
    "phrases-extractor.md": {
        "target": "/Users/eugenepotapenko/Projects/playphrase.me/phrases-extractor",
        "specific": ("18 Markdown documents", "currently checked-out"),
    },
    "playphraseme-site.md": {
        "target": "/Users/eugenepotapenko/Projects/playphrase.me/playphraseme-site",
        "specific": ("90 Markdown documents", "currently checked-out"),
    },
}
SHARED_GUARDS = (
    "checkpoint 0",
    "wait for explicit approval",
    "3 documents or 12,000 source words",
    "do not create json",
    "at most 100 physical lines",
    "do not start",
    "safe, writable upstream",
    "unrelated local commits",
    "checkpoint commit and push",
    "currently checked-out",
    "do not report the batch complete",
    "both commit and push succeed",
)


class ProjectMigrationPromptTests(unittest.TestCase):
    def test_index_and_root_readme_link_every_prompt(self) -> None:
        index = (PROMPT_ROOT / "README.md").read_text(encoding="utf-8")
        root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("prompts/project-migrations/README.md", root_readme)
        for name in PROJECTS:
            self.assertIn(f"]({name})", index)

    def test_prompts_are_bounded_and_self_contained(self) -> None:
        for name, expected in PROJECTS.items():
            with self.subTest(prompt=name):
                text = (PROMPT_ROOT / name).read_text(encoding="utf-8")
                lowered = text.lower()
                normalized = " ".join(lowered.split())
                self.assertLessEqual(len(text.splitlines()), 100)
                self.assertIn(expected["target"], text)
                self.assertIn("spec-first-bootstrap", text)
                for guard in SHARED_GUARDS:
                    self.assertIn(guard, normalized)
                for value in expected["specific"]:
                    self.assertIn(value.lower(), normalized)

    def test_prompt_directory_contains_only_the_index_and_named_projects(self) -> None:
        actual = {path.name for path in PROMPT_ROOT.glob("*.md")}
        self.assertEqual(actual, {"README.md", *PROJECTS})

    def test_prompts_require_safe_checkpoint_pushes(self) -> None:
        for name in PROJECTS:
            with self.subTest(prompt=name):
                text = (PROMPT_ROOT / name).read_text(encoding="utf-8")
                lowered = text.lower()
                self.assertNotRegex(lowered, r"current\s+`[^`]+`")
                self.assertNotIn("until the commit succeeds", lowered)


if __name__ == "__main__":
    unittest.main()
