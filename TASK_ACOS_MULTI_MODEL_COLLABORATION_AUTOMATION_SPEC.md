# TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_SPEC

## Status

SECOND LIMITED REVISION MATERIALIZED — AUTHORIZED RE-REVIEW PENDING


## System Identification

Operating System:

```text
ACOS — Architecture & Control Operating System
```

Capability Track:

```text
MULTI-MODEL COLLABORATION AUTOMATION
```

Delivery Type:

```text
DESIGN SPEC ONLY
```

Target Project:

```text
claude-for-legal-cn-phase2.5
```


## Authorization Basis

Project Owner Decision:

```text
ACOS MULTI-MODEL COLLABORATION AUTOMATION DESIGN SPEC AUTHORIZED
```

Unique Authorized Deliverable:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_SPEC.md
```

Bound Handoff SHA-256:

```text
3B615C826EA1D54C9BCAB8A530BECCE4F935197BAE3174AD57D1958296692919
```

Authorized Scope:

```text
DESIGN SPEC ONLY
```

Authorized Design Subjects:

1. 四方角色与权限矩阵；
2. Internal / External Review 生命周期与状态机；
3. Review Packet 的抽象治理契约；
4. Queue、Ledger 与 Decision Gate 的治理边界；
5. SHA 绑定、失效、撤回与重新审查规则；
6. Standing External Review Authorization 边界；
7. Cross-Vendor 独立性判定；
8. 额度不足、外部不可用及模型分歧的 Fail-Closed；
9. G0–G5 数据隔离和真实案件外传禁令；
10. Review Questions 与 Acceptance Gates。

Explicitly Unchanged Authorization States:

```text
External Model Invocation / Asset Transfer:
NOT AUTHORIZED

API / Connector / MCP / Code / Credential:
NOT AUTHORIZED

Executable Configuration / Concrete Field Schema:
NOT AUTHORIZED

Real Matter / Implementation:
NOT AUTHORIZED

RESULT:
NOT AUTHORIZED
```

本授权不启动 External Connection Test、Design Review、External Review、Implementation 或任何后续阶段。

上述句子记录原始 Design Spec materialization authorization 的边界。后续 Project Owner 仅另行授权了本次第二次受限修订后 fixed-SHA 的 Architecture Coordinator internal re-review；该单项授权不适用于其他 Design Review 或任何 External Review。


## Bound Accepted Handoff

Handoff Asset:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_HANDOFF.md
```

Bound SHA-256:

```text
3B615C826EA1D54C9BCAB8A530BECCE4F935197BAE3174AD57D1958296692919
```

Internal Architecture Review:

```text
PASS — GRADE A
30 OF 30 HANDOFF ACCEPTANCE GATES PASS
BLOCKERS: 0
NON-BLOCKERS: 0
```

External Advisory Review:

```text
OUTCOME:
PASS

PROVIDER / MODEL:
Google / Gemini 3.6 Flash

REASONING CONFIGURATION:
HIGH

TRANSFER MODE:
MANUAL

ATTESTATION:
PROJECT OWNER ATTESTED

BOUND ASSET SHA-256:
3B615C826EA1D54C9BCAB8A530BECCE4F935197BAE3174AD57D1958296692919
```

Project Owner Decision:

```text
HANDOFF ACCEPTED & SHA BOUND
```

Handoff Governance State:

```text
ACCEPTED & CLOSED
```


## Acceptance Snapshot Rule

本 Spec 记录 Handoff 的当前治理接受快照，不回写或修改已固定 SHA 的 Handoff。

若 Handoff 文件内部保留了物化时的历史状态文本，该历史文本不覆盖后续已经形成并由 Project Owner 确认的：

- Internal Review；
- External Advisory Review；
- Project Owner Acceptance；
- SHA binding。

Handoff 的接受不自动授予：

- Automation Design Review；
- Standing External Review Authorization；
- External Invocation；
- Asset Transfer；
- API、Connector、MCP、Code 或 Credential；
- Implementation；
- 任何其他项目资产的外部审查。

External Advisory Review 的 `MANUAL / PROJECT OWNER ATTESTED` 属性必须保真记录，不得伪装为：

- connector-observed response；
- API-generated ledger event；
- standing authorization dispatch；
- system-verified transfer。


## Limited Revision Record

Original Design Spec SHA-256:

```text
948A62F86310F78BB0310365555D4200976E56A01AE09ED3D9EC7EDEAABA65C8
```

Initial Internal Design Review:

```text
OUTCOME:
FAIL — GRADE C

ACCEPTANCE GATES:
41 PASS / 4 FAIL

REVIEW QUESTIONS:
41 PASS / 4 FAIL

BLOCKERS:
3

NON-BLOCKERS / REGRESSIONS / OVERREACH:
0 / 0 / 0
```

Failed Gates:

```text
MMCA-DS-014
MMCA-DS-016
MMCA-DS-019
MMCA-DS-036
```

Project Owner Limited Revision Authorization:

1. 关闭 B1，补齐 External PASS、FAIL、BLOCKED、LIMITED、PENDING、UNBOUND、CANCELLED 等状态的唯一总体映射、Transition Rules 与 Transition Matrix；
2. 关闭 B2，补齐 Human Review resolution、Project Owner 各项决定以及 Design Spec Review FAIL、拒绝、暂停和撤回路径；
3. 关闭 B3，统一 per-asset authorization 与 Standing Authorization 的 Fail-Closed 语义；
4. 不扩大其他设计范围，不创建任何新资产；
5. 修订后计算新 SHA，并由 Architecture Coordinator 重新执行完整的 45 项只读 Design Review。

本记录不接受原 SHA，不授权 External Invocation、Asset Transfer、RESULT、runtime asset 或 Implementation。


## Second Limited Revision Record

First Revised Design Spec SHA-256:

```text
FFF0DD9846A73C2919FBC7062A46A4295CDCAD8B3FAF35173287C5736838AB64
```

First Re-Review:

```text
OUTCOME:
FAIL — GRADE C

ACCEPTANCE GATES:
41 PASS / 4 FAIL

REVIEW QUESTIONS:
43 PASS / 2 FAIL

BLOCKERS:
4

NON-BLOCKERS / UPSTREAM REGRESSIONS / OVERREACH:
0 / 0 / 0

GATE REGRESSION AGAINST INITIAL REVIEW:
1
```

Failed Gates:

```text
MMCA-DS-014
MMCA-DS-016
MMCA-DS-019
MMCA-DS-040
```

Project Owner Second Limited Revision Authorization:

1. 关闭 RR-B1，分离 `LIMITED` 与 `UNBOUND` 的触发条件；
2. 关闭 RR-B2，统一 PASS / FAIL 分歧进入 Human Review；
3. 关闭 RR-B3，统一 `OWNER HOLD`，并彻底分离 request cancellation 与 asset withdrawal；
4. 关闭 RR-B4，明确仅本次修订后 fixed-SHA Architecture Coordinator internal re-review 已授权，其他 Review 仍未授权；
5. 不创建任何新资产；
6. 修订后计算新 SHA，并重新执行完整的 45 项只读 Review。

本次授权不调用 External Model，不传输项目资产，不创建 RESULT、runtime asset 或 Implementation。


## Objective

定义 ACOS 四方协作自动化的抽象治理设计，使未来系统可以减少人工复制、排队、状态同步和重复核验，同时通过技术门禁阻止错误被接受、传播或进入下游。

本设计追求：

```text
ERROR OCCURRENCE:
REDUCED, NOT ELIMINATED

ERROR DETECTION:
MULTI-LAYERED

ERROR PROPAGATION:
FAIL-CLOSED

FINAL POSITIVE AUTHORITY:
PROJECT OWNER ONLY
```

最高治理公式：

```text
INTERNAL PASS
+
EXTERNAL PASS FROM AN ELIGIBLE INDEPENDENT REVIEWER
+
PROJECT OWNER ACCEPTED
+
SHA MATCH
=
MAY PROCEED
```

任一必要条件不满足：

```text
BLOCKED / PENDING / HUMAN REVIEW REQUIRED
```

本公式中的 `MAY PROCEED` 仅表示满足当前已授权转换的前置条件，不产生新的授权。


## Architectural Position

```text
Authorized Project Asset
        |
        v
Deterministic Integrity Controls
        |
        v
Codex Executor
        |
        v
Internal Architecture Review
        |
        v
Review Orchestration Governance Boundary
        |
        +-----------------------------+
        |                             |
        v                             v
External Review Eligibility      Review Ledger
        |
        v
Review Queue
        |
        v
Cross-Vendor / Human External Review
        |
        v
Response Binding and Reconciliation
        |
        v
Decision Gate
        |
        v
Project Owner
```

Deterministic integrity controls、内部 Review、外部 Review 与 Project Owner Decision 是互补控制，不得相互替代。

本 Spec 不是：

- API 设计；
- Connector 设计；
- MCP 设计；
- Agent 或 Skill 设计；
- 数据库设计；
- 消息队列实现；
- Review Packet Schema；
- 运行时配置；
- credential 管理方案；
- 真实案件审查流程；
- Implementation plan。


## Governing Distinctions

```text
Design Spec
≠
Design Review

Design Review PASS
≠
Design Spec Acceptance

Design Spec Acceptance
≠
Standing External Review Authorization

Standing External Review Authorization
≠
Blanket Asset Transfer Authorization

Review Eligibility
≠
Review Authorization

Review Authorization
≠
Dispatch

Dispatch
≠
Review Completion

Review Completion
≠
Review PASS

Internal Independent Review
≠
External Third-Party Review

Same-Family Review
≠
Cross-Vendor Review

Reviewer PASS
≠
Project Owner Acceptance

Queue State
≠
Authorization State

Ledger Record
≠
Governing Decision

Decision Gate Ready
≠
Asset Accepted

SHA Match
≠
Content Correctness

Manual Transfer
≠
Connector Transfer

Project Owner Attestation
≠
Tool-Observed Evidence

External Unavailable
≠
External FAIL

Quota Exhausted
≠
Permission To Bypass

Human Review Required
≠
Automatic Escalation

Accepted Asset
≠
Downstream Authorization
```


## Governance Principles

### MMCA-D-001 Authorization Fidelity

任何状态转换、外部传输、调用、修订或下游动作必须具有明确且可绑定的 Project Owner 授权依据。


### MMCA-D-002 Sole Positive Authority

ACCEPT、AUTHORIZE、PUBLISH、START EXECUTION 与 START DOWNSTREAM 的正向权力由 Project Owner 独占。

Reviewer PASS、模型多数意见或自动化置信度均不得形成正向授权。


### MMCA-D-003 Reviewer Negative Authority

内部和外部 reviewer 可以在授权范围内：

- PASS as advisory；
- FAIL；
- BLOCK；
- RETURN；
- FLAG；
- REQUEST CLARIFICATION；
- REQUEST REVISION。

其中 PASS 仅表示 reviewer 未发现足以阻断的事项，不产生资产接受。


### MMCA-D-004 Fixed Asset Identity

每项 Review、response 和 Project Owner decision 必须绑定：

- project identity；
- asset filename；
- exact SHA-256；
- review scope。

文件名相同不得替代 SHA 身份。


### MMCA-D-005 Cross-Vendor Independence

外部模型审查必须来自与内部生成及内部审查模型不同的底层模型供应商。

相同供应商的不同模型、不同 session、不同 prompt 或不同子代理，不构成 Cross-Vendor independence。


### MMCA-D-006 No Same-Family Substitution

外部 reviewer 不可用时，可以增加内部检查，但 External Review 状态必须保持 pending。

内部子代理数量增加不得改变 reviewer classification。


### MMCA-D-007 Deterministic Controls Are Non-Substitutive

SHA、资产唯一性、授权状态、禁入项和引用链检查属于确定性门禁。

这些检查可以阻断机械错误，但不得替代语义 Review、外部独立审查或 Project Owner decision。


### MMCA-D-008 Review Blindness

内部和外部 reviewer 应先形成独立结论，再进行结果比对。

初始 Review 不应接收另一 reviewer 的最终 verdict，除非另行授权执行争议复核。


### MMCA-D-009 Minimal Disclosure

任何未来 Review Packet 只能包含完成被授权审查所需的最少内容。

便利性、速度或模型上下文容量不得作为扩大披露范围的理由。


