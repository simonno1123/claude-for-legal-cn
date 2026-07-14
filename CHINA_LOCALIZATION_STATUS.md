# 中国化落地状态

本文件记录 `claude-for-legal-cn` 中国化改造历史和当前阶段状态。Phase 1 已完成中国法实体对齐、12 根模块和基线可运行性；Phase 1.5 本地状态化工作流已实现并通过验收。Phase 2 真实 Provider、外部自动化和高权限操作仍不得因模板或占位文件存在而标记为已完成。

## 已完成

- Phase 1.5 本地工作流层完成：`TASK_019_PHASE1_5_WORKSPACE_RECOVERY` 于 2026-07-14 经 Gemini `ACCEPTED`；共享 `local-workflow-contract`、五模块 matter lifecycle、Product launch tracker/review queue 与 Commercial 本地 persistence/threshold/history/dedup 均进入 active baseline。

- Marketplace 改为 `claude-for-legal-cn`，默认插件清单移除仅面向境外法研究的第三方插件。
- 12 个一线插件的 `plugin.json` 和 marketplace 展示名/描述改为中国法律实务语境。
- 12 个一线插件的 `CLAUDE.md` 注入“中国法律本地化规则”，默认法域为中华人民共和国大陆地区法律。
- 当前 12 个根模块共 169 个 `SKILL.md`，均纳入中国法域、引用规则和人工确认门检查；新增项为 Phase 1.5 根级 `product-legal/launch-tracker`。
- 保留并接入 `references/china-legal-standards.md` 作为全局中国法引用、来源、审阅和争议解决规范。
- 12 个第一方插件均位于根目录并进入默认 Marketplace；不存在 10+2 或教育/公益模块降权。
- 12 个根模块 `.mcp.json` 使用统一中国占位配置；本地 `legal-data` 仅提供样例索引，WPS、商业数据库和企业系统仍是未生产接入的 Provider 占位。
- 原国际办公协作、境外案例检索和境外诉讼数据连接器封存至 `references/international-extensions.md`。
- 新增 `references/us-to-cn-legal-terms.md`，并在根 `CLAUDE.md` 中加入中国法语境下的强制术语替换约束。
- 第三方 `external_plugins/cocounsel-legal` 标记为非中国版默认插件。
- 根 `README.md` 已按中国律师、企业法务、法律诊所和法律学习者共同适用的基础层定位重写，并提供中文 Quickstart。
- `employment-legal` 已完成第一轮深改：注入中国劳动法 System Alignment，重写 `termination-review`，新增 `severance-calculator`，中文重写劳动插件 README。
- `employment-legal` 第二轮深改完成：新增 `handbook-audit`，重写 `wage-hour-qa` 和 `worker-classification`，建立 `employment-legal/references/test-cases-cn.md` 六个劳动法回归用例。
- `employment-legal` 第三轮深改完成：重写 `cold-start-interview`、`log-leave` 与 `leave-tracker`，新增 `social-insurance-audit`，并将插件级 `CLAUDE.md` 尾部美国法模板替换为中国用工画像、审阅人备注和社保公积金审计模板。
- `employment-legal` 收尾轮完成：重写 `hiring-review`、`policy-drafting`、`handbook-updates`、`internal-investigation` 与 `investigation-memo`；`customize` 不再作为初始化入口，改为地方司法裁审口径定制，企业用工画像统一由 `cold-start-interview` 初始化。
- `employment-legal` 复核修正完成：经多模型交叉复核，删除调查链路英美法特权语义，重写 `leave-tracker` 入口，补强第38/42/46/47/48/87条法条路由，并将劳动法回归用例扩展至 15 个高压案例。Phase 1.5 已交付默认关闭、可 opt-in 的本地 matter lifecycle；跨境 expansion 实质能力仍属于 Phase 2。
- `corporate-legal` 已完成 Phase 1 深改：聚焦 2024 年 7 月 1 日施行的新公司法下公司治理、章程旧转新、出资期限/加速到期、股权转让与质押登记。
- `corporate-legal` 第一批深改完成：重写插件级 `CLAUDE.md`、`README.md`、`board-minutes` 与 `written-consent`，新增 `governance-audit`、`capital-contribution-audit`、`equity-transfer-pledge-review` 三个新公司法专项技能。
- `corporate-legal` 第二批深改完成：重写 `cold-start-interview` 为中国境内企业公司画像访谈，重写 `entity-compliance` 为市场监管年报/登记备案/章程健康检查。M&A/尽调/交割/整合实质内容保存在历史 `corporate-legal/phase-2/skills/` 路径，但已通过根级 wrappers 暴露，不再暂缓加载。
- `corporate-legal` 第三批深改完成：建立 `references/test-cases-cn.md` 七个新公司法高压回归用例，新增 `references/articles-old-to-new.md` 章程旧法残留替换表，并重写 `capital-contribution-audit` 为覆盖第47条五年出资期、第54条出资加速到期、第88条责任分流和董事催缴责任的王牌技能。
- `corporate-legal` 收尾轮完成：新增 `articles-of-association-audit` 章程旧转新全量审计，重写 `governance-audit` 为“三会一层”内部治理审计，并删除 `customize` 独立入口，统一由 `cold-start-interview` 生成和更新 `company_profile`。
- `commercial-legal` 第一阶段深改完成：基于多模型方案对比，重写插件级 `README.md` 与 `CLAUDE.md`，新增中国商事合同 references/test cases，重写 `cold-start-interview`、`review`、`vendor-agreement-review`、`saas-msa-review`、`nda-review`、`renewal-tracker`、`escalation-flagger`、`stakeholder-summary`、`amendment-history`、`review-proposals` 与 `matter-workspace`，重写 3 个 agents，并删除 `customize` 独立入口；已按交叉复核结论补齐先票后款/进项税损失、可靠电子签名/萝卜章、或审或仲/各自所在地法院等 P0/P1 控制点。
- `commercial-legal` P1 收口完成：经法律与工程双轨复核，软化“三流合一”、部门章/项目章、定金与违约金、电子签 CA 和各自所在地法院的绝对化表述；补齐销售侧显式路由、Case 11/12/15 回归归属、用户画像读取路径和仓库级 references 路径说明。
- `litigation-legal` 第一阶段深改完成：按交叉复核决策重写中国民商事诉讼/仲裁 System Alignment、README、核心规则字典和 10 个高压测试用例；新增 `court-order-triage`、`witness-trial-prep`、`confidential-evidence-review`、`evidence-preservation` 四个中国语义核心命令，并将 `subpoena-triage`、`deposition-prep`、`privilege-log-review`、`legal-hold` 保留为兼容旧命令；已补齐律师调查令非强制边界、证据保密不得误用英美法特权、仲裁保全经仲裁委转交法院、执行终本/中止/异议等状态。
- `privacy-legal` 第一阶段深改完成：重写插件级 `CLAUDE.md`、`README.md`、`currency-watch.md`，新增 `references/china-privacy-data-playbook.md` 与 `references/test-cases-cn.md`；重写 `cold-start-interview`、`use-case-triage`、`pia-generation`、`dpa-review`、`dsar-response`、`reg-gap-analysis`、`policy-monitor`、`matter-workspace`、`customize`，将 GDPR/CCPA/HIPAA/COPPA/DSAR/DPIA/controller/processor 默认框架切换为中国《个人信息保护法》《数据安全法》《网络安全法》下的个人信息处理者、受托处理、共同处理、PIPIA、数据出境、个人权利请求、SDK/隐私政策一致性和安全事件响应。

