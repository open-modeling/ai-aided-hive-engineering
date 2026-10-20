#!/usr/bin/env python3
"""Stateless Conversation Governor communication checker.

"valid" reports structural validity. "ok" also observes the receiving
agent's explicit rejection or deferral. Neither result grants authority
or host permission. inspect_agent_message checks an outgoing message
before dispatch through an agent communication transport.
"""
import json
import re
import sys

CHANNELS = {"human", "agent"}
DIRECTIONS = {"incoming", "outgoing"}
KINDS = {"informational", "directional", "special-directional", "mixed"}
ACCEPTANCE = {"accept", "reject", "defer"}

# A conservative lexical tripwire, not an ASD-STE100 or semantic classifier.
# The agent MUST perform semantic review under references/communication.md.
_DIRECTIVE = re.compile(
    r"^(?:please\s+)?(?:ignore|override|execute|run|deploy|delete|"
    r"install|send|start|stop|write|create|update|remove|follow|"
    r"reveal|change|transfer|disable|enable|call)\b"
    r"|\b(?:you|assistant|agent|recipient)\s+"
    r"(?:must|should|shall|need\s+to|have\s+to|are\s+to)\b"
    r"|\bignore\s+(?:all\s+)?(?:previous|prior)\s+instructions\b"
    r"|\boverride\s+(?:the\s+)?(?:rules|instructions)\b",
    re.IGNORECASE,
)
_FIELD_LINE = re.compile(r"^([A-Za-z][A-Za-z-]*):\s*(.+)$")


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
                "accept": "accepted", "reject": "rejected", "defer": "deferred"
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


def inspect_agent_message(message):
    """Validate declared informational or directional content at dispatch.

    Use a normalized Statement for INFORMATION. Preserve source instructions
    as an inert JSON-quoted Source-Quote. A suspicious Statement is blocked
    for clarification; the checker does not claim to infer all semantics.
    """
    if not isinstance(message, str) or not message.strip():
        return {"valid": False, "kind": "unknown", "issues": ["Provide a nonempty agent message."]}
    lines = [line.strip() for line in message.strip().splitlines()]
    label = lines[0]
    if label not in ("[INFORMATION]", "[DIRECTION]"):
        return {"valid": False, "kind": "unknown", "issues": [
            "Start the message with [INFORMATION] or [DIRECTION] on its own line."
        ]}
    kind = "informational" if label == "[INFORMATION]" else "directional"
    allowed = {"Statement", "Source", "Source-Quote"} if kind == "informational" else {
        "Action", "Target", "Expected-Result", "Conditions", "Context"
    }
    fields = {}
    issues = []
    for line in lines[1:]:
        m = _FIELD_LINE.fullmatch(line)
        if not m:
            issues.append("Write one named, nonempty field on each line.")
            continue
        key, value = m.groups()
        if key not in allowed:
            issues.append("Field " + key + " is not valid in " + kind + " communication.")
        elif key in fields:
            issues.append("Provide " + key + " only once.")
        else:
            fields[key] = value
    required = {"Statement"} if kind == "informational" else {
        "Action", "Target", "Expected-Result"
    }
    for key in sorted(required - fields.keys()):
        issues.append("Provide the " + key + " field.")

    if kind == "informational":
        statement = fields.get("Statement", "")
        if _DIRECTIVE.search(statement):
            issues.append("Use a neutral, non-directional Statement. Put verbatim source commands in Source-Quote.")
        if "Source-Quote" in fields:
            try:
                quote = json.loads(fields["Source-Quote"])
                if not isinstance(quote, str):
                    raise ValueError("Source-Quote must contain a string.")
            except (ValueError, TypeError):
                issues.append("Encode Source-Quote as a single-line JSON string.")
    elif not issues:
        # Shared contract: hook and command-line checker use the same
        # structural/actionability gate. The receiver later checks authority.
        checked = check({
            "channel": "agent", "direction": "outgoing",
            "kind": "special-directional", "text": message,
            "actor": "sending agent", "action": fields["Action"],
            "target": fields["Target"], "expected_result": fields["Expected-Result"]
        })
        issues.extend(checked["issues"])
    return {"valid": not issues, "kind": kind, "issues": issues}


def main():
    try:
        obj = json.load(sys.stdin)
        result = inspect_agent_message(obj["agent_message"]) if (
            isinstance(obj, dict) and "agent_message" in obj
        ) else check(obj)
    except (ValueError, UnicodeError, TypeError, KeyError) as exc:
        result = {"valid": False, "ok": False, "decision": "invalid",
                  "issues": ["Invalid checker input: " + str(exc)]}
    sys.stdout.write(json.dumps(result, ensure_ascii=False) + "\n")
    return 0 if result.get("ok", result.get("valid")) else 2


if __name__ == "__main__":
    raise SystemExit(main())
