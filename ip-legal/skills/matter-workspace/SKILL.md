---
name: matter-workspace
description: >
  管理中国商标、专利、著作权、商业秘密、开源、平台投诉和维权事项的本地工作区与隔离生命周期。
argument-hint: "<status | new | list | switch | update | close | reopen | none> [slug]"
---

# /matter-workspace

## 定位

这是 Phase 1.5 的本地、人工触发知识产权事项工作区。企业统一权利画像默认关闭；需要按权利组合、产品线、平台投诉、FTO、商业秘密或客户委托隔离时可 opt-in 启用。清除、FTO、投诉和侵权分析仍由各实质技能完成。

## 数据位置

```text
~/.claude/plugins/config/claude-for-legal/ip-legal/matters/
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
- `list`：列出活动和归档事项，不读取其他事项正文。
- `switch <slug>`：切换到存在且未归档的事项。
- `update <slug>`：显示 diff，经确认更新 owner/status/deadline 等。
- `close <slug>`：追加历史并归档，绝不删除。
- `reopen <slug>`：无冲突时确认恢复，不自动切换。
- `none`：清空 active matter，回到 practice-level。

## `new` 必采字段

- 权利人/客户、相对方或疑似侵权方、Owner、律师/代理师复核人。
- 事项类型：商标清除/申请/异议/无效/撤三、专利 FTO/无效/侵权、著作权/软著、平台投诉、商业秘密、开源、海关保护或其他。
- 权利编号、类别/技术领域/作品、官方状态 `[待查证]`、关键期限和 deadline。
- 证据、检索结果、官方文件、平台材料、合同和技术材料索引。
- 维权姿态、停止动作门、保密级别；FTO/商业秘密可使用 `clean_team`。

插件字段写入 `matter.yaml.module_fields`。

## 写入与隔离

1. slug 必须匹配 `^[a-z0-9][a-z0-9-]{0,62}$`；拒绝路径穿越。
2. `new/update/close/reopen` 必须预览并取得明确确认。
3. 状态变化追加唯一历史事件；重复运行不重复写入。
4. 写前解析旧 YAML，写后验证索引/目录一致；失败则保留旧状态并披露。
5. 默认不跨事项读取。`heightened`/`clean_team` 事项即使全局允许跨事项，也只能按用户明确范围读取。

## 实质技能联动

IP 技能开始前读取画像与索引。已启用但没有 active matter 时，询问继续 practice-level 还是切换；存在 active matter 时只加载该事项授权材料。任何投诉、反通知、律师函、申请、无效、撤三、海关或诉讼动作仍需独立人工确认。

## 状态输出

```markdown
# 知识产权事项状态

- Enabled: [true/false]
- Active matter: [slug/none]
- Matter type/right: [类型/权利]
- Owner: [负责人]
- Deadline: [日期/none]
- Status: [active/on_hold/archived]
- Read scope: [practice-level / active matter files]
```

## 不做

- 不运行律所利益冲突、官方检索或监控服务。
- 不自动申请、投诉、反通知、发送函件、缴费、续展、放弃或提起程序。
- 不把本地状态解释为官方权利状态或不侵权结论。
