# TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_SPEC

## Status

ACCEPTED — DESIGN SPEC REVIEW PASSED


## Phase Identification

Phase:
PHASE 3

Track:
Track C

Name:
FACT SCHEMA MATERIALIZATION

Deliverable Type:
DESIGN SPEC ONLY


## Authorization Basis

Project Owner Decision:

```text
Phase 3 Track C Handoff:
ACCEPTED — ARCHITECTURE REVIEW PASSED

Fact Schema Materialization Design:
AUTHORIZED — DESIGN SPEC ONLY
```

Accepted Handoff:

TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_HANDOFF.md

Accepted Handoff SHA-256:

F822C4BA3DEE2D1F449E3AE3A2F3054825502F4B62A109007AF46290A97129DB

Authorized Deliverable:

TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_SPEC.md


## Authorization Limit

本授权仅允许设计 Fact Schema Materialization 的抽象治理机制。

本 Spec 可以定义：

- 治理目标与不变量；
- Materialization 治理生命周期；
- 授权、Review、阻断和重新验证门禁；
- 已接受治理基线的绑定规则；
- 状态与人工处置语义保真要求；
- Disputed 与 Unknown 保留要求；
- Traceability 与 Human Validation 保留要求；
- 版本、完整性、撤回与 fail-closed 要求；
- 抽象接口边界；
- 未来 Schema Creation Authorization 决议必须封闭的治理范围；
- Design Spec Review 与 Acceptance Gates。

本授权不允许：

- 创建具体 Fact Schema；
- 创建或修改 `fact.yaml`；
- 定义任何 Schema 字段、字段名称、类型、必填规则、默认值或约束；
- 选择或创建 YAML、JSON、数据库、API 或其他具体结构；
- 创建 Schema 实例、示例记录或测试数据；
- 运行 Schema Validation；
- 创建迁移、生成器、转换器、Agent、Skill、工具或代码；
- 创建本 Track 的 RESULT；
- 修改 Evidence Registry；
- 导入真实或模拟案件事实；
- 自动提取或构建案件事实；
- 生成 Legal Fact；
- 推导 Request Right；
- 生成诉讼策略或胜诉预测；
- 自动激活 Implementation 或任何后续 Track、Layer 或 Phase。


## Objective

建立从已接受的 Fact Schema Governance 到未来具体 Fact Schema 创建之间的受控设计层。

本 Spec 的目标不是创建 Schema，而是确保未来任何 Schema 创建行为：

1. 具有单独、明确、封闭的 Project Owner 授权；
2. 仅以已接受的 Track A、Track B 和 Track C 治理资产为规范来源；
3. 不创造、验证、补全或重新评价事实；
4. 不改变生命周期状态或人工处置语义；
5. 不消除 Disputed 或补全 Unknown；
6. 不切断 Evidence 与 Human Validation 追溯；
7. 不把结构有效性解释为事实有效性；
8. 不进入 Legal Fact、Request Right 或 Implementation；
9. 在来源、授权、语义或完整性无法确认时 fail closed。


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
        | accepted normative baseline
        v
Fact Schema Materialization Design
        |
        | separate Project Owner authorization required
        v
Concrete Fact Schema Creation Boundary
        |
        | separate Review and acceptance required
        v
Schema Validation Boundary
        |
        | no implementation authority
        v
Implementation Boundary
        |
        | hard isolation
        v
Legal Fact Layer
        |
        v
Request Right Foundation
```

Fact Schema Materialization Design：

- 不替代 Fact Construction Governance；
- 不替代 Fact Schema Governance；
- 不创建具体 Fact Schema；
- 不执行 Schema Validation；
- 不实现任何运行时能力；
- 不修改 Evidence Registry；
- 不执行事实构建；
- 不生成 Legal Fact；
- 不触发 Request Right；
- 不授权任何下游层。


## Normative Source Baseline

### Binding Rule

本 Spec 仅继承下列已接受资产。

除非相应资产经 Project Owner 授权完成治理变更、重新 Review 和重新接受，否则不得使用其他文件、草稿、聊天摘要或模型记忆替代规范来源。

### Bound Assets

| Normative Asset | SHA-256 | Governing Role |
|---|---|---|
| TASK_PHASE3_TRACK_A_FACT_CONSTRUCTION_GOVERNANCE_HANDOFF.md | 33C7AF56B80015804BCE056AAEFBABB6FC30811908652E0EE68709342A06AEC8 | Track A boundary |
| TASK_PHASE3_TRACK_A_FACT_CONSTRUCTION_GOVERNANCE_SPEC.md | 2721F31685A3831EA68792AEE1C011599E7DF2E122FB41B5D1BB1A5C967CF1FA | Fact lifecycle and transition governance |
| TASK_PHASE3_TRACK_A_FACT_CONSTRUCTION_GOVERNANCE_RESULT.md | EB24C7C46FDF70EA71999EDAE46E905301F19E7DBEE6F19F54B66D5C07E6938E | Track A accepted result |
| TASK_PHASE3_TRACK_B_FACT_SCHEMA_GOVERNANCE_HANDOFF.md | EF7788D15F037705CD6932CD772B6C78E6961EC0D9F64CDD06620DF2693A8E3E | Track B boundary |
| TASK_PHASE3_TRACK_B_FACT_SCHEMA_GOVERNANCE_SPEC.md | 9DCF9D7794E3C91A1ADF3902C2EA45056395F5F03A2645ED7B2721104477AD96 | Fact Schema governance requirements |
| TASK_PHASE3_TRACK_B_FACT_SCHEMA_GOVERNANCE_RESULT.md | 6F02F5016572DBE4C014EA9E66856D13A0DADB696D28B8F56CBAD621D6D342C6 | Track B accepted result |
| TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_HANDOFF.md | F822C4BA3DEE2D1F449E3AE3A2F3054825502F4B62A109007AF46290A97129DB | Track C accepted Handoff boundary |

### Baseline Mismatch

出现以下任一情形时，必须阻断 Design 接受、Schema 创建授权或任何后续动作：

- 规范资产缺失；
- 资产身份无法确认；
- 哈希与绑定值不一致；
- 接受状态无法确认；
- 存在未经接受的替代版本；
- 资产之间出现无法解释的治理冲突；
- 试图仅根据摘要、转述或模型输出重建规范；
- 任何上游治理资产被撤回、失效或重新开放 Review。

Baseline mismatch 不得由模型自动修复。


## Governing Distinctions

```text
Accepted Governance Baseline ≠ Concrete Schema