## 当前模块阶段账本

当前阶段账本区分已交付的 Phase 1/1.5 能力与仍属 Phase 2 的扩展：

| 模块 | 必须重写的实质内容 | 优先级 |
|---|---|---|
| `employment-legal` | **PHASE 1 + 1.5 VALID**：中国劳动法核心能力和 opt-in 本地 matter lifecycle 已完成；跨境 expansion 实质能力为 Phase 2 | 已完成/Active |
| `privacy-legal` | **PHASE 1 + 1.5 VALID**：中国个人信息与数据合规主线及处理活动/产品/供应商/事件的本地 matter lifecycle 已完成 | 已完成/Active |
| `corporate-legal` | **PHASE 1 BASELINE COMPLETE**：新公司法及 M&A 根命令均已暴露；历史存储路径不构成阶段降级 | 已完成 |
| `litigation-legal` | **PHASE 1 COMPLETE（第一阶段完成）**：已完成中国民商事诉讼/仲裁下管辖、时效、证据交换、调查令、财产/证据/行为保全、举证期限、庭审质证、律师函、案件汇报、执行和外部律师协作主线改造 | 已完成 |
| `ip-legal` | **PHASE 1 + 1.5 VALID**：中国知识产权主线及权利组合/FTO/商业秘密/维权事项的本地隔离 lifecycle 已完成 | 已完成/Active |
| `product-legal` | **PHASE 1 + 1.5 VALID**：中国产品审查、本地 matter lifecycle、launch tracker 和人工 review queue 已完成；外部自动监控仍为 Phase 2 | 已完成/Active |
| `ai-governance-legal` | **PHASE 1 COMPLETE（第一阶段完成）**：已完成中国 AI 治理主线改造，覆盖生成式 AI、算法推荐、深度合成、公众服务、备案/安全评估触发、内容安全、训练数据合法性、个人信息/PIPIA、供应商禁训/留存/跨境、企业 AI 使用制度和 AI 系统台账 | 已完成 |
| `commercial-legal` | **PHASE 1 + 1.5 VALID**：中国商事合同主线、本地 matter lifecycle、deviation log、proposal threshold、renewal history 和去重已完成；外部系统连接器仍为 Phase 2 | 已完成/Active |
| `regulatory-legal` | **PHASE 1 COMPLETE（第一阶段完成）**：已完成中国监管合规主线改造，覆盖国家法律法规数据库、中国人大、国务院、部委、地方政府、规范性文件、监管问答、征求意见稿、执法案例、政策差异分析、整改台账和制度修订 | 已完成 |
| `law-student` | **PHASE 1 BASELINE COMPLETE**：根级法考、请求权基础、法条体系、案例研习和法律写作训练 | 已完成 |
| `legal-clinic` | **PHASE 1 BASELINE COMPLETE**：根级法律援助、12348、高校诊所、导师复核和执业边界 | 已完成 |
| `legal-builder-hub` | **PHASE 1 BASELINE PARTIAL COMPLETE**：技能 QA、静态来源审查、变更计划和 MCP 安全边界已具备；物理安装/更新/回滚/禁用/卸载为 Phase 2 | 已完成基线/已登记 Phase 2 |

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

