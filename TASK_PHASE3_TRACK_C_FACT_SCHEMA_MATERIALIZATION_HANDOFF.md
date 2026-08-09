# TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_HANDOFF

## Status

ACCEPTED — ARCHITECTURE REVIEW PASSED


## Phase Identification

Phase:
PHASE 3

Track:
Track C

Name:
FACT SCHEMA MATERIALIZATION

Deliverable Type:
HANDOFF ONLY


## Authorization Basis

Project Owner Confirmation:

```text
Phase: PHASE 3
Track: Track C
Name: FACT SCHEMA MATERIALIZATION
```

Authorized Artifact:

TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_HANDOFF.md

Authorization Limit:

仅允许物化本 Handoff。

本授权不包括：

- Fact Schema Materialization Design；
- 具体 Fact Schema；
- `fact.yaml`；
- 字段、类型、必填规则、默认值或约束；
- YAML、JSON、数据库或 API 结构；
- Schema 实例；
- Agent、Skill、工具或代码；
- 真实或模拟案件事实；
- Legal Fact；
- Request Right；
- Implementation。


## Objective

为未来可能获授权的 Fact Schema Materialization 建立独立治理交接边界。

本 Handoff 的目标不是创建 Schema，而是确认：

- Materialization 必须独立于 Governance Design 获得授权；
- 未来具体 Schema 只能来源于已接受的 Track B 治理要求；
- 具体结构不得改变 Fact 状态、处置、争议、Unknown、追溯或人工门禁语义；
- Schema 文件创建、Schema Review、Implementation 和真实数据接入必须分别授权；
- 在任何前置条件不满足时必须 fail closed。


## Architectural Position

```text
Evidence Governance Layer
        |
        v
Fact Construction Governance
        |
        v
Fact Schema Governance
        |
        |  accepted governance requirements
        v
Fact Schema Materialization
        |
        |  inactive until separately authorized
        v
Schema Validation Boundary
        |
        |  no implementation authority
        v
Legal Fact Isolation Boundary
        |
        v
Legal Fact Layer
        |
        v
Request Right Foundation
```

Fact Schema Materialization：

- 不得替代 Fact Construction Governance；
- 不得改写 Fact Schema Governance；
- 不得自行授权 Schema；
- 不得执行案件事实构建；
- 不得生成 Legal Fact；
- 不得触发 Request Right；
- 不得自动进入 Implementation。


## Relationship With Previous Tracks

### Phase 3 Track A

Name:
FACT CONSTRUCTION GOVERNANCE

Final State:

```text
Governance Handoff: ACCEPTED
Governance Design Spec: ACCEPTED
Governance Design Result: ACCEPTED
```

Track A 提供：

- Fact 生命周期；
- Human Validation Gate；
- Confirmed、Disputed、Unknown；
- Evidence → Fact 转换治理；
- Fact → Legal Fact 隔离；
- Traceability；
- Revalidation 与 fail-closed。


### Phase 3 Track B

Name:
FACT SCHEMA GOVERNANCE

Final State:

```text
Governance Handoff: ACCEPTED
Governance Design Spec: ACCEPTED
Governance Design Result: ACCEPTED
Concrete Fact Schema: NOT CREATED
```

Track B 提供：

- Schema 不创造事实；
- Structural Validity ≠ Fact Validity；
- 全生命周期和处置语义保真；
- Disputed 与 Unknown 保留；
- Evidence 与 Human Validation 追溯；
- 撤回、版本与重新验证；
- Schema Materialization Boundary；
- 无具体字段、结构或实现。


### Phase 3 Track C

Name:
FACT SCHEMA MATERIALIZATION

Current State:

HANDOFF ACCEPTED — ARCHITECTURE REVIEW PASSED

Track C 当前仅建立 Materialization 的治理入口，不创建任何 Schema。


## Governing Distinctions

```text
Schema Governance Acceptance ≠ Schema Materialization Authorization

Materialization Handoff ≠ Materialization Design

Materialization Design ≠ Concrete Schema

Concrete Schema ≠ Validated Schema

Validated Schema ≠ Implementation

Schema File ≠ Fact Record

Schema Conformance ≠ Fact Truth

Fact Schema ≠ Legal Fact Schema

Schema Availability ≠ Downstream Authorization
```


