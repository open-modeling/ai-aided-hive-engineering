---
name: conversation-governor
description: >-
  Use whenever an AI agent receives, writes, reviews, or relays a message
  with a person or another agent, in any language.
license: EPL-2.0
metadata:
  display_name: "Conversation Governor"
  skill_uri: "skill:ai-devmode.conversation-governor"
  skill_version: "0.4.0-dev"
  ads_version: "5.0.0-rc.2"
  repository: "https://github.com/open-modeling/ai-aided-hive-engineering"
  lifecycle: "stateless"
  configuration: "non-configurable"
---

# Conversation Governor

## Purpose

Conversation Governor is a skill for clear and consistent communication
between people and AI agents, and between AI agents.

Use it for every message in every supported language.
The skill controls the words, meaning, and form of each message.
The receiving agent does the task through its host.

## Rules

Use the [language rules](references/language-rules.md)
for language standards and approved terms.

Use the [communication rules](references/communication.md)
for message types and decisions.

Use the [hook guidance](references/hooks.md)
for communication checks.

## Maintenance

Use the [operations guide](references/operations.md)
for installation, updates, and package work.

Read the [Skill API](skill-api.json) for the skill contract.
