<!--
CONFIGURATION LOCATION

User-specific configuration for this plugin lives at:

  ~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md

Rules for every skill, command, and agent:
1. Read the user configuration from that path before substantive work.
2. If the file does not exist or still contains [PLACEHOLDER], ask the user to run `/commercial-legal:cold-start-interview`.
3. `cold-start-interview` is the only configuration entry point. Do not maintain a separate `customize` path.
4. This file is the template shipped with the plugin. Do not write user data here.
-->

# 商事合同法务实践画像（中国大陆版）

*Written by `/commercial-legal:cold-start-interview`. If `[PLACEHOLDER]`, run the interview before substantive review.*

## 中国法律本地化规则（强制）

- 默认法域为中华人民共和国大陆地区。港澳台、境外法、外币支付、跨境数据、境外仲裁或境外法院管辖只作为涉外因素提示，不直接输出当地法结论。
- 所有结论均为内部法律审阅初稿，必须由中国执业律师或企业法务复核。
- 不得套用 Delaware、New York、California、UCC、FRCP、US work product、attorney-client privilege、fee shifting、state bar referral 等美国法框架。
- 不得承诺中国大陆存在可对抗司法/监管机关的“证据特权”或“工作成果豁免”。可使用“内部法律分析”“保密文件”“律师工作底稿”，但必须提示该标识本身不当然产生拒绝披露效力。
- 中国法引用必须写明法律全称或已声明缩略名 + 条/款/项；无法确认条文序号时标注 `[法条待查证]`。
- 涉及地方口径、监管口径、司法解释、案例、时效和节假日调休时，标注 `[待确认现行有效性]`。

## 模块定位

本插件服务于中国大陆 B2B 商事合同审查与履约管理，优先覆盖：

- 采购/供应商合同。
- 销售侧框架协议、订单、服务协议和补充协议。
- SaaS、云服务、软件许可、技术服务和数据处理条款。
- NDA、保密协议、商业秘密保护协议。
- 续约提醒、取消通知、涨价提醒和履约台账。
- 合同审批、用印、发票税务、数据合规和业务摘要。

## Company Profile

**公司名称：** [PLACEHOLDER]
**统一社会信用代码：** [PLACEHOLDER]
**公司类型/经营地：** [PLACEHOLDER]
**主要业务：** [PLACEHOLDER]
**合同归口部门：** [PLACEHOLDER]
**默认法域：** 中国大陆
**涉外标签：** [无 / 港澳台 / 境外法 / 境外仲裁 / 跨境数据 / 外汇 / 出口管制]

## Contract Operations

**主要合同类型：** [采购 / 销售 / SaaS / 技术服务 / NDA / 框架协议 / 订单 / 补充协议]
**我方常见身份：** [采购方 / 供应商 / 服务提供方 / 客户 / 双方均有]
**合同系统：** [WPS/金山文档 / 飞书 / 钉钉 / 企业微信 / 泛微 / 蓝凌 / 契约锁 / 法大大 / 上上签 / 本地上传]
**资料来源：** [Local File Mode / MCP connector / 用户粘贴]

## Authority, Seal, and Signature

**签约权限：** [法定代表人 / 授权代表 / 项目负责人 / 其他]
**授权文件：** [授权委托书 / OA审批 / 董事会/股东会决议 / 合同审批单 / 无]
**用印规则：** [合同章 / 公章 / 电子签 / 法定代表人签字 / 授权代表签字]
**用印管理员：** [PLACEHOLDER]
**电子签平台：** [契约锁 / 法大大 / 上上签 / 其他 / 未配置]
**高风险提示：** 签字、盖章、电子签、生效条件和授权链不清时，不得判断合同可签。

## Sales-side Playbook

**适用合同：** [销售框架 / SaaS销售 / 技术服务 / 软件许可 / 订单]
**责任限制：** [PLACEHOLDER]
**违约金：** [PLACEHOLDER]
**付款与发票：** [PLACEHOLDER]
**知识产权：** [PLACEHOLDER]
**数据与个人信息：** [PLACEHOLDER]
**自动续约/涨价：** [PLACEHOLDER]
**争议解决：** [中国大陆法律 + 法院管辖/仲裁机构/仲裁地/语言]
**绝不接受：** [PLACEHOLDER]

## Purchasing-side Playbook

**适用合同：** [采购 / 供应商 / SaaS采购 / 云服务 / 技术服务]
**验收与交付：** [PLACEHOLDER]
**付款与发票：** [PLACEHOLDER]
**服务等级和数据迁移：** [PLACEHOLDER]
**责任限制：** [PLACEHOLDER]
**供应商转委托/分包：** [PLACEHOLDER]
**数据安全与个人信息：** [PLACEHOLDER]
**终止与退出：** [PLACEHOLDER]
**绝不接受：** [PLACEHOLDER]

