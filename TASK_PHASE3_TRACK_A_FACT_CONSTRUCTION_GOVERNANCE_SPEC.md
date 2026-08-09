# TASK_PHASE3_TRACK_A_FACT_CONSTRUCTION_GOVERNANCE_SPEC

## Status

ACCEPTED — DESIGN SPEC REVIEW PASSED


## Phase Identification

Phase:
PHASE 3

Track:
Track A

Name:
FACT CONSTRUCTION GOVERNANCE

Deliverable Type:
DESIGN SPEC ONLY


## Authorization Basis

本 Spec 依据 Project Owner 作出的以下授权决议编制：

TASK_PHASE3_TRACK_A_FACT_CONSTRUCTION_GOVERNANCE_DESIGN_AUTHORIZATION

授权状态：

FACT CONSTRUCTION GOVERNANCE DESIGN AUTHORIZED

授权限制：

- 仅允许治理设计；
- 不创建 Fact Schema 或 YAML；
- 不设计或实现事实抽取 Agent、Skill、工具或代码；
- 不导入、处理或分析真实案件材料；
- 不生成或推导法律事实；
- 不推导请求权基础；
- 不生成诉讼策略或胜诉预测；
- 不自动激活任何后续阶段。


## Purpose

本 Spec 定义 Evidence Governance Layer 与 Legal Fact Layer 之间的事实构建治理机制。

其目的不是执行案件事实提取或法律分析，而是规定：

- 何种证据输入具有进入事实构建流程的治理资格；
- 事实候选如何形成、验证、争议保留、退回与失效；
- 客观事实与法律事实之间如何保持硬性隔离；
- 人工审核如何成为关键状态转换的必要门禁；
- 上下游系统只能在何种边界内交换治理信息；
- 任何越权、缺失或不确定状态如何以 fail-closed 方式阻断。


## Normative Language

本 Spec 中：

- “必须”表示强制治理要求；
- “不得”表示硬性禁令；
- “可以”表示在全部前置门禁满足时允许的行为；
- “仅”表示排他性边界；
- “阻断”表示不得继续向下一状态或下游层流转；
- “人工审核”表示由具备相应授权的人类角色作出的可追溯决定，模型输出不得替代该决定。


## Non-Schema Declaration

本 Spec 仅定义治理语义、状态、门禁、责任和接口边界。

本 Spec：

- 不定义事实对象的具体字段；
- 不规定 YAML、JSON、数据库或 API 数据结构；
- 不创建 `fact.yaml`；
- 不规定实现类、函数、服务、Agent、Skill 或工作流代码；
- 不包含任何真实案件事实实例；
- 不构成 Legal Fact Layer、Request Right Foundation 或其实现授权。


## Architectural Position

受控架构关系：

```text
Evidence Governance Layer
        |
        |  verified evidence reference only
        v
Fact Construction Governance
        |
        |  human-validated objective fact boundary only
        v
Legal Fact Isolation Boundary
        |
        |  inactive unless separately authorized
        v
Legal Fact Layer
        |
        |  no invocation or inference authorized in this phase
        v
Request Right Foundation
```

Fact Construction Governance 不得修改 Evidence Registry，不得替代 Legal Fact Layer，也不得调用或模拟 Request Right Foundation。


## Governance Objectives

### FC-D-001 Evidence / Fact Separation

Evidence 与 Fact 必须作为不同治理对象处理。

Evidence 的存在、完整性或已验证状态，不当然证明某一 Fact 成立。

任何从 Evidence 到 Fact 的转换必须形成独立、可审核、可撤回的事实候选，并保留其证据来源和形成路径。


### FC-D-002 Fact / Legal Fact Separation

Objective Fact 与 Legal Fact 必须位于不同治理层。

Fact Construction Governance 只能形成和治理客观事实及其候选状态，不得赋予法律定性、法律效果或请求权意义。


### FC-D-003 Traceability

任何事实候选或经验证事实必须能够追溯至：

```text
Fact State
    ↓
Construction / Validation Decision
    ↓
Verified Evidence Reference
    ↓
Evidence Governance Verification
```

追溯链断裂时，事实不得保持可向下游流转的状态。


