---
name: matter-workspace
description: >
  管理中国产品、功能、营销活动或监管事项的本地工作区，支持 opt-in 状态化生命周期和材料隔离。
argument-hint: "<status | new | list | switch | update | close | reopen | none> [slug]"
---

# /matter-workspace

## 定位

这是 Phase 1.5 的本地、人工触发产品法务事项工作区。企业单一产品画像继续默认关闭；需要隔离多个产品、功能、营销活动、监管整改或客户委托时可 opt-in 启用。主审查入口仍是 `/product-legal:launch-review`，本命令只管理上下文和状态。

## 数据位置

```text
~/.claude/plugins/config/claude-for-legal/product-legal/matters/
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

- 产品、功能或活动名称，版本/批次，业务 Owner、产品经理、法务复核人。
- 预计上线日期、评审 deadline、发布渠道、目标用户和地域。
- PRD、界面/交互、营销文案、价格页、协议/隐私政策、数据流、供应商和测试材料索引。
- 消费者权益、平台、电商、广告、个人信息、算法/AI、未成年人、质量/召回等风险标签。
- 当前状态：`active` 或 `on_hold`；保密级别和关联 launch tracker ID。

插件字段写入 `matter.yaml.module_fields`。

## 写入与隔离

1. slug 必须匹配 `^[a-z0-9][a-z0-9-]{0,62}$`；拒绝路径穿越。
2. `new/update/close/reopen` 必须先预览并获得明确确认。
3. 状态变化追加唯一历史事件；重复运行不重复写入。
4. 写前解析旧 YAML，写后验证索引/目录一致；失败则保留旧状态并披露。
5. 默认不跨事项读取；上线材料、监管沟通和 `clean_team` 文件只能在授权范围内加载。

## 实质技能联动

产品技能开始前读取画像与索引。已启用但没有 active matter 时，询问继续 practice-level 还是切换；存在 active matter 时只加载其授权材料。`launch-tracker` 可引用 matter slug，但 tracker 与 matter 各自保留独立历史。输出落盘须经确认。

## 状态输出

```markdown
# 产品事项状态

- Enabled: [true/false]
- Active matter: [slug/none]
- Product/feature: [名称]
- Owner: [负责人]
- Launch date: [日期/none]
- Status: [active/on_hold/archived]
- Read scope: [practice-level / active matter files]
```

## 不做

- 不自动读取飞书、企微、钉钉、WPS、TAPD、Jira 或其他产品系统。
- 不自动放行、阻断、下架、召回、备案、发送或通知。
- 不把事项状态当作监管许可或最终法律意见。
