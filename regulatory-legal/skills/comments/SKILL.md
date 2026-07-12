---
name: comments
description: >
  中国征求意见稿反馈决策、截止日期、意见草稿和提交状态管理。读取/更新 comment tracker，支持决定反馈、放弃反馈、记录已提交。
argument-hint: "[list | decide CMT-ID | draft CMT-ID | submit CMT-ID]"
---

# /comments

## 目标

征求意见稿和草案不是现行有效规则，但评论截止日期是真实项目管理风险。本技能负责跟踪是否反馈、谁决策、何时截止、是否已提交。

默认路径：

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml`

加载 `gap-surfacer` reference，沿用 comment tracker schema。

## 强制规则

- 征求意见稿不是现行有效规则。
- 对外提交意见前必须经企业授权审批。
- 不得替用户决定是否反馈。
- 未经确认不得生成“可直接提交”的版本。
- 对外提交后才可标记 `submitted`。

## Modes

### `list` / 默认

按截止日期输出：

- 14 日内到期。
- 30 日内到期。
- undecided。
- submit / not-submit / waived / submitted。

### `decide CMT-ID`

记录反馈决策：

- `submit`
- `not-submit`
- `waived`

必须记录 rationale、决策人、日期。若选择 submit，提示内部审批和提前 5 个工作日完成定稿。

### `draft CMT-ID`

生成内部审批版意见草稿。必须：

- 引用征求意见稿条款。
- 区分企业影响、建议修改、事实依据。
- 标注待核验事实和数据。
- 输出“内部审批版”，不是提交版。

### `submit CMT-ID`

提交状态只能在用户确认已通过授权审批并已提交后记录。更新：

```yaml
decision: submitted
submitted_at: "[YYYY-MM-DD]"
notes: "[提交渠道/文号/经办人]"
```

## 输出格式

```markdown
# 征求意见稿反馈跟踪

> **复核提示**
> - **来源：** comment-tracker.yaml / 官方来源 / 用户提供
> - **读取范围：** [N 项]
> - **待判断事项：** [未决策/临期/待审批]
> - **时效性：** [截止日期]
> - **行动前：** 对外提交需授权审批

## 临期事项
| ID | 文件 | 发布机关 | 截止 | 决策 | Owner |
|---|---|---|---|---|---|

## 意见草稿（内部审批版）

## 提交前确认
- [ ] 主体授权
- [ ] 事实和数据核验
- [ ] 口径一致
- [ ] 提交渠道和截止日期
- [ ] 法务/合规负责人确认
```