### FC-D-004 Dispute Preservation

证据冲突、主体异议、语义歧义和信息不足必须被显式保留。

系统不得通过合并、平均、置信度排序、单方覆盖或模型偏好自动消除争议。


### FC-D-005 Human Validation

事实成立、争议认定、未知认定、重新开放以及进入 Legal Fact Candidate 隔离区，均必须经过相应人工门禁。

模型、自动化流程或下游系统不得作为最终批准者。


### FC-D-006 Reversibility

事实状态必须能够因证据撤回、版本变化、验证失效、发现冲突或人工复核而重新进入审核。

任何已验证状态均不得被视为不可撤销。


### FC-D-007 No Silent Escalation

事实状态变化不得自动触发：

- 法律事实生成；
- 法律关系判断；
- 请求权基础推导；
- 诉讼策略生成；
- 后续阶段授权；
- 实现或代码生成。


## Governance Red Lines

出现以下任一情形时必须阻断：

1. 输入证据未达到 Evidence Governance Layer 的 Verified Evidence 状态；
2. 无法建立稳定、可追溯的证据来源关系；
3. 事实候选包含未经隔离的法律评价、责任判断或请求权推导；
4. 争议或信息不足被自动改写为确定事实；
5. 关键状态转换缺少获授权的人类审核；
6. 审核者的权限、身份或决定无法验证；
7. 证据状态发生撤回、失效或重大版本变化但事实未重新验证；
8. 下游层试图反向修改事实或证据治理状态；
9. 处理对象包含未经授权的真实案件材料；
10. 任何流程试图跨越本阶段授权边界。


## Fact Lifecycle

### Lifecycle States

#### 1. Unverified Fact Candidate

含义：

由符合准入条件的 Verified Evidence 提出、但尚未完成人工事实验证的客观陈述候选。

治理限制：

- 不得表述为已成立事实；
- 不得进入 Legal Fact Layer；
- 不得用于请求权或策略推导；
- 必须与来源证据保持可追溯关联。


#### 2. Validation Pending

含义：

事实候选已提交至 Human Validation Gate，等待获授权的人类审核。

治理限制：

- 等待期间不得自动升级；
- 新增冲突、证据变化或来源失效必须中止当前审核；
- 模型建议仅可作为非决定性辅助信息，且不得替代审核结论。


#### 3. Verified Objective Fact

含义：

事实候选已由获授权的人类审核，并被确认在限定证据范围内得到支持。

必要验证结论：

Confirmed

治理限制：

- “Verified”仅表示通过本治理层的事实验证，不表示完成法律评价；
- 必须保留验证范围、证据基础及人工决定的可追溯性；
- 不得直接转化为 Legal Fact；
- 证据基础变化时必须重新验证。


#### 4. Disputed Objective Fact

含义：

事实候选存在实质冲突、明确异议、相互竞争的事实版本，或人工审核无法消除的争议。

必要验证结论：

Disputed

治理限制：

- 各争议版本及其证据基础必须分别保留；
- 不得自动选择“最可能”版本作为确定事实；
- 不得以置信度或多数证据数量替代人工争议处理；
- 未经新的人工验证，不得升级为 Verified Objective Fact。


#### 5. Unknown / Insufficient

含义：

现有证据不足以支持、否定或完整描述事实候选。

必要验证结论：

Unknown

治理限制：

- 不得以推测、常识补全、默认值或概率预测填补缺口；
- 不得将未知状态静默省略；
- 仅在新增或重新验证的证据出现后，方可重新进入 Validation Pending。


#### 6. Rejected / Out of Scope

含义：

候选不具备事实构建资格，或超出本治理层授权范围。

适用情形包括：

- 缺少合格证据来源；
- 内容属于法律评价或请求权推导；
- 内容无法形成可验证的客观陈述；
- 来源或处理场景未经授权。

治理限制：

不得向任何下游事实或法律层流转。


#### 7. Superseded / Revalidation Required

含义：

原状态因证据撤回、证据版本变化、新冲突出现、人工决定被撤销或治理规则变化而不再可依赖。

治理限制：

