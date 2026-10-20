# Hook control and coverage

The hook calls the shared checker for declared agent-message transports. It uses exact host tool names and the specified message field. The adapter checks `SendMessage.message`, `send_message.message`, `Task.prompt`, `Agent.prompt`, and explicitly mapped `functions.*` tools. Install only verified host-specific matchers. Tool identifiers may change with host versions.

Task-list tools, including `TaskCreate`, are outside the agent-message boundary. Other tools receive no communication-quality claim.

The message begins with a standalone `[INFORMATION]` or `[DIRECTION]` line. An informational message uses `Statement:` with neutral, descriptive wording. Optional `Source-Quote:` preserves a verbatim source instruction as a JSON string. A directional message uses `Action:`, `Target:`, and `Expected-Result:`. The receiver decides acceptance independently.

The checker applies a conservative lexical tripwire to informational statements. It cannot establish full semantic intent or ASD-STE100 conformance. Model-side interpretation and authorized language review remain necessary.

For Claude Code, register `UserPromptSubmit` and narrowly matched `PreToolUse` command hooks after verifying the installed host version. For Codex, verify supported event names, payload shape, and registration before activation. Neither host has been tested here. Test pre-dispatch denial in the live host before claiming enforcement.
