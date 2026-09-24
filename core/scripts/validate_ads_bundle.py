#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urldefrag

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
LMC_SCHEMAS = ROOT / 'language-core' / 'schemas'
SA_SCHEMAS = ROOT / 'skill-architecture' / 'schemas'
SUITE_VERSION = '5.0.0-rc.1'
ADS_FILES = [
    ROOT / '00_governance_and_bootstrap.md',
    ROOT / 'language-core' / 'LMC-01_language_standards_profile.md',
    ROOT / 'language-core' / 'LMC-02_terminology_and_meaning_control.md',
    ROOT / 'language-core' / 'LMC-03_information_construction_and_applicability.md',
    ROOT / 'language-core' / 'LMC-04_language_and_meaning_conformance.md',
    ROOT / 'skill-architecture' / 'SA-01_skill_architecture_dictionary.md',
    ROOT / 'skill-architecture' / 'SA-02_skill_architecture_framework.md',
    ROOT / 'skill-architecture' / 'SA-03_machine_readable_contracts.md',
    ROOT / 'skill-architecture' / 'SA-04_required_host_compatibility.md',
    ROOT / 'skill-architecture' / 'SA-05_versioning_and_evolution.md',
    ROOT / 'skill-architecture' / 'SA-06_skill_api_and_communication.md',
    ROOT / 'skill-architecture' / 'SA-07_skill_development_and_conformance.md',
]

class Failure(Exception):
    pass