## Core Principles

### FSM-G-001 Handoff ≠ Materialization

本 Handoff 不创建或授权创建具体 Fact Schema。

不得将 Handoff 的原则、术语或状态名称机械转换为字段、类型、枚举或文件结构。


### FSM-G-002 Accepted Governance Baseline Only

未来 Materialization 只能以已接受的 Track A 和 Track B 治理资产为规范来源。

不得：

- 引入未经审查的新事实状态；
- 删除既有生命周期状态；
- 修改人工处置语义；
- 弱化 Evidence Traceability；
- 弱化 Human Validation Gate；
- 改变 Legal Fact 隔离。


### FSM-G-003 No Fact Creation

具体 Schema 即使未来获授权，也只能约束表达，不得：

- 创建事实；
- 验证事实；
- 补全事实；
- 消除争议；
- 将 Unknown 变成默认值；
- 将结构校验结果变成 Confirmed；
- 将结构缺失变成否定事实。


### FSM-G-004 State Fidelity

未来 Materialization 必须忠实表达：

生命周期状态：

- Unverified Fact Candidate；
- Validation Pending；
- Verified Objective Fact；
- Disputed Objective Fact；
- Unknown / Insufficient；
- Rejected / Out of Scope；
- Superseded / Revalidation Required；
- Legal Fact Candidate — Isolated。

人工处置：

- Confirmed；
- Disputed；
- Unknown；
- Rejected / Out of Scope；
- Return for Revalidation。

本清单仅确认治理语义，不定义枚举、字段或编码。


### FSM-G-005 Dispute and Unknown Preservation

未来 Materialization 必须能够保留：

- 竞争事实版本；
- 不同证据基础；
- Disputed 的非确定性；
- Unknown 的信息不足；
- Unknown 与缺失、不可获得、不适用、已否定之间的区别。

不得以单值、默认值、空值或技术约束自动消除治理差异。


### FSM-G-006 Traceability Preservation

未来 Schema 必须能够保持：

```text
Fact State
    ↓
Construction / Validation Decision
    ↓
Verified Evidence Reference
    ↓
Evidence Governance Verification
```

本 Handoff 不定义追溯字段、标识、格式、签名或存储方式。


### FSM-G-007 Human Validation Preservation

未来 Materialization 不得把 Human Validation Gate 转换为自动状态规则。

结构校验、格式校验、模型置信度、数据完整度或来源数量不得替代人工决定。


### FSM-G-008 Revalidation and Revocation

未来 Schema 必须支持治理意义上的暂停、撤回、失效、被取代和重新验证。

`Return for Revalidation → Validation Pending` 必须保持，同时重新验证仍须基于当前有效的 Verified Evidence。


### FSM-G-009 Legal Isolation

未来 Fact Schema 不得包含、推导或触发：

- 法律要件匹配；
- 法律关系判断；
- 责任认定；
- Legal Fact；
- Request Right；
- 诉讼策略；
- 胜诉预测。


### FSM-G-010 Version and Change Control

未来 Schema 版本变化不得静默改变治理语义。

任何影响状态、处置、追溯、人工门禁或法律隔离的变化，必须：

- 被识别为治理影响变化；
- 阻断自动发布；
- 接受独立 Review；
- 由 Project Owner 另行授权。


### FSM-G-011 Artifact Integrity

未来具体 Schema 如获授权，必须具备可验证的资产身份、版本、来源和完整性。

本原则不定义哈希算法、签名格式、文件名、版本号或存储位置。


### FSM-G-012 Fail-Closed

当治理来源、状态语义、追溯、人工决定、版本、资产完整性或授权无法确认时，Materialization 必须阻断。


### FSM-G-013 No Automatic Escalation

本 Handoff 的物化、Review 或接受均不得自动授权：

- Materialization Design；
- Track C SPEC 或 RESULT；
- 具体 Fact Schema；
- `fact.yaml`；
- Schema Validation；
- Implementation；
- 真实案件接入；
- Legal Fact；
- Request Right；
- 后续 Track 或 Phase。


## Materialization Preconditions

本节仅定义未来 Materialization 启动前必须满足的治理条件，不授权启动。

### Precondition 1 — Accepted Governance Sources

