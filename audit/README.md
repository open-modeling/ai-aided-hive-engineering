# Audit records

This directory stores human-readable audit records for specific committed repository states.

Audit records are evidence and rationale, not canonical proposal semantics and not a substitute for Git history or release tags. A record should identify the audited commit or version, the audit scope, checks performed, findings, limitations, and any external or third-party tool execution relevant to that state.

Use audit records for material that helps a human understand why a repository state was accepted, rejected, or left with known issues. Keep reconstruction of repository evolution in Git commits and tags.

Audit records are repository records and are not included in proposal release archives unless the release policy is changed explicitly.

Recommended filename form:

`YYYY-MM-DD_<scope>_<audited-commit>.md`
