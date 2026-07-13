# TASK_017 Scope Reclassification Result

TASK ID: `TASK_017_PHASE1_SCOPE_RECLASSIFICATION`

PRODUCER: Codex

NEXT RECEIVER: Gemini

MODE: READ ONLY

PROJECT: `/Users/zhang/Documents/claude-for-legal-cn`

## Executive Summary

本次重分类覆盖 `TASK_016_PHASE1_FINAL_AUDIT_RESULT.md` 的 B-1 至 B-5、G-1 至 G-5，并以 TASK_017 指定的三层模型进行判断：

1. Phase 1 Baseline Recovery：保证 12 个根模块、核心中国法能力、命令发现、必需 CI、配置生成和文档声明真实一致；
2. Phase 1.5 Legal Workflow Layer：提供本地、人工触发、可持久化的事项空间、tracker、监测和生命周期；
3. Phase 2 Advanced Integration / External Capability：提供外部系统自动监控、真实 Provider、跨境专业能力和可改变本机插件状态的生态操作。

按该模型，TASK_016 的问题不应整体作为一个 Phase 1 修复包处理。B-1 及 G 类中的运行时、断链、声明真实性问题必须在 Phase 1 闭环；B-2、B-4 和 G-1/G-2 的状态化深度主要属于 Phase 1.5；B-3 的跨境用工实质能力和 B-5 的插件生态执行能力主要属于 Phase 2。

但存在一项治理前提：`docs/PROJECT_SCOPE.md:5-19,46-53`、`README.md:5-20,74-76` 和 `docs/FAITHFUL_PORT_STANDARD.md:14-21,178-188` 仍把 v1 定义为 Complete Chinese Port / Faithful Port，并要求上游职责等效。TASK_017 使用的“中国律师 AI 平台基础能力层”及 Phase 1/1.5/2 分层仅见于 TASK_017 本身，尚未进入冻结治理文档。因此，本 RESULT 是范围重分类建议，不能自行撤销 TASK_016 的 Gemini `REJECTED`，也不能在不调整治理口径的情况下同时声称“上游职责完整移植”与“相关上游职责延后”。

### Issue Crosswalk

| Issue | Reclassification | Core reason |
|---|---|---|
| B-1 Runtime / CI Drift | Phase 1 Mandatory | 必需 CI 当前退出 `1`，MCP 配置源表仍指向不存在路径；这是基线可验证性问题。 |
| B-2 Product launch watcher / matter workspace | Phase 1.5；外部自动监控为 Phase 2 | `launch-review` 已覆盖本地材料审查；缺失部分是持续 tracker、事项隔离和外部系统监控。 |
| B-3 Employment expansion | Phase 2；通用 tracker 能力可复用 Phase 1.5 基础设施 | 目标法域用工、EOR、税务、移民和当地律师协作属于跨境专业扩展，不是中国劳动法基础层。 |
| B-4 IP matter workspace | Phase 1.5 | 核心 IP 审查能力已经存在；缺失的是通用的多事项状态与隔离生命周期。 |
| B-5 Legal Builder Hub action workflows | Phase 2；Phase 1 仅需真实声明和安全边界 | 安装、更新、回滚、禁用、卸载会改变本机插件状态，属于 Agent 生态执行层。 |
| G-1 Workspace behavior | Phase 1.5；误导性命令契约为 Phase 1 | 持久化生命周期属于工作流层，但当前声明不得超出实际能力。 |
| G-2 Commercial agents | 元数据/发现性为 Phase 1；本地状态化为 Phase 1.5；外部通知为 Phase 2 | 需要拆分运行时元数据、工作流深度和 Provider 自动化。 |
| G-3 Broken command references | Phase 1 Mandatory | 两个引用指向不存在命令，属于直接断链。 |
| G-4 WPS schema | schema 一致性为 Phase 1；真实 WPS Provider 为 Phase 2 | 修正当前声明与正则冲突不等于接入真实 Provider。 |
| G-5 Governance/document drift | Phase 1 Mandatory | RC 文档必须描述当前真实目录、状态和范围。 |

## Phase 1 Mandatory Fixes

