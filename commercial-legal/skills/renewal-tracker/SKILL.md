---
name: renewal-tracker
description: >
  中国商事合同续约、取消通知、涨价和送达期限的本地 YAML 台账；支持人工录入、导入、更新、查询、关闭和历史留痕。
argument-hint: "<status | add | import | list | update | due | close> [renewal-id] [--next 30|60|90|180|365]"
---

# /renewal-tracker

## 强制规则

- 调用 `references/china-renewal-deadline-rules.md`。
- 关注“送达期限”，不是只关注“发送日期”。
- 中国法定节假日、调休工作日和具体年度安排必须标注 `[待查证]`。
- 若通知需盖章、纸质件、EMS、系统确认或对方签收，必须前置缓冲。
- 本地台账位于 `~/.claude/plugins/config/claude-for-legal/commercial-legal/renewal-register.yaml`；不得写入插件目录。
- 所有写操作先显示 diff 并取得人工确认；不得自动发送通知或决定续约。

## 台账 Schema

```yaml
version: 1
updated_at: "ISO datetime"
entries:
  - renewal_id: "renewal-counterparty-contract-2027"
    contract_name: "合同名称"
    counterparty: "相对方"
    owner: "负责人"
    status: active
    start_date: "YYYY-MM-DD"
    end_date: "YYYY-MM-DD"
    auto_renewal: true
    renewal_term: "12 months"
    cancel_notice_deadline: "YYYY-MM-DD"
    price_notice_deadline: null
    notice_method: "盖章纸质件/EMS/邮箱/系统"
    approval_lead_days: 15
    matter_slug: null
    source_files: []
    notes: []
```

允许状态：`active`、`decision_pending`、`renewing`、`cancelling`、`expired`、`closed`。

## 子命令

- `status`：只读显示台账状态、条目数和最近更新时间。
- `add`：采集单条记录，预览确认后写入。
- `import`：解析用户本次上传的合同/台账，列出拟新增、疑似重复和缺失字段，确认后写入。
- `list`：按 owner、status、相对方或日期筛选。
- `update <renewal-id>`：显示字段 diff，确认后更新。
- `due --next N`：只读生成 N 天窗口报告；默认使用画像中的窗口。
- `close <renewal-id>`：确认后设为 `closed`，保留记录，不删除。

`renewal_id` 必须匹配 `^renewal-[a-z0-9][a-z0-9-]{0,62}$`。写入前按 ID 去重；规范化相对方、合同名称和 end date 相同的条目作为疑似重复交用户判断。每次写入向 `renewal-run-history.yaml` 追加唯一事件。写前解析旧 YAML，写后验证 schema；失败时保留旧状态或 `.bak` 并披露。

## 必提字段

- 合同名称、相对方、我方身份、金额、币种、含税/不含税。
- 起止日期、自动续约期限、取消通知期限、涨价通知期限。
- 通知方式、通知地址/邮箱/系统、收件人、送达认定规则。
- 是否需要盖章件或授权签字。
- 预算归口、经办部门、法务/财务/采购审批人。

## 输出格式

```markdown
# 续约与通知期限台账

> **审阅人备注**
> - **来源：** [合同/台账]
> - **法域：** 中国大陆 / [涉外因素]
> - **待复核：** [节假日调休/送达方式/用印要求]

| 风险 | 合同 | 到期/续约 | 通知送达截止 | 建议内部启动日 | 送达方式 | 负责人 |
|---|---|---|---|---|---|---|

## 高风险提醒
- [ ] 自动续约
- [ ] 自动涨价
- [ ] 需盖章通知
- [ ] 预算/采购审批
```

## Matter 联动与边界

`matter_slug` 只可引用存在且未归档的 commercial matter；引用无效时保留 `null`。不得因续约条目自动创建或切换 matter。法定节假日、送达认定、合同效力和解除权仍须法务/律师复核。