Track A 与 Track B 的 Handoff、Spec 和 Result 必须保持 ACCEPTED。


### Precondition 2 — Explicit Materialization Design Authorization

必须存在 Project Owner 对 Track C Materialization Design Spec 的独立授权。


### Precondition 3 — Explicit Schema Creation Authorization

Design Spec 被接受后，仍必须另行授权具体 Fact Schema 的创建。


### Precondition 4 — Closed Scope

必须明确：

- 允许创建的唯一 Schema 资产；
- 禁止创建的其他资产；
- 是否允许任何格式；
- Review 权限；
- 版本与完整性要求；
- 后续状态仍保持关闭。

本 Handoff 不决定上述具体内容。


### Precondition 5 — Human Review Availability

必须存在获授权的人类审核者，且模型不得作为最终批准者。


### Precondition 6 — No Real Matter

除非未来另行明确授权，Materialization 设计与 Schema 创建不得导入真实或模拟案件事实。


### Precondition 7 — Legal Isolation

Legal Fact Layer 与 Request Right Foundation 必须继续保持未激活。


### Precondition 8 — Fail-Closed Capability

无法确认任何前置条件时，必须阻断 Materialization。


## Authorized Scope

本 Handoff 仅授权：

1. Handoff Materialization；
2. Architecture Review；
3. Fact Schema Materialization Design Preparation。

Design Preparation 仅允许识别未来设计问题和门禁，不表示 Materialization Design、Schema Creation 或 Implementation 已获授权。


## Not Authorized

以下行为继续禁止：

1. 创建 Track C SPEC；
2. 创建 Track C RESULT；
3. 创建具体 Fact Schema；
4. 创建或修改 `fact.yaml`；
5. 定义字段、字段名称、类型、必填规则、默认值或约束；
6. 创建 YAML、JSON、数据库或 API 结构；
7. 创建 Schema 实例；
8. 运行 Schema Validation；
9. 创建迁移、生成器或转换工具；
10. 创建 Agent、Skill、工具或代码；
11. 修改 Track A 或 Track B 已接受资产；
12. 修改 Evidence Registry；
13. 导入真实或模拟案件事实；
14. 自动提取案件事实；
15. 生成 Legal Fact；
16. 推导 Request Right；
17. 生成诉讼策略或胜诉预测；
18. 启动 Implementation；
19. 自动激活后续 Track 或 Phase。


## Expected Future Artifacts

仅在 Project Owner 另行明确授权后，方可创建：

TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_SPEC.md

TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_RESULT.md

具体 Fact Schema 或 `fact.yaml` 不因本节而获得创建授权。

未来 Schema 资产的名称、格式和位置必须在独立授权中确定。


## Architecture Review Questions

Architecture Review 仅可评估：

1. Track C 的架构位置是否正确；
2. Track A 与 Track B 的接受状态是否被完整继承；
3. Governance、Materialization、Validation 与 Implementation 是否分离；
4. Materialization 前置条件是否充分；
5. 状态、处置、Disputed、Unknown 是否保持保真；
6. Traceability 与 Human Validation Gate 是否保留；
7. Revalidation、Revocation 与 Version Control 是否充分；
8. Schema 是否被禁止创造或验证事实；
9. Objective Fact / Legal Fact 隔离是否保持；
10. 是否未创建具体 Schema、结构、实例或代码；
11. 是否无真实案件或法律推理污染；
12. 是否无自动阶段升级。

Architecture Review 不得借审查之名创建 Schema 或 Materialization Design。


## Acceptance Gates

### FSM-H-001 Phase and Track Boundary

Phase 3 Track C 的身份、架构位置和 Handoff-only 范围明确。


### FSM-H-002 Accepted Source Integrity

Track A 与 Track B 的已接受治理资产被完整继承且未被改写。


### FSM-H-003 Governance / Materialization Separation

Schema Governance Acceptance 与 Materialization Authorization 明确分离。


### FSM-H-004 Materialization / Schema Separation

Materialization Handoff、Materialization Design 与具体 Schema 创建明确分离。


### FSM-H-005 Schema / Implementation Separation

具体 Schema、Schema Validation 与 Implementation 明确分离。


### FSM-H-006 State Fidelity