|Issue|Reason|Decision|
|-|-|-|
|B-1a：`scripts/localization-regression.py` 仍使用 10+2 模块集合|`.github/workflows/ci.yml:25-26` 强制执行该脚本；脚本在 `scripts/localization-regression.py:19-35,89-92,125-138` 把根级 `law-student`、`legal-clinic` 误判为 extra，并读取不存在的旧路径。2026-07-13 复跑结果为 exit code `1`。|Phase 1 必修：统一为 12 个根模块，并保留 vendor 隔离检查。|
|B-1b：localization regression 扫描协调历史记录|`scripts/localization-regression.py:162-177` 扫描 `.codex-coordination/`，把历史审计中的外国法关键词当成产品内容回退；当前失败项来自 TASK_012 RESULT。|Phase 1 必修：把协调、审计和历史证据目录排除出产品内容扫描，同时继续扫描实际插件与治理文档。|
|B-1c：MCP 模块源表保留旧路径|`scripts/mcp-modules.json:91,97` 指向 `phase-2/law-student`、`phase-2/legal-clinic`；`scripts/generate-mcp-configs.py:38-45` 正确 fail-fast，但因此无法完成生成。|Phase 1 必修：仅修正模块源表为根路径并验证生成结果；生成器主体无需为本问题重写。|
|B-1d：旧 `phase-2/law-student`、`phase-2/legal-clinic` 引用|实际模块已位于根目录，旧目录不存在。缺陷在脚本和文档引用，不在已恢复模块内容。|Phase 1 必修：清除旧引用；不重新移动模块，不重做 law-student/legal-clinic。|
|G-3：product 两个跨插件命令断链|`product-legal/skills/launch-review/references/seven-category-framework.md:23,31` 引用不存在的 `/privacy-legal:pia-audit` 与 `/ai-governance-legal:cac-filing`。|Phase 1 必修：路由到现有根命令，并做全仓命令引用复检。|
|G-4a：WPS reader 声明与 URL schema 冲突|`managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml:29,32` 启用 `wps-cloud-docs`，但 line 42 的允许域名不含 `docs.wps.cn`/`kdocs.cn`。这属于当前配置内部不一致，不要求真实网络接入。|Phase 1 必修：让 schema 接受已声明的 WPS/金山域名，或明确把该 reader 改为禁用占位；不得声称已完成真实 Provider 接入。|
|G-5a：12 根模块治理文档不同步|`AGENTS.md:26`、`QUICKSTART.md:56-57,68`、`PHASE_2_ROADMAP.md:7,50,71`、`CHINA_LOCALIZATION_STATUS.md:12-13,116-117` 仍保留 10+2 或旧路径。|Phase 1 RC 必修：统一当前目录和 marketplace 事实；历史记录可保留日期，但必须与当前状态明确分层。|
|G-5b：README / Usage Guide 状态错误|`README.md:31` 仍称 employment 为“当前重点深改”；`PROJECT_USAGE_GUIDE.md:324` 仍把已完成的目录/marketplace 调整描述为未来决定。|Phase 1 RC 必修：删除业务优先级与过期未来时表述。|
|G-5c：Mapping Matrix 未记录已接受恢复|`docs/UPSTREAM_MAPPING_MATRIX.md:19,32-35` 仍把 corporate root exposure 记为未决，未完整记录后续 accepted recoveries；external plugin 行也仍为未决。|Phase 1 RC 必修：把已完成事实、明确后移事项及其阶段写入矩阵。|
|G-5d：Legal Builder Hub 当前声明超出实现|`legal-builder-hub/README.md:3`、manifest description 与 `skill-installer`/`disable`/`uninstall` 的描述使用执行性措辞，但技能目前主要输出计划或记录。|Phase 1 必修的是声明真实性：明确当前仅 QA/计划/人工执行，或在 UI/文档中标为 deferred；物理执行逻辑本身归 Phase 2。|
|G-1a：commercial workspace 命令契约超出实现|`commercial-legal/skills/matter-workspace/SKILL.md:5` 宣称 `new/list/switch/close/none`，但正文仅给字段和静态模板。|Phase 1 必修的是消除误导：在 Phase 1.5 实现前，明确模板模式/未持久化状态，或收窄 argument contract。|
|G-2a：Agent 发现性元数据缺失|三个 `commercial-legal/agents/*.md` 与 `legal-builder-hub/agents/registry-sync.md` 缺少 agent frontmatter；官方 validator 虽退出 `0`，但产生 discoverability warning。|Phase 1 必修：补齐合法 frontmatter 和真实可用的最小工具声明；不要求同时实现自动调度或外部通知。|
|B-2/B-3/B-4/B-5 的阶段声明|若相关能力后移而 mapping/README 仍宣称 Complete Chinese Port 已完成，RC 状态不真实。|Phase 1 必修：在 Gemini 接受本重分类后，将每项明确登记为 Phase 1.5 或 Phase 2；不能继续使用“已完整实现”与“占位”并存的口径。|