Materialization Design Authorization ≠ Schema Creation Authorization

Design Spec Materialization ≠ Design Spec Acceptance

Design Spec Acceptance ≠ Concrete Schema Creation

Concrete Schema Creation ≠ Schema Acceptance

Schema Acceptance ≠ Schema Validation

Schema Validation ≠ Fact Validation

Structural Validity ≠ Fact Validity

Data Presence ≠ Confirmed Fact

Data Absence ≠ Fact Non-Existence

Unknown ≠ Empty

Disputed ≠ Invalid

Rejected ≠ Deleted History

Superseded ≠ Silently Overwritten

Schema Conformance ≠ Fact Truth

Schema File ≠ Fact Record

Fact Schema ≠ Legal Fact Schema

Materialization ≠ Implementation

Human Review Support ≠ Human Decision

Technical Completeness ≠ Governance Completeness

Schema Availability ≠ Downstream Authorization
```


## Materialization Design Principles

### FSM-D-001 Authorization Fidelity

每一个治理动作必须受其当前明确授权边界约束。

授权不得通过以下方式扩大：

- 推定；
- 默示；
- 文件存在；
- Review PASS；
- 模型建议；
- 技术可执行性；
- 上游资产已接受；
- 前一阶段完成。


### FSM-D-002 Accepted Baseline Only

未来具体 Schema 只能表达已接受治理基线。

不得：

- 创造新事实状态；
- 删除既有状态；
- 合并生命周期状态与人工处置；
- 重命名后改变治理含义；
- 弱化 Human Validation；
- 缩短 Traceability；
- 改变 Legal Fact 隔离；
- 根据技术便利重写 Track A 或 Track B。


### FSM-D-003 No Fact Creation

Materialization 只能约束表达，不得：

- 创建事实；
- 验证事实；
- 补全事实；
- 推测事实；
- 自动确认事实；
- 自动否定事实；
- 自动选择竞争事实版本；
- 将结构缺失解释为事实不存在；
- 将结构校验成功解释为事实成立。


### FSM-D-004 State Fidelity

未来任何具体 Schema 必须忠实保持 Track A 已接受的生命周期状态：

1. Unverified Fact Candidate；
2. Validation Pending；
3. Verified Objective Fact；
4. Disputed Objective Fact；
5. Unknown / Insufficient；
6. Rejected / Out of Scope；
7. Superseded / Revalidation Required；
8. Legal Fact Candidate — Isolated。

必须独立保持人工处置：

- Confirmed；
- Disputed；
- Unknown；
- Rejected / Out of Scope；
- Return for Revalidation。

上述清单仅绑定治理语义，不定义字段、枚举、编码、类型或存储结构。


### FSM-D-005 Dispute Preservation

未来 Materialization 必须允许治理意义上的竞争事实版本、不同证据基础、人工异议和无法消除的语义差异保持可区分。

不得通过：

- 单值限制；
- 覆盖；
- 排序；
- 多数来源；
- 置信度；
- 默认选择；
- 最新版本优先；
- 技术校验结果

自动确定唯一事实版本。


### FSM-D-006 Unknown and Absence Preservation

Unknown / Insufficient 必须与下列语义保持区别：

- 未提供；
- 技术缺失；
- 暂不可获得；
- 不适用；
- 已否定；
- 已拒绝；
- 超出范围；
- 已确认不存在。

不得使用默认行为补全 Unknown，也不得把技术缺失自动提升为最终 Unknown 人工处置。


### FSM-D-007 Traceability Fidelity

未来 Materialization 必须保持以下治理链：

```text
Fact State
    ↓
Construction / Validation Decision
    ↓
Authorized Human Decision
    ↓
Verified Evidence Reference
    ↓
