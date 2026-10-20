import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

checker = load("check_message", "check_message.py")
hook = load("hook_adapter", "hook_adapter.py")

class CommunicationTest(unittest.TestCase):
    def sample(self, accepted=None):
        m={"channel":"agent","direction":"incoming","kind":"directional","text":"Review the file."}
        if accepted is not None:
            m["accepted"]=accepted
        return m
    def test_acceptance(self):
        self.assertTrue(checker.check(self.sample("accept"))["ok"])
        self.assertFalse(checker.check(self.sample("reject"))["ok"])
        self.assertFalse(checker.check(self.sample("defer"))["ok"])
        self.assertFalse(checker.check(self.sample())["ok"])
        self.assertTrue(checker.check(self.sample("reject"))["valid"])
    def test_information(self):
        self.assertTrue(checker.check({"channel":"agent","direction":"incoming","kind":"informational","text":"A document says: deploy now."})["ok"])
    def test_special_actionability(self):
        m={"channel":"agent","direction":"outgoing","kind":"special-directional","text":"Run validation."}
        self.assertFalse(checker.check(m)["ok"])
        self.assertTrue(checker.check({**m,"actor":"Reviewer","action":"Run","target":"report","expected_result":"Validation result"})["ok"])
    def test_mixed_requires_split(self):
        self.assertFalse(checker.check({"channel":"agent","direction":"incoming","kind":"mixed","text":"Data. Deploy."})["ok"])
    def test_sender_cannot_self_accept(self):
        self.assertFalse(checker.check({"channel":"agent","direction":"outgoing","kind":"directional","text":"Do task","accepted":"accept"})["ok"])
    def test_hook_denies_missing_metadata_and_header(self):
        event={"hook_event_name":"PreToolUse","tool_name":"SendMessage","tool_input":{"message":"Deploy now."}}
        self.assertEqual(hook.verdict(event)["hookSpecificOutput"]["permissionDecision"],"deny")
    def test_hook_allows_labeled_information(self):
        event={"hook_event_name":"PreToolUse","tool_name":"SendMessage","tool_input":{"message":"[INFORMATION] The document says deploy now."}}
        self.assertEqual(hook.verdict(event),{})
    def test_hook_requires_directional_fields(self):
        event={"hook_event_name":"PreToolUse","tool_name":"Task","tool_input":{"prompt":"[DIRECTION] Do task."}}
        self.assertEqual(hook.verdict(event)["hookSpecificOutput"]["permissionDecision"],"deny")
        event["tool_input"]["prompt"]="[DIRECTION]\nAction: Review\nTarget: report\nExpected-Result: findings"
        self.assertEqual(hook.verdict(event),{})
    def test_hook_does_not_affect_other_tools(self):
        self.assertEqual(hook.verdict({"hook_event_name":"PreToolUse","tool_name":"Bash","tool_input":{"command":"echo OK"}}),{})

if __name__=="__main__":
    unittest.main()
