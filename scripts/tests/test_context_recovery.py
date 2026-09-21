from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


class ContextRecoveryTests(unittest.TestCase):
    def test_no_installable_legacy_payload_survives(self):
        adapter = ROOT / "integrations/codex-lifecycle"
        self.assertEqual([p.name for p in adapter.iterdir() if p.is_file()], ["README.md"])
        for scope in ("project", "global"):
            text = (ROOT / f"prompts/setup-{scope}-codex-lifecycle.md").read_text()
            self.assertIn("informational and changes no files", text)
            self.assertIn("does not authorize removing existing hooks", text)
            self.assertIn("migrate-codex-lifecycle.md", text)
            self.assertNotIn("## Install", text)

    def test_no_active_blanket_restart_gate(self):
        paths = [ROOT / "AGENTS.md", ROOT / "docs/spec-first-workflow.md"]
        paths += list((ROOT / "docs/agent-governance").rglob("*.md"))
        paths += list((ROOT / "prompts").glob("*.md"))
        forbidden = ("first re-reads:", "re-read every applicable instruction",
                     "State the route and contracts re-read", "MANDATORY CODEX LIFECYCLE")
        for path in paths:
            text = " ".join(path.read_text().split())
            for marker in forbidden:
                with self.subTest(path=path, marker=marker):
                    self.assertNotIn(marker, text)

    def test_migration_keeps_scope_and_ownership_guards(self):
        text = " ".join((ROOT / "prompts/migrate-codex-lifecycle.md").read_text().split())
        for marker in ("An old installation request is not removal authority",
                       "A `SessionStart`/`SubagentStart` event",
                       "matching content", "Customized scripts, compound commands",
                       "Never replace the entire hooks object/file",
                       "Never disable the general hooks feature",
                       "retain the script", "already-retired target is a no-op"):
            with self.subTest(marker=marker):
                self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
