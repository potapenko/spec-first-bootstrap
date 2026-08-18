import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "lifecycle_restart.py"
SPEC = importlib.util.spec_from_file_location("lifecycle_restart", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class LifecycleRestartTests(unittest.TestCase):
    def test_all_session_sources_use_root_context(self) -> None:
        for source in ("startup", "resume", "clear", "compact"):
            with self.subTest(source=source):
                output = MODULE.build_output(
                    {"hook_event_name": "SessionStart", "source": source}
                )
                self.assertTrue(output["continue"])
                hook = output["hookSpecificOutput"]
                self.assertEqual(hook["hookEventName"], "SessionStart")
                self.assertIn("Contract Change Envelope", hook["additionalContext"])
                self.assertIn("Markdown traversal receipt", hook["additionalContext"])
                self.assertIn("revision", hook["additionalContext"])
                self.assertIn("unselected siblings", hook["additionalContext"])
                self.assertNotIn("finite worker packet", hook["additionalContext"])

    def test_subagent_uses_bounded_worker_context(self) -> None:
        output = MODULE.build_output(
            {"hook_event_name": "SubagentStart", "agent_type": "worker"}
        )
        hook = output["hookSpecificOutput"]
        self.assertEqual(hook["hookEventName"], "SubagentStart")
        self.assertIn("finite worker packet", hook["additionalContext"])
        self.assertIn("Markdown traversal receipt", hook["additionalContext"])
        self.assertIn("pinned closure", hook["additionalContext"])
        self.assertIn("unselected sibling", hook["additionalContext"])
        self.assertIn("Own exactly the assigned finite scope", hook["additionalContext"])
        self.assertNotIn("If a persistent goal is paused", hook["additionalContext"])

    def test_non_mapping_payload_falls_back_to_session_start(self) -> None:
        output = MODULE.build_output(["unexpected"])
        self.assertEqual(
            output["hookSpecificOutput"]["hookEventName"], "SessionStart"
        )

    def test_malformed_cli_input_returns_valid_json(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input="not-json\n",
            text=True,
            capture_output=True,
            check=True,
            timeout=5,
        )
        output = json.loads(result.stdout)
        self.assertTrue(output["continue"])
        self.assertEqual(
            output["hookSpecificOutput"]["hookEventName"], "SessionStart"
        )

    def test_contexts_fit_configured_limit_conservatively(self) -> None:
        self.assertLess(len(MODULE.ROOT_CONTEXT), 5000)
        self.assertLess(len(MODULE.WORKER_CONTEXT), 5000)


if __name__ == "__main__":
    unittest.main()
