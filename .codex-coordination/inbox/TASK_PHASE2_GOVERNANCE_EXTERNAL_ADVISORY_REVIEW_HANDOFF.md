# TASK_PHASE2_GOVERNANCE_EXTERNAL_ADVISORY_REVIEW_HANDOFF

## 0. Document Control

| Field | Value |
|---|---|
| Task | TASK_PHASE2_GOVERNANCE_EXTERNAL_ADVISORY_REVIEW |
| Version | v1.1 APPROVED |
| Status | APPROVED — AUTHORIZED ADVISORY REVIEW |
| Type | Advisory Review Handoff |
| Mode | Advisory Only — No Execution Authority, No Architecture Control |
| Date | 2026-07-22 |
| Author | Architecture Coordinator |
| Source Directive | Project Owner directive (2026-07-22) |

---

## 1. Task Identity

### 1.1 Task Name

```text
TASK_PHASE2_GOVERNANCE_EXTERNAL_ADVISORY_REVIEW
```

### 1.2 Task Objective

对已采纳的 `LEGAL_REASONING_GOVERNANCE_PATTERN v1.0`（Canonical Governance Asset）进行独立外部审查（Independent External Advisory Review），在进入 Route A（OCR 基础设施）或 Route B（C03 执行案对抗设计）之前，验证治理模型的结构完整性、长期稳定性和领域适用性。

### 1.3 Task Nature

```text
Advisory Only

第三方角色：
  - CAN:    Review / Challenge / Provide Advisory Opinions
  - CANNOT: Modify State / Authorize Execution / Close Tasks / Edit Governance Assets
```

### 1.4 Rationale

Project Owner 判断：

> Governance Pattern 已成为整个系统的"宪法层"。后续 OCR、执行案件、公司责任、MCP 等所有实施均依赖于它。在此阶段发现问题，成本最低。

---

## 2. Review Object Binding

### 2.1 Primary Review Object

| Attribute | Value |
|---|---|
| Document | `LEGAL_REASONING_GOVERNANCE_PATTERN.md` |
| Path | `docs/phase2/governance/LEGAL_REASONING_GOVERNANCE_PATTERN.md` |
| Version | v1.0 Canonical |
| Status | ADOPTED — CANONICAL GOVERNANCE ASSET |
| Adoption Date | 2026-07-22 |
| Source Draft SHA-256 | `95199F93877966458A29EFD6ABF6F83459C62AC7D59E5402825FB5B662B2C724` |

### 2.2 Upstream Binding

本审查对象所依赖的完整上游基线：

| Stage | Status | Artifact Type |
|---|---|---|
| C02-I Request Right Validation | CLOSED / DONE | Spec + Result |
| C02-II Request Right Framework Design | CLOSED / DONE | Spec + Result |
| C02-III Request Right Validation Enhancement | CLOSED / DONE | Spec + Result |
| C02-IV Input Readiness Design | CLOSED / DONE | Spec + Result |
| Governance C01 Pattern Extraction | CLOSED / DONE | Draft → Canonical |

---

## 3. External Advisory Layer Architecture

### 3.1 ACOS Position

```text
                Project Owner
                      │
              Final Decision
                      │
        ┌─────────────┼─────────────┐
        │                           │
Architecture Coordinator    Codex Executor
        │
        │
External Advisory Reviewer
(Expert / Counsel / Specialist)
```

### 3.2 Governance Constraints

External Advisory Reviewer 的权限边界：

| Permission | Status |
|---|---|
| Read Canonical Governance Pattern | ✅ GRANTED |
| Read upstream Spec/Result artifacts | ✅ GRANTED |
| Issue advisory opinions / challenge reports | ✅ GRANTED |
| Propose amendments to Governance Pattern | ✅ GRANTED (advisory only) |
| Modify Governance Pattern directly | ❌ PROHIBITED |
| Modify ACOS coordination state | ❌ PROHIBITED |
| Authorize Route A / Route B / any execution | ❌ PROHIBITED |
| Close tasks or issue decisions | ❌ PROHIBITED |
| Access case materials (CASE-A/B/C) | ❌ PROHIBITED |
| Modify Skills / Agents / MCP / Code | ❌ PROHIBITED |

### 3.3 Advisory Workflow

```text
Phase 1: Architecture Coordinator 准备 Review Package
              ↓
Phase 2: External Advisory Reviewer 独立审查
              ↓
Phase 3: External Advisory Review Report 提交
              ↓
Phase 4: Architecture Coordinator 收录审查意见
              ↓
Phase 5: Project Owner 决策（采纳 / 部分采纳 / 记录但不采纳）
              ↓
Phase 6: 如需修正 → Governance Pattern Amendment（需完整 ACOS 治理流程）
              ↓
Phase 7: Route A / Route B Authorization Decision
```

