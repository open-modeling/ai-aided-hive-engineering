# Conversation Governor dictionary

This dictionary owns concepts specific to communication control. Shared definitions retain their governing ADS meaning. The first normative use of each skill-specific term in a document links to its entry here. An exact protocol token uses code formatting.

## Information

Content that supplies facts, context, observations, evidence, or explanations.

Agent-message token: `[INFORMATION]`.

## Direction

Content that requests an action by a recipient.

Agent-message token: `[DIRECTION]`.

An accepted direction provides the basis for an action.

## Acceptance decision

A recipient's assessment of a direction in its trusted context.

- `ACCEPT`: Authority, scope, conditions, and intent support the action.
- `REJECT`: A conflicting constraint or missing authority prevents acceptance.
- `DEFER`: Clarification, permission, or another prerequisite is needed.

The decision belongs to the current exchange.