### MMCA-D-010 Data Classification Before Dispatch

外部 dispatch 前必须完成数据分类。

分类不明、内容混合、附件来源不明或脱敏状态不明时，必须阻断。


### MMCA-D-011 Real Matter Isolation

G4 真实案件、Evidence、PII、privileged material 不得进入一般 Standing External Review Authorization。

本 Spec 不设计 G4 的外传例外。


### MMCA-D-012 Credential Isolation

G5 credential 和 secret 绝对禁止进入 Review Packet、prompt、日志、附件或 reviewer response request。


### MMCA-D-013 Fail-Closed

授权、身份、SHA、数据分类、reviewer eligibility、response binding 或 Project Owner decision 任一不明时，状态必须保持 blocked 或 pending。


### MMCA-D-014 No Silent Downgrade

外部服务不可用、额度不足、成本超限或超时时，不得：

- 改用未授权 provider；
- 缩减必要 Review scope 并仍宣称完整 PASS；
- 将 internal review 重标为 external；
- 自动接受；
- 自动升级。


### MMCA-D-015 Human Disagreement Gate

内部与外部结论发生实质分歧时，必须进入 Human Review。

不得通过多数票、模型数量、模型置信度、响应速度或成本自动裁决。


### MMCA-D-016 Immutable History

历史 Review、阻断、取消、撤回、过期、失效和 supersession 不得静默删除或覆盖。

修正必须通过追加保真记录或 superseding decision 表达。


### MMCA-D-017 SHA Change Invalidates Carry-Forward

任何字节变化导致新 SHA 后：

- 原 Review 仅对旧 SHA 有效；
- 原 Project Owner acceptance 仅对旧 SHA 有效；
- 新候选不得继承 PASS；
- 必须重新进行适用的完整性检查和 Review。


### MMCA-D-018 Protective Automation Only

未来自动化只可自动执行保护性动作：

- 阻断；
- 暂停；
- 取消；
- 标记 stale；
- 防止重复 dispatch；
- 在授权范围内有限重试；
- 路由至 Human Review；
- 报告；
- 保留历史。

保护性动作不得成为自动正向授权。


### MMCA-D-019 No Automatic Escalation

Handoff、Spec、Result、Review 或 Acceptance 的完成均不自动启动：

- 下一 Design；
- Standing Authorization；
- External Invocation；
- Asset Transfer；
- Connection Test；
- Code；
- Implementation；
- 下一 Phase、Track 或 Layer。


### MMCA-D-020 Evidence-Level Fidelity

外部审查证据必须区分：

```text
PROJECT OWNER ATTESTED — MANUAL
```

与：

```text
SYSTEM OBSERVED — CONNECTOR
```

两者不得互相伪装。是否可作为 governing external review，取决于适用授权是否允许该 transfer mode。


## Four-Party Role and Authority Matrix

### Party Definitions

#### Codex Executor

Role Class:

```text
AUTHORIZED MATERIALIZATION AND ORCHESTRATION EXECUTOR
```

仅可在明确授权内：

- 物化唯一获准资产；
- 计算 SHA；
- 执行确定性完整性检查；
- 准备未来 Review Packet；
- 维护状态边界；
- 报告 blockers；
- 执行获准的保护性动作。


#### Architecture Coordinator

Role Class:

```text
INTERNAL INDEPENDENT REVIEWER
```

仅可在明确 Review 授权内：

- 对固定 SHA 资产执行只读 Review；
- 独立核验引用和边界；
- 报告 PASS、FAIL、BLOCKER 或 limitation；
- 请求 clarification 或 revision。

其与 Codex 属于同一模型家族时，不得记为 External Review。


#### External Consultant

Role Class:

```text
EXTERNAL THIRD-PARTY ADVISORY REVIEWER
```

可以是：

- 获授权的 Cross-Vendor model；
- 获授权且满足独立性要求的人类顾问。

仅可：

- 接收被授权的最小 Review Packet；
- 对固定 scope 和 SHA 执行只读咨询；
- 返回 advisory outcome、blockers 和 limitations。


#### Project Owner

Role Class:

```text
FINAL GOVERNANCE AUTHORITY
```

唯一有权：

- 授予和撤回授权；
- 接受或拒绝资产；
- 授权修订；
- 授权外部传输和调用；
- 处理或指定处理 Review 分歧；
- 授权后续阶段。


### Decision Rights Matrix

| Action | Codex | Architecture Coordinator | External Consultant | Project Owner |
|---|---|---|---|---|
| Materialize an authorized asset | Execute only | No | No | Authorize |
| Compute and verify SHA | Yes | Independently verify | Verify packet-bound identity | Bind decision |
| Classify internal review | Report | Perform | No | Confirm policy |
| Classify external review | No unilateral authority | No | Declare identity and limits | Authorize and recognize |
| Issue advisory PASS / FAIL | Internal check only | Yes | Yes | Consider |
| Block or request revision | Flag / enforce protection | Yes | Yes | Decide |
| Accept asset | No | No | No | Yes |
| Grant Standing Authorization | No | No | No | Yes |
| Dispatch externally | Execute only if authorized | No | Receive only if authorized | Authorize |
| Change provider or model | No | No | No | Authorize |
| Resolve substantive disagreement | No | Recommend only | Recommend only | Decide or appoint human review |
| Start downstream stage | No | No | No | Authorize |
| Modify accepted asset | Only under revision authorization | No | No | Authorize |
| Create or use credentials | No current authority | No | No | Future separate authorization only |


### Authority Invariant

```text
REVIEWER NEGATIVE AUTHORITY
MAY STOP A TRANSITION

REVIEWER NEGATIVE AUTHORITY
MUST NOT START A TRANSITION
```


## Independence and Reviewer Eligibility

### Internal Functional Independence

Internal Review 可认定为独立任务回合，仅当：

1. reviewer 与 materialization 回合分离；
2. 固定 SHA；
3. 上下文按最小必要提供；
4. 初始阶段不提供 Codex 最终 verdict；
5. reviewer 可独立读取资产并核验；
6. Review 权限为只读；
7. Review Questions 和 Gates 固定；
8. reviewer identity 和 model family 可记录；
9. response 可绑定固定 SHA。


### Cross-Vendor Model Independence

外部模型 Reviewer Eligibility 必须同时满足：

1. 底层模型供应商与内部模型供应商不同；
2. provider identity 已知；
3. model identity 已知；
4. reasoning configuration 与 model identity 分开记录；
5. transport mode 已知；
6. asset 和 packet identity 固定；
7. transfer 已获授权；
8. data classification 允许；
9. reviewer 只读；
10. response 可绑定 asset SHA、packet identity 和 reviewer identity；
11. reviewer 不拥有 Project Owner 权力；
12. limitation 和未审范围可记录。


### Human External Independence

人类顾问可以构成 External Third-Party Review，仅当：

- 身份和角色已获授权；
- 不属于当前生成/内部审查执行链；
- 利益冲突已披露或不存在；
- 接收范围已授权；
- 采用只读 Review；
- response 与固定资产和 SHA 绑定；
- 结论仅为 advisory；
- Project Owner acceptance 保持独立。


### Aggregator and Proxy Rule

仅知道 aggregator、proxy 或中间服务名称，不足以证明 Cross-Vendor independence。

底层 provider 或 model identity 不明时：

```text
EXTERNAL REVIEWER ELIGIBILITY:
BLOCKED
```


### Same-Vendor Rule

以下均只能增强 Internal Review，不构成 Cross-Vendor Review：

- 同供应商不同模型；
- 同模型不同 reasoning level；
- 同模型不同 prompt；
- 同模型不同 session；
- 同模型多个子代理；
- 通过代理服务调用相同底层模型。


### Attestation Evidence Levels

#### Level E0 — Unverified Claim

只有文本声称“已外审”，但缺少 reviewer、asset SHA、outcome 或 transfer mode。

Governance Effect:

```text
EXTERNAL PASS:
NOT ESTABLISHED
```


#### Level E1 — Project Owner Attested Manual Review

Project Owner 明确确认：

- provider / reviewer；
- model；
- reasoning configuration；
- manual transfer；
- reviewed asset；
- exact SHA；
- outcome；
- read-only scope。

Governance Effect:

可在适用授权允许 Manual Review 时作为 external advisory record。

不得标记为 connector-observed。


#### Level E2 — Future System-Observed Connector Review

未来仅在 Connector 和 Invocation 获得独立授权后，系统可以记录 connector-observed evidence。

本 Spec 不建立 E2 能力。


## Governance State Model

### Multi-Axis Requirement

未来协作状态必须至少在概念上区分：

1. Authorization Axis；
2. Asset Integrity Axis；
3. Data Eligibility Axis；
4. Internal Review Axis；
5. External Review Axis；
6. Disagreement Axis；
7. Project Owner Decision Axis；
8. History / Supersession Axis。

这些轴用于保留不同治理事实，不是 Concrete Field Schema。


### Authorization Axis

```text
NOT AUTHORIZED
AUTHORIZED — SCOPED
SUSPENDED
REVOKED
EXPIRED
SUPERSEDED
```

只有 Project Owner 可以产生 `AUTHORIZED — SCOPED`。

系统可以根据已授权规则检测 expiry、revocation 或 mismatch，并执行保护性阻断。


### Asset Integrity Axis

```text
UNBOUND
BOUND — SHA MATCH
MISMATCH
STALE
SUPERSEDED
WITHDRAWN
```

`BOUND — SHA MATCH` 只证明版本身份，不证明内容正确。


### Data Eligibility Axis

```text
UNKNOWN
ELIGIBLE — WITHIN AUTHORIZED CLASS
RESTRICTED — SEPARATE AUTHORIZATION REQUIRED
PROHIBITED
CLASSIFICATION STALE
```


### Internal Review Axis

```text
NOT AUTHORIZED
NOT STARTED
IN PROGRESS
PASS
FAIL
BLOCKED
RETURNED FOR REVISION
STALE
WITHDRAWN
```


### External Review Axis

```text
NOT AUTHORIZED
ELIGIBILITY PENDING
READY
QUEUED
DISPATCHED
RESPONSE PENDING
RESPONSE RECEIVED — BINDING PENDING
PASS
FAIL
LIMITED — SCOPE RESTRICTED
BLOCKED — REVIEW COULD NOT VALIDLY PROCEED
BLOCKED — AUTHORIZATION
BLOCKED — DATA CLASSIFICATION
PENDING — GOVERNING OUTCOME NOT YET AVAILABLE
PENDING — EXTERNAL UNAVAILABLE
PENDING — QUOTA EXHAUSTED
REJECTED — UNBOUND RESPONSE
CANCELLED
SUPERSEDED
STALE
WITHDRAWN
```


### Disagreement Axis

```text
NOT EVALUATED
NONE
DETECTED
HUMAN REVIEW REQUIRED
HUMAN REVIEW IN PROGRESS
RESOLVED — BOTH REVIEWS GOVERNING
RESOLVED — BLOCKER CONFIRMED
RESOLVED — SUPPLEMENTAL REVIEW REQUIRED
RESOLVED — SCOPE OR AUTHORITY INVALID
UNRESOLVED
STALE
```


### Project Owner Decision Axis

```text
NOT REQUESTED
NOT READY
DECISION READY
DECISION PENDING
ACCEPTED — SHA BOUND
REJECTED — SHA BOUND
REVISION AUTHORIZED — SCOPED
HOLD — OWNER
HUMAN REVIEW REQUESTED
WITHDRAWN
SUPERSEDED
```


### History Axis

```text
CURRENT
HISTORICAL
STALE
SUPERSEDED
CANCELLED
WITHDRAWN
```

历史状态不得作为当前 governing status。


## Unique Current Governing Status

未来系统必须为每个 asset SHA 和 review profile 导出唯一的当前 governing status。

各轴的原始状态必须保留，但不得同时声称多个相互冲突的总体状态为“当前”。


### Deterministic Priority

总体状态按以下优先级导出：

