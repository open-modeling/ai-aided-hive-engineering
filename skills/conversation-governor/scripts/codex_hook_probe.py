#!/usr/bin/env python3
"""Stateless, read-only Codex hook feasibility probe (A02).

No hook is registered by this script. No decisions are issued, and no message
bodies are logged or echoed. --inspect reports local observations. --marker
emits only an inert PreToolUse additionalContext marker for opt-in field tests.
"""
import argparse
import json
import re
import sys

# Candidate identities, not verified actual Codex hook dispatch names.
# A tool's displayed API name may differ from the name delivered to hooks.
CANDIDATE_FIELDS = {
    "collaboration.spawn_agent": "message",
    "collaboration.followup_task": "message",
    "collaboration.send_message": "message",
    "collaborationspawn_agent": "message",
    "collaborationfollowup_task": "message",
    "collaborationsend_message": "message",
    "spawn_agent": "message",
    "followup_task": "message",
    "send_message": "message",
    "mcp__codex_tui__send_message_to_thread": "prompt",
}
OPAQUE_LIKE = re.compile(r"^gAAAA[A-Za-z0-9_-]{20,}={0,2}$")


def inspect(event, sentinel=None):
    """Describe one synthetic or actual event without certifying its origin."""
    base = {"probe": "CG-A02-v1", "host_verified": False,
            "permission_decision": "none"}
    if not isinstance(event, dict):
        return {**base, "status": "invalid", "tool": None,
                "reason": "Expected a JSON event object."}
    if event.get("hook_event_name") != "PreToolUse":
        return {**base, "status": "not_pretooluse", "tool": None,
                "reason": "No PreToolUse event supplied."}
    tool = event.get("tool_name")
    if not isinstance(tool, str) or not tool.strip():
        return {**base, "status": "invalid", "tool": None,
                "reason": "Expected a nonempty tool_name."}
    field = CANDIDATE_FIELDS.get(tool)
    if field is None:
        return {**base, "status": "unmapped", "tool": tool,
                "message_field": None,
                "reason": "No candidate mapping; no coverage claim."}
    args = event.get("tool_input")
    if not isinstance(args, dict):
        return {**base, "status": "invalid", "tool": tool,
                "message_field": field,
                "reason": "Expected an object for tool_input."}
    message = args.get(field)
    string_payload = isinstance(message, str)
    return {
        **base, "status": "candidate", "tool": tool,
        "message_field": field,
        "message_field_present": field in args,
        "message_is_string": string_payload,
        "opaque_token_like": bool(string_payload and OPAQUE_LIKE.fullmatch(message)),
        "sentinel_visible": (sentinel in message if sentinel is not None
                             and string_payload else False if sentinel is not None
                             else None),
        "reason": ("Candidate mapping only. Marker presence does not prove the "
                   "same plaintext was delivered to the recipient."),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--inspect", action="store_true",
                      help="Print sanitized evidence to stdout.")
    mode.add_argument("--marker", action="store_true",
                      help="Print inert additionalContext for opt-in PreToolUse probe.")
    parser.add_argument("--sentinel", help="Harmless test token to find, never print.")
    args = parser.parse_args(argv)
    if args.sentinel == "":
        parser.error("sentinel must be nonempty")
    try:
        event = json.load(sys.stdin)
    except (ValueError, UnicodeError, TypeError):
        event = None
    report = inspect(event, args.sentinel)
    if args.inspect:
        print(json.dumps(report, ensure_ascii=False))
        return 2 if report["status"] == "invalid" else 0
    if report["status"] != "candidate":
        print("{}")
        return 0
    # Output no message content, source quotation, or secret values.
    found = report["sentinel_visible"]
    found_label = "unspecified" if found is None else "yes" if found else "no"
    marker = ("CG-A02-PROBE-v1 observed_candidate_tool; "
              "sentinel_visible=" + found_label + "; no permission decision")
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "additionalContext": marker,
    }}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
