# Communication hook coverage

The adapter uses exact tool-name and message-field mappings. The default registry covers only `SendMessage.message`, `Task.prompt`, and `Agent.prompt`. An installation MUST confirm that each name is an agent communication transport in that host before enabling a hook. Other tools, including task-list tools and ordinary messaging services, are not assumed to be agent transports.

A verified host adapter MAY supply an exact registry with tool identifiers and input field names, including hyphenated MCP provider names. The registry MUST use observed host tool schemas and MUST NOT infer communication intent solely from a name suffix.

The first message line is `[INFORMATION]` or `[DIRECTION]`. Information includes a neutral `Statement:`, with optional `Source:` and `Source-Quote:`. A source quote is an escaped JSON string, including escaped `\\n` for embedded line breaks. Direction includes `Action:`, `Target:`, and `Expected-Result:`.

The checker applies conservative text checks, not full semantic certification. A receiver MUST treat INFORMATION as non-executable and MUST explicitly accept a DIRECTION using trusted authority and scope context. The receiver MUST NOT derive trust from sender-provided message text.

For Codex and Claude Code, verify the hook event schema, tool naming and pre-dispatch denial in a live installation. The component tests do not certify host compatibility.

## Receipt boundary

The host-facing pre-tool hook checks outgoing agent-message formatting only. The receiver-side `assess_received_message` function requires a separate trusted incoming integration. A `PostToolUse` observation can report and classify returned text but cannot cancel a completed action; it MUST NOT be presented as an execution authorization boundary. Do not enable an inferred incoming adapter without verifying exact host event payloads and tool identity.