## Phase 1.5 Backlog

|Issue|Reason|Decision|
|-|-|-|
|B-2a：Product 本地 launch tracker / manual watcher|`product-legal:launch-review` 已能处理人工上传 PRD、营销方案和上线材料；缺失的是跨会话 watchlist、到期窗口、owner/status 和人工触发的差异提醒。该能力无需 Jira/Linear/MCP 即可实现。|Phase 1.5：实现本地 YAML/JSON tracker 和人工触发的 review queue；不自动读取外部产品系统。|
|B-2b：Product matter workspace|`product-legal/skills/matter-workspace/SKILL.md:10-28` 当前明确关闭，核心产品合规审查不受影响；缺失的是多客户/多产品事项隔离。|Phase 1.5：提供 opt-in 的 `new/list/switch/close/none` 本地生命周期，企业单一上下文继续默认关闭。|
|B-4：IP matter workspace|`ip-legal/skills/matter-workspace/SKILL.md:10-28` 同样明确关闭；商标、专利、著作权、平台维权等基础能力已经存在。|Phase 1.5：与其他模块采用统一的 opt-in 本地事项隔离契约，避免单独复制一套不一致实现。|
|G-1b：Commercial/privacy/employment workspace 状态化|Commercial 和 privacy 当前主要输出静态模板；employment 的 in-house default-off 与 TASK_003 的既有决策一致，但没有 private-practice activation。|Phase 1.5：建立通用的本地事项生命周期、active matter、archive、history 和隔离规则；各插件只保留法域/事项字段适配。|
|G-2b：Commercial agent 本地状态化|`deal-debrief`、`playbook-monitor`、`renewal-watcher` 已有中国法流程和人工输出，但未定义持久 deviation log、proposal threshold、续约运行记录等。|Phase 1.5：补本地 persistence、阈值、去重和人工触发的 schedule contract。|
|通用 tracker 基础设施|Product、employment expansion、IP 和多个 workspace 的缺口重复指向 owner/status/deadline/history/close 语义。逐插件临时拼装会造成实现漂移。|Phase 1.5：先定义最小本地 tracker/workspace contract，再由各模块映射；不在 Phase 1 RC 中做架构重构。|

## Phase 2 Deferred Items

|Issue|Reason|Decision|
|-|-|-|
|B-3：`expansion-kickoff` / `expansion-update` / `international-expansion`|上游能力围绕进入新法域、EOR/实体、当地劳动法、税务、移民和外部律师协调。CN 当前技能已安全限制为问题清单和当地专业人士转介（`employment-legal/skills/expansion-*:SKILL.md`、`international-expansion/SKILL.md`）。TASK_003 的既有条件 C-1 允许“映射 or 保持悬挂”的最终裁定。|Phase 2：归类为跨境用工/出海企业专业扩展能力。Phase 1 保留安全 intake/handoff 和负向约束；专门 tracker 可在 Phase 2 复用 Phase 1.5 通用 tracker。|
|B-5：Legal Builder Hub 物理安装、更新、回滚、禁用、卸载、registry sync|这些操作会读取外部来源并修改 `~/.claude`、技能文件、hooks、日志和备份。它们不是运行 12 个中国法模块的必要条件，且需要权限、供应链信任、allowlist 和回滚安全设计。|Phase 2：作为 Agent 生态扩展能力实施。Phase 1 保留 skills QA、静态审查、计划输出和明确的人工作业边界。|
|B-2c：Product 外部系统自动监控|`product-legal/agents/launch-watcher.md:19-21` 的飞书、企微、钉钉、WPS、项目系统自动读取依赖部署方 Provider。|Phase 2：真实连接器、定时触发和自动通知；Phase 1.5 只做本地/人工触发 tracker。|
|G-2c：Agent 外部 schedule/notification|Slack/协同系统投递、自动日程和外部 tracker 查询属于 Provider 自动化，不影响本地审查能力。|Phase 2：在连接器授权、凭证和人工发送门确定后实施。|
|G-4b：真实 WPS Provider 可用性|放行域名只能修复 schema 自洽，不能证明鉴权、API、权限范围、文件读取和审计能力可用。|Phase 2：真实 Provider 集成和端到端验证；Phase 1 不得把 schema 修正表述为生产接入完成。|

