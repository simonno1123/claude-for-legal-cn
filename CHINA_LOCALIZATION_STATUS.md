# 中国化落地状态

本文件记录 `claude-for-legal-cn` 第一阶段中国化改造范围。目标不是简单翻译，而是把默认法域、资料源、审阅门槛、连接器和工作流改为中国法律实务可落地的形态。

## 已完成

- Marketplace 改为 `claude-for-legal-cn`，默认插件清单移除仅面向美国法研究的 CoCounsel / Westlaw 第三方插件。
- 12 个一线插件的 `plugin.json` 和 marketplace 展示名/描述改为中国法律实务语境。
- 12 个一线插件的 `CLAUDE.md` 注入“中国法律本地化规则”，默认法域为中华人民共和国大陆地区法律。
- 当前 155 个 `SKILL.md` 注入“中国法域与引用规则”，强制要求法条全称/缩略 + 条/款/项、效力层级、地方差异标注和人工确认门。
- 保留并接入 `references/china-legal-standards.md` 作为全局中国法引用、来源、审阅和争议解决规范。
- 主线插件收敛为 9 个企业法务核心模块；`law-student`、`legal-clinic`、`legal-builder-hub` 移入 `phase-2/`。
- 9 个主线插件 `.mcp.json` 改为中国默认占位连接器：国家法律法规数据库、国务院/部委/地方监管官网、WPS/金山文档。
- 原 Slack、Google Drive、Box、CourtListener、Trellis 等国际连接器封存至 `references/international-extensions.md`。
- 新增 `references/us-to-cn-legal-terms.md`，并在根 `CLAUDE.md` 中加入中国法语境下的强制术语替换约束。
- 第三方 `external_plugins/cocounsel-legal` 标记为非中国版默认插件。
- 根 `README.md` 已按中国企业法务主场景彻底重写，并合并中文 Quickstart。
- `employment-legal` 已完成第一轮深改：注入中国劳动法 System Alignment，重写 `termination-review`，新增 `severance-calculator`，中文重写劳动插件 README。
- `employment-legal` 第二轮深改完成：新增 `handbook-audit`，重写 `wage-hour-qa` 和 `worker-classification`，建立 `employment-legal/references/test-cases-cn.md` 六个劳动法回归用例。
- `employment-legal` 第三轮深改完成：重写 `cold-start-interview`、`log-leave` 与 `leave-tracker`，新增 `social-insurance-audit`，并将插件级 `CLAUDE.md` 尾部美国法模板替换为中国用工画像、审阅人备注和社保公积金审计模板。
- `employment-legal` 收尾轮完成：重写 `hiring-review`、`policy-drafting`、`handbook-updates`、`internal-investigation` 与 `investigation-memo`；`customize` 不再作为初始化入口，改为地方司法裁审口径定制，企业用工画像统一由 `cold-start-interview` 初始化。
- `employment-legal` 复核修正完成：经 GPT-5.5、GPT-5.4 与 Gemini 3.5 Flash 复核，删除调查链路英美法特权语义，重写 `leave-tracker` 入口，默认关闭 `matter-workspace`，将 `expansion-*` 挂起至 Phase 2，补强第38/42/46/47/48/87条法条路由，并将劳动法回归用例扩展至 15 个高压案例。
- `corporate-legal` 已完成 Phase 1 深改：聚焦 2024 年 7 月 1 日施行的新公司法下公司治理、章程旧转新、出资期限/加速到期、股权转让与质押登记。
- `corporate-legal` 第一批深改完成：重写插件级 `CLAUDE.md`、`README.md`、`board-minutes` 与 `written-consent`，新增 `governance-audit`、`capital-contribution-audit`、`equity-transfer-pledge-review` 三个新公司法专项技能。
- `corporate-legal` 第二批深改完成：重写 `cold-start-interview` 为中国境内企业公司画像访谈，重写 `entity-compliance` 为市场监管年报/登记备案/章程健康检查，并将 M&A/尽调/交割/整合相关技能移入 `corporate-legal/phase-2/skills/` 暂缓加载。
- `corporate-legal` 第三批深改完成：建立 `references/test-cases-cn.md` 七个新公司法高压回归用例，新增 `references/articles-old-to-new.md` 章程旧法残留替换表，并重写 `capital-contribution-audit` 为覆盖第47条五年出资期、第54条出资加速到期、第88条责任分流和董事催缴责任的王牌技能。
- `corporate-legal` 收尾轮完成：新增 `articles-of-association-audit` 章程旧转新全量审计，重写 `governance-audit` 为“三会一层”内部治理审计，并删除 `customize` 独立入口，统一由 `cold-start-interview` 生成和更新 `company_profile`。
- `commercial-legal` 第一阶段深改完成：基于 GPT-5.5 与 GPT-5.4 双模型方案对比，重写插件级 `README.md` 与 `CLAUDE.md`，新增中国商事合同 references/test cases，重写 `cold-start-interview`、`review`、`vendor-agreement-review`、`saas-msa-review`、`nda-review`、`renewal-tracker`、`escalation-flagger`、`stakeholder-summary`、`amendment-history`、`review-proposals` 与 `matter-workspace`，重写 3 个 agents，并删除 `customize` 独立入口；已按 Gemini 3.5 Flash 条件复核补齐先票后款/进项税损失、可靠电子签名/萝卜章、或审或仲/各自所在地法院等 P0/P1 控制点。
- `litigation-legal` 第一阶段深改完成：按 Gemini 3.5 Flash 决策重写中国民商事诉讼/仲裁 System Alignment、README、核心规则字典和 10 个高压测试用例；新增 `court-order-triage`、`witness-trial-prep`、`confidential-evidence-review`、`evidence-preservation` 四个中国语义核心命令，并将 `subpoena-triage`、`deposition-prep`、`privilege-log-review`、`legal-hold` 保留为兼容旧命令；已补齐律师调查令非强制边界、证据保密不得误用英美法特权、仲裁保全经仲裁委转交法院、执行终本/中止/异议等状态。

