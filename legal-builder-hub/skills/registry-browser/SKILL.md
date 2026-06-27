---
name: registry-browser
description: >
  浏览本地和候选技能注册表，按中国法适配状态、风险等级和安装资格筛选技能。
---

# /legal-builder-hub:registry-browser

## 输出字段

| 字段 | 含义 |
|---|---|
| 技能名 | 技能或插件名称 |
| 来源 | 本仓库/内部/外部/商业 |
| 中国化状态 | complete/in_progress/not_started/blocked |
| 风险等级 | high/medium/low |
| 是否可安装 | yes/review_required/no |
| 缺口 | 需要补齐的文件或规则 |

## 筛选规则

- 默认只展示中国法适配完成或可审查的技能。
- 含真实凭证、美国法默认框架或乱码的技能标为 `no`。
- 未提供测试用例的技能标为 `review_required`。

