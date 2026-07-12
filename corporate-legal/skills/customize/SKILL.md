---
name: customize
description: >
  Faithful Port compatibility entry for China-law corporate profile
  customization. Preserves /corporate-legal:customize root command
  discoverability and maps customization to corporate profile updates.
argument-hint: "[公司画像/治理结构/出资/股权/登记/并购口径]"
---

# /corporate-legal:customize

This is a Faithful Port compatibility entry, not a new v2 feature.

## Responsibility Mapping

Upstream `customize` updates the corporate practice profile without forcing a
full reinstall or unrelated workflow change.

In the China-law port, that responsibility maps to updating the China corporate
profile at:

`~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`

The profile controls company type, registration place, articles, governance
structure, capital contribution, equity registration, state-owned/foreign
investment/listed-company overlays, M&A settings, and entity compliance posture.

## Instructions

1. Read the existing corporate profile if present.
2. If no profile exists, or it still contains `[PLACEHOLDER]`, direct the user
   to run `/corporate-legal:cold-start-interview`.
3. If the user wants a full profile refresh, direct them to run
   `/corporate-legal:cold-start-interview --redo`.
4. If the user wants to update one section, collect the changed facts and show a
   proposed patch to the relevant profile section for user confirmation.
5. Do not create a second configuration source.
6. Do not introduce Delaware, U.S. state-law, SEC, or common-law corporate
   defaults. Foreign-law references may appear only as negative constraints or
   comparative warnings.

## Output

```markdown
# corporate-legal profile update

**Mapped responsibility:** upstream `customize` -> China-law corporate profile update
**Profile path:** `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`

## Proposed update
[Show the section-level update here.]

## Confirmation gate
Confirm before writing profile changes.
```
