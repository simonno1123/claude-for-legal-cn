---
name: vendor-ai-review
description: >
  中国第三方 AI 工具、模型 API、云服务和私有化部署协议审查。Compares vendor terms against configured playbook, supports provisional review, AI addendum gap checks, redline proposals, and policy consistency diff.
argument-hint: "[供应商条款/报价单/DPA/安全白皮书/模型说明]"
---

# /vendor-ai-review

## Mandatory Rules

- Default to China Mainland procurement and public-service compliance.
- Do not accept a vendor's global SOC2, ISO, GDPR, or US policy statement as a substitute for China filing, data, personal information, cybersecurity, or content safety obligations.
- If the vendor model/API will be used to provide public-facing AI services in China and required China filing/security assessment evidence is missing, output `STOP / Critical`.
- Read the configured vendor playbook before comparing positions.

## State

Read:

- `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`
- `vendor-ai-playbook.yaml`
- `use-case-registry.yaml`
- `ai-systems.yaml`

If the playbook is missing or incomplete, offer:

- Run `/ai-governance-legal:cold-start-interview`.
- Continue in `provisional` mode with generic China AI buyer positions and mark all findings `[PROVISIONAL]`.

## Required Review Points

- China generative AI service filing/security assessment, algorithm filing, or deep synthesis compliance evidence `[待核验]`.
- Whether inputs, outputs, logs, uploaded files, code, customer data, or prompts are used for model training or service improvement.
- Data storage, support, access, backup, and cross-border transfer.
- Deletion, isolation, audit log export, data return, and regulatory cooperation.
- Real-name authentication, content safety filtering, visible/implicit marking, complaint handling, and incident response support.
- TC260-PG-20241A safety testing materials for public generative AI service review.
- Output responsibility, indemnity, liability cap, disclaimers, and regulatory cooperation.
- Open-source model licenses, model weights, training data provenance, generated-code licenses, OSS/IP risk.

## Workflow

1. Confirm document type: AI addendum, service terms, DPA, AUP, security whitepaper, model card, order form, or combination.
2. If only AUP/security whitepaper is provided, ask for terms governing data use, training, retention, deletion, liability, and model changes.
3. Extract vendor positions term by term.
4. Compare to configured playbook:
   - standard
   - acceptable fallback
   - never / red line
5. Check AI addendum gap if a DPA exists but no AI-specific terms.
6. Compare vendor terms to enterprise AI policy and use-case registry.
7. Propose redlines using the smallest practical edit.
8. Before recommending signature or production use, require legal/compliance approval.

## Output Format

```markdown
# 第三方 AI 供应商审查初稿

> **复核提示**
> - **来源：** vendor documents / playbook / inventory / registry
> - **读取范围：** [contract sections and missing docs]
> - **待判断事项：** [red lines / fallback acceptance / missing addendum]
> - **时效性：** [filing or regulatory evidence needing verification]
> - **行动前：** no signing or public-service deployment without authorized review

## 结论
[可进入签署前复核 / 需补正 / 需升级 / 暂不建议推进 / STOP]

## Playbook Comparison
| Term | Vendor says | Our standard | Gap | Severity | Proposed fix |
|---|---|---|---|---|---|

## 中国法卡点
| 风险等级 | 条款/材料 | 问题 | 中国法卡点 | 修改建议 |
|---|---|---|---|---|

## AI Addendum Gap

## Proposed Redlines

## Policy Consistency Diff
| Policy/registry item | Vendor term | Conflict | Action |
|---|---|---|---|
```
