from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


class ContextRecoveryTests(unittest.TestCase):
    def test_no_installable_legacy_payload_survives(self):
        adapter = ROOT / "integrations/codex-lifecycle"
        for name in ("lifecycle_restart.py", "context_compaction_restart.py",
                     "global-hooks.json.template", "project-hooks.json.template"):
            self.assertFalse((adapter / name).exists(), name)
        self.assertTrue((adapter / "context_reminder.py").is_file())
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


class ContextReminderTests(unittest.TestCase):
    script = ROOT / "integrations/codex-lifecycle/context_reminder.py"

    def invoke(self, raw):
        with tempfile.TemporaryDirectory(prefix="spec-first-reminder-") as cwd:
            result = subprocess.run([sys.executable, "-B", str(self.script)],
                                    input=raw, capture_output=True, text=True,
                                    cwd=cwd, timeout=5)
            self.assertEqual([], list(Path(cwd).iterdir()))
        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stderr)
        return result.stdout

    def test_supported_sources_emit_only_the_static_context_schema(self):
        replies = []
        for source in ("startup", "resume", "clear", "compact"):
            with self.subTest(source=source):
                output = self.invoke(json.dumps({"hook_event_name": "SessionStart",
                                                 "source": source}))
                body = json.loads(output)
                self.assertEqual({"hookSpecificOutput"}, set(body))
                specific = body["hookSpecificOutput"]
                self.assertEqual({"hookEventName", "additionalContext"}, set(specific))
                self.assertEqual("SessionStart", specific["hookEventName"])
                self.assertTrue(0 < len(specific["additionalContext"]) < 1000)
                replies.append(output)
        self.assertEqual(1, len(set(replies)))

    def test_malformed_or_unrelated_inputs_are_silent_noops(self):
        values = [None, [], "text", 12, {}, {"source": "compact"},
                  {"hook_event_name": "PostCompact", "source": "compact"}]
        values += [{"hook_event_name": "SessionStart", "source": source}
                   for source in (None, "other", "COMPACT", 1, True, [], {})]
        raw_values = ["", "{broken", "[" * 2000]
        raw_values += [json.dumps(value) for value in values]
        for raw in raw_values:
            with self.subTest(input=raw[:80]):
                self.assertEqual("", self.invoke(raw))

    def test_extra_input_cannot_enter_context_or_trigger_file_access(self):
        clean = {"hook_event_name": "SessionStart", "source": "compact"}
        noisy = dict(clean, cwd="UNTRUSTED_MARKER; touch injected",
                     transcript_path="/must/not/be/read", prompt="UNTRUSTED_MARKER")
        self.assertEqual(self.invoke(json.dumps(clean)), self.invoke(json.dumps(noisy)))


if __name__ == "__main__":
    unittest.main()
