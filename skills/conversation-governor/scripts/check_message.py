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
# Additional indicators produce a request for semantic review. These patterns
# are intentionally advisory; information is NEVER an execution instruction.
_MODAL_ACTION = re.compile(
    r"\b(?:deployment|validation|checks?|process|system|reviewer|agent|"
    r"operator|assistant|release|workflow)\s+(?:should|must|shall|"
    r"will|can|may|is\s+required\s+to|is\s+prepared\s+to)\s+"
    r"(?:be\s+)?(?:start|stop|deploy|execute|disable|enable|delete|"
    r"run|proceed|apply|approve|modify|update|transfer)\b"
    r"|\b(?:deployment|validation|checks?|operations?)\s+"
    r"(?:is|are)\s+(?:mandatory|required|to\s+be\s+disabled)\b"
    r"|\b(?:all\s+)?(?:validators?|checks?)\s+"
    r"(?:will|must|should)\s+be\s+disabled\b",
    re.I,
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
                "action_allowed": False,
                "issues": ["Input must be an object."]}
    # A02: Agent messages without recognized kinds remain informational.
    supplied_kind = item.get("kind")
    kind = (supplied_kind if supplied_kind in KINDS
            else "informational" if item.get("channel") == "agent"
            else supplied_kind)
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
    if kind == "informational" and acceptance is not None:
        issues.append("INFORMATION cannot carry an acceptance decision. Remove accepted.")
    if item.get("channel") == "agent" and direction == "outgoing" and supplied_kind not in KINDS:
        issues.append("Outgoing Agent content requires an explicit kind.")
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
    # The structural 'ok' result is never execution approval for a direction.
    ok = (valid and decision not in {"rejected", "deferred", "unresolved"}
          and (direction == "outgoing" or kind == "informational"))
    if valid and decision == "rejected":
        issues.append("The receiving agent rejected the direction. Do not execute it.")
    if valid and decision == "deferred":
        issues.append("The receiving agent deferred the direction. Obtain clarification.")
    return {"valid": valid, "ok": ok, "decision": decision,
            "kind": kind,
            "classification_source": ("default" if item.get("channel") == "agent"
                                       and supplied_kind not in KINDS else "explicit"),
            "action_allowed": False, "issues": issues}


