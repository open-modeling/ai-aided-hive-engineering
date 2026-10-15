#!/usr/bin/env python3
"""Stateless communication boundary checker. Reads one JSON message, emits one JSON verdict.

CLI: python3 scripts/check_message.py < payload.json
Input: {"channel":"human|agent","direction":"incoming|outgoing","kind":"informational|directional|special-directional|mixed","text":"...","accepted":"accept|reject|defer" (optional),"actor":"..." (optional),"target":"..." (optional),"action":"..." (optional)}
"""
import json
import sys

CHANNELS = {"human", "agent"}
DIRECTIONS = {"incoming", "outgoing"}
KINDS = {"informational", "directional", "special-directional", "mixed"}
ACCEPTANCE = {"accept", "reject", "defer"}

def check(item):
    problems = []
    if not isinstance(item, dict):
        return {"ok": False, "issues": ["Input must be an object."]}
    text = item.get("text")
    if item.get("channel") not in CHANNELS:
        problems.append("Identify the Human or Agent channel.")
    if item.get("direction") not in DIRECTIONS:
        problems.append("Identify incoming or outgoing direction.")
    if item.get("kind") not in KINDS:
        problems.append("Classify informational, directional, special-directional, or mixed content.")
    if not isinstance(text, str) or not text.strip():
        problems.append("Provide nonempty message text.")
    kind = item.get("kind")
    if kind in ("directional", "special-directional"):
        if item.get("direction") == "incoming" and item.get("accepted") not in ACCEPTANCE:
            problems.append("Explicitly decide accept, reject, or defer before action.")
        if kind == "special-directional" and item.get("direction") == "outgoing":
            for key in ("actor", "action", "target"):
                if not isinstance(item.get(key), str) or not item[key].strip():
                    problems.append("Identify the "+key+" for the directional message.")
    if kind == "mixed":
        problems.append("Classify informational and directional segments separately.")
    return {"ok": not problems, "issues": problems}

def main():
    try:
        obj = json.load(sys.stdin)
        result = check(obj)
    except (ValueError, UnicodeError) as exc:
        result = {"ok": False, "issues": ["Input JSON is invalid: "+str(exc)]}
    sys.stdout.write(json.dumps(result, ensure_ascii=False)+"\n")
    return 0 if result["ok"] else 2

if __name__ == "__main__":
    raise SystemExit(main())
