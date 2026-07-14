---
name: matter-workspace
description: >
  管理中国个人信息处理活动、产品功能、供应商、跨境项目或安全事件的本地工作区和完整事项生命周期。
argument-hint: "<status | new | list | switch | update | close | reopen | none> [slug]"
---

# /matter-workspace

## 定位

这是 Phase 1.5 的本地、人工触发数据合规事项工作区。默认按中国个人信息处理活动建档，而不是按 GDPR/CCPA matter、DSAR 或普通法 privilege log 建档。工作区只组织材料、状态和输出，不自动提交、发送、删除、签署或作出合规放行决定。

默认关闭；未启用时继续使用 practice-level 中国数据合规画像。

## 数据位置

```text
~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/
├── index.yaml
├── <slug>/matter.yaml
├── <slug>/history.yaml
├── <slug>/notes.md
├── <slug>/outputs/
└── _archived/<slug>/
```

`index.yaml` 是启用状态和 active matter 的唯一事实源。初始状态必须包含 `version: 1`、`enabled: true`、`active_matter: null`、`cross_matter_context: false` 和 `matters: []`。实现遵循仓库 `references/local-workflow-contract.md`。

## 子命令

- `status`：只读显示启用、active matter 和索引一致性。
- `new <slug>`：采集字段、预览、确认后创建；不自动切换。
- `list`：只读列出活动和归档事项，不读取无关事项正文。
- `switch <slug>`：切换到存在且未归档的事项。
- `update <slug>`：显示 diff，经确认后更新 owner/status/deadline 等。
- `close <slug>`：追加历史并归档，绝不删除。
- `reopen <slug>`：无冲突时确认恢复，不自动切换。
- `none`：清空 active matter，回到 practice-level。

## `new` 必采字段

- 项目/处理活动名称、产品或系统、业务 Owner、法务/隐私/安全复核人。
- 处理目的、个人信息类型、敏感个人信息、未满 14 周岁未成年人信息。
- 数据来源、保存期限、系统清单、第三方、委托处理/共同处理/对外提供关系。
- 跨境路径和机制状态 `[待查证]`。
- PIPIA、权利请求、安全事件、SDK/隐私政策一致性相关输出索引。
- 风险等级、整改动作、deadline、审批和复核状态。
- 保密级别：`standard`、`heightened` 或 `clean_team`。

插件字段写入 `matter.yaml.module_fields`。

## 写入与隔离

1. slug 必须匹配 `^[a-z0-9][a-z0-9-]{0,62}$`，拒绝任何路径穿越。
2. `new/update/close/reopen` 先显示完整变更并取得明确确认。
3. 状态变化追加唯一 `event_id` 到 `history.yaml`；禁止重复事件。
4. 写前解析旧 YAML，写后校验索引/目录一致；失败时保留旧状态并披露失败。
5. 默认不跨事项读取。敏感个人信息、安全事件和 `clean_team` 事项不得因全局设置而隐式跨读。

## 实质技能联动

`use-case-triage`、`pia-generation`、`dpa-review`、`dsar-response`、`reg-gap-analysis` 和 `policy-monitor` 开始前读取画像与索引。已启用但没有 active matter 时，询问继续 practice-level 还是切换；存在 active matter 时只读取该事项授权材料。输出落盘须经确认，并将路径与摘要写入历史。

## 状态输出

```markdown
# 数据合规事项状态

- Enabled: [true/false]
- Active matter: [slug/none]
- Processing activity: [名称]
- Owner: [负责人]
- Status: [active/on_hold/archived]
- Deadline: [日期/none]
- Read scope: [practice-level / active matter files]
```

## 不做

- 不自动对外回复个人权利请求、提交 PIPIA、报告事件或完成数据出境手续。
- 不接入真实隐私管理平台、工单系统或商业数据库。
- 不将本地工作区状态解释为监管批准或律师最终意见。
