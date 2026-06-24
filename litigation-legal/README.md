# Litigation Legal (中国民商事诉讼/仲裁定制版)

本插件面向中国大陆企业法务、争议解决律师和案件管理团队，提供民商事诉讼、商事仲裁、劳动争议、知识产权诉讼、执行和外部律师协作的结构化工作流。

> 专业提示：本插件输出均为法律工作初稿。起诉、仲裁申请、答辩、举证、质证、保全、调查令申请、和解、执行申请、对外发函等后果性动作，必须由具备相应执业资格的律师或企业法务复核确认。

## 中国化定位

本版本彻底停止默认使用 discovery、subpoena、deposition、privilege log、FRCP/FRE、PACER、CourtListener 等美国诉讼程序框架。默认适用中华人民共和国大陆地区现行民事诉讼、仲裁、执行和证据规则。

## 核心命令矩阵

| 命令 | 中国法语义 |
|---|---|
| `/litigation-legal:cold-start-interview` | 中国争议解决画像访谈：主体、常见纠纷、常用法院/仲裁委、外部律师、案件台账、保全和执行策略 |
| `/litigation-legal:matter-intake` | 收案与立案审查：管辖、诉讼时效、主体、仲裁条款、诉请、证据、保全和执行可行性 |
| `/litigation-legal:claim-chart` | 诉请/抗辩/证据对照表：诉讼请求、请求权基础、待证事实、证据编号、三性和证明目的 |
| `/litigation-legal:chronology` | 案件事实时间线：按时间、证据编号、争议焦点和证明目的整理大事记 |
| `/litigation-legal:court-order-triage` | 法院文书、协助执行通知、律师调查令、仲裁程序令、监管函甄别 |
| `/litigation-legal:witness-trial-prep` | 庭审、当事人陈述、证人出庭、鉴定人/专家辅助人发问准备 |
| `/litigation-legal:confidential-evidence-review` | 证据保密、商业秘密、个人信息、国家秘密和涉外数据出境审查 |
| `/litigation-legal:evidence-preservation` | 证据留存、电子数据固化、证据保全申请和内部数据冻结 |
| `/litigation-legal:subpoena-triage` | 兼容旧命令，已映射到法院文书/调查令甄别 |
| `/litigation-legal:deposition-prep` | 兼容旧命令，已映射到庭审与证人准备 |
| `/litigation-legal:privilege-log-review` | 兼容旧命令，已映射到证据保密与脱敏审查 |
| `/litigation-legal:legal-hold` | 兼容旧命令，已映射到证据留存/保全 |
| `/litigation-legal:demand-intake` | 律师函/催告函/解除通知/索赔函起草前信息收集 |
| `/litigation-legal:demand-draft` | 中国法语境下律师函、催告函、索赔函、保全提示函初稿 |
| `/litigation-legal:demand-received` | 收到律师函/催告函/仲裁通知/起诉材料后的应对分流 |
| `/litigation-legal:matter-briefing` | 案件汇报：事实、程序、风险、费用、保全、执行、和解窗口 |
| `/litigation-legal:portfolio-status` | 未决案件组合盘点：金额、阶段、期限、保全、执行、拨备/披露口径 |
| `/litigation-legal:oc-status` | 外部律师/仲裁代理/承办法官或仲裁员事项跟进清单 |

## 中国法核心卡点

- 管辖：级别管辖、地域管辖、专属管辖、协议管辖、仲裁条款效力、或审或仲无效风险。
- 诉讼时效：三年普通诉讼时效、最长保护期、时效中止/中断、催收和承诺还款证据。
- 立案材料：原被告主体、授权委托、证据目录、诉讼请求、事实与理由、送达地址确认。
- 举证期限：法院举证通知书、仲裁庭程序令、逾期举证后果、补充证据和证据交换节点。
- 证据三性：真实性、合法性、关联性、证明目的、反驳意见、电子数据真实性。
- 调查令：银行流水、工商内档、微信/支付宝实名信息、平台交易记录、社保公积金、房产/车辆信息。
- 保全：财产保全、证据保全、行为保全、担保金额、财产线索、错误保全赔偿风险。
- 仲裁保全：向仲裁委员会提交申请，由仲裁委员会转交有管辖权人民法院；不得默认直接向法院申请仲裁保全。
- 庭审：法庭调查、举证质证、法庭辩论、最后陈述、证人出庭、鉴定人/专家辅助人发问。
- 仲裁：仲裁协议效力、仲裁机构名称、仲裁地、保全衔接、裁决撤销/不予执行风险。
- 执行：申请执行期限两年、财产线索、限高、失信、终本、执行异议和执行和解。

## 测试与验收

中国法回归测试位于 `references/test-cases-cn.md`。任何技能重写后，应至少用其中 6 个高压用例人工回归，确认不会输出美国法概念。
