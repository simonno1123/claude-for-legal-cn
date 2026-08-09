# TASK_PHASE3_TRACK_B_FACT_SCHEMA_GOVERNANCE_HANDOFF

## Status

ACCEPTED — ARCHITECTURE REVIEW PASSED


## Phase Identification

Phase:
PHASE 3

Track:
Track B

Name:
FACT SCHEMA GOVERNANCE

Deliverable Type:
HANDOFF ONLY


## Authorization Basis

Project Owner Decision:

FACT SCHEMA GOVERNANCE HANDOFF MATERIALIZATION AUTHORIZED

Confirmed Architecture Identity:

```text
Phase: PHASE 3
Track: Track B
Name: FACT SCHEMA GOVERNANCE
```

Authorization Limit:

仅允许物化本 Handoff。

本授权不包括 Fact Schema Design、具体 Schema、YAML、JSON、`fact.yaml`、数据库结构、API 结构、实现代码或任何法律事实生成。


## Objective

建立法律 AI 系统中的 Fact Schema Governance 交接边界。

本阶段的目标不是创建事实 Schema，而是为未来可能获授权的 Schema Governance Design 建立架构审查入口。

本 Handoff 仅确认：

- Fact Schema Governance 的系统位置；
- 与 Fact Construction Governance 的依赖关系；
- 未来设计必须遵守的治理原则；
- Schema 表达不得破坏事实状态、争议、不确定性和追溯关系；
- Schema Design、Schema Materialization 与 Implementation 必须分别授权。


## Architectural Position

本 Track 位于：

Fact Construction Governance

与

Legal Fact Isolation Boundary

之间。

```text
Evidence Governance Layer
        |
        v
Fact Construction Governance
        |
        v
Fact Schema Governance
        |
        v
Legal Fact Isolation Boundary
        |
        v
Legal Fact Layer
        |
        v
Request Right Foundation
```

Fact Schema Governance 只负责未来结构表达的治理边界。

它不得：

- 替代 Evidence Governance；
- 形成或验证事实；
- 将 Fact 直接提升为 Legal Fact；
- 调用 Request Right Foundation；
- 自动启动实现。


## Relationship With Previous Track

### Phase 3 Track A

Name:
FACT CONSTRUCTION GOVERNANCE

Final State:

```text
Governance Handoff: CLOSED
Governance Design Spec: ACCEPTED
Governance Design Result: ACCEPTED
```

Track A 已建立：

- Evidence ≠ Fact；
- Fact ≠ Legal Fact；
- Fact 生命周期；
- Confirmed、Disputed、Unknown 的状态保留；
- Human Validation Gate；
- Evidence → Fact 转换治理；
- Fact → Legal Fact 硬隔离；
- fail-closed、追溯与重新验证。


### Phase 3 Track B

Name:
FACT SCHEMA GOVERNANCE

Current State:

HANDOFF ACCEPTED — ARCHITECTURE REVIEW PASSED

Track B 未来如获授权，只能治理“如何忠实表达已治理事实状态”，不得重新决定事实是否成立。


## Governing Distinctions

```text
Evidence ≠ Fact

Fact Construction ≠ Fact Schema

Fact Schema Governance ≠ Fact Schema

Fact Schema ≠ Legal Fact

Schema Design Authorization ≠ Schema Materialization Authorization

Schema Materialization Authorization ≠ Implementation Authorization
```


## Core Principles

### FS-G-001 Governance Handoff ≠ Schema

本 Handoff 不是 Fact Schema。

不得从本 Handoff 推导、创建或补全任何具体字段、对象、枚举、YAML、JSON、数据库表或 API 数据结构。


### FS-G-002 Schema Must Not Create Facts

未来任何 Schema 仅可表达经过 Fact Construction Governance 管理的事实状态。

Schema 不得：

- 生成事实；
- 验证事实；
- 推测事实；
- 合并争议事实；
- 将 Unknown 自动补全为确定值；
- 将结构完整性误认为事实真实性。


### FS-G-003 State Fidelity

未来治理设计必须保持以下事实处置的语义差异：

- Confirmed；
- Disputed；
- Unknown；
- Rejected / Out of Scope；
- Return for Revalidation；
- Superseded / Revalidation Required。

