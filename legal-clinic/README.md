# Legal Clinic (中国法律诊所与援助)

本插件是上游 `legal-clinic` 在中国大陆法律援助、公共法律服务和高校法律诊所场景下的 Faithful Port。它保留接待初筛、法律检索起点、文书学习稿、当事人沟通、期限台账、导师/律师复核队列、状态报告和学期交接等职责，同时将实体内容映射到《法律援助法》、12348 公共法律服务、高校法律诊所、基层法律援助中心和中国诉讼/仲裁/投诉程序。

**所有输出都是学生/志愿者工作底稿。** 任何对外沟通、递交材料、起诉/仲裁/复议/投诉、和解、撤诉、承认责任、处分权利或关闭案件，必须经过指导教师、执业律师、法援律师或授权复核人批准。

## 首次设置

```text
/legal-clinic:cold-start-interview
```

设置会生成本地诊所画像和状态文件：

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines-ledger.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/review-queue.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/client-comms/
~/.claude/plugins/config/claude-for-legal/legal-clinic/handoffs/
~/.claude/plugins/config/claude-for-legal/legal-clinic/guides/
```

## 核心命令

| 命令 | 作用 |
|---|---|
| `/legal-clinic:cold-start-interview` | 由指导教师/律师初始化诊所画像、服务范围、复核规则、学生名单和状态路径 |
| `/legal-clinic:build-guide` | 为劳动争议、消费者、婚姻家庭、租赁、小额债务等案由建立办案指南 |
| `/legal-clinic:ramp` | 新学生/志愿者入门培训、工具规则、保密脱敏和模拟练习 |
| `/legal-clinic:client-intake` | 接待初筛、冲突检查、法援资格初核、风险分流和期限交接 |
| `/legal-clinic:research-start` | 法条、司法解释、主管机关、案例和检索任务清单 |
| `/legal-clinic:memo` | 案件备忘录学习稿，保留学生分析区和复核问题 |
| `/legal-clinic:draft` | 投诉书、仲裁申请、起诉状提纲、证据目录等学习稿 |
| `/legal-clinic:client-letter` | 当事人说明信、材料清单、进展告知，发送前进入复核 |
| `/legal-clinic:plain-language-letters` | 将内部说明改写为白话中文，但仍需复核 |
| `/legal-clinic:form-generation` | 生成接待表、授权确认、送达地址确认、复核表等内部表单 |
| `/legal-clinic:deadlines` | 读写 `deadlines-ledger.yaml`，支持 add/report/update/complete/close |
| `/legal-clinic:supervisor-review-queue` | 读写 `review-queue.yaml`，支持 pending_review/approved/returned_with_comments |
| `/legal-clinic:client-comms-log` | 追加式记录电话、微信、短信、邮件、面谈和材料补充 |
| `/legal-clinic:status` | 面向内部、导师或当事人的案件状态摘要 |
| `/legal-clinic:semester-handoff` | 学期/人员交接，生成案件交接备忘录和班级总览 |
| `/legal-clinic:customize` | 局部更新诊所画像、复核规则、案由范围和提醒偏好 |

## 强制门控

- 默认法域：中华人民共和国大陆地区。
- 所有真实当事人事项均需人工复核。
- 未经 `review-queue.yaml` 中 `approved` 状态，不得对外发送沟通、提交文书或处分权利。
- 期限不得由 AI 自动最终计算；学生需依据文书、法条和本地规则计算，复核人确认。
- 不得承诺结果、胜诉、立案成功、法援批准或执行回款。
- 涉及家暴、人身安全、刑事风险、未成年人、精神健康、即将届满期限或重大财产处分时，必须立即升级复核和线下援助。

## 中国法场景

- 法律援助和公共法律服务初筛。
- 12348、司法局、法律援助中心、公共法律服务中心分流。
- 劳动仲裁、消费者投诉、婚姻家庭、房屋租赁、小额债务、校园权益、行政投诉。
- 学生诊所办案训练：接待、纪要、检索、期限、文书学习稿、导师复核、学期交接。