1. `WITHDRAWN`；
2. `SUPERSEDED / STALE`；
3. `CANCELLED`；
4. `REJECTED & CLOSED`；
5. `ACCEPTED & CLOSED`；
6. `BLOCKED — INTEGRITY / UNBOUND RESPONSE`；
7. `BLOCKED — DATA / CREDENTIAL`；
8. `BLOCKED — AUTHORIZATION`；
9. `BLOCKED — EXTERNAL REVIEW COULD NOT VALIDLY PROCEED`；
10. `HUMAN REVIEW REQUIRED`；
11. `REVISION REQUIRED — INTERNAL OR EXTERNAL FAIL`；
12. `EXTERNAL REVIEW LIMITED — SCOPE COMPLETION REQUIRED`；
13. `PENDING — EXTERNAL UNAVAILABLE / QUOTA EXHAUSTED`；
14. `EXTERNAL REVIEW PENDING — GOVERNING OUTCOME NOT YET AVAILABLE`；
15. `INTERNAL REVIEW PENDING`；
16. `OWNER HOLD`；
17. `OWNER DECISION PENDING`；
18. `ELIGIBILITY PENDING`；
19. `NOT AUTHORIZED`。

优先级适用条件：

- `ACCEPTED & CLOSED` 仅在相同 SHA 的有效 Project Owner acceptance 存在且资产未被 withdrawn、superseded 或 stale 时成立；
- `CANCELLED` 是当前 governing Review request / profile 的终止状态，不表示 asset 已被 ACCEPTED 或 REJECTED；如果同一 SHA 已存在仍有效的既有 acceptance，取消一个后续非 governing request 不得撤销该 acceptance；
- `REJECTED — UNBOUND RESPONSE` 导出 `BLOCKED — INTEGRITY / UNBOUND RESPONSE`，不得导出 External FAIL；
- `LIMITED — SCOPE RESTRICTED` 导出 `EXTERNAL REVIEW LIMITED — SCOPE COMPLETION REQUIRED`，不得导出完整 External PASS；
- `PENDING`、`PENDING — EXTERNAL UNAVAILABLE` 和 `PENDING — QUOTA EXHAUSTED` 均不得进入 Owner Decision Ready；
- Internal 与 External verdict 存在实质冲突时，`HUMAN REVIEW REQUIRED` 优先于单方 `REVISION REQUIRED`；
- 双方均确认 FAIL 且不存在 verdict disagreement 时，导出 `REVISION REQUIRED`；
- External `BLOCKED` 导出相应 Blocked 状态，不得导出 FAIL、PASS 或 PENDING；
- reviewer PASS 不得使总体状态变为 accepted；
- 后续 Standing Authorization 被撤回，不自动删除已经完成的历史 acceptance，但阻断新的 dispatch；
- 新 SHA 必须作为新的候选身份进入状态判断。


### Current / Historical Separation

同一文件名可以具有多个历史 SHA。

系统必须分别保留：

- 当前候选 SHA；
- 历史 accepted SHA；
- 历史 rejected SHA；
- stale reviews；
- superseded packets；
- cancelled dispatches；
- withdrawn decisions。

历史 PASS 不得成为新 SHA 的当前 PASS。


## Design Spec Governance Lifecycle

本节只描述当前 Design Spec 自身的治理生命周期。


### Stage DS0 — Handoff Accepted

Entry Conditions:

- Handoff SHA 固定；
- Internal Review PASS；
- External Review 已按 Project Owner attestation 记录；
- Project Owner 已接受 Handoff。

Current State:

```text
COMPLETED
```


### Stage DS1 — Design Spec Authorized

Entry Condition:

- Project Owner 对唯一 Spec 资产作出明确授权。

Current State:

```text
COMPLETED
```


### Stage DS2 — Baseline Bound

Entry Conditions:

- accepted Handoff SHA 与授权一致；
- 唯一 Spec 资产条件成立；
- downstream prohibitions 保持。

Current State:

```text
COMPLETED
```


### Stage DS3 — Design Spec Materialized

Entry Condition:

- 本文件已在 Design Spec scope 内完成；
- 未创建其他资产。

Current State:

```text
COMPLETED FOR ORIGINAL SHA
```


### Stage DS4 — Design Review Pending

Entry Condition:

- Project Owner 另行授权只读 Design Review。

Possible Transitions:

```text
DESIGN REVIEW PASS
DESIGN REVIEW FAIL — REVISION REQUIRED
DESIGN REVIEW BLOCKED
OWNER HOLD
WITHDRAWN
```


### Stage DS5 — Design Review Passed

Entry Conditions:

- 固定 Spec SHA；
- 获授权 reviewer 完成只读 Review；
- applicable gates PASS；
- blockers 为 0。

Current State:

```text
FUTURE / INACTIVE
```


### Stage DS5F — Design Review Failed / Revision Required

Entry Conditions:

- fixed Spec SHA 已完成只读 Design Review；
- one or more blockers 或 failed gates 存在。

Required Effects:

- Spec Acceptance 保持 `NOT AUTHORIZED`；
- 原 SHA 保留为 reviewed historical candidate；
- 不得自动修改；
- 不得自动创建 RESULT；
- 只有 Project Owner 可以授权受限修订、拒绝、暂停或撤回。

Historical Instance:

```text
ORIGINAL SHA:
948A62F86310F78BB0310365555D4200976E56A01AE09ED3D9EC7EDEAABA65C8

OUTCOME:
FAIL — GRADE C

BLOCKERS:
3
```


### Stage DS5B — Design Review Blocked

Entry Conditions:

- reviewer 无法完成有效 Review；
- identity、scope、integrity 或 authorization 不完整；
- Review response 无法绑定。

Permitted Transitions:

- 缺失条件补齐后，返回 `DS4 — Design Review Pending`；
- Project Owner `HOLD`；
- Project Owner `WITHDRAW`。

Blocked 不得自动映射为 FAIL 或 PASS。


### Stage DS5L — Limited Revision Authorized

Entry Conditions:

- Design Review FAIL 或 blocker 已形成；
- Project Owner 对同一 Spec 文件给出封闭 revision scope；
- 禁止项保持不变。

Required Effects:

- 只允许修改被授权资产；
- 原 SHA 和 Review 结论保留；
- 修订后产生新 SHA；
- 新 SHA 不继承原 PASS 或 FAIL；
- 按授权进入完整 re-review。

Current State:

```text
COMPLETED
```


### Stage DS5M — Revised Candidate Materialized

Entry Conditions:

- 仅在受限 scope 内完成修订；
- 未创建其他资产；
- 新 SHA 已计算；
- 原 SHA 历史保留。

Current State:

```text
CURRENT — RE-REVIEW AUTHORIZED
```


### Stage DS5R — Re-Review Pending

Entry Conditions:

- Project Owner 已授权对修订后新 SHA 执行完整只读 Design Review；
- 新 SHA 在 Review 开始前固定；
- reviewer 只读；
- 禁止 External Invocation、Asset Transfer、RESULT 和 Implementation。

Permitted Transitions:

```text
PASS
→ DS5 — DESIGN REVIEW PASSED

FAIL
→ DS5F — DESIGN REVIEW FAILED / REVISION REQUIRED

BLOCKED
→ DS5B — DESIGN REVIEW BLOCKED

OWNER HOLD
→ DS6H — OWNER HOLD

WITHDRAW
→ DS6W — WITHDRAWN
```


### Stage DS6 — Design Spec Accepted

Entry Conditions:

- Design Review 已完成；
- 必要外部 Review 按适用治理规则完成；
- Project Owner 对固定 Spec SHA 明确接受。

Current State:

```text
FUTURE / INACTIVE
```


### Stage DS6R — Design Spec Rejected

Entry Conditions:

- Project Owner 对 exact Spec SHA 作出 `REJECT` 决定。

Effect:

```text
DESIGN SPEC:
REJECTED & CLOSED FOR THAT SHA

DOWNSTREAM:
NOT AUTHORIZED
```

拒绝不删除历史，也不授权修订。


### Stage DS6H — Owner Hold

Entry Condition:

- Project Owner 对 exact Spec SHA 或当前 Review cycle 作出 `HOLD`。

Effect:

```text
CURRENT ACTION:
PAUSED

AUTOMATIC RESUME:
PROHIBITED
```

解除 Hold 必须依赖新的 Project Owner 决定，并重新核验 SHA、authorization 和 Review freshness。


### Stage DS6W — Withdrawn

Entry Condition:

- Project Owner 撤回 Spec candidate 或当前 Design process。

Effect:

```text
CURRENT CANDIDATE:
WITHDRAWN

AUTOMATIC RESTORATION:
PROHIBITED
```

后续恢复必须形成新的明确授权；历史 Review 保留。


### Stage DS6HR — Owner-Requested Human Review

Entry Condition:

- Project Owner 明确要求 Human Review。

Permitted Resolution:

- 返回 `DS5R — Re-Review Pending`；
- 进入 `DS5L — Limited Revision Authorized`；
- 进入 `DS6R — Design Spec Rejected`；
- 进入 `DS6H — Owner Hold`；
- 进入 `DS6W — Withdrawn`；
- 在所有必要 Review PASS 后返回 Project Owner decision。

Human Review conclusion 本身不接受 Spec。


### Stage DS7 — Awaiting Separate Downstream Decision

Entry Condition:

- Spec Accepted。

Permitted Meaning:

```text
DESIGN LAYER CLOSED
NO DOWNSTREAM AUTHORITY CREATED
```


### Stage DSB — Blocked

触发条件包括：

- Handoff SHA mismatch；
- Spec 超出授权范围；
- 创建未授权资产；
- 进入 External Invocation、Asset Transfer 或 Implementation；
- 数据或身份边界不明；
- 试图自动启动 Design Review。

解除 Blocked 必须根据 blocker 类型返回：

- `DS4 / DS5R` 重新 Review；
- `DS5L` 受限修订；
- `DS6H` Owner Hold；
- `DS6W` Withdrawn。

不得由时间经过或 reviewer PASS 之外的推定自动解除。


### Design Spec Lifecycle Transition Matrix

| Current Stage | Trigger | Next Stage | Governing Effect |
|---|---|---|---|
| DS3 — Materialized | Review separately authorized | DS4 — Review Pending | Read-only Review only |
| DS4 / DS5R — Review Pending | Full PASS | DS5 — Review Passed | Owner decision may be requested |
| DS4 / DS5R — Review Pending | FAIL / blocker | DS5F — Revision Required | Acceptance blocked |
| DS4 / DS5R — Review Pending | Review cannot validly proceed | DS5B — Review Blocked | No PASS / FAIL inference |
| DS5F — Revision Required | Owner authorizes limited revision | DS5L — Limited Revision Authorized | Revision scope only |
| DS5L — Limited Revision Authorized | Revised candidate materialized | DS5M — Revised Candidate | New SHA required |
| DS5M — Revised Candidate | Authorized re-review begins | DS5R — Re-Review Pending | Full Review required |
| DS5 — Review Passed | Owner ACCEPT | DS6 — Accepted | Exact SHA accepted |
| DS5 — Review Passed | Owner REJECT | DS6R — Rejected | Exact SHA closed |
| Any active DS stage | Owner HOLD | DS6H — Owner Hold | Paused; no auto-resume |
| Any active DS stage | Owner REQUEST HUMAN REVIEW | DS6HR — Human Review | No acceptance |
| Any active DS stage | Owner WITHDRAW | DS6W — Withdrawn | No auto-restoration |
| DS6HR — Human Review | Supplemental Review required | DS5R — Re-Review Pending | Review remains required |
| DS6HR — Human Review | Limited revision required and authorized | DS5L — Limited Revision | Revision scope only |
| DS6HR — Human Review | Owner final REJECT / HOLD / WITHDRAW | DS6R / DS6H / DS6W | Corresponding closed or paused state |
| DS6 — Accepted | Separate downstream authorization absent | DS7 — Awaiting Decision | No downstream authority |


## Future Review Orchestration Lifecycle

本节定义未来可能采用的治理状态，不创建运行时、Queue、Ledger、Packet 或 Connector。


### Stage R0 — Review Not Authorized

```text
DISPATCH:
PROHIBITED
```


### Stage R1 — Authorization Evaluation

核验：

- Project Owner authorization identity；
- scope；
- asset class；
- reviewer；
- provider / model；
- transfer mode；
- cost / quota；
- expiry；
- revocation；
- retry boundary。

任一不明：

```text
BLOCKED — AUTHORIZATION
```


### Stage R2 — Asset and Data Eligibility Evaluation

核验：

- asset filename；
- exact SHA；
- project identity；
- data class；
- attachments；
- Real Matter absence；
- credential absence；
- scope fidelity。


