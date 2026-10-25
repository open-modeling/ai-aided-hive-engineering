# Codex collaboration hook feasibility probe (A02)

This opt-in, stateless test distinguishes **tool visibility**, **hook dispatch**, and **plaintext availability**. It does not enable enforcement and it does not register a hook. This file is a diagnostic candidate, not a statement that Codex supports interception of collaboration calls.

## Offline checks

Run `python3 -m unittest discover -s tests -v` inside the skill directory. For an example input:

```sh
printf '%s\n' '{"hook_event_name":"PreToolUse","tool_name":"collaboration.spawn_agent","tool_input":{"message":"Harmless example"}}' |
  python3 scripts/codex_hook_probe.py --inspect
```

The output reports only metadata: `status=candidate`, `message_field=message`, `host_verified=false`, `permission_decision=none`. A candidate registry is not evidence of event dispatch.

## Read-only host test (requires separate opt-in)

1. Determine whether the installed Codex version and its hook documentation support `PreToolUse` for native collaboration calls. Use its actual configuration format; do not copy a Claude Code hook configuration into Codex.
2. If supported, register **only** the read-only `--marker` probe in a disposable Codex session and send a harmless sentinel through each actual collaboration tool. This is a separate opt-in activity and is not performed by installation.
3. Verify the hook ran, collect the delivered `tool_name` and whether the sentinel was visible, and verify that the recipient obtained the message. Record only boolean visibility, exact tool identity, and session/host version; do not store prompt content.
4. A marker present only in agent output does not prove pre-dispatch denial. Actual enforced blocking would need a separate safe test and supported host hook decision contract.
5. If the host cannot expose a pre-dispatch hook, mark `A02.05` / `A02.12` as **not integrated**, rather than declaring a pass.

### Candidate fields (unverified)

- `collaboration.spawn_agent.message`, `collaboration.followup_task.message`, `collaboration.send_message.message`
- Alternate display IDs without periods (`collaborationspawn_agent`, etc.) are candidate aliases only.
- `mcp__codex_tui__send_message_to_thread.prompt` is a separate thread-message surface whose recipient role requires verification.

The tests neither prove the above aliases appear in hook events nor that a host exposes readable plaintext. A message may be opaque or encrypted. Never put an authorization decision in a probe marker.

**Scope:** A01/A02 evidence collection only. No A03/A06 host receiver change and no runtime ledger.
