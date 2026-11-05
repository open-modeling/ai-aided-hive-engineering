import sys
import pathlib
import unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_ads import check_skill_api, check_envelope

class SchemaTests(unittest.TestCase):
    def envelope(self):
        return {"message_type":"role-to-skill","dispatch_state":"resolved",
                "source_role":"architect",
                "target_skill_uri":"skill:ai-devmode.conversation-governor",
                "resolved_target_version":"0.4.0-dev",
                "capability_id":"control-language",
                "expected_outcome_ids":["quality-message"],
                "intent":"Interpret request",
                "payload_schema_uri":"https://example.org/message.json",
                "payload":{"text":"Hello"}}
    def test_local_api_schema(self):
        self.assertEqual(check_skill_api(),[])
    def test_valid_envelope(self):
        self.assertEqual(check_envelope(self.envelope()),[])
    def test_wrong_target(self):
        e=self.envelope();e["target_skill_uri"]="skill:other.governor"
        self.assertTrue(check_envelope(e))
    def test_unlinked_outcome(self):
        e=self.envelope();e["expected_outcome_ids"]=["safe-acceptance"]
        self.assertTrue(check_envelope(e))
    def test_version_mismatch(self):
        e=self.envelope();e["requested_target_version"]="0.3.1-dev"
        self.assertTrue(check_envelope(e))
    def test_skill_sender_requires_uri_version(self):
        e=self.envelope();e["message_type"]="skill-to-skill";e.pop("source_role")
        self.assertTrue(check_envelope(e))
    def test_unsupported_field(self):
        e=self.envelope();e["pretend_authorized"]=True
        self.assertTrue(check_envelope(e))