### Stage R3 — Review Packet Prepared

仅在未来 Packet materialization 获授权后可进入。

Packet 仍未因“prepared”获得 dispatch authority。


### Stage R4 — Review Packet Sealed

Packet identity、asset SHA、review scope 和 prohibitions 固定。

任何内容变化产生新 packet identity。


### Stage R5 — Internal Review Pending

Architecture Coordinator 独立只读 Review。

Internal FAIL 或 BLOCKER：

```text
REVISION REQUIRED / BLOCKED
```

不得因存在外部 PASS 而覆盖。


### Stage R6 — External Review Eligibility Ready

必须满足：

- applicable external authorization 有效；
- reviewer eligible；
- data eligible；
- packet sealed；
- no blocker；
- quota / cost boundary known。


### Stage R7 — External Review Queued

Queue 仅表示等待执行。

```text
QUEUED
≠
AUTHORIZED
```


### Stage R8 — External Review Dispatched

只有在 dispatch 时再次复核 authorization、expiry、revocation、packet SHA 和 asset SHA 后才能进入。


### Stage R9 — External Response Binding

响应必须绑定：

- packet identity；
- asset SHA；
- reviewer identity；
- provider / model；
- review scope；
- response outcome；
- limitations；
- transfer mode。

Binding disposition 必须唯一导出为：

```text
BOUND — PASS
BOUND — FAIL
BOUND — BLOCKED
BOUND — LIMITED
BOUND — PENDING
REJECTED — UNBOUND RESPONSE
```

`UNBOUND` 是 response integrity disposition，不是 reviewer FAIL。


### Stage R10 — Review Reconciliation

比较 Internal 与 External Review：

- verdict；
- blockers；
- severity；
- scope；
- asset identity；
- authorization interpretation；
- limitations。

Reconciliation 必须处理：

- External PASS：可在 Internal PASS 且无分歧时进入 Owner Decision readiness evaluation；
- External FAIL：进入 Revision Required，若与 Internal PASS 冲突则先进入 Human Review；
- External BLOCKED：进入对应 Blocked，不得推定 FAIL；
- External LIMITED：进入 Scope Completion Required，不得推定完整 PASS；
- External PENDING：保持 External Review Pending；
- External UNBOUND：进入 Integrity Blocked；
- External CANCELLED：终止当前 request，asset 保持未 ready。


### Stage R11 — Human Review Required

任何实质分歧、身份冲突或无法自动归一的 scope 差异进入本状态。

这是保护性路由，不是自动阶段升级。

Human Review resolution 必须唯一映射为：

```text
REVIEWS GOVERNING AND CONSISTENT
→ RETURN TO REVIEW RECONCILIATION

BLOCKER CONFIRMED
→ REVISION REQUIRED

SUPPLEMENTAL INTERNAL OR EXTERNAL REVIEW REQUIRED
→ RETURN TO THE APPLICABLE REVIEW PENDING STATE

SCOPE OR AUTHORITY INVALID
→ BLOCKED — AUTHORIZATION / DATA / INTEGRITY

UNRESOLVED
→ HUMAN REVIEW REQUIRED / OWNER HOLD
```

Human Review 不得直接生成 `ACCEPTED`。


### Stage R12 — Owner Decision Ready

仅当：

- Internal PASS；
- eligible External PASS；
- exact SHA match；
- no unresolved disagreement；
- no active blocker；
- authorization evidence complete。

```text
OWNER DECISION READY
≠
ACCEPTED
```


### Stage R13 — Project Owner Decision

Project Owner 可以：

- ACCEPT；
- REJECT；
- AUTHORIZE LIMITED REVISION；
- REQUEST HUMAN REVIEW；
- WITHDRAW；
- HOLD。

各决定的唯一治理效果：

```text
ACCEPT
→ ACCEPTED & SHA BOUND

REJECT
→ REJECTED & SHA BOUND

AUTHORIZE LIMITED REVISION
→ REVISION AUTHORIZED — SCOPED

REQUEST HUMAN REVIEW
→ HUMAN REVIEW REQUIRED

WITHDRAW
→ WITHDRAWN

HOLD
→ OWNER HOLD
```

`AUTHORIZE LIMITED REVISION` 只授权封闭 revision scope；修订产生新 SHA 后，旧 Review 不迁移。

`HOLD` 不得自动恢复。`REQUEST HUMAN REVIEW` 不得被解释为 ACCEPT 或 REJECT。


### Stage R14 — Closed

可能的终局：

```text
ACCEPTED & SHA BOUND
REJECTED & SHA BOUND
WITHDRAWN
SUPERSEDED
```

终局不自动启动 downstream。

`OWNER HOLD`、`REVISION AUTHORIZED — SCOPED` 与 `HUMAN REVIEW REQUIRED` 是非终局控制状态，不得被记录为 Closed。


### Stage RB — Blocked

Blocked 必须记录 blocker class 和当前资产 SHA。

解除 Blocked 需要满足缺失条件或获得适当的新决定，不能由时间经过自动解除。


### Stage RS — Stale / Superseded

资产、Packet、Authorization 或 Review baseline 发生变化时进入。

Stale response 可以保留为历史，不得进入当前 Decision Gate。


## Governance Transition Rules

### MMCA-T-001 Not Authorized to Authorization Evaluation

Trigger:

- Project Owner 作出封闭授权。

禁止由 Queue、Ledger、reviewer 或系统默认值触发。


### MMCA-T-002 Authorization Evaluation to Eligibility Evaluation

Required:

- authorization valid；
- scope exact；
- reviewer and transfer mode covered；
- authorization not expired, revoked or superseded。


### MMCA-T-003 Eligibility Evaluation to Packet Preparation

Required:

- asset SHA fixed；
- data class known；
- asset class eligible；
- no G4 or G5；
- attachment list closed；
- Packet materialization separately authorized。


### MMCA-T-004 Packet Prepared to Packet Sealed

Required:

- packet scope complete；
- prohibitions explicit；
- identity fixed；
- no hidden or unclassified attachment。

任何内容改变后必须重新 seal。


### MMCA-T-005 Sealed to Internal Review Pending

Required:

- Internal Review authorized；
- reviewer identity known；
- blind review controls preserved。


### MMCA-T-006 Internal Review Pending to Internal PASS

Required:

- response bound to asset SHA；
- required gates addressed；
- blockers zero；
- limitations do not invalidate required scope。


### MMCA-T-007 Internal Review Pending to Revision Required

Trigger:

- FAIL；
- blocker；
- scope breach；
- unbound response；
- integrity mismatch。


### MMCA-T-008 Sealed to External Review Ready

Required:

- External Review authorization valid；
- reviewer eligible；
- Cross-Vendor or authorized human independence established；
- transfer mode authorized；
- data class eligible；
- quota and cost boundary known。


### MMCA-T-009 External Review Ready to Queued

Required:

- no active blocker；
- current packet not cancelled or superseded。

Queue admission不得授予新的权力。


### MMCA-T-010 Queued to Dispatched

Required at dispatch time:

- authorization rechecked；
- packet and asset SHA rechecked；
- reviewer and provider rechecked；
- quota boundary rechecked；
- no revocation；
- no expiry；
- no duplicate active dispatch。


### MMCA-T-011 Dispatched to Response Binding

Trigger:

- 收到 response。

收到 response 不等于 response governing。


### MMCA-T-012 Response Binding to Bound External Outcome

Common Required Conditions:

- identity complete；
- asset SHA exact；
- packet identity exact；
- reviewer eligible；
- transfer mode valid；
- response outcome explicit；
- actual reviewed scope explicit, identifiable and bound to the response；
- limitations explicit。

Deterministic Branches:

```text
OUTCOME PASS
+ sufficient required scope
+ compatible limitations
→ EXTERNAL PASS

OUTCOME FAIL
→ EXTERNAL FAIL
→ REVISION REQUIRED
  unless a contradictory Internal verdict requires Human Review first

OUTCOME BLOCKED
→ BLOCKED — REVIEW COULD NOT VALIDLY PROCEED

OUTCOME LIMITED
+ actual reviewed scope is identifiable and bound
+ actual reviewed scope is narrower than the required full scope
→ LIMITED — SCOPE RESTRICTED
→ SCOPE COMPLETION REQUIRED

OUTCOME PENDING
→ PENDING — GOVERNING OUTCOME NOT YET AVAILABLE
```

`FAIL`、`BLOCKED`、`LIMITED` 和 `PENDING` 均不得自动映射为 External PASS。

`LIMITED` 的必要条件是实际审查范围可以被明确识别并绑定，只是范围不足以满足 required full scope。


### MMCA-T-013 Response Binding to Rejected — Unbound

Trigger:

- identity missing；
- SHA mismatch；
- packet mismatch；
- reviewer identity unresolved；
- actual reviewed scope missing；
- actual reviewed scope ambiguous, internally contradictory or unidentifiable；
- actual reviewed scope cannot be bound to the response；
- integrity unverifiable。

Required Effect:

```text
EXTERNAL RESPONSE:
REJECTED — UNBOUND

CURRENT GOVERNING STATUS:
BLOCKED — INTEGRITY / UNBOUND RESPONSE
```

UNBOUND 不得记为 reviewer FAIL，也不得进入 reconciliation。

Mutual Exclusivity Rule:

```text
IDENTIFIABLE AND BOUND BUT NARROWER ACTUAL SCOPE
→ LIMITED

MISSING / AMBIGUOUS / UNIDENTIFIABLE / UNBINDABLE ACTUAL SCOPE
→ UNBOUND
```

“不足以满足 required full scope”本身不得触发 UNBOUND；只有实际审查范围无法识别或无法绑定时才触发 UNBOUND。


### MMCA-T-014 Review Reconciliation and Human Resolution

Human Review Entry Triggers:

- verdict disagreement；
- blocker severity disagreement；
- scope disagreement；
- asset identity disagreement；
- authorization interpretation disagreement；
- data classification disagreement。

Human Review Resolution Branches:

```text
REVIEWS GOVERNING AND CONSISTENT
→ RETURN TO REVIEW RECONCILIATION

BLOCKER CONFIRMED
→ REVISION REQUIRED

SUPPLEMENTAL REVIEW REQUIRED
→ INTERNAL REVIEW PENDING OR EXTERNAL REVIEW PENDING

SCOPE OR AUTHORITY INVALID
→ BLOCKED — AUTHORIZATION / DATA / INTEGRITY

UNRESOLVED
→ HUMAN REVIEW REQUIRED OR OWNER HOLD
```

任何 Human Review resolution 均不得直接产生 Project Owner acceptance。


### MMCA-T-015 Reviews Complete to Owner Decision Ready

Required:

- Internal PASS；
- External PASS；
- no unresolved disagreement；
- exact SHA match；
- no active blocker；
- current authorization record complete。


### MMCA-T-016 Project Owner Decision Branches

Common Required Conditions:

- Project Owner explicit decision；
- exact asset SHA stated；
- decision scope stated；
- decision identity current；
- no automatic downstream activation。

Deterministic Branches:

```text
ACCEPT
→ ACCEPTED & SHA BOUND

REJECT
→ REJECTED & SHA BOUND

AUTHORIZE LIMITED REVISION
→ REVISION AUTHORIZED — SCOPED
→ NEW SHA AND RE-REVIEW REQUIRED AFTER MODIFICATION

REQUEST HUMAN REVIEW
→ HUMAN REVIEW REQUIRED

WITHDRAW
→ WITHDRAWN

HOLD
→ OWNER HOLD
```

只有 `ACCEPT` 产生 asset acceptance；其余分支不得被归并为 accepted。


### MMCA-T-017 Any Pre-Decision Stage to Cancelled

Trigger:

- Project Owner cancellation of the current Review request；
- authorization revocation；
- packet or request supersession；
- permitted protective cancellation rule。

Cancelled request 不得自动恢复。

Asset withdrawal 由 `MMCA-T-016 WITHDRAW` 分支处理，必须导出 `WITHDRAWN`，不得与 request cancellation 混同。

Required Effect:

```text
REVIEW REQUEST:
CANCELLED

ASSET:
NOT ACCEPTED / NOT REJECTED BY CANCELLATION ALONE
```


### MMCA-T-018 Any Current Review to Stale

Trigger:

