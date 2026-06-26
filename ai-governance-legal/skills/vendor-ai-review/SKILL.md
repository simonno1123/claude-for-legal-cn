---
name: vendor-ai-review
description: >
  中国第三方 AI 工具、模型 API、云服务和私有化部署协议审查。重点审查中国备案/安全评估、禁训、留存、跨境、内容安全、输出责任和审计。
argument-hint: "[供应商条款/报价单/DPA/安全白皮书/模型说明]"
---

# /vendor-ai-review

## Mandatory Rules

- Default to China Mainland procurement and public-service compliance.
- Do not accept a vendor's global SOC2, ISO, GDPR, or US policy statement as a substitute for China filing, data, personal information, cybersecurity, or content safety obligations.
- If the vendor model/API will be used to provide public-facing AI services in China and required China filing/security assessment evidence is missing, output `STOP / Critical`.

## Required Review Points

- Whether the vendor, model, or service has completed relevant China generative AI service filing/security assessment, algorithm filing, or deep synthesis compliance evidence `[待查证]`.
- Whether inputs, outputs, logs, uploaded files, code, customer data, or prompts are used for model training or service improvement.
- Whether data is stored, accessed, supported, or backed up outside China.
- Whether deletion, isolation, audit log export, data return, and regulatory cooperation are contractually guaranteed.
- Whether real-name authentication, content safety filtering, visible/implicit marking, complaint handling, and incident response are supported where the customer uses the service externally.
- Whether the vendor can support TC260-PG-20241A safety testing materials for public generative AI service review.
- Whether the vendor disclaims all output responsibility while the customer bears all regulatory and third-party liability.
- Whether open-source model licenses, model weights, training data provenance, and generated-code licenses create IP or OSS risk.

## Output Format

```markdown
# 第三方 AI 供应商审查初稿

## 结论
[可进入签署前复核 / 需补正 / 需升级 / 暂不建议推进 / STOP]

## 供应商画像
| 项目 | 内容 |
|---|---|
| 供应商/模型 | |
| 部署方式 | SaaS / API / 私有化 / 开源模型 |
| 使用场景 | |
| 是否面向中国公众 | |
| 是否涉及个人信息/商业秘密/客户数据 | |
| 是否涉及跨境 | |

## 中国法卡点
| 风险等级 | 条款/材料 | 问题 | 中国法卡点 | 修改建议 |
|---|---|---|---|---|

## 必改条款
- [ ] 中国备案/安全评估/算法备案证明或明确不触发说明 `[待查证]`
- [ ] 禁止训练或明确训练授权边界
- [ ] 数据留存、删除、隔离、返还和审计
- [ ] 跨境处理与访问限制
- [ ] 实名制、内容安全、显式/隐式标识支持
- [ ] 24 小时安全事件通知和监管配合
- [ ] 输出责任、侵权责任、违法有害内容责任
- [ ] 终止后的数据删除和模型影响消除

## 红线
[列出必须暂停采购或不得用于对外公众服务的事项。]
```
