#!/usr/bin/env python3
"""Offline ADS 5.0.0-rc.2 envelope and local Skill API validation."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas" / "ads"
PREFIX = "https://schemas.ai-devmode.invalid/ads/5.0.0-rc.2/skill-architecture/"


def validator(filename):
    from jsonschema import Draft202012Validator, FormatChecker, RefResolver
    documents = {}
    for name in ("ads-common-definitions.schema.json", "skill-message-envelope.schema.json", "skill-api.schema.json"):
        obj = json.loads((SCHEMAS / name).read_text(encoding="utf-8"))
        documents[obj["$id"]] = obj
    schema = documents[PREFIX + filename]
    return Draft202012Validator(
        schema, resolver=RefResolver.from_schema(schema, store=documents),
        format_checker=FormatChecker(),
    )


def check_skill_api():
    data = json.loads((ROOT / "skill-api.json").read_text(encoding="utf-8"))
    issues = [e.message for e in validator("skill-api.schema.json").iter_errors(data)]
    outcomes = {v["id"] for v in data.get("outcomes", [])}
    for cap in data.get("capabilities", []):
        for outcome in cap.get("outcome_ids", []):
            if outcome not in outcomes:
                issues.append("Unknown capability outcome: " + outcome)
    return issues


def check_envelope(envelope, target_api=None):
    target_api = target_api or json.loads((ROOT / "skill-api.json").read_text(encoding="utf-8"))
    issues = [e.message for e in validator("skill-message-envelope.schema.json").iter_errors(envelope)]
    if issues or not isinstance(envelope, dict):
        return issues
    if envelope.get("target_skill_uri") != target_api["skill_uri"]:
        issues.append("Target skill URI does not match the local skill.")
    capabilities = {item["id"]: item for item in target_api["capabilities"]}
    cap = capabilities.get(envelope.get("capability_id"))
    if cap is None:
        issues.append("Unknown capability.")
    else:
        for outcome in envelope.get("expected_outcome_ids", []):
            if outcome not in cap["outcome_ids"]:
                issues.append("Outcome is not linked to capability: " + outcome)
        required_schema = cap.get("request_schema_uri")
        if required_schema and envelope.get("payload_schema_uri") != required_schema:
            issues.append("Payload schema URI differs from capability contract.")
    requested = envelope.get("requested_target_version")
    resolved = envelope.get("resolved_target_version")
    if requested is not None and resolved is not None and requested != resolved:
        issues.append("Requested and resolved versions differ.")
    if resolved is not None and resolved != target_api["version"]:
        issues.append("Resolved version differs from installed version.")
    return issues


if __name__ == "__main__":
    print(json.dumps({"skill_api_issues": check_skill_api()}, ensure_ascii=False))
    raise SystemExit(0 if not check_skill_api() else 2)
