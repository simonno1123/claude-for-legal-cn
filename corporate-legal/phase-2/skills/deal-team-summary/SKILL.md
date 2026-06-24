---
name: deal-team-summary
description: >
  Aggregate diligence findings into a deal team briefing at the right altitude
  for the audience — exec summary for leadership, working summary for the team.
  Use when user says "brief the deal team", "what's the state of diligence",
  "summarize findings for [audience]", "deal update", or on the briefing cadence.
---
<!-- CHINA_LOCALIZATION_START -->
## 中国法域与引用规则（强制）

- 默认法域为中华人民共和国大陆地区法律；不得默认套用美国法、州法、普通法或欧盟法框架。
- 引述中国法律法规时，必须标注法律全称/缩略 + 条文序号（条/款/项）；无法确认时写 `[法条待查证]`，并停止编造式引用。
- 区分法律、行政法规、部门规章、司法解释、地方性法规、规范性文件、指导案例/典型案例的效力层级。
- 涉及地方差异（最低工资、社保、公积金、产假、监管口径、法院管辖等）时，必须标注适用省/市及 `[地方规定 — 待查证]`。
- 输出均为中文法律工作初稿，供执业律师或企业法务审阅；涉及发送、签署、备案、申报、起诉、仲裁、解除劳动合同等后果性动作前，必须设置人工确认门。
<!-- CHINA_LOCALIZATION_END -->


# Deal Team Summary

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/corporate-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

The deal lead doesn't read 200 findings. They read: what's material, what changed since last brief, what needs a decision. This skill compresses the diligence output to the right level for the reader.

## Load context

- `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → Deal team briefing (cadence, format, what the business reads)
- `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md` → deal lead, timeline
- Current findings from diligence-issue-extraction output

## Audience tiers

Per `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` — what the business reads vs. what's for the file. Default tiers:

| Audience | Gets | Doesn't get |
|---|---|---|
| **Board / exec sponsor** | Top 3-5 material issues, price/structure impact, decision items | Category detail, green findings, process |
| **Deal lead** | All reds, all yellows, progress, decision items, next steps | Green finding detail |
| **Working team** | Everything — full findings, status by category, gaps | Nothing withheld |

Ask which tier if not obvious.

## The summary

### Exec tier

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> This brief aggregates privileged diligence findings and inherits the sources' privilege and confidentiality status. Distribution beyond the privilege circle (including to broader business teams) can waive privilege — confirm the distribution list matches the privilege circle before sending.

# [Deal code] — Diligence Brief — [date]

**Status:** [On track / Issues identified / Material findings]
**Coverage:** [X]% of VDR reviewed

## Material findings

[3-5 max. One paragraph each. What it is, why it matters to the deal, what
we're doing about it.]

## Decisions needed

- [ ] [Specific decision — price adjustment, indemnity ask, walk-away trigger]
  — [who decides] — [by when]

## Since last brief

[What changed. New findings, findings resolved, coverage progress.]
```

### Deal lead tier

Same as above plus:

```markdown
## All open issues by category

### 🔴 Red
[Finding title + one-line — link to full finding for detail]

### 🟡 Yellow
[same]

## Progress

| Category | Docs reviewed | Coverage | Reds | Yellows | Status |
|---|---|---|---|---|---|
| [name] | [N/M] | [%] | [N] | [N] | [Complete / In progress / Blocked] |

## Gaps and follow-ups

- [Supplemental request items outstanding]
- [Questions to management]

## Next 72 hours

[What's getting reviewed, what briefings are scheduled]
```

### Working team tier

Full finding detail. Same structure as above but every finding gets its full house-format block, not a one-liner.

## Deltas

If this is a recurring brief (per `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` cadence), lead with what changed:

- New findings since last brief
- Findings upgraded/downgraded in severity
- Findings resolved (consent obtained, issue clarified away)
- Coverage movement

Deal leads care more about movement than state. "Still 12 yellows" is less useful than "2 new yellows, 3 resolved."

## Handoffs

- **From diligence-issue-extraction:** This skill reads the accumulated findings.
- **To closing-checklist:** Any "decision needed" items that resolve into closing conditions go on the checklist.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- It doesn't make the materiality call — it reports the calls that were made at extraction time.
- It doesn't decide what the deal team does about a finding — it surfaces the decision.
- It doesn't distribute the brief — drafts it, human sends.