Evidence Governance Verification
```

本 Spec 不定义追溯字段、标识符、引用格式、签名方法、数据库关系或 API 契约。


### FSM-D-008 Human Validation Fidelity

Human Validation Gate 的决定地位必须保持。

以下结果不得替代人工决定：

- Schema 校验；
- 格式校验；
- 数据完整度；
- 模型置信度；
- 来源数量；
- 一致性评分；
- 自动工作流状态；
- 技术签名有效；
- 文件已被接受。


### FSM-D-009 Revalidation and Revocation

未来 Materialization 必须允许治理意义上的：

- 暂停；
- 撤回；
- 失效；
- 被取代；
- 重新验证；
- 重新进入 Validation Pending；
- 历史状态保留。

`Return for Revalidation → Validation Pending` 必须保持。

重新验证必须基于当前有效的 Verified Evidence，并重新经过相应 Human Validation Gate。


### FSM-D-010 Legal Isolation

未来具体 Fact Schema 不得包含、表达、推导或触发：

- 法律要件匹配；
- 法律关系判断；
- 责任认定；
- Legal Fact；
- Request Right；
- 抗辩或请求权分析；
- 诉讼策略；
- 胜诉预测。

Legal Fact Candidate — Isolated 仅保留候选隔离语义，不是 Legal Fact。


### FSM-D-011 Version and Integrity

任何未来 Schema 资产必须具有可验证的：

- 资产身份；
- 规范来源；
- 版本身份；
- Review 状态；
- 接受状态；
- 完整性状态；
- 变更历史；
- 撤回或被取代状态。

本 Spec 不定义具体版本格式、哈希算法、签名格式、文件路径或存储系统。


### FSM-D-012 Fail-Closed

当规范来源、授权、状态语义、人工决定、追溯、版本、资产完整性或法律隔离无法确认时，必须阻断。


### FSM-D-013 No Automatic Escalation

本 Spec 的创建、Review、PASS 或接受不得自动授权：

- Track C RESULT；
- 具体 Fact Schema；
- `fact.yaml`；
- Schema Creation；
- Schema Validation；
- Implementation；
- 真实案件接入；
- Legal Fact；
- Request Right；
- 后续 Track、Layer 或 Phase。


## Materialization Governance Lifecycle

本节定义治理控制阶段，不定义 Schema 内部状态或字段。

### Stage M0 — Design Authorized

含义：

Project Owner 已授权创建本 Design Spec。

允许：

- 读取已接受治理资产；
- 设计抽象治理机制；
- 准备 Design Review。

禁止：

- 创建具体 Schema；
- 选择具体结构；
- 运行 Validation；
- 创建 RESULT 或代码。


### Stage M1 — Baseline Bound

含义：

全部规范来源的身份、接受状态和完整性已被核验。

进入条件：

- Bound Assets 全部存在；
- 接受状态可验证；
- 完整性匹配；
- 无未解决的治理冲突。

阻断条件：

- 任一来源缺失、失效、被撤回或不匹配。


### Stage M2 — Materialization Boundary Defined

含义：

未来 Schema Creation Authorization 必须封闭决定的治理问题已被定义。

本阶段只定义决定要求，不作出具体 Schema 创建决定。


### Stage M3 — Semantic Preservation Plan Ready

含义：

状态、处置、Disputed、Unknown、Traceability、Human Validation、Revalidation 和 Legal Isolation 的保真要求已完整纳入 Design。

本阶段不选择任何表达结构。


### Stage M4 — Design Review Pending

含义：

本 Spec 已提交只读 Architecture Review。

在 Review 期间：

- 不得创建 RESULT；
- 不得创建具体 Schema；
- 不得修订上游已接受资产；
- 不得自动修复审查问题；
- 不得激活后续状态。


### Stage M5 — Design Review Passed

含义：

审查者认为本 Spec 满足 Design Acceptance Gates。

Review PASS：

- 不等于 Design Spec Accepted；
- 不等于 Schema Creation Authorized；
- 不等于具体 Schema 已存在；
- 不等于 Validation 或 Implementation 已授权。


### Stage M6 — Design Accepted

含义：

Project Owner 已明确接受本 Spec。

即使进入本阶段：

```text
Concrete Fact Schema Creation:
NOT AUTHORIZED

fact.yaml:
NOT CREATED / NOT AUTHORIZED

Schema Validation:
NOT AUTHORIZED

