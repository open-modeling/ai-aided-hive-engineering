#!/usr/bin/env python3
"""Stateless message checker.

The ok result means that a message passed this communication gate. It does
not grant host permissions or establish that the speaker has authority.
An explicit rejection or deferral is a valid conversational decision but
does not pass the action gate.
"""
import json
import sys

CHANNELS = {"human", "agent"}
DIRECTIONS = {"incoming", "outgoing"}
KINDS = {"informational", "directional", "special-directional", "mixed"}
ACCEPTANCE = {"accept", "reject", "defer"}


def check(item):
    issues = []
    if not isinstance(item, dict):
        return {
            "valid": False, "ok": False, "decision": "invalid",
            "issues": ["Input must be an object."]
        }

    kind = item.get("kind")
    direction = item.get("direction")
    message = item.get("text")
    acceptance = item.get("accepted")

    if item.get("channel") not in CHANNELS:
        issues.append("Identify the Human or Agent channel.")
    if direction not in DIRECTIONS:
        issues.append("Identify incoming or outgoing direction.")
    if kind not in KINDS:
        issues.append("Classify informational, directional, special-directional, or mixed content.")
    if not isinstance(message, str) or not message.strip():
        issues.append("Provide nonempty message text.")

    decision = "information" if kind == "informational" else "outgoing"
    if kind == "mixed":
        decision = "unresolved"
        issues.append("Classify informational and directional segments separately.")
    elif kind in ("directional", "special-directional"):
        if direction == "incoming":
            decision = {
                "accept": "accepted", "reject": "rejected",
                "defer": "deferred"
            }.get(acceptance, "unresolved")
            if acceptance not in ACCEPTANCE:
                issues.append("Explicitly decide accept, reject, or defer before action.")
        else:
            decision = "outgoing"
            if acceptance is not None:
                issues.append("Acceptance belongs to the receiving agent, not the sender.")
            if kind == "special-directional":
                for key in ("actor", "action", "target", "expected_result"):
                    if not isinstance(item.get(key), str) or not item[key].strip():
                        issues.append("Identify the " + key + " for the directional message.")

    valid = not issues
    ok = valid and decision not in {"rejected", "deferred", "unresolved"}
    if valid and decision == "rejected":
        issues.append("The receiving agent rejected the direction; do not execute it.")
    if valid and decision == "deferred":
        issues.append("The receiving agent deferred the direction; obtain clarification.")
    return {"valid": valid, "ok": ok, "decision": decision, "issues": issues}


def main():
    try:
        obj = json.load(sys.stdin)
        result = check(obj)
    except (ValueError, UnicodeError) as exc:
        result = {
            "valid": False, "ok": False, "decision": "invalid",
            "issues": ["Input JSON is invalid: " + str(exc)]
        }
    sys.stdout.write(json.dumps(result, ensure_ascii=False) + "\n")
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
