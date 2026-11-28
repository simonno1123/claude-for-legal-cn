# Phase 1.5 / Phase 2 路线图

本文件记录 Phase 1 中国大陆法基线之后的阶段交付。Phase 1.5 本地工作流层已完成并进入 active maintenance。Phase 2 中，民商事诉讼与民事执行的分析技能已经交付并经过试用（见"Phase 2 进展"一节）；真实 Provider、外部自动化仍为 future/planned。不得把本地 YAML 工作流描述为真实 Provider 或外部自动化已经完成。

## 阶段范围

- Phase 1.5（Implemented / Active）：本地、人工触发的 matter workspace、tracker、history、owner/status/deadline 和生命周期。
- Phase 2（Future / Planned）：真实 Provider、外部系统自动监控、跨境专业能力，以及会改变本机插件状态的安装/更新/回滚操作。

当前 12 个第一方插件均位于根目录并进入默认 Marketplace。阶段归类描述交付边界，不代表模块价值或加载顺序。

## 中国案例规则更新层

状态：COMPLETE。

项目已加入可更新的中国案例规则层：

- `references/china-case-authority.md`
- `references/case-authority-sources.json`
- `references/case-authority-mcp.example.json`

该层为人民法院案例库、最高人民法院发布、裁判文书网和商业法律数据库预留更新接口。案例用于类案检索、裁判规则校准和风险判断，不得作为英美法意义上的判例法。

## 工作流

### 1. Corporate M&A（Phase 1 已暴露）

路径：`corporate-legal/phase-2/`

目标：提供中国并购尽调、交割和投后整合工作流。

状态：Phase 1 root discoverability 已完成。七个根级 wrapper 委托到历史实现目录；`phase-2` 仅是存储路径，不是能力阶段。

已完成：

- `diligence-issue-extraction`
- `material-contract-schedule`
- `closing-checklist`
- `integration-management`
- `deal-team-summary`
- `tabular-review`
- `ai-tool-handoff`
- `references/test-cases-cn.md`

验收点：

- 已替换美国交易概念为中国股权/资产收购、工商登记、税务、劳动、反垄断、数据和国资审查逻辑。
- 已加入市场监管、外商投资、国资、经营者集中和行业许可等审批/备案检查。
- 已覆盖股权权属、出资瑕疵、关联交易、劳动社保、税务、许可、知识产权、数据合规、诉讼和重大合同。

### 2. Law Student（Phase 1 根模块）

路径：`law-student/`

目标：围绕中国法学院教育、法考、法条体系、请求权基础、案例研读和法律写作训练重建学习模块。

状态：Phase 1 baseline COMPLETE；根级 marketplace 已暴露。

已完成：

- 中国法学习画像。
- 法考客观题/主观题训练。
- 法条体系和请求权基础训练。
- 案例研读、课堂提问准备、闪卡、学习计划。
- `references/test-cases-cn.md`

验收点：

- 已移除美国 law school、Bluebook、bar exam 和 common-law case method 默认框架。
- 输出定位为学习材料，不处理真实客户事项。

### 3. Legal Clinic（Phase 1 根模块）

路径：`legal-clinic/`

目标：围绕中国法律诊所、法律援助、12348 公共法律服务、学生办案训练和导师复核重建工作流。

状态：Phase 1 baseline COMPLETE；根级 marketplace 已暴露。

已完成：

- 当事人接待和初筛。
- 法援/公服分流。
- 期限跟踪。
- 案件备忘录、文书学习稿、当事人说明信。
- 导师/律师复核队列。
- 学期交接。
- `references/test-cases-cn.md`

验收点：

- 已移除 ABA、美国学生执业规则、美国证据特权和州律师协会默认框架。
- 所有真实当事人事项均保留导师或执业律师复核门。

### 4. Legal Builder Hub

路径：`legal-builder-hub/`

目标：Phase 1 提供中国法律技能 QA、静态来源审查、变更计划和 MCP 安全边界；Phase 2 才执行安装、禁用、卸载、更新和回滚。

状态：Phase 1 baseline PARTIAL COMPLETE；物理执行能力明确列入 Phase 2。

已完成：

- 中国法技能 QA。
- 安装白名单。
- MCP 凭证占位检查。
- 技能启用/禁用/卸载的人工操作计划。
- 更新差异和人工确认计划。
- 相关技能推荐。
- `references/test-cases-cn.md`

验收点：

- 所有外部技能必须通过中国法本土化审查。
- 禁止真实凭证入库。
- 禁止未审查技能进入默认 Marketplace。
- Phase 1 不得自动复制、改名、删除或覆盖本机技能文件。

## Phase 1.5 Implemented / Active

状态：`IMPLEMENTED / ACTIVE`（`TASK_019_PHASE1_5_WORKSPACE_RECOVERY` 于 2026-07-14 经 Gemini `ACCEPTED`）。

已交付：