def load_schemas():
    docs = {}
    ids = {}
    schema_paths = sorted(LMC_SCHEMAS.glob('*.schema.json')) + sorted(SA_SCHEMAS.glob('*.schema.json'))
    for path in schema_paths:
        doc = json.loads(path.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(doc)
        sid = doc.get('$id')
        if not sid:
            raise Failure(f'{path.name}: missing $id')
        if sid in ids:
            raise Failure(f'duplicate $id: {sid} in {ids[sid]} and {path}')
        ids[sid] = path
        docs[str(path.relative_to(ROOT))] = doc
    if len(docs) != 7:
        raise Failure(f'expected 7 schemas, found {len(docs)}')
    registry = Registry()
    for doc in docs.values():
        registry = registry.with_resource(doc['$id'], Resource.from_contents(doc))
    return docs, ids, registry


def extend_registry_from_schema_dir(registry, directory: Path):
    if directory is None:
        return registry
    directory = directory.resolve()
    if not directory.is_dir():
        raise Failure(f'target schema directory does not exist: {directory}')
    for path in sorted(directory.rglob('*.json')):
        try:
            doc = json.loads(path.read_text(encoding='utf-8'))
        except Exception as exc:
            raise Failure(f'{path}: invalid JSON schema document: {exc}') from exc
        sid = doc.get('$id')
        if not sid:
            continue
        try:
            Draft202012Validator.check_schema(doc)
        except Exception as exc:
            raise Failure(f'{path}: invalid JSON Schema: {exc}') from exc
        registry = registry.with_resource(sid, Resource.from_contents(doc))
    return registry


def iter_refs(node):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == '$ref' and isinstance(v, str):
                yield v
            else:
                yield from iter_refs(v)
    elif isinstance(node, list):
        for item in node:
            yield from iter_refs(item)


def validate_refs(docs, ids, registry):
    for name, doc in docs.items():
        resolver = registry.resolver(base_uri=doc['$id'])
        for ref in iter_refs(doc):
            base, _ = urldefrag(ref)
            if base.startswith('https://schemas.ai-devmode.invalid/') and base not in ids:
                raise Failure(f'{name}: packaged ADS reference missing: {ref}')
            try:
                resolver.lookup(ref)
            except Exception as exc:
                raise Failure(f'{name}: unresolved $ref {ref}: {exc}') from exc


def validator(doc, registry):
    return Draft202012Validator(doc, registry=registry, format_checker=FormatChecker())


def assert_valid(v, instance, label):
    errors = sorted(v.iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        raise Failure(f'{label}: expected valid; first error: {errors[0].message}')


def assert_invalid(v, instance, label):
    if not list(v.iter_errors(instance)):
        raise Failure(f'{label}: expected invalid but validated')


def semantic_skill_api(api):
    expected = f"skill:{api['publisher']}.{api['name']}"
    if api.get('skill_uri') != expected:
        raise Failure(f"Skill API identity mismatch: {api.get('skill_uri')} != {expected}")
    cap_ids = [c['id'] for c in api.get('capabilities', [])]
    out_ids = [o['id'] for o in api.get('outcomes', [])]
    if len(cap_ids) != len(set(cap_ids)):
        raise Failure('Skill API capability IDs are not unique')
    if len(out_ids) != len(set(out_ids)):
        raise Failure('Skill API outcome IDs are not unique')
    known = set(out_ids)
    for cap in api.get('capabilities', []):
        missing = [oid for oid in cap.get('outcome_ids', []) if oid not in known]
        if missing:
            raise Failure(f"Capability {cap['id']} references unknown outcomes: {missing}")


def semantic_conformance_record(record, skill_api=None):
    uri = record.get('skill_uri', '')
    m = re.fullmatch(r'skill:([a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?)\.([a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?)', uri)
    if not m:
        raise Failure(f'conformance record has invalid skill_uri {uri!r}')
    local_name = m.group(2)
    if record.get('skill_name') != local_name:
        raise Failure(f"conformance record skill_name {record.get('skill_name')!r} does not match skill_uri local name {local_name!r}")
    if skill_api is not None:
        checks = [
            ('skill_uri', record.get('skill_uri'), skill_api.get('skill_uri')),
            ('skill_name', record.get('skill_name'), skill_api.get('name')),
            ('skill_version', record.get('skill_version'), skill_api.get('version')),
            ('lifecycle_classification', record.get('lifecycle_classification'), skill_api.get('lifecycle_classification')),
            ('configuration_classification', record.get('configuration_classification'), skill_api.get('configuration_classification')),
        ]
        for label, actual, expected in checks:
            if actual != expected:
                raise Failure(f'conformance record {label} {actual!r} does not match Skill API value {expected!r}')


def semantic_message(msg, target_api, target_schema_registry=None):
    requested = msg.get('requested_target_version')
    resolved = msg.get('resolved_target_version')
    if requested and resolved and requested != resolved:
        raise Failure(f'resolved target version {resolved} does not satisfy exact requested target version {requested}')
    if target_api is None:
        raise Failure('resolved target Skill API is required for semantic message validation')
    semantic_skill_api(target_api)
    if msg.get('target_skill_uri') != target_api.get('skill_uri'):
        raise Failure('message target_skill_uri does not match resolved target Skill API')
    if resolved and resolved != target_api.get('version'):
        raise Failure(f"message resolved_target_version {resolved!r} does not match target Skill API version {target_api.get('version')!r}")
    if requested and requested != target_api.get('version'):
        raise Failure(f"message requested_target_version {requested!r} does not match target Skill API version {target_api.get('version')!r}")
    cap = next((c for c in target_api.get('capabilities', []) if c.get('id') == msg.get('capability_id')), None)
    if cap is None:
        raise Failure(f"message capability_id {msg.get('capability_id')!r} is not declared by target Skill API")
    allowed_outcomes = set(cap.get('outcome_ids', []))
    missing = [oid for oid in msg.get('expected_outcome_ids', []) if oid not in allowed_outcomes]
    if missing:
        raise Failure(f'message expected outcomes are not linked to target capability: {missing}')
    declared_request_schema = cap.get('request_schema_uri')
    if declared_request_schema:
        if msg.get('payload_schema_uri') != declared_request_schema:
            raise Failure(
                f"message payload_schema_uri {msg.get('payload_schema_uri')!r} does not match target capability request_schema_uri {declared_request_schema!r}"
            )
        if target_schema_registry is None:
            raise Failure(f'target request schema {declared_request_schema!r} is unavailable for payload validation')
        try:
            schema_doc = target_schema_registry.resolver().lookup(declared_request_schema).contents
        except Exception as exc:
            raise Failure(f'target request schema {declared_request_schema!r} is unavailable for payload validation: {exc}') from exc
        payload_v = Draft202012Validator(schema_doc, registry=target_schema_registry, format_checker=FormatChecker())
        errors = sorted(payload_v.iter_errors(msg.get('payload')), key=lambda e: list(e.path))
        if errors:
            raise Failure(f'target request payload is invalid against {declared_request_schema}: {errors[0].message}')


def self_tests(docs, registry):
    api_v = validator(next(v for k,v in docs.items() if k.endswith('skill-api.schema.json')), registry)
    fm_v = validator(next(v for k,v in docs.items() if k.endswith('skill-frontmatter.schema.json')), registry)
    msg_v = validator(next(v for k,v in docs.items() if k.endswith('skill-message-envelope.schema.json')), registry)
    conf_v = validator(next(v for k,v in docs.items() if k.endswith('skill-conformance-record.schema.json')), registry)

    base = next(v for k,v in docs.items() if k.endswith('skill-api.schema.json'))['$id'].rsplit('/', 1)[0]
    good_api = {
        'publisher': 'acme',
        'name': 'document-governor',
        'skill_uri': 'skill:acme.document-governor',
        'version': '1.2.3',
        'lifecycle_classification': 'stateless',
        'configuration_classification': 'non-configurable',
        'operations_guide': 'references/operations.md',
        'applicability': {'when_to_use': ['Use when a project requires governed document checks.'], 'when_not_to_use': ['Do not use for source-code compilation.']},
        'capabilities': [{'id': 'check-document', 'where_it_helps': 'Document conformance review.', 'does': 'Checks the document against the declared rules.', 'outcome_ids': ['conformance-result'], 'request_schema_uri': 'https://example.invalid/document-check-request.schema.json'}],
        'outcomes': [{'id': 'conformance-result', 'what_to_expect': 'A conformance result with identified findings.', 'acceptance_criteria': ['The result identifies each blocking finding.']}],
        'communication': {'envelope_schema_uri': f'{base}/skill-message-envelope.schema.json'},
    }
    assert_valid(api_v, good_api, 'valid Skill API')
    semantic_skill_api(good_api)

    bad_uris = [
        'urn:uuid:123e4567-e89b-12d3-a456-426614174000',
        'skill:Acme.document-governor',
        'skill:ac.me.document-governor',
        'skill:acme.synced',
        'skill:ac%6de.document-governor',
        'skill:acme.document--governor',
    ]
    for bad in bad_uris:
        probe = dict(good_api, skill_uri=bad)
        assert_invalid(api_v, probe, f'invalid skill URI {bad}')

    mismatch = dict(good_api, skill_uri='skill:other.document-governor')
    assert_valid(api_v, mismatch, 'schema-valid identity mismatch probe')
    try:
        semantic_skill_api(mismatch)
    except Failure:
        pass
    else:
        raise Failure('semantic Skill API identity mismatch was not rejected')

    assert_valid(fm_v, {'name': 'document-governor', 'description': 'Govern project documents.'}, 'valid frontmatter')
    assert_invalid(fm_v, {'name': 'synced', 'description': 'Reserved.'}, 'reserved Claude skill name')

    request_schema = {
        '$schema': 'https://json-schema.org/draft/2020-12/schema',
        '$id': 'https://example.invalid/document-check-request.schema.json',
        'type': 'object',
        'additionalProperties': False,
        'required': ['document_id'],
        'properties': {'document_id': {'type': 'string', 'minLength': 1}},
    }
    request_registry = registry.with_resource(request_schema['$id'], Resource.from_contents(request_schema))

    role_req = {
        'message_type': 'role-to-skill',
        'dispatch_state': 'request',
        'source_role': 'reviewer',
        'target_skill_uri': 'skill:acme.document-governor',
        'capability_id': 'check-document',
        'expected_outcome_ids': ['conformance-result'],
        'intent': 'Check the document.',
        'payload_schema_uri': 'https://example.invalid/document-check-request.schema.json',
        'payload': {'document_id': 'DOC-1'},
    }
    assert_valid(msg_v, role_req, 'role request without version pin')
    semantic_message(role_req, good_api, request_registry)
    resolved = dict(role_req, dispatch_state='resolved', resolved_target_version='1.2.3')
    assert_valid(msg_v, resolved, 'resolved role request')
    semantic_message(resolved, good_api, request_registry)
    assert_invalid(msg_v, dict(role_req, dispatch_state='resolved'), 'resolved request without resolved target version')
    wrong_payload_contract = dict(resolved, payload_schema_uri='https://example.invalid/alternate-request.schema.json')
    assert_valid(msg_v, wrong_payload_contract, 'schema-valid alternate payload contract probe')
    try:
        semantic_message(wrong_payload_contract, good_api, request_registry)
    except Failure:
        pass
    else:
        raise Failure('message payload schema mismatch against target capability was not rejected')

    invalid_payload = dict(resolved, payload={})
    try:
        semantic_message(invalid_payload, good_api, request_registry)
    except Failure:
        pass
    else:
        raise Failure('payload invalid against target capability request schema was not rejected')

    pinned = dict(resolved, requested_target_version='1.2.4')
    try:
        semantic_message(pinned, good_api, request_registry)
    except Failure:
        pass
    else:
        raise Failure('mismatched exact target version was not rejected')

    skill_req = dict(role_req)
    skill_req.update(message_type='skill-to-skill', source_skill_uri='skill:acme.router', source_skill_version='2.0.0')
    skill_req.pop('source_role')
    assert_valid(msg_v, skill_req, 'skill-to-skill request')

    gates = {f'G{i}': 'PASS' for i in range(1, 17)}
    gates['G7'] = 'N/A'; gates['G8'] = 'N/A'; gates['G9'] = 'N/A'
    good_conf = {
        'skill_name': 'document-governor',
        'skill_uri': 'skill:acme.document-governor',
        'skill_version': '1.2.3',
        'canonical_package': '/repo/skills/document-governor',
        'ads_suite_version': SUITE_VERSION,
        'lifecycle_classification': 'stateless',
        'configuration_classification': 'non-configurable',
        'persists_project_data': False,
        'language_meaning_results': {'artifact_id':'skill:acme.document-governor','artifact_version':'1.2.3','lmc_version':SUITE_VERSION,'review_method':'designated-review','review_authority':'project-review','evidence':['review://skill/document-governor'],'bcp14':'PASS','asd_ste100_issue9':'PASS','project_terminology':'PASS','meaning_control':'PASS','protected_content':'N/A','result':'PASS'},
        'schema_results': {'metaschema_validation': 'PASS', 'offline_resolution': 'PASS', 'adversarial_self_tests': 'PASS'},
        'skill_api_results': {'schema_validation': 'PASS', 'identity_consistency': 'PASS', 'applicability_consistency': 'PASS', 'capability_implementation': 'PASS', 'outcome_linkage': 'PASS', 'communication_addressing': 'PASS'},
        'host_results': {'codex': 'PASS', 'claude_code': 'PASS'},
        'project_local_persistence': 'N/A',
        'changelog_results': {'candidate_entry': 'PASS', 'serving_codex': 'PASS', 'serving_claude_code': 'PASS'},
        'gates': gates,
        'should_deviations': [],
        'blocking_findings': [],
        'result': 'PASS',
    }
    assert_valid(conf_v, good_conf, 'valid conformance PASS')
    semantic_conformance_record(good_conf, good_api)

    bad_identity = json.loads(json.dumps(good_conf))
    bad_identity['skill_name'] = 'wrong-name'
    assert_valid(conf_v, bad_identity, 'schema-valid conformance identity mismatch probe')
    try:
        semantic_conformance_record(bad_identity)
    except Failure:
        pass
    else:
        raise Failure('conformance record skill_name/skill_uri mismatch was not rejected')

    probes = []
    p = json.loads(json.dumps(good_conf)); p['host_results']['codex'] = 'FAIL'; probes.append(('PASS with failed Codex', p))
    p = json.loads(json.dumps(good_conf)); p['gates']['G13'] = 'FAIL'; probes.append(('PASS with G13 FAIL', p))
    p = json.loads(json.dumps(good_conf)); p['gates']['G1'] = 'N/A'; probes.append(('unconditional G1 N/A', p))
    p = json.loads(json.dumps(good_conf)); p['gates']['G8'] = 'PASS'; probes.append(('stateless G8 PASS', p))
    p = json.loads(json.dumps(good_conf)); p['gates']['G7'] = 'PASS'; probes.append(('non-configurable G7 PASS', p))
    p = json.loads(json.dumps(good_conf)); p['should_deviations'] = ['CTL-020: justified exception']; probes.append(('PASS with SHOULD deviation', p))
    p = json.loads(json.dumps(good_conf)); p['changelog_results']['serving_codex'] = 'FAIL'; probes.append(('PASS with failed changelog serving', p))
    p = json.loads(json.dumps(good_conf)); p['skill_api_results']['outcome_linkage'] = 'FAIL'; probes.append(('PASS with failed Skill API linkage', p))
    p = json.loads(json.dumps(good_conf)); p['result'] = 'PASS WITH SHOULD DEVIATIONS'; probes.append(('PASS WITH SHOULD DEVIATIONS without deviation', p))
    for label, probe in probes:
        assert_invalid(conf_v, probe, label)

    stateful = json.loads(json.dumps(good_conf))
    stateful.update(lifecycle_classification='stateful', configuration_classification='configurable', persists_project_data=True, project_local_persistence='PASS')
    stateful['gates']['G7'] = 'PASS'; stateful['gates']['G8'] = 'PASS'; stateful['gates']['G9'] = 'PASS'
    assert_valid(conf_v, stateful, 'valid stateful configurable PASS')
    bad = json.loads(json.dumps(stateful)); bad['persists_project_data'] = False; bad['project_local_persistence'] = 'N/A'; bad['gates']['G9'] = 'N/A'
    assert_invalid(conf_v, bad, 'stateful skill without persisted project data')


def parse_frontmatter(path: Path):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        raise Failure(f'{path}: missing YAML frontmatter start')
    end = text.find('\n---\n', 4)
    if end < 0:
        raise Failure(f'{path}: missing YAML frontmatter end')
    return yaml.safe_load(text[4:end]) or {}


def validate_skill_package(path: Path, docs, registry):
    path = path.resolve()
    required = [path/'SKILL.md', path/'skill-api.json', path/'CHANGELOG.md', path/'references'/'operations.md']
    missing = [str(p.relative_to(path)) for p in required if not p.exists()]
    if missing:
        raise Failure(f'{path}: missing required package artifacts: {missing}')
    fm = parse_frontmatter(path/'SKILL.md')
    assert_valid(validator(next(v for k,v in docs.items() if k.endswith('skill-frontmatter.schema.json')), registry), fm, f'{path}: frontmatter')
    if path.name != fm['name']:
        raise Failure(f'{path}: parent directory {path.name!r} does not match SKILL.md name {fm["name"]!r}')
    api = json.loads((path/'skill-api.json').read_text(encoding='utf-8'))
    assert_valid(validator(next(v for k,v in docs.items() if k.endswith('skill-api.schema.json')), registry), api, f'{path}: skill-api.json')
    semantic_skill_api(api)
    if api['name'] != fm['name']:
        raise Failure(f'{path}: skill-api name does not match SKILL.md name')
    if not re.search(rf'(?<![A-Za-z0-9]){re.escape(api["skill_uri"])}(?![A-Za-z0-9])', (path/'SKILL.md').read_text(encoding='utf-8')):
        raise Failure(f'{path}: SKILL.md does not state canonical skill_uri {api["skill_uri"]}')


def validate_suite_text():
    for path in ADS_FILES:
        if not path.exists():
            raise Failure(f'missing normative document: {path.name}')
        text = path.read_text(encoding='utf-8')
        m = re.search(r'^\*\*(?:Suite version|Version):\*\*\s+([^\s]+)', text, re.M)
        if not m or m.group(1) != SUITE_VERSION:
            raise Failure(f'{path.name}: version is not {SUITE_VERSION}')

    # Relative Markdown links must resolve inside the candidate tree.
    link_re = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
    for path in list(ADS_FILES) + [ROOT/'README.md', ROOT/'SOURCE_INDEX.md', ROOT/'language-core'/'README.md', ROOT/'language-core'/'schemas'/'README.md', ROOT/'skill-architecture'/'README.md', ROOT/'skill-architecture'/'schemas'/'README.md', ROOT/'BOOTSTRAP_CONFORMANCE.md', ROOT/'KNOWN_ISSUES.md']:
        text = path.read_text(encoding='utf-8')
        for href in link_re.findall(text):
            if '://' in href or href.startswith('#'):
                continue
            target = (path.parent / href.split('#', 1)[0]).resolve()
            if not target.exists():
                raise Failure(f'{path.name}: broken relative link {href}')

    # Release-candidate self-language checks for known ambiguous constructions.
    prohibited_phrases = {
        'normal invocation': 'representative applicable invocation',
        'an appropriate XSD': 'a schema that completely constrains the required XML artifact',
        'normal released version': 'released version without a pre-release identifier',
        'associated normal version': 'associated version without a pre-release identifier',
        'normal normative use': 'normative use',
        'Each normal release': 'Each released version without a pre-release identifier',
    }
    for path in ADS_FILES:
        text = path.read_text(encoding='utf-8')
        for phrase, replacement in prohibited_phrases.items():
            if phrase in text:
                raise Failure(f'{path.name}: Language & Meaning finding {phrase!r}; use {replacement!r}')



def validate_part_structure():
    # Part I must not depend on Part II.
    for path in sorted((ROOT / 'language-core').glob('LMC-*.md')):
        text = path.read_text(encoding='utf-8')
        if re.search(r'\bSA-0[1-7]\b', text):
            raise Failure(f'{path.name}: Part I must not depend on Part II')
    for path in sorted((ROOT / 'skill-architecture').glob('SA-*.md')):
        text = path.read_text(encoding='utf-8')
        if '**Language baseline:** LMC' not in text:
            raise Failure(f'{path.name}: missing Language baseline metadata')
    boot = ROOT / 'BOOTSTRAP_CONFORMANCE.md'
    if not boot.is_file():
        raise Failure('missing BOOTSTRAP_CONFORMANCE.md')
    print('PASS: Part I is independent of Part II, Part II declares the LMC dependency, and bootstrap evidence exists.')


def selftest_language_conformance(docs, registry):
    schema = next(v for k,v in docs.items() if k.endswith('language-meaning-conformance.schema.json'))
    v = validator(schema, registry)
    good = {
        'artifact_id':'example','artifact_version':'1.0.0','lmc_version':SUITE_VERSION,
        'review_method':'designated-review','review_authority':'project-review',
        'evidence':['review://example'], 'bcp14':'PASS','asd_ste100_issue9':'PASS',
        'project_terminology':'PASS','meaning_control':'PASS','protected_content':'N/A','result':'PASS'
    }
    assert_valid(v, good, 'language conformance valid record')
    bad = dict(good); bad['meaning_control']='FAIL'
    assert_invalid(v, bad, 'language conformance impossible PASS')
    print('PASS: Language & Meaning conformance schema requires designated evidence and rejects contradictory PASS records.')

def main():
    ap = argparse.ArgumentParser(description='Validate the ADS 5 split bundle and optional skill package.')
    ap.add_argument('--skill-package', type=Path, help='Optional canonical skill package directory to validate.')
    ap.add_argument('--conformance-record', type=Path, help='Optional machine-readable conformance record to validate semantically.')
    ap.add_argument('--skill-api', type=Path, help='Optional Skill API to bind to --conformance-record semantic validation.')
    ap.add_argument('--message', type=Path, help='Optional addressed skill message to validate against a resolved target Skill API.')
    ap.add_argument('--target-skill-api', type=Path, help='Resolved target Skill API required with --message.')
    ap.add_argument('--target-schema-dir', type=Path, help='Directory containing the resolved target capability request schema and its JSON Schema dependencies.')
    args = ap.parse_args()
    try:
        docs, ids, registry = load_schemas()
        validate_part_structure()
        selftest_language_conformance(docs, registry)
        validate_refs(docs, ids, registry)
        self_tests(docs, registry)
        validate_suite_text()
        if args.skill_package:
            validate_skill_package(args.skill_package, docs, registry)
        if args.conformance_record:
            record = json.loads(args.conformance_record.read_text(encoding='utf-8'))
            assert_valid(validator(next(v for k,v in docs.items() if k.endswith('skill-conformance-record.schema.json')), registry), record, str(args.conformance_record))
            bound_api = None
            if args.skill_api:
                bound_api = json.loads(args.skill_api.read_text(encoding='utf-8'))
                assert_valid(validator(next(v for k,v in docs.items() if k.endswith('skill-api.schema.json')), registry), bound_api, str(args.skill_api))
                semantic_skill_api(bound_api)
            elif args.skill_package:
                api_path = args.skill_package / 'skill-api.json'
                bound_api = json.loads(api_path.read_text(encoding='utf-8'))
            semantic_conformance_record(record, bound_api)
        elif args.skill_api:
            raise Failure('--skill-api requires --conformance-record')
        if args.message:
            if not args.target_skill_api:
                raise Failure('--message requires --target-skill-api')
            msg = json.loads(args.message.read_text(encoding='utf-8'))
            target_api = json.loads(args.target_skill_api.read_text(encoding='utf-8'))
            assert_valid(validator(next(v for k,v in docs.items() if k.endswith('skill-message-envelope.schema.json')), registry), msg, str(args.message))
            assert_valid(validator(next(v for k,v in docs.items() if k.endswith('skill-api.schema.json')), registry), target_api, str(args.target_skill_api))
            target_registry = extend_registry_from_schema_dir(registry, args.target_schema_dir)
            semantic_message(msg, target_api, target_registry)
        elif args.target_skill_api or args.target_schema_dir:
            raise Failure('--target-skill-api and --target-schema-dir require --message')
    except Failure as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    print(f'PASS: {len(docs)} schemas are valid, uniquely identified, and offline-resolvable.')
    print('PASS: publisher-qualified skill URI syntax and reserved-name tests passed.')
    print('PASS: Skill API identity, outcome-link, message-version, capability payload-contract, and target request-schema payload validation tests passed.')
    print('PASS: conformance-record adversarial self-tests rejected contradictory PASS records and identity mismatches.')
    print(f'PASS: ADS normative documents use suite version {SUITE_VERSION} and required relative links resolve.')
    if args.skill_package:
        print(f'PASS: skill package {args.skill_package} satisfies deterministic package identity checks.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