Implementation:
NOT AUTHORIZED
```


### Stage M7 — Awaiting Separate Schema Creation Decision

含义：

Design 已接受，但系统保持关闭，等待 Project Owner 对具体 Schema 创建作出独立、封闭授权。

该阶段不得因等待状态而自动创建任何资产。


### Stage M8 — Closed-Scope Schema Creation Authorized — Future / Inactive

含义：

Project Owner 已在未来作出新的、独立的、范围封闭的 Schema Creation Authorization。

当前状态：

```text
INACTIVE
NOT AUTHORIZED
```

本 Spec 仅定义该未来治理阶段，不激活该阶段，也不决定 Schema 资产名称、格式、位置或结构。


### Stage M9 — Schema Materialized — Pending Review — Future / Inactive

含义：

未来唯一获授权的 Schema 资产已在封闭范围内创建，并等待独立只读 Review。

当前状态：

```text
INACTIVE
NO SCHEMA EXISTS
```

进入该阶段不授权 Schema Validation、Implementation、实例、测试数据或真实数据接入。


### Stage M10 — Schema Review Passed — Future / Inactive

含义：

未来具体 Schema 的 Review Gates 已通过。

Review PASS 不等于：

- Schema Accepted；
- Schema Validation Authorized；
- Implementation Authorized；
- Real Matter Authorized；
- Legal Fact 或 Request Right Authorized。


### Stage M11 — Schema Accepted or Rejected — Future / Inactive

含义：

Project Owner 对未来特定 Schema 资产作出明确接受或拒绝决定。

接受必须绑定特定资产版本和完整性；拒绝不得触发替代资产自动生成。


### Stage M12 — Suspended / Superseded / Revalidation Required — Future / Inactive

触发条件：

- 规范来源变化；
- 资产完整性失败；
- 授权被撤回；
- 治理冲突出现；
- Review 决定失效；
- 上游 Evidence、Fact 或 Human Validation 治理要求发生相关变化。

允许效果仅限暂停、阻断、保留历史并提交人工重新 Review。


### Stage MB — Blocked

以下任一情形出现时进入阻断状态：

- 授权不明确；
- 规范基线不完整；
- 资产完整性不匹配；
- 状态语义可能被折叠；
- Disputed 可能被自动消除；
- Unknown 可能被默认补全；
- Traceability 无法保持；
- Human Validation 可能被替代；
- Legal Fact 隔离无法保持；
- 真实或模拟案件数据进入；
- Schema、Validation 或 Implementation 越权启动；
- 后续状态被自动激活。

Blocked 不得由模型自动解除。


## Governance Transition Rules

### FSM-T-001 Authorization to Design Materialization

Source:

DESIGN NOT AUTHORIZED

Trigger:

Project Owner 明确授权唯一 Design Spec。

Target:

DESIGN AUTHORIZED — SPEC ONLY

Human Decision:

Required

Automatic Transition:

Prohibited


### FSM-T-002 Design Authorized to Baseline Bound

Trigger:

全部规范资产身份、接受状态与完整性核验通过。

Target:

BASELINE BOUND

Failure:

BLOCKED


### FSM-T-003 Baseline Bound to Boundary Defined

Trigger:

Schema Creation Authorization 必须封闭决定的治理范围已完整定义。

Target:

MATERIALIZATION BOUNDARY DEFINED

本转换不得决定具体 Schema 名称、格式、字段或结构。


### FSM-T-004 Boundary Defined to Preservation Plan Ready

Trigger:

全部保真要求和禁止性规则被覆盖。

Target:

SEMANTIC PRESERVATION PLAN READY


### FSM-T-005 Preservation Plan Ready to Design Review Pending

Trigger:

本 Spec 被提交只读 Architecture Review。

Target:

DESIGN REVIEW PENDING

Human Decision:

Required for submission authority


### FSM-T-006 Review Pending to Review Passed

Trigger:

Design Acceptance Gates 全部通过且无阻断项。

Target:

DESIGN REVIEW PASSED

Automatic Acceptance:

Prohibited


### FSM-T-007 Review Pending to Blocked

Trigger:

发现越权、治理回归、完整性异常或未解决阻断项。

Target:

BLOCKED


### FSM-T-008 Review Passed to Design Accepted

Trigger:

Project Owner 作出明确 `SPEC ACCEPTED` 决议。

Target:

DESIGN ACCEPTED

Automatic Transition:

Prohibited


### FSM-T-009 Design Accepted to Awaiting Schema Creation Decision

Trigger:

Design 接受状态被确认。

Target:

AWAITING SEPARATE SCHEMA CREATION DECISION

Effect:

保持 Schema Creation、Validation 和 Implementation 关闭。


### FSM-T-010 Baseline Change to Revalidation Required

Trigger:

任一规范资产变更、撤回、失效、被取代或完整性不匹配。

Effect:

- 暂停依赖当前 Design 的后续授权；
- 重新核验治理影响；
- 重新进入 Design Review；
- 保留历史审查记录。


### FSM-T-011 Authorization Revocation to Blocked

Trigger:

Project Owner 撤回或限制 Design 授权。

Target:

BLOCKED

Effect:

立即停止尚未完成的 Design 动作，不创建替代资产。


### FSM-T-012 Awaiting Decision to Closed-Scope Schema Creation Authorized — Future

Trigger:

Project Owner 对唯一具体 Schema 资产作出新的、独立且范围封闭的创建授权。

Target:

CLOSED-SCOPE SCHEMA CREATION AUTHORIZED

Current Availability:

```text
NOT AUTHORIZED
```

Automatic Transition:

Prohibited


### FSM-T-013 Schema Creation Authorized to Schema Materialized — Pending Review — Future

Trigger:

仅有的获授权 Schema 资产在授权范围内完成物化，且资产身份、规范基线、版本和完整性可验证。

Target:

SCHEMA MATERIALIZED — PENDING REVIEW

Effect:

只允许具体 Schema Review；Validation、Implementation 和数据接入继续关闭。


### FSM-T-014 Schema Pending Review to Review Passed or Blocked — Future

Trigger:

获授权的人类审查者完成具体 Schema Review。

Targets:

- SCHEMA REVIEW PASSED；或
- BLOCKED。

Automatic Acceptance:

Prohibited


### FSM-T-015 Schema Review Passed to Schema Accepted or Rejected — Future

Trigger:

Project Owner 对该特定资产和版本作出明确决定。

Targets:

- SCHEMA ACCEPTED；或
- SCHEMA REJECTED。

Downstream Effect:

不得自动授权 Validation、Implementation、Real Matter、Legal Fact 或 Request Right。


### FSM-T-016 Schema Governance Change to Suspended / Revalidation Required — Future

Trigger:

规范基线、授权、资产完整性、Review 决定或治理依赖发生相关变化。

Effect:

- 暂停当前依赖；
- 保留历史；
- 重新绑定当前有效规范；
- 执行影响评估；
- 重新进入人工 Review。

Automatic Repair or Reacceptance:

Prohibited


## Transition Matrix

| Source Governance Stage | Target Governance Stage | Required Trigger | Human Gate | Automatic Escalation |
|---|---|---|---|---|
| Design Not Authorized | Design Authorized — Spec Only | Explicit Project Owner authorization | Required | Prohibited |
| Design Authorized — Spec Only | Baseline Bound | Source identity, acceptance and integrity verified | Reviewable | Prohibited |
| Baseline Bound | Materialization Boundary Defined | Closed decision requirements defined | Required | Prohibited |
| Materialization Boundary Defined | Semantic Preservation Plan Ready | All fidelity domains covered | Required | Prohibited |
| Semantic Preservation Plan Ready | Design Review Pending | Authorized review submission | Required | Prohibited |
| Design Review Pending | Design Review Passed | All gates pass; no blocker | Required | Prohibited |
| Design Review Pending | Blocked | Any blocker or overreach | Required for disposition | Protective blocking allowed |
| Design Review Passed | Design Accepted | Explicit Project Owner `SPEC ACCEPTED` | Required | Prohibited |
| Design Accepted | Awaiting Separate Schema Creation Decision | Acceptance confirmed | Required | Prohibited |
| Awaiting Separate Schema Creation Decision | Closed-Scope Schema Creation Authorized — Future | New explicit and closed Project Owner authorization | Required | Prohibited |
| Closed-Scope Schema Creation Authorized — Future | Schema Materialized — Pending Review — Future | Only authorized asset created with verifiable identity and integrity | Required | Prohibited |
| Schema Materialized — Pending Review — Future | Schema Review Passed / Blocked — Future | Independent human Schema Review | Required | Prohibited |
| Schema Review Passed — Future | Schema Accepted / Rejected — Future | Explicit Project Owner decision bound to the asset version | Required | Prohibited |
| Any Future Schema Stage | Suspended / Superseded / Revalidation Required | Baseline, authorization, integrity or governance change | Required | Protective blocking allowed |
| Any Active Design Stage | Revalidation Required / Blocked | Baseline change, revocation or integrity failure | Required | Protective blocking allowed |

本矩阵仅描述治理流程，不定义 Schema 数据结构、状态字段或运行时状态机。


## Future Schema Creation Authorization Boundary

### Separate Decision Required

具体 Fact Schema 创建必须由 Project Owner 在本 Spec 被接受后另行授权。

该决议必须封闭、明确并至少回答下列治理问题：

1. 唯一允许创建的 Schema 资产身份是什么；
2. 允许使用何种具体表达形式；
3. 明确禁止创建哪些伴随资产；
4. 允许的工作范围是否仅限空 Schema 结构；
5. 是否禁止实例、样例、测试数据和真实数据；
6. 适用的规范基线版本是什么；
7. 由谁执行只读 Review；
8. 由谁作出最终接受决定；
9. 如何确认资产版本与完整性；
10. Schema Creation 完成后哪些下游状态继续保持关闭。

上述十项是未来授权决议必须覆盖的治理问题，不是 Schema 字段、技术 payload 或 API 定义。


### Default Closed Rule

若未来授权决议未明确回答任一必要问题，则：

```text
Concrete Fact Schema Creation:
BLOCKED
```

不得根据惯例、文件名、工具默认行为或模型建议补足授权。


### One-Artifact Rule

未来 Schema Creation Authorization 必须明确唯一允许创建的主要资产。

除非另行逐项授权，不得附带创建：

- 示例；
- 实例；
- 测试数据；
- 映射文件；
- 迁移文件；
- 生成器；
- 验证器；
- API；
- 数据库结构；
- Agent；
- Skill；
- 工具；
- 实现代码；
- Legal Fact 或 Request Right 资产。


## Semantic Preservation Review Domains

### Domain 1 — Lifecycle State Preservation

核验全部八项生命周期状态是否保持独立治理含义，且未被折叠为简单有效、无效或空值。


### Domain 2 — Human Disposition Preservation

核验五项人工处置是否保持为 Human Validation 决定，而非技术状态。


### Domain 3 — Evidence Qualification Separation

核验：

```text
Verified Evidence ≠ Verified Objective Fact
```

Evidence 状态不得因进入未来结构而自动成为 Fact 状态。


### Domain 4 — Structural Validity Separation

核验：

```text
Structural Validity ≠ Fact Validity
```

技术可解析、格式正确或完整性校验通过不得授予 Confirmed。


### Domain 5 — Dispute Preservation

核验竞争版本、证据冲突与人工异议是否能够保持，不被单值约束、覆盖或排序消除。


### Domain 6 — Unknown and Absence

核验 Unknown、缺失、不可获得、不适用、已否定、已拒绝和超出范围是否保持可区分。


### Domain 7 — Traceability

核验 Fact 是否仍可追溯至：

- 当前治理状态；
- Construction / Validation 决定；
- 获授权的人类决定；
- Verified Evidence；
- Evidence Governance Verification。


### Domain 8 — Revalidation and Revocation

核验来源撤回、来源失效、新冲突、权限变化或人工决定撤回时，是否能够暂停使用并重新进入验证。


### Domain 9 — Version and Supersession

核验版本变化是否保留历史、阻断静默覆盖并触发治理影响 Review。


### Domain 10 — Legal Isolation

核验 Objective Fact、Legal Fact Candidate — Isolated 与 Legal Fact 是否保持硬隔离。


### Domain 11 — Downstream Containment

核验 Schema Availability 是否不会自动激活 Validation、Implementation、Legal Fact Layer 或 Request Right Foundation。


## Interface Boundaries

本节仅定义抽象治理关系，不定义 API、协议、字段、技术 payload 或存储结构。

### Track A Inbound Boundary

允许读取：

- 已接受的生命周期与转换治理；
- 人工处置语义；
- Evidence → Fact 准入要求；
- Revalidation 与 Legal Isolation 要求。

禁止：

- 修改 Track A；
- 重新决定事实状态；
- 绕过 Human Validation；
- 接收未经治理的原始事实。


### Track B Normative Boundary

Track B 是 Materialization 设计的直接规范来源。

允许：

- 读取已接受的 Schema Governance 要求；
- 核验语义保真；
- 核验版本、撤回和 fail-closed 要求。

禁止：

- 把 Track B 抽象要求机械转换为字段；
- 以 Materialization 便利修改 Track B；
- 将 Track B 接受解释为具体 Schema 已获授权。


### Evidence Registry Boundary

当前仅允许只读核验证据治理资格与失效信号。

禁止：

- 修改 Evidence Registry；
- 提升 Evidence 状态；
- 写入 Fact；
- 将 Evidence 直接物化为 Fact；
- 绕过 Evidence Governance。


### Concrete Fact Schema Creation Boundary

当前状态：

```text
NOT CREATED
NOT AUTHORIZED
```

必须等待：

1. 本 Spec Review 通过；
2. Project Owner 明确接受本 Spec；
3. Project Owner 另行作出封闭的 Schema Creation Authorization。


### Schema Validation Boundary

当前状态：

```text
NOT STARTED
NOT AUTHORIZED
```

Schema 创建、Schema 接受与 Schema Validation 必须分别治理。


### Implementation Boundary

当前状态：

```text
NOT AUTHORIZED
```

任何 Schema 资产的存在、接受或技术校验均不得自动授权实现。


### Legal Fact Layer Boundary

当前状态：

```text
INACTIVE
NOT AUTHORIZED
```

不得生成 Legal Fact、执行法律要件匹配或评价法律关系。


### Request Right Foundation Boundary

当前状态：

```text
NOT STARTED
NOT AUTHORIZED
```

不得根据请求权目标选择、压缩、补全、改写或排序事实。


## Version and Change Governance

### Baseline Change Classification

任何可能影响下列事项的变化均属于治理影响变化：

- 生命周期状态；
- 人工处置；
- Disputed；
- Unknown；
- Traceability；
- Human Validation；
- Revalidation；
- Legal Isolation；
- 授权边界；
- 下游使用资格。


### Governance-Incompatible Change

以下变化必须视为不兼容：

- 合并或删除状态；
- 改变状态含义；
- 将人工处置自动化；
- 缩短追溯链；
- 静默覆盖历史；
- 默认补全 Unknown；
- 自动选择 Disputed 版本；
- 把 Legal Fact Candidate 表达为 Legal Fact；
- 自动激活下游。

不兼容变化必须：

- 阻断发布；
- 执行独立 Architecture Review；
- 重新绑定治理基线；
- 由 Project Owner 另行授权；
- 不得静默应用。


### Potentially Compatible Change

只有在不改变治理语义、不减少追溯、不改变人工门禁、不影响法律隔离且不扩大授权时，变化才可能被判断为兼容。

兼容性仍必须由获授权的人类审查者决定，不得由工具自动决定。


### Supersession

任何新版本不得删除旧版本的审查、接受、撤回或被取代记录。

被取代的资产不得继续作为当前有效规范或当前可用 Schema。


## Roles and Decision Rights

本节定义概念职责，不定义权限实现。

### Project Owner

拥有：

- Design Spec 授权权；
- Design Spec 接受权；
- Schema Creation 单独授权权；
- 治理变更授权权；
- 暂停、撤回和重新开放权；
- 后续阶段授权权。


### Codex Executor

可以：

- 在授权范围内物化唯一 Design Spec；
- 核验资产边界和完整性；
- 执行非裁决性一致性检查；
- 报告阻断项和越权风险。

不得：

- 自行接受 Spec；
- 自行授权具体 Schema；
- 创建未授权资产；
- 自动解除 Blocked；
- 生成 Legal Fact 或 Request Right。


### Architecture Coordinator

可以：

- 执行只读 Design Review；
- 检查架构定位、基线继承和治理完整性；
- 逐项核验 Acceptance Gates；
- 提出 PASS、FAIL 或修订建议。

不得：

- 替代 Project Owner 接受；
- 借 Review 创建 Schema；
- 扩大 Design 授权；
- 激活后续状态。


### Third-Party Consultant

角色：

ADVISORY ONLY

任何外发必须获得针对具体资产的明确授权。

第三方意见不得：

- 自动修改文件；
- 接受 Spec；
- 授权 Schema；
- 生成实现；
- 触发阶段转换。


### Future Schema Author

当前状态：

NOT ACTIVATED

仅在未来具体 Schema Creation Authorization 生效后，方可在其封闭范围内工作。


### Human Reviewer

未来必须由获授权的人类审核者决定：

- 治理基线是否匹配；
- 语义是否保真；
- 变更是否兼容；
- Review 问题是否关闭；
- 资产是否可提交 Project Owner 接受。


## Fail-Closed Rules

以下任一情形出现时必须阻断：

1. Design 授权无法确认；
2. Handoff 接受状态无法确认；
3. Track A 或 Track B 规范来源缺失；
4. 任一绑定资产完整性不匹配；
5. 上游资产被撤回、失效或重新开放；
6. 未来授权未封闭唯一 Schema 资产；
7. 具体表达形式未被明确授权；
8. 生命周期状态可能被折叠；
9. 生命周期状态与人工处置可能混同；
10. Disputed 可能被自动消除；
11. Unknown 可能被默认补全；
12. Evidence 资格可能被解释为 Fact 成立；
13. Structural Validity 可能被解释为 Fact Validity；
14. Traceability 无法保持；
15. Human Validation 可能被替代；
16. 撤回、失效或重新验证无法表达；
17. Legal Fact 隔离无法保持；
18. 真实或模拟案件事实进入；
19. 未授权的 Schema、Validation 或代码被创建；
20. 任何后续状态试图自动激活。


## Protective Actions

允许的保护性动作仅限：

- 阻断 Design 接受；
- 阻断 Schema 创建；
- 暂停下游使用；
- 标记待人工 Review；
- 请求重新验证规范来源；
- 保留当前及历史治理状态；
- 报告完整性异常；
- 报告授权冲突；
- 通知 Project Owner。

保护性动作不得：

- 创建事实；
- 自动确认事实；
- 自动消除 Disputed；
- 自动补全 Unknown；
- 创建具体 Schema；
- 运行 Validation；
- 创建代码；
- 生成 Legal Fact；
- 触发 Request Right；
- 自动接受或授权任何资产。


## Governance Invariants

以下不变量必须持续成立：

- Evidence ≠ Fact；
- Verified Evidence ≠ Verified Objective Fact；
- Fact ≠ Legal Fact；
- Legal Fact Candidate ≠ Legal Fact；
- Structural Validity ≠ Fact Validity；
- Data Presence ≠ Confirmed Fact；
- Data Absence ≠ Fact Non-Existence；
- Unknown ≠ Empty；
- Disputed ≠ Invalid；
- Rejected ≠ Deleted History；
- Superseded ≠ Silently Overwritten；
- Schema Conformance ≠ Fact Truth；
- Schema 不创造事实；
- Schema 不验证事实；
- Schema 不补全事实；
- Schema 不消除争议；
- Schema 不把 Unknown 变成默认值；
- Schema 不替代 Human Validation；
- Schema 不切断 Evidence Traceability；
- Schema 不使状态不可撤回；
- Schema 不静默覆盖历史；
- Schema 不生成 Legal Fact；
- Schema 不触发 Request Right；
- Design Authorization 不等于 Schema Creation Authorization；
- Schema Creation 不等于 Schema Acceptance；
- Schema Acceptance 不等于 Schema Validation；
- Schema Validation 不等于 Implementation；
- 任何 Review PASS 不等于 Project Owner Acceptance；
- 任何资产存在不等于下游获授权。


## Design Review Questions

Architecture Review 必须评估：

1. Phase 3 Track C 与 Design Spec-only 边界是否准确；
2. Track A、Track B 与 Track C Handoff 是否被完整绑定；
3. 绑定资产身份、接受状态与完整性是否可验证；
4. Materialization Design 与具体 Schema 是否分离；
5. Schema Creation、Acceptance、Validation 与 Implementation 是否分离；
6. 生命周期状态与人工处置是否完整且未混同；
7. Disputed 与 Unknown 是否保持；
8. Traceability 与 Human Validation 是否保持；
9. Revalidation、Revocation、Version 与 Supersession 是否充分；
10. Schema 是否被禁止创造或验证事实；
11. Objective Fact、Legal Fact Candidate 与 Legal Fact 是否隔离；
12. 未来 Schema Creation Authorization 是否必须封闭范围；
13. 是否具备充分 fail-closed 规则；
14. 是否未定义字段、类型、格式或具体结构；
15. 是否未创建 Schema、实例、Validation 或代码；
16. 是否无真实或模拟案件污染；
17. 是否无法律推理或 Request Right；
18. 是否无自动阶段升级。


## Design Spec Acceptance Gates

### FSM-DS-001 Authorization Fidelity

本 Spec 仅包含已授权的 Fact Schema Materialization 抽象治理设计。


### FSM-DS-002 Accepted Handoff Integrity

Track C Handoff 的接受状态和完整性绑定准确。


### FSM-DS-003 Normative Source Integrity

Track A、Track B 和 Track C 的规范来源被封闭识别且可验证。


### FSM-DS-004 Governance / Materialization Separation

Schema Governance Acceptance 与 Materialization Design 明确分离。


### FSM-DS-005 Design / Schema Separation

Design Spec、具体 Schema Creation 与 Schema Acceptance 明确分离。


### FSM-DS-006 Schema / Validation / Implementation Separation

Schema Creation、Schema Validation 与 Implementation 明确分离。


### FSM-DS-007 State Fidelity

八项生命周期状态与五项人工处置完整保留且未混同。


### FSM-DS-008 Dispute Preservation

Disputed 与竞争事实版本不得被自动压缩为单一结论。


### FSM-DS-009 Unknown and Absence Preservation

Unknown 与缺失、不可获得、不适用、已否定、已拒绝及超出范围保持区分。


### FSM-DS-010 Traceability Preservation

Fact 至 Human Validation、Verified Evidence 与 Evidence Governance 的追溯要求完整。


### FSM-DS-011 Human Gate Preservation

结构、模型、评分或自动流程不得替代人工决定。


### FSM-DS-012 Revalidation and Revocation

撤回、失效、被取代和重新验证得到控制。


### FSM-DS-013 Version and Integrity Control

规范基线、未来 Schema 资产及其变更必须可识别、可核验且不得静默覆盖。


### FSM-DS-014 Legal Isolation

Objective Fact、Legal Fact Candidate — Isolated 与 Legal Fact 保持硬隔离。


### FSM-DS-015 Interface Containment

Evidence Registry 保持只读；Schema Creation、Validation、Implementation、Legal Fact Layer 与 Request Right Foundation 保持关闭。


### FSM-DS-016 Closed Future Authorization

未来 Schema Creation 必须由 Project Owner 作出独立、唯一资产且范围封闭的授权。


### FSM-DS-017 Fail-Closed

来源、授权、状态、追溯、人工决定、版本或完整性不明时必须阻断。


### FSM-DS-018 No Concrete Schema

未创建具体 Fact Schema、`fact.yaml`、字段、类型、默认值、约束、YAML、JSON、数据库或 API 结构。


### FSM-DS-019 No Validation or Implementation

未运行 Schema Validation，未创建 Agent、Skill、工具、代码、迁移或部署设计。


### FSM-DS-020 No Real Matter

未导入、构造或分析真实及模拟案件事实。


### FSM-DS-021 No Legal Reasoning

未生成 Legal Fact、Request Right、诉讼策略或胜诉预测。


### FSM-DS-022 No Automatic Escalation

Spec 的物化、Review、PASS 或接受不自动授权 RESULT、具体 Schema、Validation、Implementation 或后续阶段。


### FSM-DS-023 Track A / Track B Inheritance

Track A 的生命周期、人工处置、重新验证及法律隔离与 Track B 的 Schema 治理、缺席语义、追溯及 Materialization Boundary 被完整继承且未改写。


### FSM-DS-024 Sole Artifact / No Result

本次授权仅新增唯一 Design Spec，未创建 RESULT 或任何其他 Track C 资产。


## Authorized Scope

本次 Design Spec 授权仅允许：

1. 物化本 Spec；
2. 执行 Codex 边界与完整性检查；
3. 执行只读 Architecture Review；
4. 在另行获得具体外发授权后执行第三方咨询审查；
5. 准备 Project Owner 的 `SPEC ACCEPTED` 或修订决议。


## Not Authorized

以下行为继续禁止：

1. 创建 Track C RESULT；
2. 创建具体 Fact Schema；
3. 创建或修改 `fact.yaml`；
4. 定义 Schema 字段、字段名称、类型、必填规则、默认值或约束；
5. 选择或创建 YAML、JSON、数据库、API 或其他具体结构；
6. 创建 Schema 实例、示例记录或测试数据；
7. 运行 Schema Validation；
8. 创建迁移、生成器或转换工具；
9. 创建 Agent、Skill、工具或代码；
10. 修改 Track A、Track B 或 Track C Handoff 已接受资产；
11. 修改 Evidence Registry；
12. 导入真实或模拟案件事实；
13. 自动提取或构建案件事实；
14. 生成 Legal Fact；
15. 推导 Request Right；
16. 生成诉讼策略或胜诉预测；
17. 启动 Implementation；
18. 自动激活后续 Track、Layer 或 Phase。


## Artifact Boundary

本次授权仅新增：

TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_SPEC.md

不得新增：

- TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_RESULT.md；
- `fact.yaml`；
- 具体 Fact Schema；
- 字段、类型、默认值或约束；
- YAML、JSON、数据库或 API 结构；
- Schema 实例、样例或测试数据；
- Validation 资产；
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

 ├─ Materialization Handoff:        ACCEPTED
 ├─ Materialization Design Spec:    ACCEPTED — CODEX + DUAL REVIEW PASSED
 ├─ Materialization Design Result:  NOT CREATED / NOT AUTHORIZED
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

TASK_PHASE3_TRACK_C_FACT_SCHEMA_MATERIALIZATION_SPEC

Requested Review:

DESIGN SPEC REVIEW

Review Authorities:

Architecture Coordinator

Third-Party Consultant — ADVISORY ONLY AND SEPARATELY AUTHORIZED

Review Outcome:

```text
Codex Executor Integrity Review:
  PASS

