# Communication hook controls

The hook checks recognized agent-message transports by host tool name and actual message text. It applies to SendMessage, Task, Agent, TaskCreate, and supported named delegation/message transports.

Each agent message begins with [INFORMATION] or [DIRECTION]. A directional message also supplies Action, Target, and Expected-Result on separate lines. The receiving agent evaluates authority and explicitly accepts, rejects, or defers the direction. The sender's message does not establish acceptance.

PreToolUse rejects unclassified agent messages on recognized transports. Unrecognized tools receive no communication quality guarantee. UserPromptSubmit adds interpretation guidance. Deploy hooks through verified host-specific event registration. Run real host event tests before claiming host enforcement.

The format check is mechanical. It cannot decide whether an information-labeled message conceals a direction, or independently verify sender authority. Apply the skill's semantic review as well.