## 2026-07-14 Phase 1.5 本地工作流

- 新增共享规范 `references/local-workflow-contract.md`，统一本地 YAML 路径、active matter、owner/status/deadline、history、archive/reopen、保密隔离、人工确认和失败恢复。
- `commercial-legal`、`privacy-legal`、`product-legal`、`ip-legal`、`employment-legal` 均支持 `status/new/list/switch/update/close/reopen/none`，默认 opt-in，不跨事项读取。
- 新增 `/product-legal:launch-tracker`，支持人工 `add/import/list/update/queue/close`；`launch-watcher` 仅在人工触发时读取本地台账。
- Commercial agents 已定义本地 deviation log、5 次/12 个月默认 proposal threshold、renewal run history、ID 去重和逐项人工提案确认。
- Phase 1.5 不包含真实 MCP、外部系统轮询、定时任务、自动通知、提交、签署或其他后果性动作。

## 2026-06-24 product-legal 更新

- `product-legal` Phase 1 深改完成：按多模型交叉复核与人工裁决结果，收敛为 5 个核心技能：`cold-start-interview`、`launch-review`、`marketing-claims-review`、`feature-risk-assessment`、`is-this-a-problem`。
- 已重写 `product-legal/CLAUDE.md`、`README.md`、`cold-start-interview`、`launch-review`、`marketing-claims-review`、`customize`、`matter-workspace`、`launch-watcher`、`currency-watch.md` 与 `seven-category-framework.md`。
- 新增 `product-legal/references/test-cases-cn.md`，覆盖自动续费、广告绝对化用语、大数据杀熟、未成年人单独同意、AI 深度合成标识、七日无理由退货、直播虚假宣传、CCC、默认勾选搭售和弹窗广告一键关闭 10 个高压回归用例。
- `customize` 已并入 `cold-start-interview`；本地 `matter-workspace` 和 launch tracker 已在 Phase 1.5 交付，外部系统自动监控仍属于 Phase 2。
- 残留扫描已清除核心美国法/普通法污染词，JSON 与技能 frontmatter 验证通过。