Architecture Coordinator Review:
  PASS (Grade A-)
  BLOCKERS: 0
  NON-BLOCKERS: 2

Third-Party Consultant — Gemini 3.6 Flash:
  PASS (100 / 100 — EXCELLENT)
  BLOCKERS: 0
  ADVISORY ONLY
  REVIEW CHANNEL: AUTHORIZED MANUAL WEB TRANSFER

Project Owner Decision:
  SPEC ACCEPTED

Materialization Design Result:
  NOT CREATED / NOT AUTHORIZED

Concrete Fact Schema / fact.yaml:
  NOT CREATED / NOT AUTHORIZED

Schema Validation / Implementation:
  NOT AUTHORIZED
```


## Next Authorized Action

当前不存在自动获准的下一动作。

Spec 的接受不授权创建 RESULT、具体 Schema、`fact.yaml`、字段、类型、默认值、约束、YAML/JSON、数据库/API 结构、Schema 实例、Validation、实现代码、真实或模拟案件事实、Legal Fact 或 Request Right。

是否创建 Track C Materialization Design Result，必须由 Project Owner 另行明确授权。

是否进入具体 Fact Schema Creation，必须由 Project Owner 作出独立、唯一资产且范围封闭的授权决议。

任何后续授权均不得由本 Spec 的接受、Architecture Review PASS 或第三方咨询 PASS 自动推定。
