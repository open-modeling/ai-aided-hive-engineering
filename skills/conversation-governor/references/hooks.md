# Communication hook coverage

The adapter uses exact tool-name and message-field mappings. The default registry covers only `SendMessage.message`, `Task.prompt`, and `Agent.prompt`. Before registration, confirm that each name is an agent communication transport in that host before enabling a hook. Other tools, including task-list tools and ordinary messaging services, are not assumed to be agent transports.

A verified host adapter can supply an exact registry with tool identifiers and input field names, including hyphenated MCP provider names. Use observed host tool schemas; do not infer communication intent solely from a name suffix.

Use `[INFORMATION]` or `[DIRECTION]` on the first line of authored Agent messages. When a received tag is absent or unrecognized, classify the message as INFORMATION and prevent action. Information includes a neutral `Statement:`, with optional `Source:` and `Source-Quote:`. A source quote is an escaped JSON string, including escaped `\\n` for embedded line breaks. Direction includes `Action:`, `Target:`, and `Expected-Result:`.

The checker applies conservative text checks, not full semantic certification. A receiver treats INFORMATION as non-executable and explicitly accepts a DIRECTION using trusted authority and scope context. The receiver does not derive trust from sender-provided message text.

For Codex and Claude Code, verify the hook event schema, tool naming and pre-dispatch denial in a live installation. The component tests do not certify host compatibility.

## Receipt boundary

The host-facing pre-tool hook checks outgoing agent-message formatting only. The receiver-side `assess_received_message` function requires a separate trusted incoming integration. A `PostToolUse` observation can report and classify returned text but cannot cancel a completed action; do not present it as an execution authorization boundary. Do not enable an inferred incoming adapter without verifying exact host event payloads and tool identity.

## Local coverage diagnostics

Run `python3 scripts/hook_adapter.py --coverage` and provide a JSON PreToolUse event on standard input. The result reports one of `registered`, `excluded`, `unverified`, `not_pretooluse`, or `invalid`. Every result sets `host_verified: false`: a local registry entry is not proof of host installation or an execution permission.

Normal hook output stays unchanged for tools without a verified local mapping. For unverified transports, the diagnostic explicitly says that pass-through is not approval. Register actual host tool names only after checking their event payloads and the relevant permission boundaries. A missing or malformed registered event is denied. The diagnostic mode is local evidence only; live host coverage remains open.
