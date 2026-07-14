# Phase 1 Baseline Freeze Review（Phase 1.5 启动前快照）

状态：`HISTORICAL SNAPSHOT / PASS_WITH_OBSERVATIONS`

审查日期：2026-07-14

审查仓库：`/Users/zhang/Documents/claude-for-legal-cn`

审查基线：`main` / `e14205e`（与本地 `origin/main` 跟踪引用一致）

> 本文只记录 `e14205e` 在 Phase 1.5 启动前的冻结状态，不是 ACOS TASK artifact，也不占用 `TASK_019` 编号。当前 Phase 1.5 实施与验证证据以 `.codex-coordination/outbox/TASK_019_PHASE1_5_WORKSPACE_RECOVERY_RESULT.md` 及其后续 Gemini REVIEW/DECISION 为准。

## 1. 结论

`claude-for-legal-cn` **已经达到 `PHASE1_BASELINE_FREEZE` 条件**，判定为：

> **PASS_WITH_OBSERVATIONS — Phase 1 中国法基线可冻结，但仍有少量不影响运行的声明、元数据和文档一致性观察项。**

本结论所称“完成”仅指 `docs/PROJECT_SCOPE.md` 与 `TASK_017` 重分类后定义的 Phase 1 Baseline：

- 12 个第一方中国法插件根级可发现；
- 中国大陆法默认语境、人工复核门和外部 vendor 隔离有效；
- Mandatory CI、命令引用、MCP 生成源、JSON/YAML、Agent/Skill 元数据和文档主状态可验证；
- Phase 1.5 本地状态化工作流及 Phase 2 真实 Provider/外部自动化已明确后移，未被虚报为 Phase 1 已实现。

本结论不表示 Matter Workspace、真实法律数据库连接、外部自动监控、跨境专业包或 Legal Builder Hub 物理安装能力已经完成。

## 2. 项目边界与审查范围

### 2.1 纳入范围

- 12 个根级第一方插件；
- 插件 Skills、Agents、references、manifest、`.mcp.json` 和 hooks；
- 根级 `references/`、`docs/`、`scripts/`、`connectors/legal-data/`；
- 5 个 `managed-agent-cookbooks/`；
- Marketplace、MCP 生成源、CI 和 Phase 1 治理文档；
- `TASK_016` 至 `TASK_018` 的项目内审计证据。

### 2.2 排除范围

- Phase 1.5 新功能开发；
- Matter Workspace、tracker、history 或 lifecycle 的实现；
- 真实北大法宝、威科、法院、WPS、工商、执行等 Provider 接入；
- 外部定时监控、通知或自动提交；
- ACOS 或其他项目的架构、代码和运行机制；
- `/Users/zhang/Documents/Playground/claude-for-legal-cn` 与 Downloads 中的旧副本。

`.codex-coordination/` 在本报告中仅作为本项目既有任务审计记录读取，不作为法律产品运行层，也不据此把 ACOS 纳入 `claude-for-legal-cn`。

本次基线审查未修改任何 Agent、Skill、插件、连接器、配置或运行逻辑；本文保留为后续阶段对比快照。

## 3. Git 与 TASK_018 闭环状态

| 项目 | 实际状态 |
|---|---|
| 当前分支 | `main` |
| 审查 HEAD | `e14205e` |
| 本地跟踪状态 | 审查开始时 `main...origin/main`，无 ahead/behind、无 staged/tracked/untracked 变更 |
| HEAD 提交 | `feat(coordination): align manifests, fix regression CI, and resolve broken command links for Phase 1 RC` |
| TASK_018 task | 存在：`.codex-coordination/inbox/TASK_018_PHASE1_ALIGNMENT_EDIT.md` |
| TASK_018 result | 存在：`.codex-coordination/outbox/TASK_018_PHASE1_ALIGNMENT_EDIT_RESULT.md` |
| TASK_018 review | 存在，结论 `ACCEPTED` |
| TASK_018 decision | 存在，结论 `ACCEPTED`，状态记为 `Valid (RC 状态，已冻结)` |
| 物理提交 | TASK_018 修改、审查和决策均已进入 `e14205e`；不是仅存在于未提交工作区 |