- 原验证结论必须停止作为当前有效结论使用；
- 不得静默覆盖历史状态；
- 如需继续使用，必须重新进入 Validation Pending。


#### 8. Legal Fact Candidate — Isolated

含义：

经独立人工门禁确认，仅具备在未来、经另行授权的 Legal Fact Layer 中接受法律评价的资格。

该状态：

- 不是 Legal Fact；
- 不表示任何法律关系、法律性质、责任或请求权已经成立；
- 不授权启动法律推理；
- 不得触发 Request Right Foundation；
- 在 Legal Fact Layer 未获单独授权时必须保持隔离和不可执行。


## State Transition Rules

### State Set Definitions

本节中的状态集合仅用于表达治理规则的适用范围，不构成 Fact Schema、字段定义或实现数据结构。

`Any Reviewable State` 明确且仅包括：

- Unverified Fact Candidate；
- Validation Pending；
- Verified Objective Fact；
- Disputed Objective Fact；
- Unknown / Insufficient；
- Superseded / Revalidation Required；
- Legal Fact Candidate — Isolated。

`Any Reviewable State` 不包括：

- Verified Evidence；
- Rejected / Out of Scope；
- Legal Fact。

`Any Relied-Upon State` 明确且仅包括：

- Verified Objective Fact；
- Disputed Objective Fact；
- Unknown / Insufficient；
- Legal Fact Candidate — Isolated。

Unverified Fact Candidate、Validation Pending、Rejected / Out of Scope 及 Superseded / Revalidation Required 不得作为当前可依赖事实状态。

对 Disputed Objective Fact 或 Unknown / Insufficient 的“依赖”仅指下游必须保留其争议或未知治理处置，不得将其视为事实已获确认。


### FC-T-001 Verified Evidence to Unverified Fact Candidate

触发条件：

存在建立客观事实候选的设计内合法请求。

前置门禁：

- 来源处于 Verified Evidence 状态；
- 来源引用可稳定追溯；
- 候选表达不包含法律评价；
- 当前处理环境和授权范围有效。

阻断条件：

任一前置门禁缺失，或输入包含未经授权的真实案件材料。


### FC-T-002 Unverified Fact Candidate to Validation Pending

触发条件：

候选被提交至 Human Validation Gate。

前置门禁：

- 候选与证据来源的形成路径可供审核；
- 不确定性、冲突和信息缺口未被隐藏；
- 审核者权限可验证。

阻断条件：

候选来源不完整、候选范围不明确或审核者不具备授权。


### FC-T-003 Validation Pending to Verified Objective Fact

触发条件：

获授权的人类审核者作出 Confirmed 决定。

前置门禁：

- 审核基于当前有效的 Verified Evidence；
- 支持范围和限制已被明确；
- 无未披露的实质冲突；
- 审核决定可追溯。

阻断条件：

仅存在模型判断、自动置信度或未经确认的推断。


### FC-T-004 Validation Pending to Disputed Objective Fact

触发条件：

获授权的人类审核者确认存在实质争议，或发现不能合并的竞争事实版本。

治理结果：

保留 Disputed 状态和全部相关争议路径，不得选边或自动消歧。


### FC-T-005 Validation Pending to Unknown / Insufficient

触发条件：

获授权的人类审核者确认现有证据不足。

治理结果：

保留 Unknown 状态和信息缺口，不得推测补全。


### FC-T-006 Any Reviewable State to Rejected / Out of Scope

触发条件：

人工审核确认候选不具备治理资格或超出授权范围。

治理结果：

停止下游流转，但保留可审计的拒绝决定。


### FC-T-007 Any Relied-Upon State to Superseded / Revalidation Required

触发条件：

- 证据被撤回或验证状态失效；
- 证据出现重大版本变化；
- 新证据形成实质冲突；
- 人工决定被撤销；
- 适用治理规则发生影响性变化。

治理结果：

立即停止将原状态作为当前有效事实使用，并要求重新验证。


### FC-T-008 Verified Objective Fact to Legal Fact Candidate — Isolated

触发条件：

获授权的人类角色明确批准其仅进入法律事实候选隔离区。

前置门禁：

- Objective Fact 已通过本治理层验证；
- 来源与验证链完整；
- 法律评价尚未发生；
- 下游阶段具有独立、明确且仍然有效的授权。

