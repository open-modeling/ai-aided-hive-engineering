"""A02.03: Validate the field grammar of classified Agent messages.

Traceability: A02.03; CG-FR-09; CG-TR-06; CG-VR-02.
These tests cover source formatting only. Recipient authorization remains
outside the parser and needs separate host evidence.
"""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_message import assess_received_message, inspect_agent_message
from hook_adapter import verdict


class A02FieldValidationTests(unittest.TestCase):
    DIRECTION = (
        "[DIRECTION]\n"
        "Action: Review\n"
        "Target: report\n"
        "Expected-Result: documented findings"
    )
    INFORMATION = "[INFORMATION]\nStatement: The review is complete."

    def assert_invalid_fields(self, message, expected):
        with self.subTest(message=message):
            result = inspect_agent_message(message)
            self.assertFalse(result["valid"])
            self.assertFalse(result["format_valid"])
            self.assertEqual(result["status"], "invalid")
            self.assertTrue(any(expected in issue for issue in result["issues"]), result["issues"])

    def test_direction_complete_fields_are_valid(self):
        for message in (
            self.DIRECTION,
            self.DIRECTION + "\nConditions: Review is approved.\nContext: Release gate",
        ):
            with self.subTest(message=message):
                result = inspect_agent_message(message)
                self.assertTrue(result["valid"], result["issues"])
                self.assertTrue(result["format_valid"])
                self.assertEqual(result["kind"], "directional")

    def test_information_complete_fields_are_valid(self):
        for message in (
            self.INFORMATION,
            self.INFORMATION + '\nSource-Quote: "Deploy now."',
        ):
            with self.subTest(message=message):
                result = inspect_agent_message(message)
                self.assertTrue(result["valid"], result["issues"])
                self.assertEqual(result["kind"], "informational")

    def test_duplicate_direction_fields_are_rejected(self):
        for field, value in (
            ("Action", "Review"),
            ("Target", "report"),
            ("Expected-Result", "documented findings"),
            ("Conditions", "Release approved"),
            ("Context", "Release gate"),
        ):
            base = self.DIRECTION
            if field in ("Conditions", "Context"):
                base += f"\n{field}: {value}"
            self.assert_invalid_fields(base + f"\n{field}: {value}", f"Provide {field} only once")

    def test_duplicate_information_fields_are_rejected(self):
        self.assert_invalid_fields(
            self.INFORMATION + "\nStatement: The review is complete.",
            "Provide Statement only once",
        )
        self.assert_invalid_fields(
            self.INFORMATION + "\nSource: release report\nSource: release report",
            "Provide Source only once",
        )

    def test_unknown_fields_are_rejected(self):
        for message, field in (
            (self.DIRECTION + "\nPriority: urgent", "Priority"),
            (self.DIRECTION + "\nStatement: Work is complete.", "Statement"),
            (self.INFORMATION + "\nAction: Deploy", "Action"),
            (self.INFORMATION + "\nConditions: Approved", "Conditions"),
        ):
            self.assert_invalid_fields(message, f"Field {field} is not valid")

    def test_empty_required_fields_are_rejected(self):
        for key in ("Action", "Target", "Expected-Result"):
            fields = self.DIRECTION.splitlines()
            index = next(i for i, line in enumerate(fields) if line.startswith(key + ":"))
            fields[index] = key + ":   "
            self.assert_invalid_fields("\n".join(fields), "one named, nonempty field")
        self.assert_invalid_fields("[INFORMATION]\nStatement:   ", "one named, nonempty field")

    def test_empty_optional_fields_are_rejected(self):
        for key in ("Conditions", "Context"):
            self.assert_invalid_fields(self.DIRECTION + f"\n{key}:    ", "one named, nonempty field")
        self.assert_invalid_fields(self.INFORMATION + "\nSource:    ", "one named, nonempty field")

    def test_missing_required_fields_are_rejected(self):
        for key in ("Action", "Target", "Expected-Result"):
            lines = [line for line in self.DIRECTION.splitlines() if not line.startswith(key + ":")]
            self.assert_invalid_fields("\n".join(lines), f"Provide the {key} field")
        self.assert_invalid_fields("[INFORMATION]\nSource: release report", "Provide the Statement field")

    def test_malformed_physical_lines_are_rejected(self):
        for extra in ("garbage", "Action : Review", "", "  "):
            self.assert_invalid_fields(self.DIRECTION + "\n" + extra + "\nContext: release", "one named, nonempty field")

    def test_mixed_valid_and_invalid_fields_are_rejected(self):
        message = (
            self.DIRECTION + "\nConditions: Release approved"
            "\nTarget: another report\nPriority: urgent"
        )
        result = inspect_agent_message(message)
        self.assertFalse(result["valid"])
        self.assertTrue(any("Target only once" in x for x in result["issues"]))
        self.assertTrue(any("Field Priority is not valid" in x for x in result["issues"]))

    def test_invalid_direction_cannot_pass_receiver_check(self):
        message = self.DIRECTION + "\nTarget: another report"
        result = assess_received_message(
            message, acceptance="accept", authority_verified=True,
            scope_verified=True, conditions_verified=True,
        )
        self.assertFalse(result["action_allowed"])
        self.assertFalse(result["valid"])

    def test_invalid_fields_cause_hook_denial(self):
        for message in (self.DIRECTION + "\nPriority: urgent", self.INFORMATION + "\nStatement: Duplicate"):
            with self.subTest(message=message):
                result = verdict({
                    "hook_event_name": "PreToolUse", "tool_name": "SendMessage",
                    "tool_input": {"message": message},
                })
                self.assertEqual(result["hookSpecificOutput"]["permissionDecision"], "deny")


if __name__ == "__main__":
    unittest.main()
