---
name: ai-inventory
description: >
  中国 AI 系统台账管理。Persistent inventory over ai-systems.yaml with list/add/edit/classify/show, next-review tracking, China filing/assessment fields, and launch-gate evidence.
argument-hint: "[list | add | edit <id> | classify <id> | show <id>]"
---

# /ai-inventory

## Mandatory Rules

- Do not use EU AI Act provider/deployer/high-risk as the default taxonomy.
- Use China Mainland tags and separate filing/assessment fields.
- Do not collapse algorithm filing and generative AI service filing/security assessment into one field.
- Read and write `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/ai-systems.yaml`.
- If the practice profile is missing, direct the user to `/ai-governance-legal:cold-start-interview` first.

## Storage

Inventory file:

`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/ai-systems.yaml`

Create it on first `add` if missing:

```yaml
systems: []
```

Record schema reference in this repo:

`ai-governance-legal/skills/ai-inventory/references/ai-systems-schema.yaml`

## Commands

### `list`

Read all systems and show a compact table plus counts by status, public-facing, generative AI, algorithm recommendation, deep synthesis, important data, and next review within 30 days.

### `add`

Collect required fields:

- `id`: `sys-NNN`, next available integer.
- `name`, `owner`, `description`, `status`.
- AI type: generative AI, algorithm recommendation, deep synthesis, automated decision, internal assistant, vendor API, open-source model.
- Service scope: internal only, enterprise customer, public-facing China service, overseas service, minors.
- Launch channel: website, App, mini-program, SaaS/API, internal tool, embedded product, offline deployment.
- Data categories: personal information, sensitive PI, children's PI, important data, customer data, commercial secrets, copyrighted content, source code.
- Vendor/model source.
- Filing and infrastructure status.
- `next_review` and review trigger.

Write the record after preview and confirmation.

### `edit <id>`

Read the record, show current values, update only the requested fields, preserve history by adding `last_updated` and `update_reason`.

### `classify <id>`

Classify the China AI governance tracks:

- Algorithm recommendation filing.
- Generative AI service filing/security assessment.
- Deep synthesis marking and real-name authentication.
- ICP filing / App filing.
- ICP License / value-added telecom license.
- MLPS 2.0.
- PIPIA / important data / data export.
- Content safety and 24-hour reporting.
- Human review for consequential outputs.

Write `classification`, `classification_basis`, `gates`, `evidence_gaps`, and `next_review`.

### `show <id>`

Display full record with evidence, open gaps, and recommended next command.

## Record Format

```yaml
systems:
  - id: sys-001
    name: "Customer support LLM"
    owner: "Product / Legal"
    description: "Answers user complaints with human review"
    status: planned
    ai_type: ["generative_ai"]
    service_scope: public_china
    launch_channel: ["app", "mini_program"]
    data_categories: ["personal_information", "customer_data"]
    vendor_or_model: "Vendor/model"
    filing:
      algorithm_recommendation: not_applicable
      generative_ai_service: to_assess
      deep_synthesis: not_applicable
      provincial_cac: to_verify
    infrastructure:
      icp_filing: to_verify
      app_filing: to_verify
      icp_license: to_assess
      mlps: to_assess
    controls:
      real_name_authentication: missing
      visible_marking: not_applicable
      implicit_watermark: not_applicable
      content_safety_stop_filter: to_assess
      human_review: required
    next_review: "2026-08-01"
    review_trigger: "Before public launch"
```

## Output Format

```markdown
# AI 系统台账

> **复核提示**
> - **来源：** ai-systems.yaml / 用户提供 / 企业制度库
> - **读取范围：** [N systems]
> - **待判断事项：** [unclassified / missing evidence / next review]
> - **时效性：** [filing status and standards needing verification]
> - **行动前：** launch gates require human review

| ID | 系统 | AI 类型 | 场景 | 内部/对外 | 数据类型 | 供应商 | 分类 | 下一次复核 |
|---|---|---|---|---|---|---|---|---|

## 缺口
- [ ] 数据来源合法性
- [ ] 供应商禁训/留存/删除/审计条款
- [ ] 算法推荐备案核验
- [ ] 生成式 AI 服务备案/安全评估核验
- [ ] 省级网信办沟通窗口 `[待核验]`
- [ ] 实名制
- [ ] 显式标识与隐式水印
- [ ] 内容安全 Stop-Filter 与 24 小时处置/报告
- [ ] PIPIA/数据出境
- [ ] 人工复核
```
