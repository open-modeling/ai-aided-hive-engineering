# Host communication checks

Supported adapters supplement the message procedure with machine-checkable validation.

1. Identify actual host events and inspect the event's message fields before registration.
2. Register only verified communication transports and explicit message-field mappings.
3. Apply the message checker to fields available at a supported pre-dispatch boundary.
4. Verify the communication classification and required direction fields.
5. Use receiver-side verification with trusted authority and scope context for acceptance decisions.
6. Provide corrective feedback for a detected issue.
7. Report event coverage and its verification level.

A post-dispatch observation provides diagnostics. An opaque message field produces a coverage limitation rather than a content-validation result.

Run `python3 scripts/hook_adapter.py --coverage` for local coverage diagnostics. Use `scripts/codex_hook_probe.py` for the optional synthetic Codex event probe. Actual host execution establishes host-specific coverage.