阻断条件：

- 下游阶段未获授权；
- 试图自动生成 Legal Fact；
- 试图同步触发 Request Right Foundation；
- 试图以模型决定替代人工批准。

当前阶段执行状态：

BLOCKED — LEGAL FACT GENERATION NOT AUTHORIZED


### FC-T-009 Reopening

Verified Objective Fact、Disputed Objective Fact、Unknown / Insufficient 或 Legal Fact Candidate — Isolated 均可因新证据、证据失效、人工复核或治理变更重新进入 Validation Pending。

重新开放不得删除或覆盖先前决定。


### FC-T-010 Return for Revalidation

适用来源状态：

- Verified Objective Fact；
- Disputed Objective Fact；
- Unknown / Insufficient；
- Superseded / Revalidation Required；
- Legal Fact Candidate — Isolated。

触发条件：

获授权的人类审核者明确作出 Return for Revalidation 决定。

目标状态：

Validation Pending

治理结果：

- 暂停依赖原有事实状态；
- 保留原状态、原审核决定及重新验证原因；
- 要求基于当前有效的 Verified Evidence 重新执行 Human Validation Gate；
- 不得将退回动作解释为 Confirmed、Rejected 或任何法律评价；
- 不得自动触发 Legal Fact Layer 或 Request Right Foundation。


## Transition Control Matrix

| From | To | Required Trigger | Human Gate | Automatic Transition |
|---|---|---|---|---|
| Verified Evidence | Unverified Fact Candidate | 合法的候选形成请求 | 形成阶段按权限控制 | Prohibited |
| Unverified Fact Candidate | Validation Pending | 正式提交审核 | Required | Prohibited |
| Validation Pending | Verified Objective Fact | Confirmed 决定 | Required | Prohibited |
| Validation Pending | Disputed Objective Fact | Disputed 决定 | Required | Prohibited |
| Validation Pending | Unknown / Insufficient | Unknown 决定 | Required | Prohibited |
| Any Reviewable State | Rejected / Out of Scope | 拒绝或越界决定 | Required | Prohibited |
| Any Relied-Upon State | Superseded / Revalidation Required | 来源或治理基础失效 | Required for final disposition | Only protective blocking may be automatic |
| Verified Objective Fact / Disputed Objective Fact / Unknown / Insufficient / Superseded / Revalidation Required / Legal Fact Candidate — Isolated | Validation Pending | Return for Revalidation 决定 | Required | Prohibited |
| Verified Objective Fact | Legal Fact Candidate — Isolated | 独立批准且下游另行授权 | Required | Prohibited |
| Legal Fact Candidate — Isolated | Legal Fact | Separate future authorization | Required under future design | Not Authorized |

保护性自动动作仅限暂停使用、标记待复核或阻断下游，不得自动生成新的事实结论。


## Evidence to Fact Conversion Governance

### FC-EF-001 Verified Evidence Prerequisite

仅处于 Evidence Governance Layer 的 Verified Evidence 可以成为事实候选的来源。

“Verified Evidence”仅表示证据治理资格满足，不等同于事实已被证明。


### FC-EF-002 Non-Mutation

事实构建不得修改、重写、补全或覆盖 Evidence Registry 中的证据对象及其验证状态。


### FC-EF-003 Minimal Objective Expression

事实候选必须限定为证据可支持的最小客观陈述。

不得加入：

- 法律定性；
- 主观责任归属；
- 请求权含义；
- 未被证据支持的因果补全；
- 对未知信息的推测；
- 为下游结论服务的选择性改写。


### FC-EF-004 Source-Bound Construction

每一事实候选必须与其来源证据及形成过程保持可追溯关系。

不得仅保留事实文本而丢失证据路径。


### FC-EF-005 Multi-Source Discipline

多个证据来源支持相近陈述时：

- 不得因文字相似而自动合并；
- 不得因数量优势而自动确认；
- 必须保留来源差异、版本差异和支持范围差异；
- 出现实质冲突时必须进入 Disputed 或人工审核路径。


### FC-EF-006 Uncertainty Preservation