## 2026-06-26 ip-legal 更新

- `ip-legal` Phase 1 深改完成：基于模型交叉审查和人工复核结果，重写插件级 `CLAUDE.md`、`README.md`，移除普通法证据特权、专利代理人特权、境外下架和境外商标/专利默认框架。
- 已重写 `clearance` 为中国商标清除初筛，覆盖《商标法》第10/11/30/32/33/44/49条、CNIPA 审查指南、《类似商品和服务区分表》、异议、无效和撤三策略。
- 已重写 `fto-triage` 为中国专利自由实施风险初筛，覆盖发明、实用新型、外观设计、全面覆盖原则、专利权评价报告、现有技术/现有设计抗辩、无效宣告和设计绕开。
- 已重写 `takedown` 与 `cease-desist`，切换为《民法典》第1195-1197条、《电子商务法》第41-45条下的通知删除、反通知、15天等待期、平台投诉、行政投诉、律师函和诉讼/保全路径。
- 已重写 `cold-start-interview`、`infringement-triage`、`portfolio`、`ip-renewal-watcher`、`invention-intake`、`ip-clause-review`、`oss-review` 和 `matter-workspace`，补齐 CPCC 软著、商业秘密、海关知识产权保护、开源合规和中国权利组合期限管理；本地 matter lifecycle 后于 Phase 1.5 完成状态化。
- 新增 `ip-legal/references/china-ip-core-rules.md` 与 `ip-legal/references/test-cases-cn.md`，建立 10 个中国知识产权高压回归用例。
- `ip-legal` 收口修正：重写 `customize` 为中国知识产权画像局部更新器，并将 `.mcp.json` 的知识产权连接器说明改为仓库根目录 references 路径和国内 IP 数据源语义。

## 2026-06-26 ai-governance-legal 更新

- `ai-governance-legal` Phase 1 深改完成：重写插件级 `CLAUDE.md`、`README.md`、`currency-watch.md`，新增 `references/china-ai-governance-rules.md` 与 `references/test-cases-cn.md`。
- 已重写 `cold-start-interview`、`ai-inventory`、`use-case-triage`、`aia-generation`、`vendor-ai-review`、`policy-starter`、`reg-gap-analysis`、`policy-monitor`、`matter-workspace`、`customize`。
- 默认框架已从境外 AI 治理框架和美国州法切换为中国生成式 AI、算法推荐、深度合成、PIPL/DSL/CSL、备案/安全评估、内容安全、供应商禁训/留存/跨境和企业 AI 使用制度。
- 残留扫描已清除核心美国法/普通法污染词，JSON 与技能 frontmatter 验证通过。

## 2026-06-26 regulatory-legal 更新

- `regulatory-legal` Phase 1 深改完成：重写插件级 `CLAUDE.md`、`README.md`、监管来源目录和监管变化监控 agent。
- 已重写 `cold-start-interview`、`reg-feed-watcher`、`policy-diff`、`gaps`、`gap-surfacer`、`comments`、`policy-redraft`、`matter-workspace`、`customize`。
- 默认来源已从境外联邦规则、境外判例和境外法律数据库切换为国家法律法规数据库、中国人大、国务院、司法部、网信办、市场监管总局、工信部、地方政府、规范性文件、监管问答、征求意见稿和执法案例。
- 已将征求意见跟踪模板改造为中国监管语义，覆盖草案来源、意见截止日、反馈主体、提交渠道、采纳情况和后续制度修订。
- 残留扫描仅保留“禁止默认使用/不得套用”的负向约束，JSON 与技能 frontmatter 验证通过。

