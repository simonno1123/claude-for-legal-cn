---
name: review-proposals
description: >
  审阅本地 playbook-proposals.yaml 中的中国商事合同更新建议，逐项接受、拒绝、编辑或延后，并保留人工决策历史。
argument-hint: "<list | review | history> [proposal-id]"
---

# /review-proposals

## 强制规则

- 不得仅因某条款“签过多次”就建议常态化接受。
- 必须区分：标准立场、可接受 fallback、需审批例外、禁止项。
- 涉及责任上限、数据出境、AI 训练、知识产权转让、境外仲裁、自动续约等必须升级。
- 提案来源为 `~/.claude/plugins/config/claude-for-legal/commercial-legal/playbook-proposals.yaml`。
- 任何画像/playbook 修改必须逐项显示精确 diff 并二次确认；不得批量静默采纳。

## 工作流

1. 读取提案文件和用户级 `CLAUDE.md`；任一文件无法解析时停止，不覆盖。
2. `list` 只读列出 pending/deferred 提案及样本数。
3. `review <proposal-id>` 展示 pattern、来源 deal IDs、当前立场、建议立场、风险和数据缺口。
4. 要求用户选择：`accept`、`reject`、`edit`、`defer`。
5. `accept/edit` 时显示 user-level `CLAUDE.md` 的精确 diff，再次确认后才写入。
6. `reject/defer` 不修改画像；记录决定、理由和时间。
7. 将提案状态更新为 `accepted/rejected/deferred/edited`，并向 `playbook-monitor-history.yaml` 追加唯一决策事件。
8. 写前备份并解析旧 YAML/Markdown，写后验证；失败时保留旧状态并披露。

只有用户级配置可写。仓库模板 `commercial-legal/CLAUDE.md` 只作为缺失配置时的只读参考，绝不由本技能修改。

## 输出格式

```markdown
# Playbook 更新建议审阅

| 建议 | 来源 | 类型 | 风险 | 是否采纳 | 理由 |
|---|---|---|---|---|---|

## 建议写入
- 标准立场：
- fallback：
- 禁止项：
- 审批例外：
```

## 不做

- 不自动接受达到阈值的提案。
- 不把一事一批、领导特批或战略客户例外变成默认立场。
- 不发送通知，不连接外部系统，不自动修改合同模板。