Track A 的生命周期状态与人工处置得到保留。


### FSM-H-007 Dispute and Unknown Preservation

Disputed、Unknown 及缺席语义保持区分。


### FSM-H-008 Traceability Preservation

Fact 至 Human Validation、Verified Evidence 与 Evidence Governance 的追溯要求完整。


### FSM-H-009 Human Gate Preservation

结构、模型或自动流程不得替代人工决定。


### FSM-H-010 Revalidation and Version Control

撤回、失效、被取代、重新验证和治理影响变化得到控制。


### FSM-H-011 Legal Isolation

Objective Fact、Legal Fact Candidate 与 Legal Fact 继续保持硬隔离。


### FSM-H-012 Fail-Closed

治理来源、状态、追溯、决定、资产完整性或授权不明时必须阻断。


### FSM-H-013 No Schema Materialization

未创建具体 Fact Schema、`fact.yaml`、字段、类型或结构。


### FSM-H-014 No Implementation

未创建 Agent、Skill、工具、代码、迁移或部署设计。


### FSM-H-015 No Real Matter

未导入、构造或分析真实及模拟案件事实。


### FSM-H-016 No Legal Reasoning

未生成 Legal Fact、Request Right、诉讼策略或胜诉预测。


### FSM-H-017 No Automatic Escalation

Handoff 的物化、Review 或接受不自动授权 Design、Schema、Validation、Implementation 或后续阶段。


## Artifact Boundary

本次授权仅新增：

TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_HANDOFF.md

不得新增：

- TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_SPEC.md；
- TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_RESULT.md；
- `fact.yaml`；
- 具体 Fact Schema；
- 字段、类型或约束；
- YAML、JSON、数据库或 API 结构；
- Schema 实例；
- Agent、Skill、工具或代码；
- 真实或模拟案件事实；
- Legal Fact 或 Request Right 资产。


## Current System State

```text
Phase 3 Track A (Fact Construction Governance):

 ├─ Governance Handoff:             ACCEPTED
 ├─ Governance Design Spec:         ACCEPTED
 └─ Governance Design Result:       ACCEPTED

Phase 3 Track B (Fact Schema Governance):

 ├─ Governance Handoff:             ACCEPTED
 ├─ Governance Design Spec:         ACCEPTED
 ├─ Governance Design Result:       ACCEPTED
 └─ Concrete Fact Schema:           NOT CREATED

Phase 3 Track C (Fact Schema Materialization):

 ├─ Materialization Handoff:        ACCEPTED — ARCHITECTURE REVIEW PASSED
 ├─ Materialization Design:         NOT AUTHORIZED
 ├─ Concrete Fact Schema:           NOT CREATED / NOT AUTHORIZED
 ├─ fact.yaml:                      NOT CREATED / NOT AUTHORIZED
 ├─ Schema Validation:              NOT STARTED / NOT AUTHORIZED
 └─ Implementation:                 NOT AUTHORIZED

Real Matter Analysis:               NOT AUTHORIZED
Legal Fact Generation:              NOT AUTHORIZED
Legal Reasoning & Request Right:     NOT AUTHORIZED
Next Phase Authorization:           NOT GRANTED
```


## Review Submission

Review Object:

TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_HANDOFF

Requested Review:

ARCHITECTURE REVIEW

Review Authorities:

Architecture Coordinator

Third-Party Consultant — ADVISORY ONLY

Review Outcome:

```text
Codex Executor Integrity Review:          PASS
Architecture Coordinator Review:          PASS (Grade A)
Third-Party Consultant — Gemini 3.6 Flash:
  INCOMPLETE — EXTERNAL QUOTA BLOCKED
  ADVISORY ONLY

Project Owner Decision:
  HANDOFF ACCEPTED

Materialization Design:
  NOT AUTHORIZED
```


## Next Authorized Action

当前不存在自动获准的下一动作。

Handoff 的接受不授权创建 Track C SPEC/RESULT、具体 Schema、`fact.yaml`、字段、类型、YAML/JSON、数据库/API 结构、Schema 实例、Validation、实现代码、真实或模拟案件事实、Legal Fact 或 Request Right。

是否进入 Fact Schema Materialization Design，必须由 Project Owner 另行作出明确授权决议。
