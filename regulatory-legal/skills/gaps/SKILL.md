---
name: gaps
description: >
  中国监管整改差距台账。支持 list/add/close/accept/show，维护来源、效力层级、整改动作、Owner、期限、状态、复核证据和关闭/风险接受记录。
argument-hint: "[list | add | close GAP-ID | accept GAP-ID | show GAP-ID]"
---

# /gaps

## 目标

维护监管差距直到关闭或风险接受。该技能必须读取并更新 gap tracker，不得只生成一次性表格。

默认路径：

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml`

先加载 `gap-surfacer` reference，沿用其 schema、状态桶和人工确认门。

## Modes

### `list` / 默认

1. 读取 gap tracker。
2. 按 overdue、due soon、open、watch、in progress、closed、risk accepted 分类。
3. 未核验规则不得列为 overdue。
4. 输出 Owner、截止日期、证据缺口和下一步。

### `show GAP-ID`

显示单个 gap 的完整记录、来源、政策、证据、状态历史和下一步。

### `add`

从用户输入或 `policy-diff` 输出新增 gap。必须收集：

- requirement
- regulation/source
- source_level
- policy_affected
- gap_type
- owner
- due
- status_verified
- evidence

如缺少 Owner，写 `unassigned` 并在输出中列为需分配。

### `close GAP-ID`

关闭前必须询问并记录：

- 规则现行有效和适用性是否已核验。
- 整改动作是否已完成。
- 证据位置。
- 审批/确认人。
- 关闭日期。

更新：

```yaml
status: closed
closed_at: "[YYYY-MM-DD]"
resolution: "[完成动作、证据位置、确认人]"
```

不得因为生成了 `policy-redraft` 建议稿就关闭。

### `accept GAP-ID`

风险接受不是关闭。必须记录：

- 接受人。
- 权限依据。
- 理由。
- 复核触发条件。

更新：

```yaml
status: risk-accepted
accepted_by: "[name/role]"
accepted_rationale: "[why]"
resolution: "[review trigger]"
```

## 输出格式

```markdown
# 监管整改差距台账

> **复核提示**
> - **来源：** gap-tracker.yaml
> - **读取范围：** [N 项]
> - **待判断事项：** [未分配/未核验/需升级]
> - **时效性：** [逾期/临期/观察项]
> - **行动前：** 关闭和风险接受需授权确认

## 逾期（仅已核验规则）
| ID | 来源 | 差距 | Owner | 截止 | 状态 | 证据 |
|---|---|---|---|---|---|---|

## 30 日内到期

## Open

## Watch / 未核验

## 最近关闭 / 风险接受
```