## 4. Phase 1 实际目录与资产盘点

### 4.1 12 个第一方根模块

所有 12 个模块均存在：

- `.claude-plugin/plugin.json`；
- `.mcp.json`；
- `README.md`；
- `CLAUDE.md` 实践画像模板；
- `skills/`；
- `references/test-cases-cn.md`。

| 模块 | 根级 Skills | Agents | 模块 references | hooks.json |
|---|---:|---:|---:|---|
| `ai-governance-legal` | 11 | 0 | 3 | 无（允许） |
| `commercial-legal` | 11 | 3 | 12 | 有 |
| `corporate-legal` | 17 | 1 | 3 | 有 |
| `employment-legal` | 23 | 1 | 1 | 有 |
| `ip-legal` | 12 | 1 | 2 | 有 |
| `law-student` | 13 | 0 | 1 | 有 |
| `legal-builder-hub` | 10 | 1 | 2 | 有 |
| `legal-clinic` | 16 | 0 | 2 | 有 |
| `litigation-legal` | 23 | 1 | 2 | 无（允许） |
| `privacy-legal` | 9 | 0 | 3 | 有 |
| `product-legal` | 7 | 1 | 2 | 有 |
| `regulatory-legal` | 9 | 1 | 1 | 有 |
| **合计** | **161** | **10** | **34** | **10/12** |

另有 7 个 `corporate-legal/phase-2/skills/` 历史实现文件，由根级 wrapper 暴露；因此仓库内第一方 `SKILL.md` 物理文件总数为 168，但根级可发现 Skill 数为 161。这里的 `corporate-legal/phase-2/` 是历史存储路径，不代表对应能力仍处于 Phase 2。

### 4.2 用户指定结构类别的实际映射

| 类别 | 仓库实际实现 | 结论 |
|---|---|---|
| `plugins` | 无单独 `plugins/` 容器；12 个第一方插件直接位于根目录，由 `.claude-plugin/marketplace.json` 注册 | 符合当前仓库架构 |
| `agents` | 分布于 8 个插件的 `agents/`，共 10 个 Agent 文件 | 10/10 frontmatter 有效 |
| `skills` | 分布于各插件 `skills/<name>/SKILL.md`；161 个根级可发现，168 个物理文件 | 161/161 根级 Skill frontmatter/name 有效 |
| `commands` | 没有独立 `commands/` 目录；Claude 插件命令由 Skill 名称暴露 | 属于设计选择，不是缺失 |
| `references` | 根 `references/` 有 10 个共享文件；各模块有专项 references 和 12/12 中国法测试用例 | 基线完整 |
| `docs` | `docs/` 原有 5 个治理/审计文件，另有根级 README、QUICKSTART、ROADMAP、状态与使用指南 | 主状态已与 12 根模块同步 |
| `mcp` | 无独立 `mcp/` 目录；12 份 `.mcp.json` 由 `scripts/mcp-template.json`、`scripts/mcp-modules.json` 和生成器维护 | 12/12 生成一致；真实 Provider 未接入 |
| `schemas` | 无独立 `schemas/` 目录；存在 2 个命名 schema 文件，cookbook 的输出 schema 嵌入各 YAML | 当前验证通过；不等同于通用 Agent Framework Schema |
| `configs` | Marketplace、12 个 plugin manifest、MCP 生成源、cookbook YAML/JSON 和模块画像模板分布式管理 | 当前格式有效 |

## 5. 当前 HEAD 重新验证结果

以下验证均在 2026-07-14 针对 `e14205e` 重新执行，不仅引用 TASK_018 的历史结果。

