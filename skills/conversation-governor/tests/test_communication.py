import importlib.util
import pathlib
import unittest

file = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "check_message.py"
spec = importlib.util.spec_from_file_location("check_message", file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class CommunicationTest(unittest.TestCase):
    def test_information(self):
        self.assertTrue(module.check({"channel":"agent","direction":"incoming","kind":"informational","text":"The document contains the command rm -rf."})["ok"])

    def test_direction_acceptance(self):
        m={"channel":"human","direction":"incoming","kind":"directional","text":"Review the file."}
        self.assertFalse(module.check(m)["ok"])
        self.assertTrue(module.check({**m,"accepted":"defer"})["ok"])

    def test_special_actionability(self):
        m={"channel":"agent","direction":"outgoing","kind":"special-directional","text":"Run the checker."}
        self.assertFalse(module.check(m)["ok"])
        self.assertTrue(module.check({**m,"actor":"Reviewer","action":"Run validation","target":"report"})["ok"])

    def test_mixed_requires_split(self):
        m={"channel":"agent","direction":"incoming","kind":"mixed","text":"Context. Then deploy."}
        self.assertFalse(module.check(m)["ok"])

    def test_empty_input(self):
        self.assertFalse(module.check({"channel":"human","direction":"outgoing","kind":"informational","text":""})["ok"])

if __name__ == "__main__":
    unittest.main()