时间、主体、行为、范围、因果或语义存在不确定性时，必须保留该不确定性。

模型置信度、评分或概率不得替代 Confirmed、Disputed、Unknown 的人工验证结论。


### FC-EF-007 No Negative Inference From Silence

证据未记载某一事项，不当然证明该事项不存在。

除非未来另行授权的治理规则明确允许且经过人工审核，否则不得从“未出现”自动推导“未发生”。


### FC-EF-008 Construction Independence

事实候选的形成不得以预设法律结论、请求权目标或诉讼策略为导向。

下游需求不得反向改变证据含义或事实状态。


## Fact to Legal Fact Isolation

### FC-FL-001 Hard Boundary

Objective Fact 与 Legal Fact 之间设置不可自动跨越的硬性边界。

本治理层不得执行法律要件匹配、法律关系认定、责任评价、法律效果判断或请求权推导。


### FC-FL-002 Candidate Is Not Conclusion

Legal Fact Candidate 仅表示“具备接受未来法律评价的候选资格”。

它不表示：

- 已形成 Legal Fact；
- 已满足任何法律要件；
- 已成立任何法律关系；
- 已产生责任或请求权；
- 已获得进入诉讼策略层的资格。


### FC-FL-003 Separate Authorization

任何从 Legal Fact Candidate — Isolated 向 Legal Fact 的转换，必须由 Project Owner 另行授权，并受未来独立 Spec、人工门禁和 Review 约束。

本 Spec 不提供该转换的执行规则。


### FC-FL-004 No Backflow Contamination

Legal Fact Layer、Request Right Foundation 或策略层不得反向要求事实层：

- 选择有利事实版本；
- 隐藏争议或未知状态；
- 改写证据支持范围；
- 将法律判断伪装为客观事实；
- 为满足要件而补全事实。


### FC-FL-005 Inactive Downstream

在 Legal Fact Layer 与 Request Right Foundation 未获单独授权前：

- 所有相关接口必须保持逻辑关闭；
- 不得发送执行请求；
- 不得预计算法律结论；
- 不得以“设计测试”名义使用真实或模拟案件开展法律推导；
- 不得因本 Spec 完成而自动改变其状态。


## Human Validation Gate

### Gate Principles

Human Validation Gate 必须满足：

1. 审核主体是具备当前阶段和相应动作权限的人类角色；
2. 审核对象、证据基础、争议和不确定性对审核者可见；
3. 审核决定必须明确为 Confirmed、Disputed、Unknown、Rejected 或 Return for Revalidation；
4. 审核决定及其适用范围必须可追溯；
5. 审核不得超出 Evidence 所能支持的范围；
6. 模型输出不得被视为人工确认；
7. 权限不明、依据不明或链路不完整时必须阻断；
8. 涉及进入 Legal Fact Candidate 隔离区时必须使用独立门禁。


### Separation of Duties

治理角色在概念上分为：

- Construction Submitter：提交事实候选，不拥有最终验证权；
- Fact Validator：对客观事实候选作出验证决定；
- Legal Boundary Approver：仅决定是否允许进入 Legal Fact Candidate 隔离区，不在本阶段生成 Legal Fact；
- Governance Controller：监督授权、越界阻断、复核与状态回退。

同一主体不得仅凭其提交行为自动批准自己的候选。

具体身份系统、角色映射和权限实现不属于本 Spec 的授权范围。


### Review Outcomes

允许的人工审核结果：

- Confirmed；
- Disputed；
- Unknown；
- Rejected / Out of Scope；
- Return for Revalidation。

任何审核结果均不得自动触发法律事实、请求权或策略生成。


### Mandatory Revalidation Events

发生以下事件时必须重新验证：

- 来源证据被撤回、失效或降级；
- 来源证据发生影响事实含义的版本变化；
- 新证据与当前事实形成实质冲突；
- 原审核权限或决定被撤销；
- 发现来源链、形成过程或审核记录不完整；
- 治理规则变化影响原结论有效性。


## Interface Boundaries

本节仅定义抽象治理契约，不定义 API、消息格式、字段、Schema 或实现。


### Evidence Registry Inbound Boundary

允许的交互：