- 共享规范：`references/local-workflow-contract.md` 定义本地路径、YAML 状态、active matter、owner/status/deadline、append-only history、archive/reopen、slug 安全、保密隔离、人工确认和失败恢复。
- 五模块事项空间：Product、IP、commercial、privacy、employment 均支持 opt-in 的 `status/new/list/switch/update/close/reopen/none` 生命周期。
- Product：根级 `/product-legal:launch-tracker` 支持人工 `add/import/list/update/queue/close`；`launch-watcher` 只读本地台账并由人工触发。
- Commercial：`deviation-log.yaml`、playbook proposal threshold、renewal register/run history、ID 去重和逐项人工提案审阅已经定义。
- 安全边界：所有运行状态保存在 `~/.claude/plugins/config/claude-for-legal/<plugin>/`，默认不跨事项读取，不后台运行，不自动通知，不执行法律后果性动作。

Active maintenance 只包括 schema/命令一致性、回归检查和缺陷修复。真实连接器、外部调度与通知仍属于 Phase 2。

## Phase 2 进展：民商事诉讼与民事执行（截至 2026-11-27）

以下技能都在 `litigation-legal` 插件内，输出一律为候选，须经合格律师复核；依据须经案件级依据时效包核对，未核对的事项阻断。

| 模块 | 技能 | 状态 | 验证 |
|---|---|---|---|
| C01 诉讼分析 | `matter-intake`、`chronology`、`claim-chart`、`brief-section-drafter` | 已交付，经 C01-III 至 C01-VII 多轮修订；2026-11-25 至 27 另经请求权基础接入、依据补核请求、复核状态写法统一、阻断命题不入正文、素材逐份登记等修订 | 多宗真实材料试跑（含一次从诉请对照、律师复核到起草的完整链条）；C01-VI、C01-VII 及请求权基础虚构案例试跑与复验 |
| C03 民事执行审查 | `enforcement-review` | 已交付（规格 v1.1；技能经 S6、R1–R3、S1–S2 修订）；2026-11-27 另经文书所载届满日与审查日对照、法院文书事实表述与原始记录对照、文书所载处置障碍与其后施行规范并列、新法时间效力规定列示等修订 | 8 宗虚构案件试跑与复验；3 宗类型不同的真实案件试用（第三宗在材料全部读取后补充复查） |
| 请求权基础方法 | 独立仓库 `claim-basis-cn`；本仓库 `references/claim-basis/` 为 v0.3.0 只读副本 | 2026-11-25 起由 `claim-chart` 第 3A 步调用（覆盖规则见 `VENDORED.md`）；`matter-intake`、`demand-draft` 只作分流，`enforcement-review` 不接入（2026-11-26 决定） | C01-VI 与上游 CB-01、CB-09 虚构案例试跑及复验；2 宗真实案件试用 |

已知并经所有者接受、留待真实使用中观察的事项：

- C01 金额口径核对：一处主张、另一处明确不主张的口径差异，不列入核对表；
- C03：前提事实在卷内完全没有的事项，只标律师复核、未阻断；有材料组未审阅时，后四类候选会全部阻断。
- C03：时间效力规定可能列得偏宽；依赖新法的事项可能被标为阻断，比"律师复核"更严。

治理与工具：

- V8 关口记录链与 V8-B 签名机制已建成，所有者已完成安装确认；C03 技能的输出不经 V8 链，不能据此主张已通过 V8 复核。
- 图片中文识别（Route A）：Tesseract 中文基准测试结论为"不通过"，专用识别引擎暂缺；图片内容只能取自文字层或人工目视，关键日期、金额、签章标 `[律师复核]`。

相关文件：`docs/phase2/track-c/`、`docs/phase2/route-b/`、`docs/phase2/route-a/`。

## Phase 2 Backlog

- Employment 跨境用工、EOR、目标法域税务/移民及当地律师协作专业包。
- Legal Builder Hub 物理安装、更新、回滚、禁用、卸载与远程 registry sync。
- WPS、商业法律数据库、企业协同、产品管理、法院/仲裁等真实 Provider。
- 外部系统自动监控、定时触发和通知投递。

## 后续维护入口

| 方向 | 文件/模块 | 建议周期 |
|---|---|---|
| 案例规则更新 | `references/case-authority-sources.json` | 活跃模块每周，非活跃模块每月 |
| 法律法规更新 | `references/china-legal-standards.md` 与各模块 references | 每月或重大修法时 |
| 连接器落地 | `CONNECTORS.md`、各 `.mcp.json` | 按供应商或内部系统推进 |
| 回归用例维护 | 各 `references/test-cases-cn.md` | 每次重大 Prompt 修改后 |
| Phase 1.5 工作流 | `references/local-workflow-contract.md`、五模块 workspace、Product tracker、Commercial state files | 每次 lifecycle/schema 修改后运行回归 |
| Phase 2 集成 | Provider、外部自动化、跨境专业包、技能生态执行 | 单独验收后迭代 |
| 技能生态治理 | `legal-builder-hub/` | 每次新增、安装、禁用、更新社区技能时 |

## 总结

Phase 1 已完成核心中国法内容和 12 根模块基线，Phase 1.5 已完成本地状态化工作流。剩余工作重点是：

1. 增强 Practice Profile 丰富度。
2. 维护 Phase 1.5 本地 workflow contract 与回归覆盖。
3. 仅在独立验收后，于 Phase 2 落地真实 MCP 连接器和外部自动化。
4. 接入经授权、可持续更新的案例与监管数据源。
