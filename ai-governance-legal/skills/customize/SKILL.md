---
name: customize
description: >
  Compatibility placeholder. AI governance customization is merged into /ai-governance-legal:cold-start-interview to keep a single configuration entry.
argument-hint: "[configuration update request]"
---

# /customize

## Compatibility Notice

This command is not a standalone Phase 1 entry.

For China Mainland AI governance localization, all customization fields must be handled through:

`/ai-governance-legal:cold-start-interview`

## Required Behavior

- Do not generate a second AI governance profile.
- Do not create a parallel configuration.
- Ask the user to rerun or update `cold-start-interview` when they need to change:
  - AI system inventory.
  - Public-facing service status.
  - Algorithm recommendation filing status.
  - Generative AI service filing/security assessment status.
  - ICP filing, App filing, ICP License, or MLPS status.
  - Important data or data export settings.
  - Vendor API, training, retention, deletion, or audit settings.
  - Content safety and deep synthesis marking controls.

## Output Format

```markdown
# Configuration Entry Redirect

Please update the AI governance profile through:

`/ai-governance-legal:cold-start-interview`

No standalone customize profile has been created.
```
