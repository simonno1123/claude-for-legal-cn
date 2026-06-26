# 中国并购尽调标准列

默认用于买方尽调批量合同和资料审查。交易文件、尽调清单和行业特点优先于本模板。

```yaml
schema:
  name: "中国并购尽调 - 标准列"
  columns:
    - id: counterparty
      label: "相对方"
      type: verbatim
      prompt: "合同或文件中的相对方名称是什么？按原文摘录。"

    - id: document_type
      label: "文件类型"
      type: classify
      options: [customer_contract, supplier_contract, lease, ip_license, loan, guarantee, employment, distribution, platform, government_subsidy, corporate_record, permit, litigation, other]
      prompt: "该文件属于哪一类？"

    - id: signing_date
      label: "签署日期"
      type: date
      prompt: "文件签署日期是什么？"

    - id: term
      label: "期限"
      type: duration
      prompt: "合同或权利义务期限是什么？"

    - id: change_of_control
      label: "控制权变更"
      type: classify
      options: [not_present, notice_only, consent_required, termination_right, price_adjustment, unclear]
      prompt: "是否约定股权转让、实际控制人变更、合并分立或控制权变更的通知、同意、解除或价格调整？"

    - id: assignment
      label: "合同转让/权利义务转移"
      type: classify
      options: [not_present, freely_transferable, notice_required, consent_required, prohibited, unclear]
      prompt: "合同权利义务是否可以转让？是否需要通知或同意？"

    - id: termination
      label: "终止权"
      type: classify
      options: [not_present, convenience_by_either, target_only, counterparty_only, breach_only, change_of_control_trigger, unclear]
      prompt: "相对方是否可因交易或其他原因提前终止？"

    - id: exclusivity
      label: "排他/限制"
      type: classify
      options: [not_present, exclusivity, non_compete, territory_restriction, minimum_purchase, mfn, unclear]
      prompt: "是否存在排他、竞业限制、区域限制、最低采购或最惠待遇？"

    - id: liability_cap
      label: "责任上限"
      type: currency
      prompt: "是否存在违约责任或赔偿责任上限？金额或计算方式是什么？"

    - id: guarantee_security
      label: "担保/负担"
      type: classify
      options: [not_present, guarantee, mortgage, pledge, lien, retention_of_title, unclear]
      prompt: "是否存在保证、抵押、质押、留置、所有权保留或其他负担？"

    - id: license_permit
      label: "许可/资质"
      type: classify
      options: [not_present, license_required, filing_required, cannot_transfer, renewal_required, unclear]
      prompt: "是否涉及行政许可、备案、强制认证或不可转让资质？"

    - id: personal_info_data
      label: "个人信息/数据"
      type: classify
      options: [not_present, personal_info, sensitive_personal_info, important_data_possible, cross_border_possible, unclear]
      prompt: "文件是否涉及个人信息、敏感个人信息、重要数据或数据出境？"

    - id: labor_social_security
      label: "劳动社保"
      type: classify
      options: [not_present, employee_transfer, unpaid_social_security, dispatch_or_outsourcing, non_compete, dispute, unclear]
      prompt: "是否涉及员工转移、社保公积金、劳务派遣、竞业限制或劳动争议？"

    - id: governing_law_dispute
      label: "法律适用/争议解决"
      type: verbatim
      prompt: "法律适用和争议解决条款原文是什么？"

    - id: action_required
      label: "后续动作"
      type: classify
      options: [none, add_to_closing_checklist, add_to_integration_tracker, request_more_documents, escalate_to_counsel, unclear]
      prompt: "该文件是否产生交割前或交割后行动项？"
```

## 快速首轮列

时间紧时先跑以下字段：相对方、文件类型、签署日期、控制权变更、合同转让、终止权、担保/负担、后续动作。

