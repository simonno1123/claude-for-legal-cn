---
name: ai-inventory
description: >
  中国 AI 系统台账管理。记录生成式 AI、算法推荐、深度合成、内部工具、供应商模型、数据来源、实名制、双轨备案、安全评估、标识义务和责任人。
argument-hint: "[list | add | edit | classify | show] [系统说明]"
---

# /ai-inventory

## Mandatory Rules

- Do not use EU AI Act provider/deployer/high-risk as the default taxonomy.
- Use China Mainland tags and separate filing/assessment fields.
- Do not collapse algorithm filing and generative AI service filing/security assessment into one field.

## Required Inventory Fields

- AI type: generative AI, algorithm recommendation, deep synthesis, automated decision, internal assistant, vendor API, open-source model.
- Service scope: internal only, enterprise customer, public-facing China service, overseas service, minors.
- Data: training data, fine-tuning data, prompts, outputs, logs, personal information, sensitive personal information, commercial secrets, copyrighted materials.
- Filing/assessment:
  - Algorithm recommendation filing.
  - Generative AI service filing/security assessment.
  - Provincial CAC communication.
  - PIPIA/data export.
- Service controls:
  - Real-name authentication.
  - Visible marking.
  - Implicit watermark/metadata.
  - Content safety stop-filter and 24-hour report process.
  - Human review.

## Output Format

```markdown
# AI 系统台账

| 系统 | AI 类型 | 场景 | 内部/对外 | 数据类型 | 供应商 | 实名制 | 算法备案 | 生成式 AI 备案/安全评估 | 深度合成标识 | 下一步 |
|---|---|---|---|---|---|---|---|---|---|---|

## 缺口
- [ ] 数据来源合法性
- [ ] 供应商禁训/留存/删除/审计条款
- [ ] 算法推荐备案核验
- [ ] 生成式 AI 服务备案/安全评估核验
- [ ] 省级网信办沟通窗口 `[待查证]`
- [ ] 实名制
- [ ] 显式标识与隐式水印
- [ ] 内容安全 Stop-Filter 与 24 小时处置/报告
- [ ] PIPIA/数据出境
- [ ] 人工复核
```
