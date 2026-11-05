"""Offline A02 probe tests; not evidence of actual Codex hook dispatch."""
import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from codex_hook_probe import inspect


class CodexHookProbeTests(unittest.TestCase):
    def event(self, name, field, value):
        return {"hook_event_name": "PreToolUse", "tool_name": name,
                "tool_input": {field: value}}

    def cli(self, args, payload):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "codex_hook_probe.py"),
             *args], input=payload, text=True, capture_output=True,
            check=False,
        )

    def test_namespaced_candidates_are_not_host_verified(self):
        for name, field in (
            ("collaboration.spawn_agent", "message"),
            ("collaboration.followup_task", "message"),
            ("collaboration.send_message", "message"),
            ("collaborationspawn_agent", "message"),
            ("mcp__codex_tui__send_message_to_thread", "prompt"),
        ):
            with self.subTest(name=name):
                r = inspect(self.event(name, field, "A harmless delegated task."))
                self.assertEqual(r["status"], "candidate")
                self.assertEqual(r["message_field"], field)
                self.assertFalse(r["host_verified"])
                self.assertEqual(r["permission_decision"], "none")

    def test_plaintext_sentinel_visibility_is_not_authorization(self):
        payload = "Reply with CG_TEST_SENTINEL_ABC and no other content."
        r = inspect(self.event("collaboration.spawn_agent", "message", payload),
                    sentinel="CG_TEST_SENTINEL_ABC")
        self.assertTrue(r["sentinel_visible"])
        self.assertFalse(r["host_verified"])

    def test_opaque_like_message_does_not_prove_plaintext(self):
        ciphertext = "gAAAA" + ("A" * 60)
        r = inspect(self.event("collaborationspawn_agent", "message", ciphertext),
                    sentinel="CG_TEST_SENTINEL_ABC")
        self.assertTrue(r["opaque_token_like"])
        self.assertFalse(r["sentinel_visible"])
        self.assertFalse(r["host_verified"])

    def test_unknown_and_non_tool_events_are_uncovered(self):
        r = inspect(self.event("TaskList", "foo", "bar"))
        self.assertEqual(r["status"], "unmapped")
        self.assertEqual(r["permission_decision"], "none")
        self.assertEqual(inspect({"hook_event_name": "PostToolUse"})["status"],
                         "not_pretooluse")

    def test_malformed_payloads_are_safe(self):
        for value in (None, [], "", {"hook_event_name": "PreToolUse"},
                      {"hook_event_name": "PreToolUse", "tool_name": []}):
            with self.subTest(value=value):
                self.assertEqual(inspect(value)["status"], "invalid")
        bad = {"hook_event_name": "PreToolUse",
               "tool_name": "collaboration.send_message", "tool_input": []}
        self.assertEqual(inspect(bad)["status"], "invalid")

    def test_readonly_inspect_cli_never_echoes_content(self):
        secret = "Sensitive-Payload-DO-NOT-PRINT"
        event = self.event("collaboration.send_message", "message", secret)
        p = self.cli(["--inspect", "--sentinel", secret], json.dumps(event))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertNotIn(secret, p.stdout)
        r = json.loads(p.stdout)
        self.assertTrue(r["sentinel_visible"])
        self.assertEqual(r["permission_decision"], "none")

    def test_inert_marker_cli(self):
        secret = "Sensitive-Payload-DO-NOT-PRINT"
        event = self.event("collaboration.followup_task", "message", secret)
        p = self.cli(["--marker", "--sentinel", secret], json.dumps(event))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertNotIn(secret, p.stdout)
        output = json.loads(p.stdout)["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "PreToolUse")
        self.assertIn("CG-A02-PROBE-v1", output["additionalContext"])
        self.assertNotIn("permissionDecision", output)

    def test_marker_passes_through_unknown_tools(self):
        p = self.cli(["--marker"], json.dumps(self.event("TaskList", "none", "anything")))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout), {})

    def test_invalid_json_exit_code(self):
        p = self.cli(["--inspect"], "{")
        self.assertEqual(p.returncode, 2)
        self.assertEqual(json.loads(p.stdout)["status"], "invalid")


if __name__ == "__main__":
    unittest.main()
