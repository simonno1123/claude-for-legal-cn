---
name: material-contract-schedule
description: >
  Build the material contracts disclosure schedule from diligence findings,
  applying the purchase agreement's Material Contract definition and formatting
  per the agreement's schedule format. Use when user says "build the contracts
  schedule", "disclosure schedule", "schedule 3.X", "material contracts list",
  or when drafting disclosure schedules.
argument-hint: "[purchase agreement path, or paste the Material Contract definition]"
---
<!-- CHINA_LOCALIZATION_START -->
## 中国法域与引用规则（强制）

- 默认法域为中华人民共和国大陆地区法律；不得默认套用美国法、州法、普通法或欧盟法框架。
- 引述中国法律法规时，必须标注法律全称/缩略 + 条文序号（条/款/项）；无法确认时写 `[法条待查证]`，并停止编造式引用。
- 区分法律、行政法规、部门规章、司法解释、地方性法规、规范性文件、指导案例/典型案例的效力层级。
- 涉及地方差异（最低工资、社保、公积金、产假、监管口径、法院管辖等）时，必须标注适用省/市及 `[地方规定 — 待查证]`。
- 输出均为中文法律工作初稿，供执业律师或企业法务审阅；涉及发送、签署、备案、申报、起诉、仲裁、解除劳动合同等后果性动作前，必须设置人工确认门。
<!-- CHINA_LOCALIZATION_END -->


# /material-contract-schedule

1. Load purchase agreement → Material Contract definition + schedule format.
2. Use the workflow below.
3. Apply definition to diligence findings. Flag edge cases.
4. Format per agreement. Consent overlay feeds closing checklist.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/corporate-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

The purchase agreement has a rep: "Schedule 3.X lists all Material Contracts." This skill builds that schedule from the diligence findings — which contracts are material per the agreement's definition, in the format the agreement requires.

## Load context

- Purchase agreement draft — for the definition of "Material Contract" and the schedule format
- `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → materiality thresholds (may differ from the agreement definition — use the agreement's)
- Diligence findings from diligence-issue-extraction — contract-level data

## Workflow

### Step 1: Get the definition

Pull the definition of "Material Contract" from the purchase agreement — the PA definition controls. Deal-structure differences (stock vs. asset vs. merger) can change how a prong is interpreted, and regulated-industry overlays (healthcare, defense, financial services, telecom, government contracting) can add consent requirements that live outside the PA. If the deal involves any of those overlays, research the applicable anti-assignment or novation rules (for example, federal contracts, government contracting novation, sector-specific consent statutes) and cite the controlling rule.

Common prong categories to look for in the PA definition — these are not a substitute for reading the PA, and the list the PA uses controls:

- Dollar-value threshold (annual or aggregate)
- Term length
- Change-of-control or anti-assignment provision
- Exclusivity or non-compete
- Top N customer or supplier contracts
- Real property leases
- IP licenses (in-bound and out-bound)
- Related-party agreements
- Government contracts
- Contracts outside the ordinary course

The PA's definition is the test. Apply it mechanically — every contract that meets any prong in the PA's definition goes on the schedule.

### Step 2: Apply the definition to the findings

For each contract reviewed in diligence:

| Contract | Meets prong(s) | Include |
|---|---|---|
| [name] | [$X+ annual value; CoC provision] | Yes |
| [name] | [none] | No |

**Edge cases to flag for human decision:**
- Contract is $X-1 (just under threshold) but important to the business
- Contract meets a prong but is being terminated anyway
- Oral agreements or side letters that may or may not count

### Step 3: Gather schedule data

For each included contract, the schedule typically needs:

| Field | Source |
|---|---|
| Counterparty name | Contract |
| Contract title/type | Contract |
| Date | Contract |
| Term / expiration | Contract |
| Annual/total value | Contract or management data |
| Which materiality prong it meets | Step 2 analysis |
| Consent required for the deal | Diligence finding |
| VDR reference | Diligence inventory |

Pull from existing diligence extractions. If a field is missing, flag it — don't guess.

### Step 4: Format per the agreement

Disclosure schedules have a format — usually a numbered list or a table, sometimes with sub-parts by contract type. Match the format of the other schedules in the draft agreement.

```markdown
## Schedule 3.[X] — Material Contracts

The following are the Material Contracts as of the date hereof:

### (a) Customer Contracts

1. [Agreement Title], dated [date], between [Target] and [Counterparty].
   [Brief description if the format calls for it.]
   [VDR: path]

2. [...]

### (b) Supplier Contracts

[...]

### (c) Real Property

[...]

[etc. — sub-parts per the agreement's definition structure]
```

### Step 5: Consent tracking overlay

Separately (not in the schedule itself — this is internal), track which scheduled contracts require consent.

> The consent overlay and any pre-delivery working draft of the schedule are derived from privileged diligence materials and inherit their privilege and confidentiality status — distribution beyond the privilege circle can waive privilege. The schedule itself, once delivered as an exhibit to the executed PA, is a deal document and is not privileged; strip any internal annotations before delivery.


| Schedule # | Counterparty | Consent required | Status | Owner | Due |
|---|---|---|---|---|---|
| 3.X(a)(1) | [name] | Yes — CoC §12.2 | Requested | [name] | [date] |

This feeds closing-checklist.

## Cross-check

Before delivering:

- Every contract that met a prong is on the schedule (completeness)
- No contract is on the schedule that doesn't meet a prong (no over-disclosure — it's a rep, not a data dump)
- Schedule is consistent with the other reps (a contract on Schedule 3.X that creates a lien should also be on the liens schedule)
- Every entry has a VDR cite so buyer's counsel can find the underlying doc

## Handoffs

- **From diligence-issue-extraction:** Contract-level findings are the input.
- **To closing-checklist:** Consent items go on the checklist.

## What this skill does not do

- It doesn't decide the materiality definition — that's in the purchase agreement.
- It doesn't obtain consents — it tracks which ones are needed.
- It doesn't draft the rep — it populates the schedule the rep references.