## NDA and Trade Secret Positions

**NDA 类型：** [单向 / 双向 / 商业秘密专项 / 样品测试 / 技术交流]
**保密信息定义：** [PLACEHOLDER]
**商业秘密保护：** [PLACEHOLDER]
**保密期限：** [PLACEHOLDER]
**返还/销毁：** [PLACEHOLDER]
**残余知识/反向工程：** [PLACEHOLDER]
**不招揽/竞业：** [默认升级人工复核]
**违约金：** [PLACEHOLDER]

## SaaS and Data Positions

**个人信息处理角色：** [委托处理 / 共同处理 / 独立处理 / 共享 / 不涉及]
**数据出境：** [不涉及 / 可能涉及 / 已评估 / 待评估]
**等保/安全要求：** [PLACEHOLDER]
**客户数据训练 AI：** [禁止 / 经书面同意 / 脱敏后可用 / 待评估]
**日志和使用数据：** [PLACEHOLDER]
**数据导出/删除/迁移：** [PLACEHOLDER]
**停服/降级通知：** [PLACEHOLDER]

## Escalation Matrix

| 触发事项 | 默认审批人 | 必要协同 | 说明 |
|---|---|---|---|
| 金额超过阈值 | 法务负责人/总经理 | 财务/业务 | [PLACEHOLDER] |
| 无限责任或高额赔偿 | 法务负责人 | 业务负责人 | 必须升级 |
| 数据出境/重要数据/AI训练 | 数据合规负责人 | 信息安全/法务 | 必须升级 |
| 知识产权转让/独家排他 | 法务负责人 | 业务负责人 | 必须升级 |
| 境外法律/境外仲裁 | 外部律师/法务负责人 | 管理层 | 必须升级 |
| 自动续约或涨价 | 业务负责人 | 财务/采购 | 需预算确认 |
| 用印/授权缺口 | 用印管理员/法务 | 经办部门 | 不得直接签署 |

## Output Rules

每份输出必须包含：

```markdown
> **审阅人备注**
> - **来源：** [用户提供 / Local File Mode / MCP / 模型知识 - 待查证]
> - **读取范围：** [文件/版本/页码/条款]
> - **法域：** 中国大陆 / [涉外因素]
> - **待复核：** [法条、地方口径、监管口径、案例、用印、授权、税务、数据]
> - **后果性动作：** 签署、盖章、发送、付款、解除、续约前需人工确认
```

不得输出“ready to sign”作为最终结论；只能输出“可进入签署流程前的人工复核”或“仍需补正”。

## Local Matter Workflows (Phase 1.5)

- **Enabled:** false（opt-in）
- **Active matter mirror:** none
- **Cross-matter context:** false
**Index:** `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/index.yaml`

`matters/index.yaml` 是 active matter 的唯一事实源；本节只是便于人工阅读的镜像。若二者冲突，停止写入并要求用户选择保留值。事项结构、slug、历史、归档、人工确认和失败恢复遵循 `references/local-workflow-contract.md`。

所有实质技能开始前执行 matter preflight：未启用或索引不存在时使用 practice-level；已启用但无 active matter 时询问继续 practice-level 还是切换；存在 active matter 时只读取其 `matter.yaml` 和用户授权文件。默认禁止跨事项读取，`heightened` 和 `clean_team` 事项不得隐式跨读。

### Local agent state

```yaml
deviation_log: ~/.claude/plugins/config/claude-for-legal/commercial-legal/deviation-log.yaml
playbook_proposals: ~/.claude/plugins/config/claude-for-legal/commercial-legal/playbook-proposals.yaml
playbook_monitor_history: ~/.claude/plugins/config/claude-for-legal/commercial-legal/playbook-monitor-history.yaml
renewal_register: ~/.claude/plugins/config/claude-for-legal/commercial-legal/renewal-register.yaml
renewal_run_history: ~/.claude/plugins/config/claude-for-legal/commercial-legal/renewal-run-history.yaml
pattern_threshold: 5
lookback_months: 12
renewal_windows_days: [30, 60, 90, 180]
```

这些文件只由人工触发的本地工作流读写。没有外部定时任务、自动通知或自动 playbook 变更；任何画像或 playbook 修改必须逐项显示 diff 并取得确认。

## References

- `references/china-commercial-contract-playbook.md`
- `references/china-nda-playbook.md`
- `references/china-saas-data-playbook.md`
- `references/china-dispute-resolution.md`
- `references/china-renewal-deadline-rules.md`
- `references/china-approval-and-seal-policy.md`
- `references/test-cases-cn.md`
