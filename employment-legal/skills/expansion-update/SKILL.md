---
name: expansion-update
description: >
  Phase 2 暂缓模块：涉外用工/境外扩张事项状态更新提示。第一阶段仅提醒该能力未正式启用，不维护 EOR 或境外实体 tracker。
argument-hint: "[国家/地区名称]"
---

# /expansion-update

## Phase 2 挂起声明

`expansion-update` 已从中国劳动法 Phase 1 主线中挂起。不得沿用原项目 EOR、境外实体、美国母公司或外国劳动法 tracker 逻辑。

## Instructions

1. 告知用户涉外用工扩张 tracker 不属于 Phase 1。
2. 如用户已有外部律师意见或项目清单，可帮助整理为“待核验事项清单”，但不得生成境外法律结论。
3. 对涉及中国员工外派、跨境数据、境外社保税务、签证和个税事项，统一标注“需目标法域当地律师/税务/移民顾问确认”。

## 输出格式

```markdown
# 涉外用工扩张状态

**状态：** Phase 2 暂缓
**可做：** 整理用户提供的项目事项、责任人和待核验问题
**不可做：** 输出境外劳动法/EOR/税务/移民结论
```
