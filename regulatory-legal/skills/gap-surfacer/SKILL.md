---
name: gap-surfacer
description: >
  Reference: 中国监管差距和征求意见跟踪框架。维护 gap/comment tracker 架构、状态、Owner、提醒、关闭、风险接受和人工确认门。
argument-hint: "[台账/筛选条件]"
user-invocable: false
---

# /gap-surfacer

## 定位

这是 `gaps`、`comments`、`policy-diff` 和 `reg-feed-watcher` 共享的状态框架。它不只是输出提醒表，而是规定 tracker 如何维护到关闭。

## Gap Tracker

默认路径：

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml`

最小 schema：

```yaml
gaps:
  - id: GAP-001
    requirement: "[监管要求]"
    regulation: "[文件名称 + 条款/来源]"
    source_level: "[法律/行政法规/部门规章/地方规定/规范性文件/监管问答/执法案例]"
    source_tag: "[官方来源/legal-data/用户提供/待核验]"
    policy_affected: "[制度名称或 new policy needed]"
    gap_type: "partial" # none | partial | full | new-policy | watch | comment-decision
    owner: "[Owner 或 unassigned]"
    opened: "2026-07-04"
    due: "2026-08-01"
    status_verified: true
    status: "open" # open | in-progress | closed | risk-accepted
    notified: false
    evidence: ""
    resolution: ""
    accepted_by: ""
    accepted_rationale: ""
    closed_at: null
```

## Comment Tracker

默认路径：

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml`

最小 schema：

```yaml
comments:
  - id: CMT-001
    document: "[征求意见稿名称]"
    regulator: "[发布机关]"
    level: "[草案/征求意见稿/规范性文件]"
    summary: "[拟调整内容]"
    official_link: "[官方链接]"
    comment_deadline: "2026-08-01"
    detected: "2026-07-04"
    decision: "undecided" # undecided | submit | not-submit | submitted | waived
    owner: "[意见反馈决策 Owner]"
    notified: false
    rationale: ""
    submitted_at: null
    notes: ""
```

## 状态桶

`gaps` 输出必须区分：

- `overdue`：已核验现行有效，且 due 已过。
- `due_soon`：30 日内到期。
- `open`：仍需整改。
- `watch`：草案、征求意见、监管趋势或规则效力未核验。
- `in_progress`
- `closed`
- `risk_accepted`

未核验规则不得进入 overdue，只能进入 `watch` 或 `review needed`。

## 关闭规则

关闭 gap 前必须确认：

- 规则效力和适用性已核验。
- 制度或流程已实际修订、审批、发布或整改证据已留存。
- 关闭人/确认人具备权限。
- resolution 写明证据位置和日期。

`policy-redraft` 生成建议稿后不得自动关闭 gap。

## 风险接受规则

风险接受必须记录：

- `accepted_by`
- `accepted_rationale`
- 接受日期
- 复核触发条件

不得将“暂不处理”写成 closed。

## 提醒规则

没有 Slack/企业消息连接器时，不发送消息，只在报告中列出“需人工提醒”。

如存在可用通知工具：

1. 先预览发送内容和收件人。
2. 等用户明确确认。
3. 再发送。
4. 更新 `notified` 或 `last_reminded`。

不得自动对外发送、自动向监管提交或自动关闭。

## 输出格式

```markdown
# 高风险监管差距提醒

> **复核提示**
> - **来源：** gap-tracker/comment-tracker
> - **读取范围：** [读取条数]
> - **待判断事项：** [未核验、未分配、需升级事项]
> - **时效性：** [按状态分组]
> - **行动前：** 关闭、风险接受、对外提交均需人工确认

## 立即处理
| ID | 差距 | 原因 | 截止 | Owner | 建议 |
|---|---|---|---|---|---|

## 30 日内到期

## 观察项 / 未核验规则

## 证据不足

## 需高管/法务升级
```
