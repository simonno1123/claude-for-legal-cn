# Legal Clinic Practice Profile Template (中国法律诊所与援助)

<!--
CONFIGURATION LOCATION

User-specific configuration lives at:

  ~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md

All skills must read that path before substantive work. If it does not exist or
contains [PLACEHOLDER] markers, stop and ask the supervising teacher/lawyer to
run:

  /legal-clinic:cold-start-interview

Only /legal-clinic:cold-start-interview and --check-integrations probes may run
without setup. This file ships with the plugin and must not store live client
facts.
-->

## Role And Scope

**Default jurisdiction:** 中华人民共和国大陆地区。

**Clinic type:** [PLACEHOLDER — 高校法律诊所 / 法律援助中心 / 公益组织 / 公共法律服务咨询点]
**Supervising reviewer:** [PLACEHOLDER — 指导教师 / 执业律师 / 法援律师 / 授权负责人]
**Students / volunteers:** [PLACEHOLDER]
**Service region:** [PLACEHOLDER]
**Practice areas:** [PLACEHOLDER — 劳动争议 / 消费者权益 / 婚姻家庭 / 租赁 / 小额债务 / 校园权益 / 行政投诉 / 其他]

## Mandatory Review Gate

Every real-party output is a working draft until approved.

Review queue states:

- `pending_review`
- `approved`
- `returned_with_comments`

No client communication, filing, complaint, arbitration application, lawsuit material, settlement, withdrawal, admission of liability, payment commitment, waiver, authorization, or case closure may be treated as final unless `review-queue.yaml` records `approved`.

## Stateful Files

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines-ledger.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/review-queue.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/client-comms/
~/.claude/plugins/config/claude-for-legal/legal-clinic/handoffs/
~/.claude/plugins/config/claude-for-legal/legal-clinic/guides/
~/.claude/plugins/config/claude-for-legal/legal-clinic/cases/
```

If file writes are unavailable, output YAML/Markdown records for manual saving and explicitly state persistence failed.

## Output Label

Every internal output starts with:

```text
学生/志愿者法律服务工作底稿 / 需导师或执业律师复核
```

Client-facing text must remove internal notes only after supervisor approval. Until then, it is not final advice.

## China-Law Sources

Prioritize:

- 国家法律法规数据库、中国人大网、最高人民法院、最高人民检察院、司法部。
- 《法律援助法》及当地法律援助实施规则。
- 劳动仲裁、人民法院诉讼服务、市场监管、消协、人社、公安、民政、住建等主管机关规则。
- 用户提供的文书、通知、合同、聊天记录、证据和当地模板。

Use `[待核验]` when a source, effective date, deadline, jurisdictional rule or official form is not verified.

## Referral Resources

- 12348 公共法律服务热线。
- 当地司法局、法律援助中心、公共法律服务中心。
- 劳动人事争议仲裁委员会。
- 消协、市场监管、住建、人社、公安、民政等主管机关。
- 人民法院诉讼服务中心、人民调解组织。
- 高校法律诊所指导教师、合作律所或法援律师。

## High-Risk Escalation

Immediately escalate for supervisor review when facts involve:

- 即将届满期限、开庭/仲裁/听证日期。
- 家暴、人身安全、未成年人、老年人、残障人士、精神健康危机。
- 刑事风险、行政处罚、羁押、治安处罚。
- 起诉、仲裁、复议、投诉、执行、和解、撤诉、放弃权利。
- 对外发送法律意见、律师函、投诉材料、起诉状、仲裁申请、证据目录。

## No Silent Supplementation

Do not invent statutes, cases, local forms, filing windows, limitation periods, agency requirements, legal-aid eligibility standards, or case facts. Ask for sources, tag unverified items, or stop.
