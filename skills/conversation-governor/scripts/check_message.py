#!/usr/bin/env python3
"""Stateless communication boundary validator.

Structural validity is different from acceptance and authorization.
The receiving agent selects ACCEPT, REJECT, or DEFER. This checker neither
grants host permissions nor certifies the meaning of natural language.
"""
import json
import re
import sys

CHANNELS = {"human", "agent"}
DIRECTIONS = {"incoming", "outgoing"}
KINDS = {"informational", "directional", "special-directional", "mixed"}
ACCEPTANCE = {"accept", "reject", "defer"}

# Conservative indicators for informational statements that may direct work.
# These checks trigger clarification; they do not certify semantic safety.
_IMPERATIVE = re.compile(
    r"^(?:please\s+)?(?:ignore|override|execute|run|deploy|delete|"
    r"install|send|start|stop|write|create|update|remove|follow|"
    r"reveal|change|transfer|disable|enable|call|approve|apply|"
    r"proceed|use|make|perform)\b", re.I
)
_DIRECTED_ACTOR = re.compile(
    r"\b(?:you|we|assistant|agent|recipient|operator|reviewer|"
    r"developer|system)\s+(?:must|should|shall|need\s+to|needs\s+to|"
    r"have\s+to|has\s+to|are\s+to|is\s+to|ought\s+to|"
    r"are\s+expected\s+to|is\s+expected\s+to)\b", re.I
)
_INDIRECT_DIRECTION = re.compile(
    r"\b(?:next|following|required|recommended|suggested|proposed)\s+"
    r"(?:step|action|task|operation)\s+(?:is|would\s+be|will\s+be|"
    r"should\s+be)\s+(?:to\s+)?\b"
    r"|\b(?:it\s+is|it's)\s+(?:time|necessary|required|recommended|"
    r"important|best)\s+to\b"
    r"|\b(?:please|kindly)\s+(?:ensure|arrange|make\s+sure)\b"
    r"|\b(?:ignore|override)\s+(?:all\s+)?(?:previous|prior)\s+"
    r"(?:rules|instructions)\b", re.I
)
_FIELDS = re.compile(r"^([A-Za-z][A-Za-z-]*):\s*(.+)$")
_VAGUE = {
    "Action": {"do it", "handle", "manage", "perform", "do task",
               "do the task", "anything", "whatever", "tbd", "none", "n/a"},
    "Target": {"it", "that", "something", "anything", "whatever",
               "unknown", "tbd", "none", "n/a"},
    "Expected-Result": {"done", "complete", "success", "ok", "fine",
                        "anything", "whatever", "tbd", "none", "n/a"},
}


def check(item):
    """Check message fields and explicit receipt-side acceptance (A01)."""
    issues = []
    if not isinstance(item, dict):
        return {"valid": False, "ok": False, "decision": "invalid",
                "issues": ["Input must be an object."]}
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
    elif kind in {"directional", "special-directional"}:
        if direction == "incoming":
            decision = {"accept": "accepted", "reject": "rejected",
                        "defer": "deferred"}.get(acceptance, "unresolved")
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
        issues.append("The receiving agent rejected the direction. Do not execute it.")
    if valid and decision == "deferred":
        issues.append("The receiving agent deferred the direction. Obtain clarification.")
    return {"valid": valid, "ok": ok, "decision": decision, "issues": issues}


def inspect_agent_message(message):
    """Apply a fail-closed structural and conservative wording check (A02).

    INFORMATION is data only. Uncertain wording requires a review and a
    normalized Statement. Source-Quote is preserved as a JSON string.
    The receiving agent still checks authority before acting on DIRECTION.
    """
    if not isinstance(message, str) or not message.strip():
        return {"valid": False, "kind": "unknown",
                "issues": ["Provide a nonempty agent message."]}
    lines = [line.strip() for line in message.strip().splitlines()]
    label = lines[0]
    if label not in ("[INFORMATION]", "[DIRECTION]"):
        return {"valid": False, "kind": "unknown", "issues": [
            "Start with [INFORMATION] or [DIRECTION] on a separate line."
        ]}
    kind = "informational" if label == "[INFORMATION]" else "directional"
    allowed = {"Statement", "Source", "Source-Quote"} if kind == "informational" else {
        "Action", "Target", "Expected-Result", "Conditions", "Context"
    }
    required = {"Statement"} if kind == "informational" else {
        "Action", "Target", "Expected-Result"
    }
    issues = []
    fields = {}
    for line in lines[1:]:
        match = _FIELDS.fullmatch(line)
        if not match:
            issues.append("Use one named, nonempty field on each physical line.")
            continue
        key, value = match.groups()
        if key not in allowed:
            issues.append("Field " + key + " is not valid for " + kind + " messages.")
        elif key in fields:
            issues.append("Provide " + key + " only once.")
        else:
            fields[key] = value
    for key in sorted(required - fields.keys()):
        issues.append("Provide the " + key + " field.")

    if kind == "informational":
        statement = fields.get("Statement", "")
        if (_IMPERATIVE.search(statement)
                or _DIRECTED_ACTOR.search(statement)
                or _INDIRECT_DIRECTION.search(statement)):
            issues.append(
                "Statement may direct an action. Give a neutral fact or finding. "
                "Keep verbatim instructions in Source-Quote."
            )
        if "Source-Quote" in fields:
            try:
                value = json.loads(fields["Source-Quote"])
                if not isinstance(value, str):
                    raise ValueError("Source-Quote must be a string.")
            except (ValueError, TypeError):
                issues.append(
                    "Encode Source-Quote as a JSON string. Use escaped \\n for source line breaks."
                )
    else:
        for key, vague_values in _VAGUE.items():
            if fields.get(key, "").strip().lower().rstrip(".") in vague_values:
                issues.append("Specify a concrete " + key + " value.")
        if not issues:
            # Shared structural/actionability checker. This is an outgoing
            # request; only the recipient may accept it.
            outcome = check({
                "channel": "agent", "direction": "outgoing",
                "kind": "special-directional", "text": message,
                "actor": "sending agent", "action": fields["Action"],
                "target": fields["Target"],
                "expected_result": fields["Expected-Result"]
            })
            issues.extend(outcome["issues"])

    if not issues:
        # Use the same base validator for informational communications.
        outcome = check({
            "channel": "agent", "direction": "outgoing",
            "kind": kind if kind == "informational" else "special-directional",
            "text": message,
            **({} if kind == "informational" else {
                "actor": "sending agent", "action": fields["Action"],
                "target": fields["Target"], "expected_result": fields["Expected-Result"]
            })
        })
        issues.extend(outcome["issues"])
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
