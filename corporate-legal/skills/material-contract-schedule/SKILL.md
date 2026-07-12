---
name: material-contract-schedule
description: >
  Faithful Port compatibility entry for China-law material contract schedule
  generation. Preserves /corporate-legal:material-contract-schedule root command
  discoverability and delegates to the China-law implementation maintained under
  phase-2.
argument-hint: "[交易文件路径，或粘贴重大合同定义]"
---

# /corporate-legal:material-contract-schedule

This is a Faithful Port compatibility wrapper.

The China-law implementation is maintained at:

`corporate-legal/phase-2/skills/material-contract-schedule/SKILL.md`

Use that implementation for the full workflow. It covers China Mainland material
contract disclosure schedules, change-of-control, assignment, termination,
third-party consent, guarantee, pledge, financing, lease, IP license, government
subsidy, and related-party contract review.

This root skill exists to preserve upstream command discoverability. The
`phase-2` path is a historical storage location and does not mean the capability
is lower priority or outside v1 corporate-legal responsibilities.