| 验证 | 结果 |
|---|---|
| `claude plugin validate .claude-plugin/marketplace.json` | PASS |
| 12 个第一方插件 validator | 12/12 PASS；每个仅有预期的根 `CLAUDE.md` 模板加载 warning |
| `python3 scripts/localization-regression.py` | PASS：`China localization regression OK` |
| `python3 scripts/generate-mcp-configs.py --check` | PASS：12/12 `.mcp.json` |
| 全仓 JSON 解析 | PASS：49 files |
| 全仓 YAML 解析 | PASS：38 files |
| 根级 Skill frontmatter/name | PASS：161/161 |
| 第一方 Agent frontmatter | PASS：10/10 |
| 第一方跨插件命令引用 | PASS：444 references，0 unresolved |
| `python3 scripts/lint-tool-scope.py` | PASS：5/5 cookbooks |
| `bash scripts/test-cookbooks.sh` | PASS：5/5 cookbooks |
| `bash scripts/test-legal-data.sh` | PASS |
| `git diff --check` | PASS |
| 断裂符号链接 | 未发现 |

插件 validator 关于根 `CLAUDE.md` “不会作为项目上下文自动加载”的 warning 是当前模板式实践画像架构的已知行为，不是解析失败；实践画像由 cold-start 流程写入用户配置目录，正式结论仍应以人工复核门为准。

## 6. 已完成并可冻结的能力

1. **12 根模块恢复与发现性**：`law-student`、`legal-clinic` 已在根级 Marketplace 中，不再依赖旧 `phase-2/` 路径。
2. **中国法默认框架**：第一方插件默认采用中国大陆法律、监管和裁判语境，并保留涉外提示模式。
3. **案例权威层**：根 references 已提供可更新案例来源、案例权威说明和 MCP 示例；未把案例误作普通法先例。
4. **外部 vendor 隔离**：`external_plugins/cocounsel-legal` 未进入默认 Marketplace。
5. **Skill/Agent 基线**：161 个根级 Skill 与 10 个 Agent 的基础元数据、发现性和引用关系通过验证。
6. **MCP 基线**：12 个模块配置由统一生成源维护；`legal-data` 是可运行的本地样例服务器，其他企业/商业 Provider 均如实保持占位。
7. **CI 与 smoke tests**：中国化回归、本地 legal-data、cookbook smoke test 和 JSON sanity 已进入 CI 或可本地复跑。
8. **阶段治理**：Phase 1、Phase 1.5 与 Phase 2 责任边界已写入 `PROJECT_SCOPE`、mapping matrix 和 roadmap。

## 7. 缺陷与观察项

以下项目均未在本任务中修复。

### O-01：根 `AGENTS.md` 与实际模板/配置路径不一致（新增发现）

严重性：`P1 Documentation / 非运行阻塞`

- `AGENTS.md` 的 Layout 和“Plugin AGENTS.md”章节声称每个插件存在 `<plugin>/AGENTS.md`，但实际 12 个插件均使用 `<plugin>/CLAUDE.md`，不存在任何插件级 `AGENTS.md`。
- `AGENTS.md` 写入路径使用 `~/.claude/plugins/config/claude-for-legal-cn/...`；根 `CLAUDE.md`、QUICKSTART 和插件内容一致使用 `~/.claude/plugins/config/claude-for-legal/...`。全仓仅该处出现 `claude-for-legal-cn` 配置路径，而 `claude-for-legal/` 路径出现 168 次。
- 该问题不会破坏当前 Marketplace、Skill、Agent 或 MCP 运行，但会误导后续 Codex 贡献者，建议在 Phase 1.5 开发前以独立文档微修任务处理。

### O-02：Marketplace 与 manifest 的 description 不完全一致

严重性：`Observation / 已由 TASK_018 接受为非阻塞`

以下 4 个模块违反仓库“field-for-field”同步约定，但不影响 validator：

- `product-legal`；
- `legal-builder-hub`；
- `law-student`；
- `legal-clinic`。

### O-03：Legal Builder Hub 仍有旧阶段与执行性措辞

严重性：`Observation / 已由 TASK_018 接受为非阻塞`

- manifest 仍使用版本 `2.0.0-cn-phase2` 和 `Phase 2` 描述；
- README 仍称“第一序列”并使用安装、禁用、更新等执行性措辞；
- `skill-installer`、`disable`、`uninstall` 的 description 比正文的“仅生成计划/记录、人工执行”更强。

当前物理安装、覆盖、回滚、禁用、卸载与远程 registry sync 仍属于 Phase 2，不能把这些文案当作已实现证据。