- 只读获取符合准入条件的 Verified Evidence 引用；
- 核验证据当前验证状态、版本稳定性和可追溯性；
- 接收证据撤回、失效或重大变化的治理信号。

禁止的交互：

- 修改 Evidence Registry；
- 提升或覆盖证据验证状态；
- 将原始证据直接标记为 Fact；
- 绕过 Evidence Governance Layer 接收未验证输入；
- 导入真实案件材料到本设计资产。

Fail-closed 要求：

证据状态、来源、版本或授权无法确认时，不得形成可审核的事实候选。


### Legal Fact Layer Outbound Boundary

允许声明但当前不得激活的边界能力：

- 在未来独立授权后，仅提供经过人工验证的客观事实及其治理状态；
- 保留 Confirmed、Disputed、Unknown 和失效状态；
- 保留来源与人工验证的可追溯关系；
- 发送撤回或重新验证要求。

禁止的交互：

- 自动创建 Legal Fact；
- 自动执行法律要件匹配；
- 隐藏 Disputed 或 Unknown；
- 将候选资格表述为法律结论；
- 在下游未授权时发送或执行转换请求。


### Request Right Foundation Boundary

当前状态：

NOT AUTHORIZED / NOT STARTED

Fact Construction Governance：

- 不得直接调用 Request Right Foundation；
- 不得提供请求权结论；
- 不得根据请求权目标筛选或改写事实；
- 不得触发任何请求权分析流程；
- 不得将 Spec 完成视为 Request Right Foundation 的启动条件。


### Boundary Change and Revocation

当上游 Evidence 状态失效时，下游依赖必须被阻断并进入重新验证。

下游不得通过缓存、复制或派生状态规避撤回和重新验证要求。

具体同步机制、传输协议和数据结构留待后续独立授权。


## Audit and Traceability Requirements

在不规定具体字段或存储实现的前提下，治理过程必须能够证明：

- 事实候选来源于何种已验证证据；
- 候选如何从证据形成；
- 谁在何种授权下提交和审核；
- 审核作出了何种治理决定及其限定范围；
- 是否存在争议、未知或信息缺口；
- 何时及为何发生状态变化、阻断、撤回或重新验证；
- 是否曾请求进入 Legal Fact Candidate 隔离区；
- 是否发生越界尝试及其阻断结果。

审计可追溯性不得通过删除历史决定或静默覆盖状态实现“整洁化”。


## Failure Handling

### Fail-Closed Default

无法确认输入资格、权限、追溯链、审核决定或阶段授权时，默认结果必须是阻断。


### No Error-to-Truth Conversion

系统错误、解析失败、超时、缺失或冲突不得被转换为 Confirmed 事实。


### Protective Suspension

在证据撤回、权限异常或追溯链断裂时，可以自动暂停事实使用并要求复核。

自动保护动作不得：

- 生成新的事实结论；
- 将状态升级为 Confirmed；
- 消除 Disputed 或 Unknown；
- 跨越 Legal Fact 隔离边界。


### Recovery

恢复使用必须经过：

1. 上游资格恢复确认；
2. 追溯链完整性确认；
3. 必要的 Human Validation Gate；
4. 明确的状态恢复决定。


## Governance Invariants

以下不变量在所有状态和接口中必须持续成立：

- Evidence ≠ Fact；
- Fact ≠ Legal Fact；
- Verified Evidence ≠ Verified Objective Fact；
- Legal Fact Candidate ≠ Legal Fact；
- Confirmed 不得由模型单独授予；
- Disputed 不得自动折叠为 Confirmed；
- Unknown 不得由推测自动补全；
- 证据撤回必须能够使依赖事实进入重新验证；
- 下游目标不得反向污染事实形成；
- 缺少授权时必须阻断；
- Design Authorization 不等于 Schema、Code、Legal Reasoning 或 Implementation Authorization。


## Explicitly Prohibited Activities

本 Spec 编制和 Review 期间继续执行“七不准”：

1. 不创建 `fact.yaml` 或任何 Fact Schema；
2. 不设计或编写案件事实抽取 Agent、Skill、工具或代码；
3. 不导入任何真实案件材料或物理文件；
4. 不自动生成或推导法律事实；
5. 不推导 Request Right；
6. 不生成诉讼策略或胜诉预测；
7. 不跨阶段自动激活后续流程。