任何结构表达不得将这些状态静默折叠为单一“事实存在”结论。


### FS-G-004 Dispute and Unknown Preservation

Schema Governance 必须保留争议与未知。

禁止：

- 以空值替代 Unknown 的治理含义；
- 以单一值覆盖竞争事实版本；
- 以默认值消除信息缺口；
- 以置信度自动替代人工验证结论；
- 因结构约束而丢弃 Disputed 状态。


### FS-G-005 Traceability Preservation

未来结构治理必须允许事实状态保持对以下治理链的可追溯性：

```text
Fact State
    ↓
Construction / Validation Decision
    ↓
Verified Evidence Reference
    ↓
Evidence Governance Verification
```

本原则仅规定追溯要求，不授权定义追溯字段或数据结构。


### FS-G-006 Human Validation Preservation

Schema 不得把 Human Validation Gate 转换为自动状态规则。

任何结构约束、默认行为或技术校验不得：

- 自动授予 Confirmed；
- 自动消除 Disputed；
- 自动补全 Unknown；
- 自动批准 Return for Revalidation；
- 自动批准进入 Legal Fact Candidate — Isolated。


### FS-G-007 Objective Fact / Legal Fact Isolation

未来 Fact Schema Governance 必须维持：

```text
Objective Fact ≠ Legal Fact Candidate ≠ Legal Fact
```

不得在 Fact Schema 中嵌入或预设：

- 法律要件匹配；
- 法律关系判断；
- 责任认定；
- Request Right；
- 诉讼策略；
- 胜诉预测。


### FS-G-008 Revalidation and Revocation

未来结构治理必须允许证据撤回、证据变化、新冲突或人工决定撤销引发事实重新验证。

Schema 不得使已验证状态不可撤销，也不得通过静态复制规避上游失效。


### FS-G-009 Fail-Closed

当事实状态、来源资格、追溯链、人工审核或授权无法确认时，未来治理设计必须阻断结构化发布或下游使用。

技术可用性不得替代治理资格。


### FS-G-010 No Automatic Escalation

本 Handoff 的物化、Review 或接受均不得自动授权：

- Fact Schema Governance Design；
- Fact Schema；
- `fact.yaml`；
- Implementation；
- Real Matter Analysis；
- Legal Fact Generation；
- Request Right Foundation；
- 任何后续 Track 或 Phase。


## Authorized Scope

本 Handoff 仅授权：

1. Handoff Materialization；
2. Architecture Review；
3. Fact Schema Governance Design Preparation。

Design Preparation 仅表示可识别未来设计问题，不表示 Design 已获授权。


## Not Authorized

以下行为继续禁止：

1. 创建 Fact Schema；
2. 创建或修改 `fact.yaml`；
3. 定义具体字段、字段类型、必填规则或默认值；
4. 定义 YAML、JSON、数据库或 API 数据结构；
5. 设计或编写 Agent、Skill、工具或代码；
6. 修改 Fact Construction Governance 已接受的状态定义；
7. 修改 Evidence Registry；
8. 导入真实案件材料；
9. 创建真实或模拟案件事实实例；
10. 自动提取案件事实；
11. 生成或推导 Legal Fact；
12. 推导 Request Right；
13. 生成诉讼策略或胜诉预测；
14. 自动进入 Schema Design、Schema Materialization 或 Implementation；
15. 创建本 Track 的 SPEC 或 RESULT。


## Expected Future Artifacts

仅在 Project Owner 另行明确授权后，方可创建：

TASK_PHASE3_TRACK_B_FACT_SCHEMA_GOVERNANCE_SPEC.md

TASK_PHASE3_TRACK_B_FACT_SCHEMA_GOVERNANCE_RESULT.md

本节仅登记可能的未来资产名称，不构成创建授权。


## Architecture Review Questions

Architecture Review 仅可评估：

1. Track B 的架构位置是否正确；
2. Track A 的已接受治理状态是否被完整继承；
3. Schema Governance 与 Schema Materialization 是否充分分离；
4. Confirmed、Disputed、Unknown 是否能够被忠实保留；
5. Traceability 与 Human Validation Gate 是否被保留；
6. Objective Fact 与 Legal Fact 是否继续硬隔离；
7. Schema 是否被禁止创造、验证或补全事实；
8. 下游接口是否保持未激活；
9. 是否存在真实案件、Schema、实现或法律推理污染；
10. 是否存在自动阶段升级。

