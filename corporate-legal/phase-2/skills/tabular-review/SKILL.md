---
name: tabular-review
description: >
  中国并购批量表格化审查。一份文件一行，一个问题一列，每个单元格都有
  原文引用、位置和复核状态。适用于批量合同、工商资料、诉讼清单、许可
  证照和资产清单审查。
---

# /corporate-legal:tabular-review

## 强制中国法边界

- 默认适用中国大陆并购尽调。
- 输出中的每个判断必须有原文证据；没有原文证据时标记“需人工复核”。
- 表格是审查线索，不是最终法律结论。

## 使用方式

```text
/corporate-legal:tabular-review
/corporate-legal:tabular-review --schema .review-schema.yaml --docs ./vdr/02-contracts/
/corporate-legal:tabular-review --template ma-diligence
```

## 列类型

| 类型 | 返回内容 | 用途 |
|---|---|---|
| `verbatim` | 原文逐字摘录 | 条款文本、主体名称、通知地址 |
| `classify` | 固定选项 | 有/无/不明、需同意/仅通知/无动作 |
| `date` | 日期 | 签署日、到期日、通知期 |
| `duration` | 期限 | 合同期限、提前通知期限 |
| `currency` | 金额 | 交易额、违约金、担保额 |
| `number` | 数字 | 比例、数量、天数 |
| `free` | 简短摘要 | 其他无法结构化字段 |

## 状态

| 状态 | 含义 |
|---|---|
| `answered` | 已找到原文并完成判断 |
| `not_present` | 已读文件，未发现对应内容 |
| `unclear` | 原文存在但含义不清 |
| `needs_review` | 需人工复核，不能作为结论使用 |

## 工作流程

1. 确认文件范围、审查字段、输出格式。
2. 从 `references/ma-diligence-columns.md` 或用户要求生成 schema。
3. 先抽样3-5份文件，确认列定义和分类选项。
4. 批量抽取，每个字段必须记录 `value/state/quote/location`。
5. 逐列规范化，复核异常值和引用一致性。
6. 输出 Markdown、CSV，并在用户需要时生成 Excel/WPS 可用表格。

## 原文引用规则

- `quote` 必须是来源文件中连续、可定位的原文，不得拼接、改写或臆造。
- 如果无法定位原文，状态必须为 `needs_review`。
- 引用位置应包含文件名、页码、章节号、条款号或可回查路径。

## 输出摘要

```markdown
## 批量审查摘要 - [项目代号]

文件数：[N]
字段数：[N]
已回答：[N]
未出现：[N]
含糊：[N]
需人工复核：[N]

### 异常列

- [列名]：超过 [百分比] 的行需人工复核。

### 进入下一步

- 重大风险交给 `diligence-issue-extraction`。
- 同意/通知/换签事项交给 `closing-checklist`。
- 合同清单交给 `material-contract-schedule`。
```

## 表格安全

导出 CSV/Excel/WPS 表格前，对来自合同、资料室或用户粘贴的文本做公式注入防护。以 `=`, `+`, `-`, `@` 或制表/换行开头的单元格，应转义为纯文本。

