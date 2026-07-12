---
name: tabular-review
description: >
  Faithful Port compatibility entry for China-law tabular batch review.
  Preserves /corporate-legal:tabular-review root command discoverability and
  delegates to the China-law implementation maintained under phase-2.
argument-hint: "[--schema .review-schema.yaml --docs ./vdr/02-contracts/ | --template ma-diligence]"
---

# /corporate-legal:tabular-review

This is a Faithful Port compatibility wrapper.

The China-law implementation is maintained at:

`corporate-legal/phase-2/skills/tabular-review/SKILL.md`

Use that implementation for the full workflow. It covers China Mainland M&A
batch review with cited cells, typed columns, original-text evidence, review
states, CSV/Excel/WPS-ready outputs, and formula-injection defenses.

This root skill exists to preserve upstream command discoverability. The
`phase-2` path is a historical storage location and does not mean the capability
is lower priority or outside v1 corporate-legal responsibilities.