- asset SHA changes；
- packet changes；
- required baseline changes；
- reviewer eligibility becomes invalid；
- response scope no longer covers current asset。


### MMCA-T-019 Quota Exhausted to Pending

```text
PENDING — QUOTA EXHAUSTED
```

不得进入 PASS、FAIL 或 Owner Decision Ready。


### MMCA-T-020 External Unavailable to Pending

```text
PENDING — EXTERNAL UNAVAILABLE
```

服务恢复后必须重新检查 authorization、expiry、SHA 和 Queue state，不能自动沿用旧 eligibility。


## Transition Matrix

| Current State | Required Trigger | Required Checks | Next State | Automatic Positive Authority |
|---|---|---|---|---|
| NOT AUTHORIZED | Project Owner scoped authorization | Scope and identity | AUTHORIZATION EVALUATION | No |
| AUTHORIZATION EVALUATION | Valid authorization | Expiry, revocation, scope | ELIGIBILITY EVALUATION | No |
| ELIGIBILITY EVALUATION | Eligible asset and data | SHA, G-class, attachments | PACKET PREPARATION | No |
| PACKET PREPARATION | Complete closed packet | Identity and prohibitions | PACKET SEALED | No |
| PACKET SEALED | Internal Review authorization | Reviewer and blind controls | INTERNAL REVIEW PENDING | No |
| INTERNAL REVIEW PENDING | Bound PASS | Gates and blockers | INTERNAL PASS | No |
| INTERNAL REVIEW PENDING | FAIL / blocker | Response binding | REVISION REQUIRED | No |
| PACKET SEALED | External eligibility complete | Authorization, provider, data | EXTERNAL REVIEW READY | No |
| EXTERNAL REVIEW READY | Queue admission | Current scope | QUEUED | No |
| QUEUED | Authorized dispatch | Recheck all hard gates | DISPATCHED | No |
| DISPATCHED | Response received | Identity and scope | RESPONSE BINDING | No |
| RESPONSE BINDING | Bound PASS with sufficient scope | SHA, packet, reviewer, limitations | EXTERNAL PASS | No |
| RESPONSE BINDING | Bound FAIL | SHA, packet, reviewer | EXTERNAL FAIL / REVISION REQUIRED | No |
| RESPONSE BINDING | Bound BLOCKED | SHA, packet, reviewer, blocking cause | BLOCKED — EXTERNAL REVIEW | No |
| RESPONSE BINDING | Bound LIMITED | SHA, packet, reviewer, actual scope | LIMITED — SCOPE COMPLETION REQUIRED | No |
| RESPONSE BINDING | Bound PENDING | SHA, packet, reviewer, wait condition | EXTERNAL REVIEW PENDING | No |
| RESPONSE BINDING | Binding failure | Missing or mismatched identity | REJECTED — UNBOUND | No |
| EXTERNAL PASS + INTERNAL FAIL | Verdict conflict | Comparison complete | HUMAN REVIEW REQUIRED | No |
| EXTERNAL FAIL + INTERNAL PASS | Verdict conflict | Comparison complete | HUMAN REVIEW REQUIRED | No |
| INTERNAL FAIL + EXTERNAL FAIL | Consistent blocking verdict | Bound responses | REVISION REQUIRED | No |
| REVIEWS COMPLETE | Other substantive disagreement | Comparison complete | HUMAN REVIEW REQUIRED | No |
| HUMAN REVIEW REQUIRED | Reviews governing and consistent | Resolution bound to current SHA | REVIEW RECONCILIATION | No |
| HUMAN REVIEW REQUIRED | Blocker confirmed | Resolution bound to current SHA | REVISION REQUIRED | No |
| HUMAN REVIEW REQUIRED | Supplemental review required | Scope and reviewer identified | APPLICABLE REVIEW PENDING | No |
| HUMAN REVIEW REQUIRED | Scope or authority invalid | Resolution and cause | BLOCKED — AUTHORIZATION / DATA / INTEGRITY | No |
| HUMAN REVIEW REQUIRED | Unresolved | Current SHA | HUMAN REVIEW REQUIRED / OWNER HOLD | No |
| REVIEWS COMPLETE | Both PASS and no disagreement | SHA and authority | OWNER DECISION READY | No |
| OWNER DECISION READY | Owner ACCEPT | Exact SHA and scope | ACCEPTED & CLOSED | Project Owner only |
| OWNER DECISION READY | Owner REJECT | Exact SHA and scope | REJECTED & CLOSED | Project Owner only |
| OWNER DECISION READY / REVISION REQUIRED | Owner AUTHORIZES LIMITED REVISION | Exact SHA and closed revision scope | REVISION AUTHORIZED — SCOPED | Project Owner only |
| ANY ACTIVE REVIEW STATE | Owner REQUESTS HUMAN REVIEW | Exact SHA and review scope | HUMAN REVIEW REQUIRED | Project Owner only |
| ANY ACTIVE REVIEW STATE | Owner HOLD | Exact SHA or current review cycle | OWNER HOLD | Project Owner only |
| ANY ACTIVE REVIEW STATE | Owner WITHDRAW | Exact asset identity and SHA | WITHDRAWN | Project Owner only |
| ANY PRE-DECISION | Authorization revocation / request cancellation / packet supersession | Current request identity | CANCELLED / BLOCKED | No |
| ANY CURRENT REVIEW | SHA / baseline change | Mismatch detected | STALE / SUPERSEDED | No |
| EXTERNAL READY / QUEUED | Quota exhausted | Cost boundary | PENDING — QUOTA | No |
| EXTERNAL READY / QUEUED | Service unavailable | Availability evidence | PENDING — UNAVAILABLE | No |
| CANCELLED | Time passes / service recovers | No new Owner decision | CANCELLED | No |
| OWNER HOLD | Time passes / service recovers | No new Owner decision | OWNER HOLD | No |


## Review Packet Abstract Governance Contract

### Contract Nature

Review Packet 是未来一次 Review 的不可变治理封装。

本节只定义必须表达的治理信息类别，不定义：

- field names；
- types；
- required-property syntax；
- JSON；
- YAML；
- API payload；
- database row；
- message envelope；
- executable configuration。


### Identity Declaration

未来 Packet 必须能够声明：

- packet identity；
- project identity；
- asset filename；
- exact asset SHA-256；
- review scope；
- packet supersession status。


### Authorization Declaration

未来 Packet 必须能够声明：

- applicable authorization identity；
- authorization scope；
- authorization snapshot；
- transfer mode；
- reviewer eligibility basis；
- expiry / revocation state。

Packet 不得自己创造 authorization。


### Review Instruction Declaration

未来 Packet 必须能够声明：

- review type；
- reviewer classification；
- review questions；
- acceptance gates；
- expected response semantics；
- explicit prohibitions；
- required limitations disclosure。


### Data Boundary Declaration

未来 Packet 必须能够声明：

- governing G-class；
- allowed content；
- allowed attachments；
- prohibited attachments；
- Real Matter absence；
- credential absence；
- minimal disclosure rationale。


### Baseline Declaration

未来 Packet 必须能够声明：

- upstream asset identities；
- upstream SHA values；
- whether upstream content is attached or identity-only；
- baseline acceptance status；
- baseline supersession status。


### Scope Fidelity

如果 reviewer 只收到摘要、节选或部分附件，其 verdict 只能绑定实际审查范围。

```text
PARTIAL INPUT REVIEW
≠
FULL ASSET EXTERNAL PASS
```

除非适用 gate 只要求该封闭部分，否则 partial review 不得满足完整 External PASS 条件。


### Packet Immutability

Packet sealed 后，任何内容变化必须：

- 产生新 packet identity；
- 重新执行 data classification；
- 重新执行 authorization eligibility；
- 使旧 packet response 对新 packet 失效。


### Attachment Isolation

上游资产默认只以 identity 和 SHA 引用。

实际附带内容必须逐项获得授权，且不得因主资产获准外发而自动获得附件外发权限。


### Packet Expiry and Supersession

Packet 必须可被标记为：

```text
CURRENT
EXPIRED
CANCELLED
SUPERSEDED
STALE
```

非 CURRENT packet 不得 dispatch 或进入当前 Decision Gate。


## Internal Review Design

### Purpose

Internal Review 用于快速发现：

- 授权漂移；
- 架构遗漏；
- blocker；
- 反例；
- SHA 或引用错误；
- 状态语义冲突；
- 未授权资产污染。


### Blind Review Input

初始 Internal Review 原则上仅接收：

- fixed asset；
- exact SHA；
- accepted baselines；
- authorization snapshot；
- Review Questions；
- Acceptance Gates；
- explicit prohibitions。


### Internal Review Output

应至少表达：

- reviewer identity and classification；
- reviewed asset and SHA；
- outcome；
- gate-by-gate result；
- blockers；
- non-blockers；
- limitations；
- whether edits occurred；
- whether external tools or transfer occurred。

本列表不定义输出 Schema。


### Internal Review Limitation

Internal PASS 不能证明：

- Cross-Vendor independence；
- external certification；
- legal correctness；
- absence of all systemic error；
- Project Owner acceptance。


## External Review Design

### Purpose

External Review 用于降低内部同模型家族或同执行环境造成的相关错误风险。


### Required Eligibility

External Review 前必须满足：

- reviewer eligibility established；
- applicable authorization valid；
- asset and packet SHA fixed；
- data class eligible；
- minimal disclosure；
- transfer mode authorized；
- quota and cost boundary known；
- no G4 / G5；
- response binding requirement defined。


### External Review Outcome Semantics

```text
PASS:
No blocking issue found within declared scope

FAIL:
One or more blocking defects identified

BLOCKED:
Review could not validly proceed

LIMITED:
Review completed only for a restricted scope

PENDING:
No governing review outcome yet
```

`LIMITED` 不得自动映射为完整 PASS。

Response binding dispositions 和 request lifecycle states 与 reviewer outcomes 分离：

```text
UNBOUND:
Response cannot be admitted as a governing reviewer outcome

CANCELLED:
Current review request has been terminated

SUPERSEDED / STALE:
Response or request no longer governs the current asset SHA
```

确定映射：

| External State | Unique Governing Effect | Owner Decision Ready |
|---|---|---|
| PASS | External requirement satisfied for declared sufficient scope | Possible, if all other gates pass |
| FAIL | Revision Required, or Human Review when verdicts conflict | No |
| BLOCKED | External Review Blocked | No |
| LIMITED | Scope Completion Required | No |
| PENDING | External Review Pending | No |
| UNBOUND | Integrity Blocked / Response Rejected | No |
| CANCELLED | Current Review Request Cancelled | No |

`UNBOUND` 不得伪装为 FAIL；`CANCELLED` 不得伪装为 asset rejection。


### Manual Transfer

Manual transfer 只有在 per-asset authorization 或适用 Standing Authorization 明确允许时，才可形成 governing external review。

必须保真记录：

- `MANUAL`；
- Project Owner attestation or authorized operator；
- asset SHA；
- reviewer identity；
- outcome；
- scope；
- limitations。


### Future Connector Transfer

Connector transfer 当前未授权。

即使未来获授权，也不得：

- 产生 Project Owner decision；
- 绕过 data classification；
- 静默改变 provider；
- 无限重试；
- 隐藏 model identity；
- 将 connector success 当作 reviewer PASS。


## Standing External Review Authorization Design

### Current State

```text
STANDING EXTERNAL REVIEW AUTHORIZATION:
NOT GRANTED
```


### Nature

Standing Authorization 是 Project Owner 对重复、低变异、明确范围的外部 Review dispatch 作出的可撤回委托。

它只减少重复机械授权，不减少必要治理条件。


### Mandatory Decision Questions

任何未来 Standing Authorization 必须封闭回答全部 25 项：

1. 适用项目；
2. 适用 Phase、Track 或资产类别；
3. 允许文件名模式；
4. 允许传输的内容类型；
5. 禁止传输的内容类型；
6. Schema 是否允许；
7. source code 是否允许；
8. Real Matter 是否允许；
9. PII、Evidence 或当事人信息是否允许；
10. external reviewer identity；
11. provider、model 或 service；
12. Review Packet 必要内容；
13. upstream assets 是否可附带；
14. 最大单次资产大小；
15. 最大频率、额度和成本；
16. quota exhausted 处置；
17. external unavailable 处置；
18. automatic retry 是否允许；
19. retry count 和 stop condition；
20. response 如何绑定 packet 和 SHA；
21. data retention 和 logging boundary；
22. external FAIL 或 disagreement 如何升级；
23. revocation authority；
24. Project Owner 独占状态；
25. expiry 和 invalidation conditions。