同时不得创建：

TASK_PHASE3_TRACK_A_FACT_CONSTRUCTION_GOVERNANCE_RESULT.md

除非 Spec 已完成 Review 且 Project Owner 另行明确授权。


## Deferred Decisions

以下事项明确留待未来独立授权，不在本 Spec 中决定：

- Fact Schema 及具体字段；
- YAML、JSON、数据库或 API 结构；
- Agent、Skill、工具、代码或部署架构；
- 具体身份认证、角色映射和权限系统；
- 具体审计存储、保留期限和技术实现；
- Legal Fact 生成规则；
- 法律要件、法律关系或请求权模型；
- 真实案件材料的接入与分析；
- 测试数据、测试案件和实现验收；
- Request Right Foundation 和诉讼策略层设计。


## Design Spec Acceptance Gates

### FC-DS-001 Authorization Fidelity

Spec 仅包含 Design Spec 授权范围内的抽象治理设计。


### FC-DS-002 Evidence / Fact Separation

Verified Evidence 不被直接等同于 Verified Objective Fact。


### FC-DS-003 Fact / Legal Fact Separation

Objective Fact、Legal Fact Candidate 与 Legal Fact 被明确分离。


### FC-DS-004 State Governance Completeness

生命周期、触发条件、人工门禁、阻断规则、回退与重新验证机制完整。


### FC-DS-005 Dispute and Unknown Preservation

Confirmed、Disputed、Unknown 均被保留，且不存在自动消争议或推测补全路径。


### FC-DS-006 Human Validation Preservation

关键状态转换必须由获授权的人类角色确认，模型不得作为最终批准者。


### FC-DS-007 Interface Containment

Evidence Registry 为只读治理边界；Legal Fact Layer 与 Request Right Foundation 未被激活。


### FC-DS-008 No Schema or Implementation

未创建 Fact Schema、YAML、API 数据结构、Agent、Skill、工具或代码。


### FC-DS-009 No Real Matter Pollution

未导入、引用或分析任何真实案件材料。


### FC-DS-010 No Legal Reasoning

未生成法律事实、法律关系、请求权、诉讼策略或胜诉预测。


### FC-DS-011 No Automatic Escalation

Spec 完成和 Review 均不得自动授权 RESULT、Schema、Implementation 或后续阶段。


## Review Submission

Review Object:

TASK_PHASE3_TRACK_A_FACT_CONSTRUCTION_GOVERNANCE_SPEC

Review Authorities:

Architecture Coordinator

Third-Party Consultant:

Gemini 3.6 Flash — ADVISORY ONLY

Requested Review:

DESIGN SPEC REVIEW

Final Review Outcome:

Architecture Coordinator:
PASS — Grade A

Third-Party Consultant:
PASS — Grade A

Original Review Findings:
RESOLVED

Project Owner Decision:
DESIGN SPEC ACCEPTED


## Current System State

```text
Phase 3 Track A (Fact Construction Governance):

 ├─ Governance Handoff:             CLOSED (SHA Bound & Accepted)
 ├─ Governance Architecture Review: PASS (Grade A)
 ├─ Design Authorization:           APPROVED (TRANSITION COMPLETE)
 └─ Governance Design Spec:         ACCEPTED (DUAL REVIEW PASSED)

Fact Schema (fact.yaml):            NOT CREATED
Result Document:                    NOT CREATED / NOT AUTHORIZED
Real Matter Analysis:               NOT AUTHORIZED
Legal Fact Generation:              NOT AUTHORIZED
Legal Reasoning & Request Right:     NOT AUTHORIZED
Implementation / Code:              NOT AUTHORIZED
Next Phase Authorization:           NOT GRANTED
```


## Next Authorized Action

本 Spec 不自动授权任何下一动作。

是否进入 RESULT、Fact Schema、Implementation、Legal Fact Generation、Request Right Foundation 或任何后续状态，必须由 Project Owner 另行作出明确授权决议。

在新的授权决议作出前，不得创建新资产或启动后续流程。