## 2026-06-27 收尾修复记录

- 已按第二轮复核报告完成收尾修复：`CONNECTORS.md`、`PROJECT_USAGE_GUIDE.md`、`CONTRIBUTING.md` 与 managed-agent cookbooks 的已知乱码、硬编码路径和美国/国际 SaaS 示例残留已清理。
- 已建立统一 MCP 配置生成体系：新增 `scripts/mcp-template.json`、`scripts/mcp-modules.json` 与 `scripts/generate-mcp-configs.py`，12 个模块的 `.mcp.json` 统一由模板生成，默认接入 `legal-data` 与 `wps-cloud-docs`，并按模块追加中国合同管理、电子签章、法院/仲裁、协同系统等占位连接器。
- 根目录 `CLAUDE.md` 已加入 MCP 维护规则：后续不得直接手改各模块 `.mcp.json`，应修改模板或模块表后重新生成并验证。
- managed-agent cookbooks 已统一注入中国大陆默认法域声明，并清除旧的英美法工作成果标签、特权圈、旧协作工具占位符和国外合同/电子签工具命名。
- 收尾校验通过：12 个 `.mcp.json` 全部可解析，仓库目标范围内 JSON 全部可解析，cookbook 与脚本目标范围未检出旧协作工具、硬编码本机路径、乱码哨兵或英美工作成果特权残留。

## 2026-06-27 序列调整记录（历史，已由 2026-07-13 范围决策取代）

- `legal-builder-hub` 已从历史路径移至根目录；该移动不表示模块价值优先级。
- 2026-07-13 起，12 个第一方插件均为根级模块；`law-student`、`legal-clinic` 不再属于 Phase 2。
- MCP 模块表按 12 个根路径维护，后续 `.mcp.json` 由 `scripts/generate-mcp-configs.py` 生成或以 `--check` 只读验证。

## 2026-06-30 legal-data 最小可运行层

- 新增 `connectors/legal-data/server.js`：无依赖 Node stdio MCP server，支持 `law_search`、`article_lookup`、`regulation_detail`、`case_search`、`case_detail`、`case_authority_rank`、`judicial_answer_search`、`judicial_answer_detail`、`citation_check`。
- 新增 `connectors/legal-data/local-index.sample.json`：用于 smoke test 的本地样例索引，覆盖《劳动合同法》《公司法》《个人信息保护法》的核心样例条文、案例权威等级和法答网样例。
- 新增 `scripts/test-legal-data.sh`：验证本地 server、自测、法条定位和引用校验混合结果。
- `legal-data` 当前只读取 `LOCAL_LEGAL_INDEX` 本地 JSON 索引；未配置时使用样例索引并强制返回人工复核提示。不联网、不调用商业库、不把样例摘要当作正式法律文本。

## 2026-07-01 自动化收口

- 新增 `scripts/localization-regression.py`：自动检查默认 marketplace 不包含海外 vendor 插件、各默认模块均保留中国法测试用例、`.mcp.json` 均接入 `legal-data`、核心文档不回退到旧的 vendor/default 口径，并对未授权路径中的境外法研究默认语境做回归拦截。
- 新增 `.github/workflows/ci.yml`：在 push/PR 上运行 JSON 解析、localization regression、`legal-data` smoke test 和 managed-agent cookbook smoke test。
- 更新根 `README.md`、`CLAUDE.md`、`AGENTS.md`，明确 `legal-data` 已具备最小本地 server，其他企业系统连接器仍为部署占位，`external_plugins/cocounsel-legal` 是可选外部插件且不进入中国版默认 marketplace。