---

## 4. Review Dimensions & Question Checklist

### 4.1 Dimension A — 法律推理逻辑完整性

审查是否符合法律推理的专业逻辑：

| # | Review Question |
|---|---|
| A-1 | Evidence → Fact → Legal Fact 推演链是否完整？是否存在逻辑跳跃？ |
| A-2 | 是否混淆事实认定（fact-finding）与法律评价（legal characterization）？ |
| A-3 | 证明责任（burden of proof）模型是否完整？是否覆盖举证责任分配、举证标准、举证期限？ |
| A-4 | 抗辩结构（defense / rebuttal）是否被充分治理？是否存在遗漏？ |
| A-5 | 请求权基础分析（claim basis analysis）与要件映射（element mapping）是否合理？ |
| A-6 | 是否支持中国民商事诉讼特有的证明责任倒置、推定、免证事实等规则？ |

### 4.2 Dimension B — AI Agent 系统治理原则

审查是否符合 Agentic Workflow 最佳实践：

| # | Review Question |
|---|---|
| B-1 | Human Decision Gate（LRG-05）是否足够？是否存在绕过路径？ |
| B-2 | 是否存在自动法律结论生成风险（auto-conclusion risk）？ |
| B-3 | 是否存在幻觉传播链（hallucination propagation chain）？即上游幻觉被下游层级合法化？ |
| B-4 | Agent 边界控制是否清晰？工具授权（Tool Use）是否受控？ |
| B-5 | Memory / Context 隔离（LRG-00 Matter Isolation）是否足够？ |
| B-6 | SUPPORTED / UNKNOWN / BLOCKED 三状态是否充分？是否需要更细粒度？ |

### 4.3 Dimension C — 领域可扩展性

审查当前模型能否支撑后续法律领域扩展：

| # | Review Question |
|---|---|
| C-1 | 当前模型（请求权分析）是否能扩展到执行案件（enforcement）？ |
| C-2 | 是否能扩展到公司责任（corporate liability）？ |
| C-3 | 是否能扩展到破产案件（bankruptcy）？ |
| C-4 | 是否能扩展到侵权案件（tort liability）？ |
| C-5 | 扩展是否需要重新设计（breaking change）还是仅需 Adapter？ |
| C-6 | 是否需要增加：Counterargument Model / Burden of Proof Model / Litigation Strategy Layer？ |

### 4.4 Dimension D — 中国大陆法律场景适配

审查是否适合中国大陆法律实务：

| # | Review Question |
|---|---|
| D-1 | 是否依赖普通法概念？是否存在未清除的普通法残留？ |
| D-2 | 是否符合中国法律职业道德规范关于律师保密义务的要求？ |
| D-3 | 案例治理是否正确区分了指导性案例与参考性案例的效力差异？ |
| D-4 | 是否适配中国诉讼证据规则（《民事诉讼法》《最高人民法院关于民事诉讼证据的若干规定》）？ |
| D-5 | 是否支持中国特有的诉讼程序（如庭前会议、举证期限、证据交换）？ |

### 4.5 Dimension E — 诉讼实务落地适配性 (Litigation Practice Operational Fit)

审查治理模型是否能真正辅助律师业务工作流：

| # | Review Question |
|---|---|
| E-1 | 是否能辅助律师自动/半自动形成标准化证据目录与证据说明？ |
| E-2 | 是否能辅助律师识别调查取证需求并生成法院调查令申请书草案？ |
| E-3 | 是否能精准识别要件证明缺口并给出调查/补强指引？ |
| E-4 | 是否能支持多重诉讼策略与请求权基础的对比与风险提示？ |
| E-5 | 治理流程是否符合中国执业律师在真实办案中的工作习惯与审慎原则？ |

---

## 5. Reviewer Categories

### 5.1 Category 1 — 法律 AI 架构审查（Priority: HIGH）

| Attribute | Value |
|---|---|
| Target Profile | 法律科技研究人员 / 法学院法律 AI 方向 / 法律产品团队 |
| Review Focus | Dimension A + B |
| Expected Output | External Governance Review Report |
| Output Format | 结构性审查意见（非代码） |

### 5.2 Category 2 — AI Agent / LLM 架构专家

| Attribute | Value |
|---|---|
| Target Profile | Agentic Workflow 设计 / LLM 系统工程 / Human-in-the-loop 研究 |
| Review Focus | Dimension B |
| Expected Output | Agent Architecture Advisory Report |
| Output Format | 结构性审查意见 + 架构建议 |

### 5.3 Category 3 — 诉讼实务专家（Value: HIGHEST）