### Completeness Rule

任一答案：

- 缺失；
- 模糊；
- 相互冲突；
- 使用开放式“所有未来资产”；
- 未给出上限；
- 未给出失效条件；

则：

```text
STANDING AUTHORIZATION:
INCOMPLETE

EXTERNAL DISPATCH:
BLOCKED
```


### Scope Rule

Standing Authorization 必须同时受以下维度约束：

- project；
- asset class；
- filename pattern；
- G-class；
- provider / reviewer；
- model or service；
- transfer mode；
- packet scope；
- cost / quota；
- time；
- retry；
- retention；
- revocation。


### Non-Delegable Decisions

Standing Authorization 不得委托：

- asset acceptance；
- stage authorization；
- G4 transfer；
- G5 handling；
- provider expansion；
- unlimited cost；
- unlimited retry；
- automatic downstream activation；
- Project Owner final decision。


### Revocation

Project Owner 可随时撤回。

撤回后：

- not-yet-dispatched requests 必须取消；
- queued requests 必须转为 CANCELLED 或 BLOCKED；
- dispatched requests 的后续 response 只能作为历史；
- response 不得进入当前 Decision Gate；
- 不得在额度恢复或服务恢复后自动重启；
- 恢复必须依赖新的有效授权。


### Expiry

Standing Authorization 到期后：

```text
NEW DISPATCH:
BLOCKED
```

既有历史记录保留，但不得生成新的 governing review。


## G0–G5 Data Classification

### Classification Rule

复合资产按其中最高敏感等级治理。

无法确定分类时：

```text
CLASSIFICATION:
UNKNOWN

EXTERNAL TRANSFER:
BLOCKED
```


### G0 — Public or Non-Sensitive Governance Material

可能在明确 Standing Authorization 覆盖后 eligible。

公开性必须基于实际内容，不得仅凭文件名推定。


### G1 — Internal Governance Assets Without Real Matter

包括 no-matter Handoff、Spec、Result 和 governance decision。

只有在项目、资产类别和 transfer mode 明确授权后才 eligible。


### G2 — Schema Assets Without Instances

仅当确认：

- 无真实记录；
- 无示例中的真实或可识别数据；
- 无 credential；
- 无隐藏业务秘密；
- SHA fixed；
- Schema transfer separately covered；

才可能 eligible。


### G3 — Source Code or Operational Configuration

Default:

```text
EXTERNAL TRANSFER:
DENIED
```

需要独立授权。

本 Design Spec 不授予该授权。


### G4 — Real Matter, Evidence, PII or Privileged Material

包括：

- 真实案件材料；
- Evidence Registry 内容；
- 当事人、证人或代理人信息；
- 身份信息；
- 通信记录；
- 律师工作成果；
- 保密或 privileged material；
- 可识别事实记录。

Rule:

```text
GENERAL STANDING AUTHORIZATION:
INELIGIBLE

CURRENT EXTERNAL TRANSFER:
PROHIBITED
```

本 Spec 不定义 G4 例外流程。


### G5 — Credentials and Secrets

包括：

- API key；
- token；
- password；
- private key；
- session credential；
- encrypted credential material；
- internal secret。

Rule:

```text
REVIEW PACKET / PROMPT / ATTACHMENT / LOG:
ABSOLUTELY PROHIBITED
```


### Redaction and Reclassification

脱敏或删除部分内容不自动降低 G-class。

重新分类必须：

- 基于实际输出内容；
- 检查残留可识别性；
- 检查 metadata；
- 检查附件；
- 由获授权的治理主体确认。

本 Spec 不创建 redaction tool。


## Review Queue Governance

### Purpose

Queue 仅管理已经具有相应 eligibility 的 Review 请求等待状态。

它不是授权源、接受源或 reviewer。


### Conceptual Queue States

```text
NOT AUTHORIZED
ELIGIBILITY PENDING
READY
QUEUED
DISPATCHED
RESPONSE PENDING
BLOCKED — AUTHORIZATION
BLOCKED — DATA
BLOCKED — INTEGRITY
PENDING — QUOTA
PENDING — UNAVAILABLE
CANCELLED
SUPERSEDED
STALE
COMPLETED — RESPONSE BOUND
```


### Queue Admission

进入 `READY` 或 `QUEUED` 前必须具备：

- valid authorization；
- fixed packet；
- fixed asset SHA；
- eligible data class；
- eligible reviewer；
- known cost boundary。


### Queue Priority

Priority 不得覆盖：

- authorization；
- data prohibition；
- quota ceiling；
- revocation；
- SHA mismatch；
- Project Owner gate。

高优先级只影响已合法请求的处理顺序。


### Deduplication Equivalence

未来去重判断必须至少比较：

- project identity；
- asset SHA；
- packet identity；
- review type；
- reviewer target；
- authorization identity。

任一不同，不得静默视为同一 governing request。


### Retry

Retry 只有在授权明确允许且以下条件仍成立时才可发生：

- authorization current；
- packet current；
- asset SHA current；
- reviewer target unchanged；
- retry ceiling not exceeded；
- request not cancelled；
- no governing response already accepted into reconciliation。


### Conflicting Duplicate Responses

同一请求产生不同 verdict 时：

```text
DISAGREEMENT:
HUMAN REVIEW REQUIRED
```

不得选择最快、最便宜或最有利的 response。


## Review Ledger Governance

### Purpose

Ledger 用于保留 Review、状态和决策链的审计事实。

Ledger 不拥有治理权。


### Conceptual Record Categories

未来 Ledger 至少应能够保留：

- asset identity and SHA；
- packet identity；
- authorization identity and status；
- reviewer identity and classification；
- provider / model / reasoning configuration；
- transfer mode；
- Internal Review status；
- External Review status；
- response identity；
- verdict；
- blockers and limitations；
- disagreement state；
- cancellation / revocation / supersession；
- Project Owner decision；
- current / historical classification。

本列表不定义 Ledger Schema、database 或 file format。


### Append-Only History Principle

历史事实不得静默改写。

错误记录应通过：

- correction event；
- superseding record；
- withdrawal；
- explicit invalidation；

进行保真修正。


### Manual / Connector Provenance

Ledger 必须区分：

```text
MANUAL — PROJECT OWNER ATTESTED
```

与：

```text
CONNECTOR — SYSTEM OBSERVED
```


### Current Status Derivation

Ledger 可以为当前状态提供证据，但：

```text
LEDGER ENTRY
≠
CURRENT GOVERNING DECISION
```

当前状态必须依据有效、未撤回、未 supersede 且 SHA 匹配的记录导出。


### Prohibited Ledger Content

Ledger 不得因审计目的保存：

- G5 credential；
- 未授权 G4 内容；
- 完整 prompt 中的受限数据；
- 未授权附件副本。

可以保存必要的 identity、classification 和 prohibition result，但不得保存被禁止的内容本身。


## Decision Gate Governance

### Purpose

Decision Gate 将：

- deterministic integrity；
- Internal Review；
- External Review；
- disagreement；
- Project Owner decision；

保持分离并执行硬门禁。


### Hard Gate Formula

```text
AUTHORIZATION VALID
AND
ASSET SHA MATCH
AND
DATA ELIGIBLE
AND
INTERNAL PASS
AND
EXTERNAL PASS
AND
NO UNRESOLVED DISAGREEMENT
AND
PROJECT OWNER ACCEPTED
=
CURRENT ASSET MAY PROCEED WITHIN THE SEPARATELY AUTHORIZED NEXT ACTION
```


### Pre-Owner Decision Matrix

本 Matrix 按以下优先顺序解释：

```text
INTEGRITY MISMATCH
→ BLOCKED — INTEGRITY

REVIEW BLOCKED
→ BLOCKED

PASS / FAIL VERDICT CONFLICT
→ HUMAN REVIEW REQUIRED

CONSISTENT FAIL
→ REVISION REQUIRED

INCOMPLETE EXTERNAL OUTCOME
→ EXTERNAL REVIEW NOT COMPLETE

BOTH PASS
→ OWNER DECISION READY
```

| Internal | External | Integrity | Disagreement | Gate State |
|---|---|---|---|---|
| Any | Any | MISMATCH | Any | BLOCKED — INTEGRITY |
| BLOCKED | Any | Any | Any | BLOCKED |
| Any | BLOCKED | Any | Any | BLOCKED |
| PASS | FAIL | MATCH | DETECTED | HUMAN REVIEW REQUIRED |
| FAIL | PASS | MATCH | DETECTED | HUMAN REVIEW REQUIRED |
| FAIL | FAIL | MATCH | NONE | REVISION REQUIRED |
| FAIL | PENDING / MISSING / LIMITED | MATCH | NONE | REVISION REQUIRED — INTERNAL BLOCKER |
| PENDING / MISSING | FAIL | MATCH | NONE | REVISION REQUIRED — EXTERNAL BLOCKER |
| PENDING / MISSING | PASS | MATCH | NONE | INTERNAL REVIEW PENDING |
| PASS | LIMITED | MATCH | NONE | EXTERNAL REVIEW LIMITED — SCOPE COMPLETION REQUIRED |
| PASS | UNBOUND | Any | Any | BLOCKED — INTEGRITY / UNBOUND RESPONSE |
| PASS | CANCELLED | MATCH | NONE | EXTERNAL REVIEW CANCELLED / NOT READY |
| PASS | PENDING | MATCH | NONE | PENDING EXTERNAL REVIEW |
| PASS | UNAVAILABLE | MATCH | NONE | PENDING EXTERNAL REVIEW |
| PASS | QUOTA EXHAUSTED | MATCH | NONE | PENDING EXTERNAL REVIEW |
| PASS | PASS | MATCH | DETECTED | HUMAN REVIEW REQUIRED |
| PASS | PASS | MATCH | NONE | OWNER DECISION READY |
| Missing | Missing | Any | Any | NOT READY |


### Post-Review Owner Matrix

| Reviews and Integrity | Project Owner Decision | Governing State |
|---|---|---|
| Ready | ACCEPTED — exact SHA | ACCEPTED & CLOSED |
| Ready | REJECTED — exact SHA | REJECTED & CLOSED |
| Any current decision state | HOLD | OWNER HOLD |
| Any active review state | REQUEST HUMAN REVIEW | HUMAN REVIEW REQUIRED |
| Revision Required / Owner Decision Ready | AUTHORIZE LIMITED REVISION — exact SHA and scope | REVISION AUTHORIZED — SCOPED |
| Any active asset state | WITHDRAW — exact asset SHA | WITHDRAWN |
| Not ready | ACCEPTED text without exact SHA | REJECTED AS UNBOUND DECISION |
| Stale | Prior ACCEPTED | STALE — RE-REVIEW REQUIRED |

Review request cancellation 不属于本 Owner asset-decision Matrix；它必须依据 `MMCA-T-017` 导出 `CANCELLED`，不得导出 `WITHDRAWN`。


### No Automatic Acceptance

Decision Gate 可以产生：

```text
OWNER DECISION READY
```

不得产生：

```text
PROJECT OWNER ACCEPTED
```


### No Automatic Downstream

即使当前资产已 `ACCEPTED & CLOSED`：

```text
NEXT STAGE:
NOT AUTHORIZED
```

除非 Project Owner 对下一动作另行授权。


## SHA Binding, Invalidation and Re-Review

### Binding Unit

Review 的最小绑定单位是：

```text
PROJECT
+
ASSET FILENAME
+
EXACT SHA-256
+
REVIEW SCOPE
```


### Change Rule

任何字节变化，包括：

- 内容修订；
- metadata 变化；
- encoding 变化；
- line ending 变化；
- whitespace 变化；

只要改变 SHA，即形成新候选身份。


### Invalidation Effect

新 SHA 出现后：

- old Internal PASS → HISTORICAL / STALE FOR NEW SHA；
- old External PASS → HISTORICAL / STALE FOR NEW SHA；
- old Owner Acceptance → APPLIES TO OLD SHA ONLY；
- old Packet → SUPERSEDED；
- current Decision Gate → NOT READY；
- re-review → REQUIRED according to applicable profile。


