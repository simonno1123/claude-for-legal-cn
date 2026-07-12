---
name: ai-tool-handoff
description: >
  Faithful Port compatibility entry for China-law AI/bulk-review handoff.
  Preserves /corporate-legal:ai-tool-handoff root command discoverability and
  delegates to the China-law implementation maintained under phase-2.
---

# /corporate-legal:ai-tool-handoff

This is a Faithful Port compatibility wrapper.

The China-law implementation is maintained at:

`corporate-legal/phase-2/skills/ai-tool-handoff/SKILL.md`

Use that implementation for the full workflow. It covers China Mainland
transaction document review handoff, enterprise AI/document platforms, evidence
chain QA, personal information, important data, trade secret, and confidentiality
approval checks.

This root skill exists to preserve upstream command discoverability. The
`phase-2` path is a historical storage location and does not mean the capability
is lower priority or outside v1 corporate-legal responsibilities.