def inspect_agent_message(message):
    """Apply a fail-closed structural and conservative wording check (A02).

    INFORMATION is data only. Uncertain wording requires a review and a
    normalized Statement. Source-Quote is preserved as a JSON string.
    The receiving agent still checks authority before acting on DIRECTION.
    """
    if not isinstance(message, str) or not message.strip():
        return {"valid": False, "kind": "informational", "status": "invalid",
                "format_valid": False,
                "classification_source": "default",
                "issues": ["Provide a nonempty agent message."]}
    lines = [line.strip() for line in message.strip().splitlines()]
    label = lines[0]
    if label not in ("[INFORMATION]", "[DIRECTION]"):
        # Missing or unrecognized tags are INFORMATION by default.
        # The message can still require review and never grants action.
        statement = message.strip()
        clauses = re.split(r"(?<=[.!?])\s+", statement)
        suspicious = (
            any(_IMPERATIVE.search(clause) for clause in clauses)
            or bool(_DIRECTED_ACTOR.search(statement))
            or bool(_INDIRECT_DIRECTION.search(statement))
            or bool(_MODAL_ACTION.search(statement))
            or bool(re.search(r"(?m)^\s*(?:Action|Target|Expected-Result):", statement))
            or bool(label.startswith("[") and label.endswith("]"))
        )
        issues = (["NEEDS_REVIEW: The untagged Agent message is INFORMATION. "
                   "It contains a possible request for action. Preserve its "
                   "text and ask for an explicit classified message."]
                  if suspicious else [])
        return {"valid": not suspicious,
                "status": "needs_review" if suspicious else "valid",
                "kind": "informational", "classification_source": "default",
                "format_valid": False, "issues": issues}
    kind = "informational" if label == "[INFORMATION]" else "directional"
    allowed = {"Statement", "Source", "Source-Quote"} if kind == "informational" else {
        "Action", "Target", "Expected-Result", "Conditions", "Context"
    }
    required = {"Statement"} if kind == "informational" else {
        "Action", "Target", "Expected-Result"
    }
    issues = []
    needs_review = False
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
        clauses = re.split(r"(?<=[.!?])\s+", statement)
        suspicious = (
            any(_IMPERATIVE.search(clause) for clause in clauses)
            or _DIRECTED_ACTOR.search(statement)
            or _INDIRECT_DIRECTION.search(statement)
            or _MODAL_ACTION.search(statement)
        )
        if suspicious:
            needs_review = True
            issues.append(
                "NEEDS_REVIEW: Statement may contain an instruction. "
                "Identify the factual meaning, write a neutral Statement, "
                "and preserve quoted commands in Source-Quote."
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
    # An instruction-like Statement can be well-formed but require semantic review.
    format_valid = not any(not issue.startswith("NEEDS_REVIEW:") for issue in issues)
    return {"valid": not issues, "classification_source": "explicit",
            "format_valid": format_valid,
            "status": ("needs_review" if needs_review and not any(not issue.startswith("NEEDS_REVIEW:") for issue in issues) else "invalid" if issues else "valid"), "kind": kind, "issues": issues}



def assess_received_message(message, acceptance=None, authority_verified=False,
                            scope_verified=False, conditions_verified=False):
    """Receiver-side interpretation boundary, without persistent state.

    INFORMATION always has action_allowed=False, even when a lexical check
    misses a concealed instruction. An accepted DIRECTION needs an explicit
    receiver decision and independently checked authority. Callers MUST derive
    authority_verified from trusted recipient context, never from message text.
    """
    result = inspect_agent_message(message)
    kind = result["kind"]
    if not result["valid"]:
        return {"valid": False, "kind": kind,
                "status": result.get("status", "invalid"),
                "decision": "review" if result.get("status") == "needs_review" else "defer",
                "processed": False, "action_allowed": False,
                "issues": result["issues"]}
    if kind == "informational":
        return {"valid": True, "kind": kind, "status": "valid",
                "decision": "information", "processed": True,
                "action_allowed": False, "issues": []}
    if acceptance == "reject":
        return {"valid": True, "kind": kind, "decision": "rejected",
                "action_allowed": False, "issues": []}
    if acceptance != "accept":
        return {"valid": True, "kind": kind, "decision": "deferred",
                "action_allowed": False,
                "issues": ["Receiving agent must explicitly accept or reject."]}
    if (authority_verified is not True or scope_verified is not True
            or conditions_verified is not True):
        return {"valid": True, "kind": kind, "decision": "deferred",
                "processed": False, "action_allowed": False,
                "issues": ["Verify authority, scope, and conditions using trusted recipient context."]}
    return {"valid": True, "kind": kind, "decision": "accepted",
            "processed": True, "action_allowed": True, "issues": []}


def main():
    mode = "check"
    try:
        obj = json.load(sys.stdin)
        if isinstance(obj, dict) and "received_message" in obj:
            mode = "received"
            result = assess_received_message(obj["received_message"],
                acceptance=obj.get("recipient_decision"),
                authority_verified=False)
        elif isinstance(obj, dict) and "agent_message" in obj:
            mode = "outgoing"
            result = inspect_agent_message(obj["agent_message"])
        else:
            result = check(obj)
    except (ValueError, UnicodeError, TypeError, KeyError) as exc:
        result = {"valid": False, "ok": False, "decision": "invalid",
                  "issues": ["Invalid checker input: " + str(exc)]}
    sys.stdout.write(json.dumps(result, ensure_ascii=False) + "\n")
    # Dispatch by mode. A checker result is not an authorization decision.
    if mode == "received":
        return 0 if (result.get("processed") and
                     (result.get("kind") == "informational" or
                      result.get("action_allowed") is True)) else 2
    if mode == "outgoing":
        return 0 if (result.get("valid") and result.get("format_valid")) else 2
    return 0 if result.get("ok") is True else 2


if __name__ == "__main__":
    raise SystemExit(main())