### Review Reuse Prohibition

不得因：

- 文件名相同；
- 修改“很小”；
- reviewer 相同；
- diff 看似无关；
- 旧版本 Grade A；

将旧 PASS 自动迁移到新 SHA。


### Limited Revision

Project Owner 可以授权只修改特定资产并关闭特定 blocker。

修订后仍必须：

- 计算新 SHA；
- 重新核验 scope；
- 重新执行获授权的 Review；
- 保留旧 SHA 和旧 Review 历史。


### Withdrawal

Project Owner 可以撤回：

- asset；
- Review request；
- Standing Authorization；
- prior delegation。

撤回后不得自动恢复。


## Quota, Availability and Retry Governance

### Quota Exhausted

State:

```text
EXTERNAL REVIEW:
PENDING — QUOTA EXHAUSTED
```

Allowed Protective Actions:

- queue；
- report；
- wait；
- authorized limited retry；
- request Project Owner select an authorized human or another provider。

Prohibited:

- internal substitution；
- unlimited cost；
- scope downgrade；
- silent provider switch；
- automatic PASS；
- automatic stage progression。


### External Service Unavailable

State:

```text
EXTERNAL REVIEW:
PENDING — EXTERNAL UNAVAILABLE
```

不可用不等于 asset FAIL，也不等于 External PASS。


### Timeout

Timeout 表示在适用窗口内没有收到可绑定 response。

除非未来授权明确规定，否则不得自动推定：

- PASS；
- FAIL；
- cancellation；
- provider switch。


### Retry Ceiling

未来 retry 必须具有：

- maximum attempts；
- time window；
- cost ceiling；
- stop condition；
- cancellation rule；
- duplicate response rule。

本 Spec 不设具体数值，也不创建 retry configuration。


### Availability Recovery

服务或额度恢复后：

- 不得自动恢复 cancelled request；
- 不得使用 expired authorization；
- 必须重新检查 SHA；
- 必须重新检查 packet current status；
- 必须重新检查 provider eligibility；
- 必须重新检查 cost boundary。


## Disagreement and Human Review Governance

### Disagreement Types

- verdict disagreement；
- blocker existence disagreement；
- severity disagreement；
- scope disagreement；
- SHA or identity disagreement；
- authorization interpretation disagreement；
- reviewer classification disagreement；
- data classification disagreement；
- limitation disagreement。


### Required State

```text
SUBSTANTIVE DISAGREEMENT:
HUMAN REVIEW REQUIRED
```


### Human Review Function

Human Review 可以：

- 核验双方实际审查范围；
- 确认 asset 和 SHA；
- 确认 blocker 是否成立；
- 请求补充 Review；
- 请求受限修订；
- 建议 Project Owner decision。


### Human Review Resolution Semantics

Human Review 必须对当前 asset SHA 形成且只能形成以下一种 resolution：

```text
REVIEWS GOVERNING AND CONSISTENT
```

含义：

- identity、scope 和 reviewer eligibility 均有效；
- 若 Internal 与 External 均为 PASS，可返回 Review Reconciliation 并评估 Owner Decision Ready；
- 不直接接受资产。

```text
BLOCKER CONFIRMED
```

含义：

- 当前候选进入 Revision Required；
- 只有 Project Owner 可以授权受限修订。

```text
SUPPLEMENTAL REVIEW REQUIRED
```

含义：

- 返回适用的 Internal 或 External Review Pending；
- 原不完整或受限结论不得补写为 PASS。

```text
SCOPE OR AUTHORITY INVALID
```

含义：

- 进入 Authorization、Data 或 Integrity Blocked；
- 需要适当的新决定或边界修复。

```text
UNRESOLVED
```

含义：

- 保持 Human Review Required，或由 Project Owner 置为 HOLD；
- 不得通过自动 tie-breaker 结束。

Human Review resolution 必须与当前 SHA 绑定；SHA 改变后 resolution 对新候选失效。


### Human Review Is Not Automatic Acceptance

若 Human Reviewer 不是 Project Owner：

```text
HUMAN REVIEW RESOLUTION
≠
PROJECT OWNER ACCEPTANCE
```

若 Project Owner 亲自执行 Human Review，仍必须分别记录：

- disagreement resolution；
- final asset decision；
- exact SHA。


### Prohibited Automated Tie-Breakers

不得依据：

- majority；
- number of agents；
- confidence score；
- token count；
- response speed；
- cost；
- model popularity；
- same-family third opinion；
- favorable outcome；

自动解决分歧。


## Fail-Closed Conditions

以下任一情形必须阻断 External Dispatch 或 Decision Gate：

1. 当前动作未授权；
2. authorization scope 不完整；
3. 既不存在适用且有效的 per-asset authorization，也不存在适用且有效的 Standing Authorization；
4. 当前所依赖的 per-asset authorization 或 Standing Authorization 已 expired、revoked、suspended 或 superseded；
5. asset filename 不在 scope；
6. asset SHA missing 或 mismatch；
7. packet identity missing；
8. packet stale、cancelled 或 superseded；
9. data class unknown；
10. asset 或附件包含 G4；
11. packet、prompt、附件或日志包含 G5；
12. reviewer identity unknown；
13. provider identity unknown；
14. model identity unknown；
15. same-family reviewer 被标记为 external；
16. transfer mode 未授权；
17. quota / cost boundary unknown；
18. retry ceiling unknown；
19. response 无法绑定 packet；
20. response 无法绑定 asset SHA；
21. response 无法绑定 reviewer；
22. response actual scope missing、ambiguous 或 unbindable，或者 actual scope 可绑定但不足以满足 required full scope；前者必须分类为 UNBOUND，后者必须分类为 LIMITED，二者均阻断 Owner Decision Ready；
23. Internal Review FAIL 或 BLOCKED；
24. External Review FAIL 或 BLOCKED；
25. Internal / External disagreement unresolved；
26. Project Owner decision missing；
27. Project Owner decision 未绑定 exact SHA；
28. asset changed after Review；
29. 试图自动接受；
30. 试图自动启动 downstream；
31. 发生未授权 provider switch；
32. 发生未授权 asset transfer；
33. 发生未授权 API、Connector、MCP、Code 或 Credential；
34. 发生未授权 Real Matter 或 Implementation。


## Protective Actions

在未来获得相应执行授权后，系统可以设计为自动：

- set BLOCKED；
- set PENDING；
- cancel un-dispatched request；
- mark stale；
- mark superseded；
- prevent duplicate dispatch；
- prevent old response reuse；
- route to Human Review；
- notify Project Owner；
- preserve history；
- retry within an explicit boundary；
- refuse prohibited data；
- refuse unbound response。

系统不得自动：

- ACCEPT；
- AUTHORIZE；
- PUBLISH；
- expand scope；
- change provider；
- increase budget；
- waive external review；
- waive SHA binding；
- waive G4 / G5 prohibition；
- start downstream。


## Governance Invariants

1. Project Owner 始终持有唯一 Positive Authority；
2. reviewer PASS 始终只是 advisory；
3. same-family review 始终不是 Cross-Vendor Review；
4. SHA mismatch 始终阻断 current governing use；
5. asset filename 始终不能替代 SHA；
6. Queue 始终不是 authorization；
7. Ledger 始终不是 acceptance；
8. Decision Gate 始终不能接受资产；
9. G4 始终不进入一般 Standing Authorization；
10. G5 始终绝对禁止外发；
11. external unavailable 始终不等于 FAIL 或 PASS；
12. quota exhausted 始终不产生 bypass；
13. disagreement 始终进入 Human Review；
14. manual attestation 始终不伪装为 connector evidence；
15. connector evidence 始终不伪装为 Project Owner decision；
16. old review 始终不迁移到 new SHA；
17. revoked authorization 始终阻断新 dispatch；
18. cancelled request 始终不自动恢复；
19. accepted asset 始终不自动授权 downstream；
20. 本 Spec 始终不构成 Implementation authority。


## Interface Boundaries

### Project Asset Boundary

未来 orchestration 只能处理已明确进入 scope 的资产。

Repository 中其他文件不因同属项目而自动进入 Review Packet。


### Internal Architecture Review Boundary

Architecture Coordinator 只提供内部独立只读 Review。

其结论不得被重标为 External Third-Party Review。


### External Consultant Boundary

外部 reviewer 只接收获授权 packet，并返回 advisory response。

不得写入项目资产或触发 Project Owner decision。


### Project Owner Boundary

Decision Gate 只可向 Project Owner 报告 readiness、blockers 和 evidence。

Project Owner decision 必须独立、明确且绑定 SHA。


### Track D Boundary

Phase 3 Track D Result 仍为 accepted：

```text
EC0DFD7D54573E4E50696EEABCD620F83ACC3F58E7C14BB3454766DB1A56F217
```

本 Spec 不启动 Schema Validation Execution。


### Fact Schema Boundary

Accepted `fact.yaml`：

```text
50E3C2B53BBE485B503852E2E663CCE874B9284C7FA4AE76D42E453E1C0A5A6F
```

本 Spec 不修改、验证或实现该 Schema。


### Real Matter Boundary

本 Spec 不导入、处理、分析或外发任何真实案件材料。


### Legal Reasoning Boundary

本 Spec 不执行：

- legal fact generation；
- request right inference；
- legal reasoning；
- litigation strategy；
- success prediction。


### Implementation Boundary

本 Spec 不创建：

- Review Packet instance；
- Queue；
- Ledger；
- Decision Gate；
- API；
- Connector；
- MCP；
- webhook；
- Agent；
- Skill；
- script；
- source code；
- executable configuration；
- credential；
- test data。


## Design Review Questions

Design Review 获得单独授权后，至少必须评估：

1. Spec 是否绑定 accepted Handoff 的 exact SHA；
2. Handoff internal、external 和 Project Owner acceptance snapshot 是否保真；
3. Manual attestation 是否与 connector evidence 分离；
4. 本资产是否仅为 Design Spec；
5. 四方角色是否完整且不混同；
6. Project Owner 是否独占 Positive Authority；
7. reviewer PASS 是否保持 advisory；
8. same-family review 是否明确不能替代 Cross-Vendor；
9. Cross-Vendor eligibility 是否要求底层 provider identity；
10. human external reviewer 条件是否封闭；
11. 多轴状态是否保留授权、完整性、数据、Review、分歧和 Owner decision；
12. 是否定义唯一 current governing status；
13. current 与 historical 是否分离；
14. Design Spec lifecycle 是否完整；
15. future Review lifecycle 是否不构成 implementation；
16. Transition Rules 和 Matrix 是否禁止自动正向动作；
17. Review Packet 是否仅为 abstract governance contract；
18. partial input review 是否不能冒充 full asset PASS；
19. upstream attachments 是否逐项授权；
20. Standing Authorization 25 项问题是否完整；
21. Standing Authorization 是否可撤回、可过期、不可 blanket；
22. G0–G5 是否完整；
23. G4 是否禁止进入一般 Standing Authorization；
24. G5 是否绝对禁止；
25. Queue 是否不产生 authority；
26. deduplication 和 retry 是否不扩大权限；
27. Ledger 是否区分 manual 与 connector provenance；
28. Ledger 是否不产生 acceptance；
29. Decision Gate 是否实现硬门禁公式；
30. owner decision ready 是否不等于 accepted；
31. SHA 改变是否使旧 Review 对新候选失效；
32. quota exhausted 是否保持 pending；
33. external unavailable 是否保持 pending；
34. retry 是否要求重新核验 authorization 和 SHA；
35. disagreement 是否强制 Human Review；
36. Human Review 是否不自动接受；
37. Fail-Closed 条件是否覆盖 identity、data、authority 和 response；
38. 是否禁止自动 provider switch、预算扩大和 scope downgrade；
39. 是否未调用 External Model 或传输资产；
40. 是否未创建 API、Connector、MCP、Code、Credential；
41. 是否未创建 Packet、Queue、Ledger 或 Decision Gate 实例；
42. 是否未创建 executable configuration 或 concrete field schema；
43. 是否未导入 Real Matter；
44. 是否未启动 Implementation；
45. 是否未创建 RESULT 或自动启动 Design Review。


## Design Spec Acceptance Gates

### MMCA-DS-001 Authorization Fidelity

本 Spec 严格保持 `DESIGN SPEC ONLY`。


### MMCA-DS-002 Sole Artifact