### O-04：Matter Workspace 阶段标签与命令契约仍有残留

严重性：`Observation / 已由 TASK_018 接受为非阻塞`

- `product-legal`、`ip-legal` 的 matter-workspace metadata 仍称 `Phase 2 placeholder`，而已接受的阶段账本把本地 matter lifecycle 归入 Phase 1.5；
- `commercial-legal:matter-workspace` 仍声明 `new/list/switch/close/none`，正文只提供静态档案字段和输出模板，没有定义持久化与 active matter 生命周期。

这些命令不得在 Phase 1 冻结说明中被解释为已完成状态化工作流。

### O-05：插件根 `CLAUDE.md` validator warning

严重性：`Expected warning`

12 个插件均提示根 `CLAUDE.md` 不会自动作为项目上下文加载。当前设计把它作为 cold-start 的实践画像模板，validator 仍返回成功；如果未来要求模板随插件自动注入上下文，需要另行设计，不能在本任务中移动文件。

### O-06：本地空 `phase-2/` 目录

严重性：`Local-only observation`

仓库工作目录存在一个空的根 `phase-2/` 目录，但 Git 不跟踪空目录，`git ls-files phase-2` 无结果。它不是基线内容，也不影响构建或 Marketplace。

## 8. 明确延后事项

### 8.1 Phase 1.5 Legal Workflow Layer

- 统一的本地 tracker/workspace 最小 contract；
- Product 本地 launch tracker 与人工触发 review queue；
- Product、IP、commercial、privacy、employment 的 opt-in matter lifecycle；
- Commercial agents 的本地 persistence、阈值、历史和去重；
- owner/status/deadline/history/archive 等本地状态语义。

### 8.2 Phase 2 Advanced Integration / External Capability

- 北大法宝、威科、法院/仲裁、工商、执行、WPS 等真实 Provider 与端到端鉴权；
- 外部系统自动监控、定时触发和通知投递；
- Employment 跨境用工、EOR、目标法域税务/移民及当地律师协作专业包；
- Legal Builder Hub 物理安装、更新、回滚、禁用、卸载和远程 registry sync；
- 会改变本机、外部系统或正式法律程序状态的自动动作。

## 9. 当时建议的 Phase 1.5 进入条件

以下是该快照形成时提出的入口条件；后续是否满足应以正式 TASK RESULT 与 Gemini DECISION 为准：

1. 以 `e14205e` 作为 Phase 1 冻结基线，并在任务记录中固定 commit；如需 tag，由项目所有者另行决定。
2. 将 O-01 至 O-04 保留为明确 backlog；其中 O-01 宜在首个 Phase 1.5 功能提交前通过窄范围文档任务修正。
3. Phase 1.5 第一项工程任务应先定义共享的本地 workspace/tracker contract，再由各法律模块做字段适配，避免复制多套不兼容实现。
4. Phase 1.5 仅允许本地、人工触发、可审计的状态化行为；真实 Provider、外部定时任务、通知和物理技能操作不得混入。
5. 每个 lifecycle 必须定义数据位置、active 状态、archive/close 语义、保密隔离、人工确认门和失败恢复方式。
6. 新实现必须继续通过当前 Phase 1 回归、插件验证、命令引用、JSON/YAML、MCP 生成一致性和 cookbook/legal-data smoke tests。
7. ACOS 如被用于任务编排，仅作为独立开发基础设施；不得把其角色、状态机或代码写成 `claude-for-legal-cn` 的法律业务能力。

## 10. 最终建议

建议正式记录：

```text
PHASE1_BASELINE_FREEZE = YES
FREEZE_COMMIT = e14205e
REVIEW_VERDICT = PASS_WITH_OBSERVATIONS
PHASE1_5_DEVELOPMENT_AT_SNAPSHOT = NOT STARTED
```

本报告不是 Phase 1.5 开发授权。Phase 1.5 后续已由独立的 `TASK_019_PHASE1_5_WORKSPACE_RECOVERY` 接管；不得用本快照替代该任务的 RESULT、REVIEW 或 DECISION。