| Attribute | Value |
|---|---|
| Target Profile | 民商事诉讼律师 / 执行律师 / 公司争议律师 |
| Review Focus | Dimension A + C + D |
| Expected Output | Practice Validation Report |
| Output Format | 实务场景测试反馈 + 缺陷清单 |

### 5.4 Exclusions — 当前阶段不引入

| Category | Reason |
|---|---|
| 普通 AI 顾问 | 缺乏法律推理知识，仅能评价技术/Prompt/Agent |
| 软件开发团队 | 当前瓶颈是"实现什么"而非"怎么实现"，过早开发导致错误模型固化 |
| OCR 厂商 | C02-IV 已确认 OCR 是基础设施不是核心逻辑，当前缺的是 Evidence Governance 不是 OCR API |

---

## 6. Deliverable Specification

### 6.1 Review Package（Architecture Coordinator 准备）

| Item | Description |
|---|---|
| LEGAL_REASONING_GOVERNANCE_PATTERN v1.0 | 完整正本文档 |
| Review Question Checklist | 本 Handoff §4 问题清单 |
| Upstream Stage Summary | C02-I ~ C02-IV + Governance C01 阶段总结（不含案件材料） |
| Known Limitations | C02-I BLOCKED 状态说明、OCR 缺口说明 |

### 6.2 Expected Output（External Advisory Reviewer 提交）

| Item | Description |
|---|---|
| External Advisory Review Report | 结构性审查报告，按 Dimension A/B/C/D 分节 |
| Defect List | 已识别的结构性缺陷清单（如有） |
| Amendment Proposals | 建议修订事项（advisory only，不直接修改） |
| Scope Expansion Assessment | 是否需要 breaking change 的评估 |

### 6.3 Non-Deliverables

| Item | Reason |
|---|---|
| Code | 本阶段不产出代码 |
| Skill / Agent modifications | 不授权 |
| MCP configuration changes | 不授权 |
| Case material access | 案件材料不向 External Reviewer 开放 |

---

## 7. Governance Constraints

### 7.1 Zero Code Drift

```text
本任务执行期间：
  - 不修改任何 Skill / Agent / Hook / MCP
  - 不修改 litigation-legal/ 或其他插件代码
  - 不创建新的 runtime / database / API
  - 仅产出文档级审查报告
```

### 7.2 Governance Pattern Immutability

```text
LEGAL_REASONING_GOVERNANCE_PATTERN v1.0 在 External Review 期间保持不变。
任何修订必须通过完整 ACOS Amendment 流程：
  Amendment Proposal → Architecture Review → Project Owner Decision → New Version
```

### 7.3 Case Material Isolation

```text
External Reviewer 不访问 CASE-A / CASE-B / CASE-C 材料。
审查仅基于治理模型文档本身。
```

---

## 8. Post-Review Decision Path

```text
External Advisory Review Report
            ↓
    ┌───────┼───────┐
    │       │       │
  No       Some    Critical
  Issues   Issues  Issues
    │       │       │
    ↓       ↓       ↓
  Route    Amend   Major
  A/B      then    Redesign
  Auth     Route   Required
            A/B
```

### Decision Authority

所有 Post-Review 决策由 **Project Owner** 做出，外部审查报告仅作为输入。

---

## 9. Success Criteria

| # | Criterion |
|---|---|
| SC-1 | External Advisory Review Report 至少覆盖 Dimension A 和 Dimension B |
| SC-2 | 报告包含明确的 Pass / Conditional Pass / Fail 结论 |
| SC-3 | 所有识别的缺陷均有严重性分级（Critical / Major / Minor / Advisory） |
| SC-4 | Amendment Proposals（如有）以独立条目形式提交，可逐条评估 |
| SC-5 | 报告不包含代码、Skill 修改或执行授权 |
| SC-6 | Review Package 不包含案件材料 |

---

## 10. ACOS Coordination

### Required Approvals

| Step | Approver |
|---|---|
| Handoff Architecture Review | Architecture Coordinator |
| Handoff Decision | Project Owner |
| Review Package Preparation | Architecture Coordinator |
| External Review Execution | External Advisory Reviewer |
| Review Report Acceptance | Architecture Coordinator + Project Owner |
| Post-Review Route Authorization | Project Owner |

### Task Lifecycle

```text
Handoff (CURRENT)
    ↓
Architecture Review
    ↓
Project Owner Decision
    ↓
Review Package Preparation
    ↓
External Advisory Review Execution
    ↓
Review Report Submission
    ↓
Architecture Coordinator Reception
    ↓
Project Owner Post-Review Decision
    ↓
Route Authorization (or Amendment)
```
