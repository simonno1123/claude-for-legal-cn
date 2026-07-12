---
name: policy-monitor
description: >
  Stateful AI policy drift monitor. Sweeps output folders, inventory, registry, vendor reviews, and policy commitments; records Last policy sweep and gaps_found only after human acknowledgment.
argument-hint: "[sweep | acknowledge | direct-query | policy/台账/日志/供应商协议/新使用场景]"
---

# /policy-monitor

## Goal

Detect drift between:

- AI use policy and actual AI use.
- Use-case registry and new triage/assessment outputs.
- AI system inventory and launch/filling evidence.
- Vendor playbook and accepted vendor terms.
- New China AI regulatory requirements and internal controls.

## State

Read:

- `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`
- outputs folder path
- `ai-systems.yaml`
- `use-case-registry.yaml`
- `vendor-ai-playbook.yaml`
- `policy-sweep-log.yaml`

Update `Last policy sweep` and `gaps_found` only after the user confirms results were reviewed/acknowledged.

## Modes

### `sweep`

1. Read last acknowledged sweep date.
2. Scan configured outputs folder for new triage, assessment, vendor review, policy, and matter outputs.
3. Extract approved/conditional/rejected use cases, open remediation, accepted vendor deviations, and new public-service launch facts.
4. Compare against AI policy commitments, registry, inventory, and vendor playbook.
5. Output REQUIRED / ADVISABLE / WATCH gaps.
6. Do not update profile until acknowledgment.

### `direct-query`

If outputs folder is not configured, compare the provided practice or policy issue against profile, registry, and inventory. Do not update `Last policy sweep`.

### `acknowledge`

After user says results are reviewed, update:

- `Last policy sweep: [date]`
- `gaps_found: [N REQUIRED + ADVISABLE]`
- append an entry to `policy-sweep-log.yaml`

## Gap Types

- `REQUIRED`: actual practice conflicts with policy, registry, China launch gate, or vendor standard.
- `ADVISABLE`: policy is silent or should be clarified.
- `WATCH`: facts/rule status are unverified or future-triggered.

## Output Format

```markdown
# AI 治理一致性监控

> **复核提示**
> - **来源：** outputs folder / profile / inventory / registry / vendor playbook
> - **读取范围：** [files and state records]
> - **待判断事项：** [required/advisable/watch]
> - **时效性：** [rules and filings needing verification]
> - **行动前：** profile sweep status updates only after acknowledgment

## 漂移发现
| 类型 | 政策/承诺 | 实际情况 | 缺口 | 动作 |
|---|---|---|---|---|

## Registry Sync
| Use case | Current registry | Finding | Suggested update |
|---|---|---|---|

## Inventory Sync
| System | Current status | Finding | Suggested update |
|---|---|---|---|

## Sweep State
| Field | Value |
|---|---|
| Last acknowledged sweep | |
| gaps_found | |
| Update now? | wait for acknowledgment |
```
