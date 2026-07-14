# Privacy Legal（中国个人信息与数据合规定制版）

本插件面向中国大陆企业的数据合规、隐私合规与产品上线审查，默认适用《个人信息保护法》《数据安全法》《网络安全法》及相关监管规则。它帮助企业法务、隐私合规负责人、产品与安全团队完成处理活动初筛、个人信息保护影响评估、数据处理协议审查、个人权利请求响应和隐私政策一致性监控。

> 专业提示：本插件输出均为内部合规协同初稿。涉及监管报送、用户正式回复、跨境数据提供、重大安全事件处置或行政调查回应时，必须经中国执业律师或企业数据合规负责人复核。

## 核心场景

| 命令 | 用途 |
|---|---|
| `/privacy-legal:cold-start-interview` | 建立中国数据合规画像：主体、行业、数据类型、敏感信息、第三方、跨境和权利请求流程 |
| `/privacy-legal:use-case-triage` | 判断新处理活动是否可推进、需 PIPIA、需跨境专项复核或应暂停 |
| `/privacy-legal:pia-generation` | 生成个人信息保护影响评估（PIPIA）报告初稿 |
| `/privacy-legal:dpa-review` | 审查受托处理、共同处理、对外提供、跨境提供相关协议 |
| `/privacy-legal:dsar-response` | 起草个人信息主体权利请求的内部处理记录和对外回复 |
| `/privacy-legal:reg-gap-analysis` | 将中国新规、监管问答或执法案例转化为差距清单 |
| `/privacy-legal:policy-monitor` | 对照隐私政策、App 权限、SDK 清单、Cookie/追踪和实际处理活动 |
| `/privacy-legal:matter-workspace` | 按处理活动、产品、供应商、跨境项目或事件管理 opt-in 本地 YAML 生命周期 |
| `/privacy-legal:customize` | 局部更新画像、阈值、联系人和模板；不替代冷启动访谈 |

## 第一阶段边界

默认主线聚焦中国大陆法。GDPR、CCPA、HIPAA、COPPA、GLBA、FERPA、DSAR、DPIA、controller/processor、SCC 等词仅在涉外材料中作为原文术语或比较法提示，不作为中国法默认判断框架。

Phase 1.5 的 `matter-workspace` 默认关闭，可人工启用 `status/new/list/switch/update/close/reopen/none`。状态、历史和归档保存在用户配置目录；默认不跨事项读取，不自动回复个人权利请求、提交 PIPIA、报告事件或连接外部隐私平台。

## 快速开始

1. 运行 `/privacy-legal:cold-start-interview` 建立企业数据合规画像。
2. 对新产品功能、营销活动、SDK 接入、AI 训练、员工数据处理或跨境共享运行 `/privacy-legal:use-case-triage`。
3. 命中敏感个人信息、自动化决策、委托处理/对外提供/公开/跨境提供等触发项时，运行 `/privacy-legal:pia-generation`。
4. 签署云服务、外包客服、支付、广告、数据分析、集团共享或跨境相关协议时，运行 `/privacy-legal:dpa-review`。
5. 用户提出查阅、复制、更正、删除、撤回同意、注销账号或自动化决策解释请求时，运行 `/privacy-legal:dsar-response`。

## 参考资料

- `references/china-privacy-data-playbook.md`：中国个人信息与数据合规通用审查框架。
- `references/test-cases-cn.md`：中国隐私合规高压回归测试用例。
- `references/currency-watch.md`：中国数据合规动态监控清单。