## Recommended Next Step

1. 由 Gemini 对本 RESULT 做 REVIEW / DECISION，重点裁定 TASK_017 的“基础能力层”定位是否获准覆盖当前冻结的 Complete Chinese Port v1 口径。
2. 若 Gemini 接受重分类，由 ChatGPT 创建一个窄范围的 Phase 1 RC Alignment EDIT TASK，仅包含：
   - B-1 CI 与 MCP 路径；
   - G-3 命令断链；
   - G-4a WPS schema/占位声明一致性；
   - G-5 文档、manifest、mapping 状态同步；
   - G-1a 命令契约真实性；
   - G-2a agent frontmatter；
   - B-2/B-3/B-4/B-5 的正式阶段登记。
3. 该 EDIT TASK 不应实现 matter workspace、launch automation、跨境用工专业包或 Legal Builder Hub 物理文件操作。
4. Phase 1 修复后重新运行 mandatory CI、MCP 生成一致性检查、全仓 command reference scan、plugin validator、JSON/YAML 解析和文档路径扫描。
5. 将 Phase 1.5 与 Phase 2 项作为独立 backlog artifact 管理，不以空壳文件或“COMPLETE”文案替代实现状态。

如果 Gemini 不接受定位变化，则应沿用 `docs/FAITHFUL_PORT_STANDARD.md` 的冻结规则，B-2 至 B-5 仍是未完成的上游职责，TASK_016 的 `REJECTED` 继续成立，不能用本次分层直接降级其严重性。

## Risk Assessment

| Risk | Impact | Required control |
|---|---|---|
| 冻结治理与 TASK_017 新定位冲突 | 同一版本可能同时声称“Complete Chinese Port”并延后 upstream responsibilities，造成验收口径不可判定。 | Gemini 必须先裁定范围；若接受，后续 EDIT 必须同步 `PROJECT_SCOPE`、标准引用、README、mapping 和 roadmap，或明确将本轮称为 Baseline RC 而非 Faithful Port 完成版。 |
| 仅后移实现、不修正执行性文案 | 用户可能调用实际不会安装、切换、关闭或监控的命令。 | Phase 1 必须收紧 descriptions、argument hints、README 和 manifest 声明。 |
| Workspace 在多个插件分别实现 | 存储路径、active state、archive、保密隔离和 retention 可能不一致。 | Phase 1.5 先定义最小 contract，再做插件字段适配；避免 Phase 1 临时复制。 |
| 为通过 RC 匆忙加入 Builder Hub 写操作 | 可能绕过 allowlist、误改 first-party skill、触发恶意 hooks，或缺少回滚。 | 保持 Phase 2，单独进行权限模型、供应链安全和回滚审计。 |
| WPS schema 修正被误报为数据接入完成 | 域名允许不代表 Provider、鉴权和权限边界有效。 | 把 schema consistency 与 production integration 分开验收。 |
| `.codex-coordination` 继续进入产品回归扫描 | 每次审计产生的历史外国法术语都可能重新使 CI 失败。 | Phase 1 明确排除治理 artifacts，同时保留对实际产品路径的扫描。 |
| Employment expansion 被简单删除 | 失去 upstream diff 追踪和安全转介入口。 | 保留命令/映射记录和中国法侧安全 intake；仅将实质跨境专业能力后移。 |

## Execution Record

- 读取了 TASK_017、TASK_016 RESULT/REVIEW/DECISION、冻结治理标准和指定项目文档。
- 对 B-1 至 B-5、G-1 至 G-5 的当前 CN 文件及相关 upstream 文件进行了只读核对。
- 只读复跑 `python3 scripts/localization-regression.py`，确认 exit code `1`；未运行会写入模块 `.mcp.json` 的生成器。
- 未修改项目文件、插件内容、审计结论或目录结构。
- 未执行 `git add`、`git commit` 或自动修复。
- 本 TASK 唯一写入是本 RESULT artifact。