唯一新资产为 `TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_SPEC.md`。


### MMCA-DS-003 Accepted Handoff Integrity

Handoff SHA 必须匹配：

```text
3B615C826EA1D54C9BCAB8A530BECCE4F935197BAE3174AD57D1958296692919
```


### MMCA-DS-004 Acceptance Snapshot Fidelity

Internal Review、External Review 和 Project Owner acceptance 必须保真记录。


### MMCA-DS-005 Manual / Connector Separation

Project Owner-attested manual review 不得记录为 connector-observed。


### MMCA-DS-006 Four-Party Separation

Codex、Architecture Coordinator、External Consultant 与 Project Owner 职责不混同。


### MMCA-DS-007 Positive Authority

ACCEPT、AUTHORIZE 和 START DOWNSTREAM 由 Project Owner 独占。


### MMCA-DS-008 Reviewer Negative Authority

Reviewer outcome 不产生资产接受。


### MMCA-DS-009 Internal / External Classification

Internal functional independence 与 External third-party independence 明确分离。


### MMCA-DS-010 Cross-Vendor Rule

同供应商、同模型家族、不同 session 或不同 prompt 不构成 Cross-Vendor Review。


### MMCA-DS-011 Human External Eligibility

人类外部顾问必须满足授权、独立、只读、SHA 绑定和利益冲突边界。


### MMCA-DS-012 Deterministic Non-Substitution

确定性检查不替代 Internal Review、External Review 或 Project Owner decision。


### MMCA-DS-013 Multi-Axis State Preservation

授权、完整性、数据、内部 Review、外部 Review、分歧、Owner decision 和历史分别保留。


### MMCA-DS-014 Unique Governing Status

必须通过确定优先级导出唯一当前总体状态。


### MMCA-DS-015 Current / Historical Separation

历史 PASS、response 和 decision 不得作为新 SHA 的当前状态。


### MMCA-DS-016 Design Lifecycle

Design Spec 自身生命周期完整；仅本次第二次受限修订后 fixed-SHA 的 Architecture Coordinator internal re-review 已获授权，其他 Design Review 和全部 External Review 仍未授权。


### MMCA-DS-017 Future Review Lifecycle

Future lifecycle 仅为治理设计，不创建运行时。


### MMCA-DS-018 Transition Control

所有正向转换均需要明确 Project Owner authority。


### MMCA-DS-019 Transition Matrix

Transition Matrix 必须明确每个状态不产生自动 Positive Authority。


### MMCA-DS-020 Packet Abstractness

Review Packet 仅定义治理信息类别，不定义具体字段 Schema 或 payload。


### MMCA-DS-021 Packet Identity

Packet 必须绑定 project、asset、SHA 和 review scope。


### MMCA-DS-022 Scope Fidelity

partial input review 不得冒充 full asset external PASS。


### MMCA-DS-023 Minimal Disclosure

Packet 仅包含被授权 Review 所需的最小内容。


### MMCA-DS-024 Attachment Isolation

上游附件必须逐项授权，主资产权限不得自动扩展。


### MMCA-DS-025 Standing Authorization Separation

本 Spec 不授予 Standing External Review Authorization。


### MMCA-DS-026 Standing Authorization Completeness

未来 Standing Authorization 必须回答全部 25 项问题。


### MMCA-DS-027 Standing Authorization Revocation

Standing Authorization 必须可撤回、可过期且不可自动恢复。


### MMCA-DS-028 G0–G5 Classification

数据分类覆盖 public、governance、Schema、code、Real Matter 和 credential。


### MMCA-DS-029 G4 Isolation

G4 不得进入一般 Standing Authorization。


### MMCA-DS-030 G5 Prohibition

G5 绝对禁止进入 Packet、prompt、附件或日志。


### MMCA-DS-031 Queue Is Not Authorization

READY、QUEUED 和 DISPATCHED 均不产生 authority。


### MMCA-DS-032 Idempotency and Retry

Deduplication 和 retry 不得扩大 scope、cost、provider 或 authorization。


### MMCA-DS-033 Ledger Is Not Acceptance

Ledger event 不得替代 Project Owner decision。


### MMCA-DS-034 Provenance Fidelity

Manual 与 connector provenance 必须分离。


### MMCA-DS-035 Decision Gate Separation

OWNER DECISION READY 不等于 ACCEPTED。


### MMCA-DS-036 Hard Gate Formula

Internal PASS、External PASS、Project Owner ACCEPTED 与 SHA MATCH 均为必要条件。


### MMCA-DS-037 SHA Invalidation

任何新 SHA 均不得继承旧 Review 或 acceptance。


### MMCA-DS-038 Quota Fail-Closed

Quota exhausted 保持 pending，不得内部替代或自动放行。


### MMCA-DS-039 Availability Fail-Closed

External unavailable 保持 pending，不得推定 PASS 或 FAIL。


### MMCA-DS-040 Disagreement Human Gate

实质分歧强制 Human Review，禁止自动 tie-breaker。


### MMCA-DS-041 No External Invocation or Transfer

本 Spec 物化未调用外部模型或传输项目资产。


### MMCA-DS-042 No API, Connector, MCP or Credential

未创建或测试 API、Connector、MCP、webhook 或 credential。


### MMCA-DS-043 No Runtime Assets

未创建 Packet、Queue、Ledger、Decision Gate、Agent、Skill、script、code 或 configuration。


### MMCA-DS-044 No Concrete Schema or Data

未创建 concrete field schema、instance、example、test data 或 Real Matter。


### MMCA-DS-045 No Result or Automatic Escalation

未创建 RESULT，未自动启动 Design Review、External Review、Implementation 或 downstream。


## Authorized Scope

本次仅允许：

1. 创建本 Design Spec；
2. 绑定 accepted Handoff SHA；
3. 设计四方角色和权限矩阵；
4. 设计 Internal / External Review 生命周期和状态机；
5. 设计 Review Packet 抽象治理契约；
6. 设计 Queue、Ledger 与 Decision Gate 治理边界；
7. 设计 SHA 绑定、失效、撤回和重新审查规则；
8. 设计 Standing External Review Authorization 边界；
9. 设计 Cross-Vendor independence；
10. 设计 quota、availability、retry 和 disagreement Fail-Closed；
11. 设计 G0–G5 数据隔离；
12. 定义 Design Review Questions 和 Acceptance Gates；
13. 保持 External Invocation、Transfer、Code 与 Implementation 关闭。


## Not Authorized

以下行为均未获授权：

1. 启动除本次第二次受限修订后 fixed-SHA Architecture Coordinator internal re-review 之外的任何 Design Review 或 External Review；
2. 创建 Automation Result；
3. 授予 Standing External Review Authorization；
4. 创建 Standing Authorization Policy 文件；
5. 创建 Review Packet 实例；
6. 创建 Review Queue；
7. 创建 Review Ledger；
8. 创建 Decision Gate；
9. 调用 Gemini；
10. 调用任何 External Model；
11. 发送本 Spec、Handoff 或其他项目资产；
12. 执行 Connection Test；
13. 创建或测试 API；
14. 创建或测试 Connector；
15. 创建或测试 MCP；
16. 创建 webhook；
17. 创建 Agent；
18. 创建 Skill；
19. 创建 script；
20. 创建 source code；
21. 创建 executable configuration；
22. 创建 concrete field Schema；
23. 创建或使用 credential；
24. 创建 instance、example 或 test data；
25. 导入或处理 Real Matter；
26. 外发 Evidence、PII 或 privileged material；
27. 修改 accepted Handoff；
28. 修改任何 accepted Phase 3 asset；
29. 启动 Schema Validation Execution；
30. 启动 Implementation；
31. 执行 Legal Reasoning；
32. 自动接受本 Spec；
33. 自动启动任何后续 Phase、Track 或 Layer。


## Artifact Boundary

Authorized New Asset:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_SPEC.md
```

Bound Read-Only Asset:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_HANDOFF.md
SHA-256:
3B615C826EA1D54C9BCAB8A530BECCE4F935197BAE3174AD57D1958296692919
```

Explicitly Not Created:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_RESULT.md
Standing Authorization Policy
Review Packet
Review Queue
Review Ledger
Decision Gate
API
Connector
MCP
Webhook
Agent
Skill
Script
Code
Executable Configuration
Concrete Field Schema
Credential
Instance
Example
Test Data
```


## Current System State

```text
Phase 3 Track D:
SCHEMA VALIDATION GOVERNANCE DESIGN

Handoff:
ACCEPTED & SHA BOUND

Spec:
ACCEPTED & SHA BOUND

Result:
ACCEPTED & SHA BOUND

Schema Validation Execution:
NOT AUTHORIZED


ACOS Multi-Model Collaboration Automation:

Handoff:
ACCEPTED & CLOSED

Handoff SHA-256:
3B615C826EA1D54C9BCAB8A530BECCE4F935197BAE3174AD57D1958296692919

Internal Handoff Review:
PASS — GRADE A / 30 OF 30

External Handoff Review:
PASS — GOOGLE GEMINI 3.6 FLASH / HIGH
MANUAL / PROJECT OWNER ATTESTED

Project Owner Handoff Acceptance:
ACCEPTED & SHA BOUND

Automation Design Spec:
LIMITED REVISION MATERIALIZED

Initial Design Review:
FAIL — GRADE C / 41 OF 45 GATES PASS
SHA: 948A62F86310F78BB0310365555D4200976E56A01AE09ED3D9EC7EDEAABA65C8

First Limited Revision Re-Review:
FAIL — GRADE C / 41 OF 45 GATES PASS
SHA: FFF0DD9846A73C2919FBC7062A46A4295CDCAD8B3FAF35173287C5736838AB64

Second Limited Revision:
AUTHORIZED / MATERIALIZED

Second Internal Re-Review:
AUTHORIZED / PENDING FIXED SECOND-REVISED SHA

Automation Result:
NOT CREATED / NOT AUTHORIZED

Standing External Review Authorization:
NOT GRANTED

External Model Invocation:
NOT AUTHORIZED

Project Asset Transfer:
NOT AUTHORIZED

Review Packet / Queue / Ledger / Decision Gate:
NOT CREATED / NOT AUTHORIZED

API / Connector / MCP / Code / Credential:
NOT CREATED / NOT AUTHORIZED

Executable Configuration / Concrete Field Schema:
NOT CREATED / NOT AUTHORIZED

Real Matter:
NOT AUTHORIZED

Implementation:
NOT AUTHORIZED
```


## Review Submission

Review Object:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_SPEC.md
```

Proposed Internal Reviewer:

```text
Architecture Coordinator
```

Current Review Authority:

```text
GRANTED — CURRENT SECOND-REVISION FIXED-SHA
INTERNAL ARCHITECTURE COORDINATOR RE-REVIEW ONLY
```

Authorized Re-Review Scope:

```text
READ-ONLY DESIGN, AUTHORITY, INDEPENDENCE, STATE-MACHINE,
DATA-BOUNDARY AND FAIL-CLOSED REVIEW
```

Authorized Re-Review must not:

- edit this Spec；
- invoke Gemini；
- transfer project assets；
- test external connectivity；
- create Packet、Queue、Ledger or Decision Gate；
- create API、Connector、MCP、Code or Credential；
- create RESULT；
- accept this Spec；
- activate any downstream stage。


## Next Authorized Action

当前唯一获准的下一动作是：

```text
ARCHITECTURE COORDINATOR
FULL 45-GATE READ-ONLY RE-REVIEW
OF THE FIXED SECOND-REVISED SPEC SHA
```

在 Re-Review 结论形成前必须停留在：

```text
SECOND LIMITED REVISION MATERIALIZED
INTERNAL RE-REVIEW AUTHORIZED / PENDING
STANDING EXTERNAL REVIEW AUTHORIZATION NOT GRANTED
EXTERNAL INVOCATION NOT AUTHORIZED
PROJECT ASSET TRANSFER NOT AUTHORIZED
API / CONNECTOR / MCP / CODE / CREDENTIAL NOT AUTHORIZED
IMPLEMENTATION NOT AUTHORIZED
RESULT NOT AUTHORIZED
```

Re-Review PASS 不等于 Spec Acceptance，不等于 External Review，不等于 Standing External Review Authorization，也不等于 External Invocation、Asset Transfer、Code 或 Implementation Authorization。