## 仍需第二阶段深改

第一阶段解决“默认不再套美国法”的底座问题；以下内容还需要逐技能重写：

| 模块 | 必须重写的实质内容 | 优先级 |
|---|---|---|
| `employment-legal` | **PHASE 1 COMPLETE（Gemini/GPT 复核后完成）**：已完成中国劳动法下解除/终止、补偿金、员工手册、工时休假、法定假别/医疗期、社保公积金、入职、内部调查、地方口径定制和用工画像主线改造；涉外扩张与 matter-workspace 暂缓/默认关闭 | 已完成 |
| `privacy-legal` | GDPR/CCPA/DSAR 语境替换为《个保法》《数安法》《网安法》、个人信息权利请求、数据出境、重要数据、关键信息基础设施 | 高 |
| `corporate-legal` | **PHASE 1 COMPLETE（第一阶段完成）**：已完成新公司法下股东会/董事会/经理层、监事会或审计委员会、职工董事、章程旧转新、五年出资期、出资加速到期、股权转让/质押登记、市场监管登记主线改造；M&A 暂列 Phase 1.5/Phase 2 | 已完成 |
| `litigation-legal` | **PHASE 1 COMPLETE（第一阶段完成）**：已完成中国民商事诉讼/仲裁下管辖、时效、证据交换、调查令、财产/证据/行为保全、举证期限、庭审质证、律师函、案件汇报、执行和外部律师协作主线改造 | 已完成 |
| `ip-legal` | USPTO/DMCA/FTO 美国路径替换为 CNIPA、商标局、版权登记、反不正当竞争、平台投诉/行政投诉/诉讼路径 | 高 |
| `product-legal` | FTC/US consumer law 替换为《广告法》《消保法》《电商法》、市场监管、网信、算法/深度合成/生成式 AI 合规 | 高 |
| `ai-governance-legal` | NIST/EU AI Act 默认框架替换为生成式 AI、算法推荐、深度合成、数据安全、个人信息保护、科技伦理和备案/评估路径 | 高 |
| `commercial-legal` | **PHASE 1 COMPLETE（第一阶段完成）**：已完成中国商事合同审查、采购/销售、SaaS、NDA、续约、授权用印、发票税务、审批流转和合同项目管理主线改造；后续可继续细化 agents 与外部系统连接器 | 已完成 |
| `regulatory-legal` | Federal Register/Regulations.gov 替换为中国人大、国务院、部委、地方人大/政府、征求意见稿、规范性文件和监管问答 | 中 |
| `law-student` | US case method/bar prep 替换为中国法考、请求权基础、法条体系、指导案例/典型案例、司法解释训练 | 中 |
| `legal-clinic` | ABA/US clinic 语境替换为中国法律援助、12348、律协/高校诊所、导师审阅、执业边界 | 中 |
| `legal-builder-hub` | 社区技能 QA 保留，但信任审查增加中国法律资料源、MCP 安全、合规边界 | 低 |

## 中国版默认资料源

中国法律结论应优先通过以下来源核验：

- 国家法律法规数据库、中国人大网
- 最高人民法院、最高人民检察院
- 国务院、司法部、网信办、市场监管总局、人社部、工信部、证监会、银保监相关继承/现行监管机构官网
- 地方人大、地方政府、地方人社/市场监管/网信等主管部门官网
- 北大法宝、威科先行、法信、Alpha、裁判文书网、中国审判流程信息公开网
- 用户提供的合同、制度、案件材料、内部审批规则

## 人工确认门

以下动作不得由插件直接执行，必须提示律师/法务确认：

- 对外发送法律意见、律师函、催告函、谈判立场或监管回复
- 签署、盖章、备案、申报、提交诉讼/仲裁材料
- 解除/终止劳动合同、发出处分决定、作出赔偿承诺
- 删除、披露、跨境传输个人信息或重要数据
- 放弃权利、承认责任、撤回申请、和解、调解、付款或退款承诺

## 2026-06-24 product-legal 更新

- `product-legal` Phase 1 深改完成：按 GPT-5.5、GPT-5.4 与 Gemini 人工裁决结果，收敛为 5 个核心技能：`cold-start-interview`、`launch-review`、`marketing-claims-review`、`feature-risk-assessment`、`is-this-a-problem`。
- 已重写 `product-legal/CLAUDE.md`、`README.md`、`cold-start-interview`、`launch-review`、`marketing-claims-review`、`customize`、`matter-workspace`、`launch-watcher`、`currency-watch.md` 与 `seven-category-framework.md`。
- 新增 `product-legal/references/test-cases-cn.md`，覆盖自动续费、广告绝对化用语、大数据杀熟、未成年人单独同意、AI 深度合成标识、七日无理由退货、直播虚假宣传、CCC、默认勾选搭售和弹窗广告一键关闭 10 个高压回归用例。
- `customize` 已并入 `cold-start-interview`；`matter-workspace`、`launch-watcher` 与法律动态自动监控降级为 Phase 2/兼容占位。
- 残留扫描已清除核心美国法/普通法污染词，JSON 与技能 frontmatter 验证通过。
