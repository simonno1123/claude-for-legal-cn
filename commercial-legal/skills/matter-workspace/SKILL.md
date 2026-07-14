---
name: matter-workspace
description: >
  管理中国商事合同项目、供应商、客户或业务线事项的本地工作区，支持状态、创建、列表、切换、更新、归档、恢复和退出。
argument-hint: "<status | new | list | switch | update | close | reopen | none> [slug]"
---

# /matter-workspace

## 定位

这是 Phase 1.5 的本地、人工触发事项生命周期。企业法务可按合同项目、供应商、客户或业务线建档；外部律师可按客户委托建档。它不是美国诉讼式 matter，也不提供自动签署、发送、续约或外部系统同步。

默认关闭。未启用时继续使用 practice-level 中国商事合同画像，不自动创建目录。

## 数据位置

```text
~/.claude/plugins/config/claude-for-legal/commercial-legal/
├── CLAUDE.md
└── matters/
    ├── index.yaml
    ├── <slug>/matter.yaml
    ├── <slug>/history.yaml
    ├── <slug>/notes.md
    ├── <slug>/outputs/
    └── _archived/<slug>/
```

`matters/index.yaml` 是启用状态和 active matter 的唯一事实源。初始状态必须包含 `version: 1`、`enabled: true`、`active_matter: null`、`cross_matter_context: false` 和 `matters: []`。字段、历史、隔离、人工确认和失败恢复遵循仓库 `references/local-workflow-contract.md`；本文件保留独立运行所需的核心规则。

## 子命令

- `status`：只读显示是否启用、active matter 和索引一致性。
- `new <slug>`：采集字段、显示预览，经确认后创建；不自动切换。
- `list`：只读列出 active/on-hold 与 archived 项目，不读取其他项目正文。
- `switch <slug>`：仅切换到存在且未归档的项目。
- `update <slug>`：显示字段 diff，经确认后更新 owner/status/deadline 等。
- `close <slug>`：经确认后追加历史并移入 `_archived`，不得删除。
- `reopen <slug>`：无 slug 冲突时经确认恢复，不自动切换。
- `none`：将 active matter 设为 `null`，回到 practice-level。

## `new` 必采字段

- 项目名称、业务线、我方身份、相对方、合同类型。
- Owner、法务复核人、状态、开始日期、关键期限。
- 金额、币种、含税口径、期限、续约/取消通知节点。
- 主合同、订单、附件、补充协议、审批、用印、发票和验收材料索引。
- 高风险标签：数据出境、境外争议解决、知识产权转让、自动续约、国企/政府客户。
- 保密级别：`standard`、`heightened` 或 `clean_team`。

插件特有字段写入 `matter.yaml.module_fields`，通用字段不得改名。

## 写入规则

1. slug 必须匹配 `^[a-z0-9][a-z0-9-]{0,62}$`；拒绝路径、`..`、隐藏目录和软链接穿越。
2. `new/update/close/reopen` 必须先显示完整变更并取得明确确认。
3. 每次状态变化向 `history.yaml` 追加唯一 `event_id`；重复运行不得重复记录。
4. 写前解析现有 YAML，写后校验索引、目录和状态一致；失败时保留旧文件或 `.bak`，不得声称成功。
5. 默认 `cross_matter_context: false`。只能加载 active matter；即使开启跨事项上下文，也必须由用户明确指定比较范围。

## 实质技能联动

商事技能开始工作前读取 `CLAUDE.md` 和 `matters/index.yaml`。若已启用但没有 active matter，询问继续使用 practice-level 还是切换；存在 active matter 时只加载该项目的 `matter.yaml` 和用户授权材料。经用户确认写入输出后，才在 `history.yaml` 记录输出路径和摘要。

## 状态输出

```markdown
# 商事合同事项状态

- Enabled: [true/false]
- Active matter: [slug/none]
- Owner: [负责人]
- Status: [active/on_hold/archived]
- Deadline: [日期/none]
- Read scope: [practice-level / active matter files]
- Pending confirmation: [none / proposed write]
```

## 不做

- 不运行利益冲突审查或替代律所冲突系统。
- 不删除事项或执行保留期限销毁。
- 不自动签署、盖章、付款、发送、续约、解除或通知。
- 不连接 CLM、WPS、飞书、钉钉、企业微信或其他 Provider。
