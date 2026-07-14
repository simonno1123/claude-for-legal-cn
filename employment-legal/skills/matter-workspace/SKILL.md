---
name: matter-workspace
description: >
  管理中国员工、调查、解除、工时休假、社保或制度事项的 opt-in 本地工作区与保密隔离生命周期。
argument-hint: "<status | new | list | switch | update | close | reopen | none> [slug]"
---

# /matter-workspace

## 定位

这是 Phase 1.5 的本地、人工触发劳动事项工作区。企业单一用工画像继续默认关闭；需要隔离敏感员工、内部调查、解除、群体事项或外部律师客户时可 opt-in 启用。它采用中国劳动用工事项字段，不引入 employment-at-will、美国州法或普通法 privilege 默认框架。

## 数据位置

```text
~/.claude/plugins/config/claude-for-legal/employment-legal/matters/
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
- `list`：列出活动和归档事项，不读取其他员工/事项正文。
- `switch <slug>`：切换到存在且未归档的事项。
- `update <slug>`：显示 diff，经确认更新 owner/status/deadline 等。
- `close <slug>`：追加历史并归档，绝不删除。
- `reopen <slug>`：无冲突时确认恢复，不自动切换。
- `none`：清空 active matter，回到 practice-level。

## `new` 必采字段

- 用人单位/客户、员工或群体标识、工作地、用工主体、Owner、HR/法务/律师复核人。
- 事项类型：招聘、合同、工时休假、社保公积金、调查、处分、解除/终止、手册制度、仲裁诉讼或其他。
- 关键事实、证据目录、工会/民主程序状态、地方口径 `[待查证]`。
- 保护状态、法定程序节点、送达/仲裁时效、deadline、当前状态。
- 保密级别；内部调查、医疗、三期和举报事项默认至少 `heightened`。

插件字段写入 `matter.yaml.module_fields`。不应在标题或 slug 中写入身份证号、手机号、健康信息等敏感个人信息。

## 写入与隔离

1. slug 必须匹配 `^[a-z0-9][a-z0-9-]{0,62}$`；拒绝路径穿越。
2. `new/update/close/reopen` 必须预览并取得明确确认。
3. 状态变化追加唯一历史事件；重复运行不重复写入。
4. 写前解析旧 YAML，写后验证索引/目录一致；失败则保留旧状态并披露。
5. 默认不跨事项读取。员工个人信息、调查材料和 `heightened`/`clean_team` 事项只能按明确授权加载。

## 实质技能联动

劳动技能开始前读取画像与索引。已启用但没有 active matter 时，询问继续 practice-level 还是切换；存在 active matter 时只加载其授权材料。解除、处分、调岗降薪、付款承诺、工会/监管/仲裁/法院文件仍须独立人工确认，事项状态不能替代该门控。

## 状态输出

```markdown
# 劳动事项状态

- Enabled: [true/false]
- Active matter: [slug/none]
- Matter type/location: [类型/地区]
- Owner: [负责人]
- Deadline: [日期/none]
- Status: [active/on_hold/archived]
- Read scope: [practice-level / active matter files]
```

## 不做

- 不自动连接 HRIS、OA、工资、考勤或仲裁法院系统。
- 不自动解除、处分、调岗降薪、付款、发送、备案或提交材料。
- 不把工作区归档解释为劳动争议、证据保全或法定保存义务完成。
