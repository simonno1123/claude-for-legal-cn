---
name: launch-tracker
description: >
  维护中国大陆产品上线事项的本地 YAML 台账，并按人工指定窗口生成待法务审查队列；不读取外部产品系统或自动通知。
argument-hint: "<status | add | import | list | update | queue | close> [launch-id] [--days N]"
---

# /launch-tracker

## 定位

这是 Phase 1.5 的本地、人工触发上线台账。输入只来自用户手工录入或当前会话上传的 PRD、排期表和需求清单。它不连接飞书、企微、钉钉、WPS、TAPD、Jira 或内部系统，也不决定是否上线。

## 数据位置

```text
~/.claude/plugins/config/claude-for-legal/product-legal/
├── launch-tracker.yaml
└── launch-tracker-history.yaml
```

## 台账 Schema

```yaml
version: 1
updated_at: "YYYY-MM-DDTHH:MM:SS+08:00"
entries:
  - launch_id: launch-20260731-example
    title: "产品/功能名称"
    owner: "产品负责人"
    legal_owner: "法务负责人或待指定"
    launch_date: "YYYY-MM-DD"
    review_deadline: "YYYY-MM-DD"
    status: planned
    source: manual
    matter_slug: null
    channels: []
    regions: [china-mainland]
    risk_tags: []
    materials: []
    legal_review:
      status: not_started
      reviewed_at: null
      output_path: null
      decision: null
    notes: []
```

允许的 entry status：`planned`、`needs_review`、`in_review`、`conditional_go`、`blocked`、`cleared`、`launched`、`closed`。`cleared` 仅表示台账记录了人工复核结论，不代表本技能作出批准。

## 子命令

- `status`：只读显示台账是否存在、条目数和最近更新时间。
- `add`：采集单个条目，显示完整 YAML，经确认后写入。
- `import`：解析当前会话上传的表格/文本，先输出拟导入清单和重复项，经确认后批量写入。
- `list`：按状态、Owner 或日期只读列出条目。
- `update <launch-id>`：显示字段 diff，经确认后写入；不得自行把状态改成 `cleared`。
- `queue [--days N]`：生成未来 N 天内或已逾期的人工审查队列，默认 30 天；只读，不改变条目。
- `close <launch-id>`：经确认后设为 `closed`，保留全部历史，不删除。

## ID、去重与历史

- `launch_id` 必须匹配 `^launch-[0-9]{8}-[a-z0-9][a-z0-9-]{0,40}$`。
- 写入前按 `launch_id` 去重；标题规范化后与 launch date 相同的条目作为疑似重复，必须交用户选择 merge 或保留。
- 每次成功写入向 `launch-tracker-history.yaml` 追加唯一事件：`event_id`、时间、action、launch_id、before、after、actor: human-confirmed。
- 写前解析旧 YAML，写后验证 schema 和唯一性；失败时保留旧文件或 `.bak`，并提供待恢复片段。

## Review Queue

队列必须包括：

1. 已逾期且未完成法务复核；
2. 未来窗口内上线且 `legal_review.status` 为 `not_started`/`in_progress`；
3. 含未成年人、敏感个人信息、数据出境、自动化决策、算法推荐、深度合成、生成式 AI、自动续费、特殊广告、平台治理、CCC/质量/召回等风险标签；
4. 缺少 PRD、界面、营销、价格、协议/隐私政策、数据流或检测材料的条目。

输出按 `overdue`、`0-7 days`、`8-14 days`、`15-N days` 分组，并为每项给出 `/product-legal:launch-review` 的建议输入。不得自动运行完整审查。

## 与 Matter Workspace 联动

`matter_slug` 可引用已存在且未归档的 product matter。引用前校验 `matters/index.yaml`；找不到时保留 `null` 并提示。不得因 tracker 条目自动创建、切换或读取 matter。

## 人工确认门

`add/import/update/close` 必须先预览并取得明确确认。对外通知、上线放行、阻断、下架、召回、监管提交和状态变更到 `cleared` 需要独立法务/律师确认。

## 输出

```markdown
# Product Launch Review Queue

| Priority | Launch ID | Product/feature | Launch date | Review status | Risk tags | Missing materials | Owner |
|---|---|---|---|---|---|---|---|

## Suggested next action
- `/product-legal:launch-review` [launch-id and material scope]

## Boundaries
- Local/manual source only
- No external polling or notification
- No automatic launch decision
```