Architecture Review 不得借审查之名创建 Schema 或实现设计。


## Acceptance Gates

### FS-H-001 Phase and Track Boundary

Phase 3 Track B 的身份及范围明确。


### FS-H-002 Track A Dependency Integrity

Fact Construction Governance 的已接受原则、状态和门禁未被改写。


### FS-H-003 Governance / Schema Separation

Fact Schema Governance 与具体 Fact Schema 被明确分离。


### FS-H-004 State Fidelity

Confirmed、Disputed、Unknown 及重新验证状态得到保留。


### FS-H-005 Traceability Preservation

未来 Schema Governance 不得切断 Fact 至 Verified Evidence 与 Human Validation 的追溯链。


### FS-H-006 Human Gate Preservation

Schema 不得替代或自动化关键人工决定。


### FS-H-007 Fact / Legal Fact Separation

Objective Fact、Legal Fact Candidate 与 Legal Fact 继续保持硬隔离。


### FS-H-008 No Schema Materialization

未创建 `fact.yaml`、字段定义、YAML、JSON、数据库或 API 结构。


### FS-H-009 No Implementation

未创建 Agent、Skill、工具、代码或部署设计。


### FS-H-010 No Real Matter Pollution

未导入或分析任何真实案件材料。


### FS-H-011 No Legal Reasoning

未生成 Legal Fact、Request Right、诉讼策略或胜诉预测。


### FS-H-012 No Automatic Escalation

Handoff 的物化和 Review 不自动授权 Design、Schema、Implementation 或后续阶段。


## Artifact Boundary

本次授权仅新增：

TASK_PHASE3_TRACK_B_FACT_SCHEMA_GOVERNANCE_HANDOFF.md

不得新增：

- TASK_PHASE3_TRACK_B_FACT_SCHEMA_GOVERNANCE_SPEC.md；
- TASK_PHASE3_TRACK_B_FACT_SCHEMA_GOVERNANCE_RESULT.md；
- `fact.yaml`；
- 任何 YAML、JSON、数据库或 API Schema；
- 任何 Agent、Skill、工具或代码；
- 任何案件事实或法律事实资产。


## Current System State

```text
Phase 3 Track A (Fact Construction Governance):

 ├─ Governance Handoff:             CLOSED
 ├─ Governance Design Spec:         ACCEPTED
 └─ Governance Design Result:       ACCEPTED

Phase 3 Track B (Fact Schema Governance):

 ├─ Governance Handoff:             ACCEPTED (CODEX + DUAL REVIEW PASSED)
 ├─ Governance Design:              NOT AUTHORIZED
 ├─ Fact Schema:                    NOT CREATED / NOT AUTHORIZED
 └─ Implementation:                 NOT AUTHORIZED

Real Matter Analysis:               NOT AUTHORIZED
Legal Fact Generation:              NOT AUTHORIZED
Legal Reasoning & Request Right:     NOT AUTHORIZED
Next Phase Authorization:           NOT GRANTED
```


## Review Submission

Review Object:

TASK_PHASE3_TRACK_B_FACT_SCHEMA_GOVERNANCE_HANDOFF

Requested Review:

ARCHITECTURE REVIEW

Review Authorities:

Codex Executor

Architecture Coordinator

Third-Party Consultant:

Gemini 3.6 Flash — ADVISORY ONLY

Final Review Outcome:

Codex Executor:
PASS

Architecture Coordinator:
PASS — Grade A-

Third-Party Consultant:
PASS — Grade A

FS-H-001 through FS-H-012:
ALL PASS

Blocking Findings:
NONE

Non-Blocking Findings:
2 — ACCEPTED AS NON-BLOCKING

Authorization Overreach:
NONE

Project Owner Decision:
HANDOFF ACCEPTED


## Next Authorized Action

本 Handoff 的接受不自动授权任何下一动作。

是否进入 Fact Schema Governance Design、创建 SPEC、Fact Schema、`fact.yaml`、Implementation 或任何后续状态，必须由 Project Owner 另行作出明确授权决议。

在新的授权决议作出前，不得创建新资产或启动后续流程。
