---
name: cold-start-interview
description: >
  中国争议解决画像访谈。采集企业/律所的案件类型、常用法院与仲裁机构、外部律师、证据来源、保全和执行策略，生成 litigation_profile。
argument-hint: "[--redo | --check-integrations]"
---

# /cold-start-interview

## 强制规则

- 默认适用中国大陆民事诉讼、商事仲裁和执行规则。
- 不询问 US federal/state court、FRCP、FRE、discovery、deposition、subpoena、privilege log、PACER、CourtListener。
- 统一由本技能生成 `litigation_profile`；`customize` 不再作为独立入口。
- 调用 `references/china-litigation-core-rules.md`。

## 访谈维度

1. **使用者身份**
   - 企业法务、争议解决律师、律师助理、业务负责人、其他。
   - 是否有执业律师/外部律师复核机制。

2. **案件类型**
   - 合同、劳动、公司、知识产权、产品/消费者、数据/网络、建设工程、金融借款、执行、商事仲裁。

3. **常用程序路径**
   - 民事诉讼、商事仲裁、劳动仲裁、诉前调解、行政/监管、执行。
   - 常用法院/仲裁委：基层/中级/高院、专门法院、互联网法院、劳动仲裁委、CIETAC/贸仲、地方仲裁委。

4. **地域与管辖**
   - 注册地、主要经营地、合同履行地、不动产所在地、侵权行为地、被告住所地。
   - 常见争议解决条款模板和是否存在“或审或仲”历史风险。

5. **案件台账**
   - 未决案件数量、金额分布、阶段、下一期限、外部律师、保全状态、执行状态。

6. **证据来源**
   - 合同、订单、发票、付款流水、微信/邮件、系统日志、平台订单、工商档案、现场照片、录音录像、证人。
   - 电子数据是否有原始载体、公证、可信时间戳或平台导出记录。

7. **保全和调查令**
   - 是否常用财产保全、证据保全、行为保全。
   - 常见财产线索：银行账户、股权、房产、车辆、知识产权、应收账款、平台账户。
   - 常见调查对象：银行、市场监管、社保、公积金、平台、运营商、不动产登记。

8. **外部律师与汇报**
   - 律所、主办律师、预算、授权范围、汇报频率、审批人。
   - 重大案件是否涉及财务拨备、上市公司披露、董事会/审计委员会汇报。

## 输出

生成 `litigation_profile`：

```yaml
jurisdiction: 中国大陆
user_role:
case_types: []
frequent_forums: []
common_regions: []
outside_counsel:
evidence_sources:
preservation_strategy:
investigation_order_targets:
portfolio_thresholds:
manual_review_gates:
```

## 完成后建议

- 新案件：`/litigation-legal:matter-intake`
- 证据整理：`/litigation-legal:claim-chart` 或 `/litigation-legal:chronology`
- 法院文书/调查令：`/litigation-legal:subpoena-triage`
