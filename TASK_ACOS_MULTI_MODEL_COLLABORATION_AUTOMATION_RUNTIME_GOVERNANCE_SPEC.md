# TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_RUNTIME_GOVERNANCE_SPEC

## Status

```text
MATERIALIZED — DESIGN REVIEW NOT AUTHORIZED
```


## System Identification

System:

```text
ACOS — Architecture & Control Operating System
```

Program:

```text
Multi-Model Collaboration Automation
```

Design Layer:

```text
Runtime Governance
```

Artifact Type:

```text
DESIGN SPEC ONLY
```


## Design Authorization

Project Owner authorized the materialization of exactly one asset:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_RUNTIME_GOVERNANCE_SPEC.md
```

Authorized Scope:

```text
DESIGN SPEC ONLY
```

Authorized Design Subjects:

1. Runtime Governance 角色、权限与责任矩阵；
2. Authorization、SHA、数据分级及 Review 状态机；
3. Packet、Queue、Ledger、Decision Gate 的抽象治理契约；
4. Connector、Credential 与外部调用隔离规则；
5. kill switch、撤回、恢复及 Human Review 控制；
6. G0–G5 与 Real Matter 禁入规则；
7. Threat / Privacy / Security 前置条件；
8. 测试、Pilot、部署与回滚的阶段门禁；
9. Review Questions 与 Acceptance Gates。

Explicitly Excluded:

```text
Standing External Review Authorization:
NOT GRANTED

External Invocation / Asset Transfer:
NOT AUTHORIZED

Concrete Packet / Queue / Ledger / Decision Gate:
NOT AUTHORIZED

API / Connector / MCP / Code / Credential:
NOT AUTHORIZED

Test Data / Runtime / Real Matter / Implementation:
NOT AUTHORIZED

RESULT:
NOT AUTHORIZED

DESIGN REVIEW:
NOT AUTHORIZED
```


## Bound Runtime Governance Handoff

Asset:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_RUNTIME_GOVERNANCE_HANDOFF.md
```

Bound SHA-256:

```text
0A81B06B2EB3F85515185FB9FAFCE12C99E9E47B81D227461F1E07773E4645DE
```

Status:

```text
ACCEPTED & SHA BOUND
```

Review Baseline:

```text
Architecture Review:
PASS — GRADE A

Acceptance Gates:
45 / 45 PASS

Review Questions:
45 / 45 PASS

Blockers / Non-Blockers / Regressions / Overreach:
0 / 0 / 0 / 0
```


## Inherited Accepted Automation Baseline

### Automation Governance Handoff

```text
Asset:
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_HANDOFF.md

SHA-256:
3B615C826EA1D54C9BCAB8A530BECCE4F935197BAE3174AD57D1958296692919

Status:
ACCEPTED & CLOSED
```


### Automation Design Spec

```text
Asset:
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_SPEC.md

SHA-256:
4EF5D1FABEC63FA82D9E5F20F7443D4D3BD4BF7A54CFF8578490A7ECCADDED48

Status:
ACCEPTED & SHA BOUND
```


### Automation Design Result

```text
Asset:
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_RESULT.md

SHA-256:
5E464640F105A934163EC0EF95710601C09C8632FFF7EC1835387B4574585B2B

Status:
ACCEPTED & SHA BOUND
```


## Acceptance Snapshot Fidelity

本 Spec 记录 accepted assets 的治理快照，不回写或修改任何 accepted asset。

Rules:

- conversation-level Project Owner decision 不伪装为物化 decision file；
- exact SHA 是当前资产身份；
- 文件名相同但 SHA 不同，必须视为不同候选；
- 历史 PASS、acceptance 或 authorization 不自动迁移至新 SHA；
- lower-precedence asset 不得扩大 higher-precedence authority；
- 当前 Spec 的物化状态不构成 Review、Acceptance 或 Runtime authorization。


## Normative Precedence

发生解释冲突时，按以下顺序适用：

1. Project Owner 针对 exact asset / action 的当前有效决定；
2. accepted Automation Design Spec exact SHA；
3. accepted Automation Design Result exact SHA；
4. accepted Automation Handoff exact SHA；
5. accepted Runtime Governance Handoff exact SHA；
6. 本 Runtime Governance Design Spec 当前候选 SHA；
7. 未来经单独授权和接受的 Runtime Governance Result。

Rules:

- higher-precedence prohibition 不得被 lower-precedence permission 覆盖；
- source conflict 未解决时进入 `BLOCKED — GOVERNANCE CONFLICT`；
- compressed Result wording 不得覆盖 accepted Spec 的完整控制语义；
- revoked、expired、withdrawn 或 superseded decision 不得作为 current authority；
- 本 Spec 不得自我授权 Review、Result、component、Code、Test、Pilot 或 Deployment。


## Known Accepted Interpretation

Decision Gate 的唯一正向 readiness output：

```text
OWNER DECISION READY
```

允许的保护性结果包括但不限于：

```text
BLOCKED
PENDING
HUMAN REVIEW REQUIRED
STALE
CANCELLED
SUPERSEDED
PAUSED/BLOCKED BY KILL
```

Decision Gate 禁止产生：

```text
PROJECT OWNER ACCEPTED
START EXECUTION
START DOWNSTREAM
```

该解释继承 accepted Automation Spec 与 Result，不修改其内容或 SHA。


## Objective

本 Spec 将 accepted Runtime Governance Handoff 具化为可审查的抽象治理设计。

目标是定义未来 Runtime 必须满足的：

- authority separation；
- exact-SHA integrity；
- data-class isolation；
- review independence；
- deterministic protective state transitions；
- Human Review and Project Owner gates；
- audit fidelity；
- fail-closed behavior；
- kill、revocation and recovery controls；
- staged security、test and deployment authorization。

本目标不创建 Runtime。


## Design Non-Goals

本 Spec 不定义：

- concrete field names；
- JSON、YAML 或 database Schema；
- API endpoint、method 或 payload；
- protocol；
- class、function、module 或 package；
- executable state machine；
- database；
- deployment topology；
- provider SDK；
- credential value or storage instance；
- test plan、test case、fixture 或 test data；
- actual Packet、Queue、Ledger、Decision Gate 或 Connector；
- production control；
- Real Matter processing；
- legal reasoning。


## Governing Distinctions

```text
Runtime Governance Design Spec
≠
Runtime Governance Result

Runtime Governance Design
≠
Runtime Component Design

Abstract Governance Contract
≠
Concrete Field Schema

Conceptual State
≠
Executable State Machine

Packet Eligibility
≠
Dispatch Authorization

Queue Admission
≠
Authorization

Ledger Record
≠
Current Governing Decision

Decision Gate Readiness
≠
Project Owner Acceptance

Acceptance
≠
Downstream Authorization

Connector Eligibility
≠
Connector Creation

Credential Isolation Rule
≠
Credential Creation or Use

Validation PASS
≠
Pilot Authorization

Pilot PASS
≠
Deployment Authorization
```


## Runtime Governance Design Principles

### MMCRG-D-001 Authorization Before Action

任何未来 Runtime action 发生前，必须存在当前有效、范围明确且可绑定的 Project Owner authorization。


### MMCRG-D-002 Sole Positive Authority

只有 Project Owner 可以产生 `ACCEPT`、`AUTHORIZE`、`PUBLISH`、`START EXECUTION` 或 `START DOWNSTREAM`。


### MMCRG-D-003 Protective Automation Only

未来自动化只能产生保护性阻断、等待、取消、失效标记、人工路由和通知；不得产生正向治理决定。


### MMCRG-D-004 Exact Identity

Asset、authorization、Packet、request、response、review、Human Review resolution 和 Project Owner decision 必须绑定 exact identity 与 exact SHA。


### MMCRG-D-005 SHA Change Invalidates Carry-Forward

任何内容变化均产生新候选 SHA；旧 Review 与 readiness 不得迁移。


### MMCRG-D-006 Multi-Axis State Preservation

Authorization、integrity、data、review、disagreement、kill、decision 和 history 状态必须分别保留。


### MMCRG-D-007 Unique Governing Status

多轴事实可以并存，但每个 exact request profile 只能导出一个 current governing status。


### MMCRG-D-008 Internal / External Non-Substitution

same-family internal agent 可增强内部审查，但不得被标记为 Cross-Vendor external reviewer。


### MMCRG-D-009 Cross-Vendor Identity

External model independence 必须基于 underlying provider，不得依据产品标签、代理名称或 aggregator branding 推断。


### MMCRG-D-010 Data Classification First

External eligibility evaluation 必须晚于 G0–G5 classification；UNKNOWN 或 MIXED 未解时必须阻断。


### MMCRG-D-011 G4 Runtime Exclusion

Real Matter、Evidence、PII 和 privileged material 不得进入 external Runtime path。


### MMCRG-D-012 G5 Absolute Exclusion

Credential 或 secret 不得进入 Packet、prompt、Queue content、Ledger content、log、response evidence 或 model context。


### MMCRG-D-013 Minimal Disclosure

任何未来获授权的 external transfer 只能包含完成固定审查范围所必需的最小信息。


### MMCRG-D-014 Queue Is Not Authority

Queue 只能管理已具备 eligibility 的请求，不能产生或扩大 authority。


### MMCRG-D-015 Ledger Is Not Decision

Ledger 只能保存治理事实与 provenance，不能接受资产、裁决分歧或授权下游。


### MMCRG-D-016 Decision Gate Is Not Owner

Decision Gate 的唯一正向输出是 `OWNER DECISION READY`；任何 acceptance 均需 Project Owner 明确决定。


### MMCRG-D-017 Human Disagreement Gate

实质分歧必须进入 Human Review，不得采用 majority、confidence、speed、cost 或 favorable-outcome tie-break。


### MMCRG-D-018 Fail-Closed Availability

Quota、timeout、provider failure 或 connector unavailable 不得被转换为 PASS、FAIL 或 provider switch。


### MMCRG-D-019 Revocation Dominance

Revocation、expiry、suspension、supersession、withdrawal 和 kill 必须优先于 Queue、retry、delayed response 与历史 PASS。


### MMCRG-D-020 No Silent Recovery

服务恢复、额度恢复、process restart 或 operator login 不得自动恢复 cancelled、OWNER HOLD、revoked 或 killed work。


### MMCRG-D-021 Kill Authority Separation

Project Owner 是 kill activation authority 与 delegation 的唯一来源；受委托执行者只能在 exact scope 内执行机械性保护动作。


### MMCRG-D-022 Owner-Only Re-Enable

Kill 后的 re-enable authority 仅属于 Project Owner，且不可委托。


### MMCRG-D-023 Immutable Audit History

历史事实不得静默删除或改写；纠错必须通过 correction、supersession、withdrawal 或 explicit invalidation 保真记录。


### MMCRG-D-024 No Automatic Escalation

Materialization、Review PASS、Acceptance、Validation PASS 或 Pilot PASS 均不自动激活下一阶段。


### MMCRG-D-025 Design Is Not Implementation

本 Spec 的任何状态、契约或门禁均为治理设计，不构成组件、接口、代码、配置、凭证或运行许可。


## Four-Party Roles and Authority Matrix

### Project Owner

Exclusive Positive Authority:

- authorize exact asset / action；
- accept or reject exact SHA；
- authorize limited revision；
- request Human Review；
- place OWNER HOLD；
- release or redirect OWNER HOLD through a new exact-scope decision；
- withdraw exact asset；
- grant、suspend、revoke 或 supersede per-asset authorization；
- grant、suspend、revoke 或 supersede future Standing Authorization；
- authorize external transfer、provider、model、cost、retry and time scope；
- authorize component design、Code、Test、Pilot、Deployment and rollback；
- originate kill activation authority and delegate exact-scope activation execution；
- authorize re-enable after kill；
- authorize downstream。

Project Owner decision 不得从 silence、default、UI selection、reviewer PASS 或 Queue state 推断。


### Codex Executor

Design-Time Authority Under This Authorization:

- read bound governance assets；
- materialize this Spec；
- preserve exact SHA bindings；
- define abstract governance design；
- perform static integrity and boundary checks；
- calculate candidate SHA；
- report status。

Must Not:

- self-authorize Design Review；
- create Result；
- create components or concrete Schema；
- invoke external model；
- transfer project asset；
- create or use credential；
- implement Runtime。


### Architecture Coordinator

Future Role After Separate Authorization:

- fixed-SHA read-only Design Review；
- question and gate evaluation；
- blocker、non-blocker、regression and overreach classification；
- recommendation to Project Owner。

Must Not:

- edit candidate while reviewing；
- act as Cross-Vendor reviewer merely because it is a separate agent；
- accept asset；
- expand authorization；
- create downstream authority。

Current:

```text
DESIGN REVIEW:
NOT AUTHORIZED
```


### External Consultant

Future Role After Separate Per-Asset or Standing Authorization:

- independent advisory review；
- bind provider、model、scope、asset SHA and limitations；
- return PASS、FAIL、BLOCKED、LIMITED or PENDING。

Must Not:

- produce Project Owner acceptance；
- receive G4 or G5；
- broaden transfer scope；
- be inferred from same-family internal agent。

Current:

```text
EXTERNAL INVOCATION / TRANSFER:
NOT AUTHORIZED
```


### Human Reviewer

Future Role:

- resolve substantive disagreement；
- validate identity、scope、authority and blocker interpretation；
- request supplemental review；
- recommend but not accept。

If the Project Owner personally performs Human Review, disagreement resolution and final Owner decision must remain separately recorded.


### Future Protective Operator

Future Role Exists Only After Separate Authorization:

- execute kill activation only within Project Owner delegated exact scope；
- perform mechanical protective action；
- preserve history and notify Owner。

Must Not:

- create、expand、modify or redelegate authority；
- produce OWNER HOLD；
- authorize re-enable；
- disable kill switch；
- resume work。


### Future Runtime

Permitted Future Function:

- evaluate deterministic eligibility；
- emit protective states；
- preserve provenance；
- route decision readiness to Project Owner。

Prohibited Function:

- act as any reviewer or Project Owner；
- create authority；
- access prohibited data；
- change provider or cost silently；
- accept asset；
- start downstream。


### Decision Rights Matrix

| Action | Project Owner | Codex | Architecture Coordinator | External Consultant | Protective Operator | Runtime |
|---|---|---|---|---|---|---|
| Create positive authorization | EXCLUSIVE | NO | NO | NO | NO | NO |
| Accept exact SHA | EXCLUSIVE | NO | NO | NO | NO | NO |
| Recommend PASS / FAIL | May consider | Internal evidence only | YES — internal | YES — external | NO | NO |
| Produce protective BLOCKED | May direct | Static only | Recommend | Recommend | Exact delegated kill only | Future deterministic only |
| Grant Standing Authorization | EXCLUSIVE | NO | NO | NO | NO | NO |
| Place or release OWNER HOLD | EXCLUSIVE | NO | NO | NO | NO | NO |
| Activate kill | Direct or delegate | NO | NO | NO | Exact delegated scope only | NO self-authorization |
| Authorize re-enable | EXCLUSIVE / NON-DELEGABLE | NO | NO | NO | NO | NO |
| Start downstream | EXCLUSIVE separate authorization | NO | NO | NO | NO | NO |


## Authorization Governance Contract

### Authorization Sources

External Review authority may in the future be satisfied by either:

```text
VALID PER-ASSET AUTHORIZATION
OR
VALID STANDING AUTHORIZATION
```

If neither exists:

```text
BLOCKED — AUTHORIZATION
```

The two paths are alternatives, not cumulative requirements.


### Authorization Completeness

Future authorization evaluation must conceptually establish:

- Project identity；
- action type；
- asset identity and SHA scope；
- reviewer class；
- provider and model scope；
- transfer mode；
- data-class scope；
- review scope；
- time and expiry；
- cost / quota；
- retry ceiling；
- cancellation and revocation authority；
- whether attachments are covered；
- whether manual or connector execution is covered。

These are binding obligations, not concrete fields.


### Authorization Axis

```text
NOT AUTHORIZED
AUTHORIZED — SCOPED
SUSPENDED
REVOKED
EXPIRED
SUPERSEDED
```

Only Project Owner can create `AUTHORIZED — SCOPED`.


### Authorization Priority

Priority:

1. active kill；
2. current revocation；
3. current suspension；
4. expiry；
5. supersession；
6. applicable exact per-asset authorization；
7. applicable Standing Authorization；
8. no authority。

Historical authorization cannot override a current protective state.


## Multi-Axis Runtime Governance State Model

本节定义 conceptual state vocabulary，不定义 fields、enums in code 或 executable configuration。


### Asset Integrity Axis

```text
UNBOUND
BOUND — SHA MATCH
MISMATCH
STALE
SUPERSEDED
WITHDRAWN
```

`SHA MATCH` 仅证明版本身份，不证明语义正确。


### Data Eligibility Axis

```text
UNKNOWN
ELIGIBLE — WITHIN AUTHORIZED CLASS
RESTRICTED — SEPARATE AUTHORIZATION REQUIRED
PROHIBITED
CLASSIFICATION STALE
```


### Packet Axis

```text
NOT AUTHORIZED
ELIGIBILITY PENDING
PREPARED
SEALED
STALE
CANCELLED
SUPERSEDED
BLOCKED
```

`SEALED` 不等于 dispatch authorized。


### Queue Axis

```text
NOT AUTHORIZED
ELIGIBILITY PENDING
READY
QUEUED
DISPATCHED
RESPONSE PENDING
PENDING — QUOTA
PENDING — UNAVAILABLE
BLOCKED — AUTHORIZATION
BLOCKED — DATA
BLOCKED — INTEGRITY
PAUSED/BLOCKED BY KILL
CANCELLED
SUPERSEDED
STALE
COMPLETED — RESPONSE BOUND
```

`PAUSED/BLOCKED BY KILL` 不是 `OWNER HOLD`。


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
RESOLVED — REVIEWS GOVERNING AND CONSISTENT
RESOLVED — BLOCKER CONFIRMED
RESOLVED — SUPPLEMENTAL REVIEW REQUIRED
RESOLVED — SCOPE OR AUTHORITY INVALID
UNRESOLVED
STALE
```


### Decision Gate Axis

```text
NOT READY
BLOCKED — AUTHORIZATION
BLOCKED — DATA
BLOCKED — INTEGRITY
BLOCKED — REVIEW
PENDING — INTERNAL
PENDING — EXTERNAL
LIMITED — SCOPE COMPLETION REQUIRED
REVISION REQUIRED
HUMAN REVIEW REQUIRED
PAUSED/BLOCKED BY KILL
OWNER DECISION READY
STALE
CANCELLED
SUPERSEDED
```

Only `OWNER DECISION READY` is positive readiness. It is not acceptance.


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
HOLD RELEASED — REVALIDATION REQUIRED
HUMAN REVIEW REQUESTED
WITHDRAWN
SUPERSEDED
```


### Kill Axis

```text
INACTIVE
ACTIVATION AUTHORIZED — EXACT SCOPE
ACTIVE
RECOVERY REVIEW REQUIRED
RE-ENABLE AUTHORIZED — OWNER ONLY
RE-ENABLED AFTER REVALIDATION
```

No state transition to re-enable may be inferred from availability recovery.


### History Axis

```text
CURRENT
HISTORICAL
STALE
SUPERSEDED
CANCELLED
WITHDRAWN
INVALIDATED
```


### Canonical State Names and Projection

各轴保留自身的 evidence / decision disposition；current governing status 必须使用下表的 canonical projection。

| Axis / Historical Label | Canonical Meaning | Current Governing Projection |
|---|---|---|
| `ACCEPTED — SHA BOUND` / `ACCEPTED & SHA BOUND` | Project Owner acceptance decision bound to exact SHA | `ACCEPTED & CLOSED`，但仅在无更高优先级状态时成立 |
| `REJECTED — SHA BOUND` / `REJECTED & SHA BOUND` | Project Owner rejection decision bound to exact SHA | `REJECTED & CLOSED`，但仅在无更高优先级状态时成立 |
| `HOLD — OWNER` | Project Owner explicit hold decision | `OWNER HOLD` |
| `REJECTED — UNBOUND RESPONSE` / `UNBOUND` | response integrity disposition，不是 reviewer verdict | `BLOCKED — INTEGRITY / UNBOUND RESPONSE` |
| `LIMITED — SCOPE RESTRICTED` / `LIMITED` | bound response 的实际范围不足 | `LIMITED — SCOPE COMPLETION REQUIRED` |
| `PENDING — EXTERNAL UNAVAILABLE` / `PENDING — QUOTA EXHAUSTED` | external governing outcome 尚不可获得 | `PENDING — EXTERNAL UNAVAILABLE / QUOTA` |
| `PAUSED/BLOCKED BY KILL` | active kill 产生的 protective operational pause | `PAUSED/BLOCKED BY KILL` |

Rules:

- axis label 不得被直接当作另一个轴的状态；
- projection 只能在完成全局优先级判断后产生；
- historical alias 不得创造新的 current status；
- 同一 exact profile 在同一时点只能有一个 canonical current governing status。


## Unique Current Governing Status

### Deterministic Priority

每个 exact asset / request / review profile 的 current governing status 按以下优先级导出：

1. `KILL ACTIVE / PAUSED/BLOCKED BY KILL`；
2. `WITHDRAWN`；
3. `SUPERSEDED / STALE`；
4. `CANCELLED`；
5. `OWNER HOLD`；
6. `REJECTED & CLOSED`；
7. `ACCEPTED & CLOSED`；
8. `BLOCKED — INTEGRITY / UNBOUND RESPONSE`；
9. `BLOCKED — DATA / CREDENTIAL`；
10. `BLOCKED — AUTHORIZATION`；
11. `BLOCKED — REVIEW COULD NOT VALIDLY PROCEED`；
12. `HUMAN REVIEW REQUIRED`；
13. `REVISION REQUIRED`；
14. `LIMITED — SCOPE COMPLETION REQUIRED`；
15. `PENDING — EXTERNAL UNAVAILABLE / QUOTA`；
16. `EXTERNAL REVIEW PENDING`；
17. `INTERNAL REVIEW PENDING`；
18. `OWNER DECISION PENDING`；
19. `ELIGIBILITY PENDING`；
20. `NOT AUTHORIZED`。


### Priority Interpretation

- `KILL ACTIVE` 阻断 operational progression，但不删除历史 acceptance；
- global priority 是 current governing status 的唯一优先级；任何 component-local 或 reconciliation priority 仅用于生成 axis evidence，不得覆盖本表；
- active kill 时，integrity、review and pending states 继续作为 axis evidence 保留，但不得取代 `PAUSED/BLOCKED BY KILL` 的 current governing status；
- `OWNER HOLD` 仅能由 Project Owner 对未关闭的 exact profile 明确产生；Hold active 时，原 pending、review and readiness states 保留为 non-governing evidence；
- `ACCEPTED & CLOSED` 仅适用于未 withdrawn、未 superseded、SHA 仍匹配的 exact asset；
- request cancellation 不撤销另一个仍有效的 historical asset acceptance；
- `UNBOUND` 是 integrity disposition，不是 reviewer FAIL；
- `LIMITED` 要求 actual scope 可识别且可绑定，但不足以覆盖 required full scope；
- `PENDING`、`LIMITED`、`BLOCKED` 和 `UNBOUND` 均不得进入 Owner Decision Ready；
- Internal FAIL 与 External LIMITED、PENDING 或 MISSING 并存且无实质 verdict disagreement 时，导出 `REVISION REQUIRED — INTERNAL BLOCKER`；
- Internal PENDING / MISSING 与 External FAIL 并存且无实质 disagreement 时，导出 `REVISION REQUIRED — EXTERNAL BLOCKER`；
- Internal / External verdict conflict 优先进入 Human Review；
- reviewer PASS 不得产生 asset acceptance；
- new SHA 必须作为新候选重新评估。


## Runtime Governance Design Lifecycle

本生命周期管理本 Spec，不启动 Runtime。

```text
RGDS0  Runtime Governance Handoff Accepted
RGDS1  Runtime Governance Design Spec Authorized
RGDS2  Bound Baseline Verified
RGDS3  Design Spec Materialized
RGDS4  Design Review Authorized
RGDS5  Internal Design Review Completed
RGDS6  External Design Review Authorized
RGDS7  External Design Review Completed
RGDS8  Project Owner Decision Ready
RGDS9  Design Spec Accepted
RGDSF  Design Review Failed / Revision Required
RGDSB  Blocked
RGDSH  Owner Hold
RGDSW  Withdrawn
RGDSS  Superseded / Stale
```

Current:

```text
RGDS3 — DESIGN SPEC MATERIALIZED

RGDS4–RGDS9:
NOT AUTHORIZED
```

No stage automatically activates the next.


## Conceptual Runtime Review Lifecycle

本生命周期是 future governance model，不创建 executable state machine。

```text
OPS0   ACTION NOT AUTHORIZED
OPS1   AUTHORIZATION EVALUATION
OPS2   ASSET INTEGRITY EVALUATION
OPS3   DATA CLASSIFICATION
OPS4   PACKET ELIGIBILITY / SEALING
OPS5   INTERNAL REVIEW EVIDENCE EVALUATION
OPS6   EXTERNAL REVIEW ELIGIBILITY
OPS7   QUEUED
OPS8   DISPATCH REVALIDATION
OPS9   RESPONSE BINDING
OPS10  REVIEW RECONCILIATION
OPS11  HUMAN REVIEW
OPS12  OWNER DECISION READY
OPS13  PROJECT OWNER DECISION
OPS14  CLOSED
OPSB   BLOCKED
OPSK   PAUSED/BLOCKED BY KILL
OPSH   OWNER HOLD
OPSS   STALE / SUPERSEDED
OPSC   REQUEST CANCELLED
```


## Governance Transition Rules

### MMCRG-T-001 OPS0 to OPS1

Trigger:

- Project Owner current scoped authorization exists。

Queue、Ledger、reviewer、system default 或 prior PASS 不得触发。


### MMCRG-T-002 OPS1 to OPS2

Required:

- per-asset or Standing authorization valid；
- scope exact；
- no revocation、suspension、expiry or supersession；
- action、reviewer、provider、model、transfer and cost covered。

Failure:

```text
OPSB — BLOCKED AUTHORIZATION
```


### MMCRG-T-003 OPS2 to OPS3

Required:

- exact asset identity；
- exact SHA match；
- packet baseline identity known；
- no stale or withdrawn condition。

Mismatch:

```text
OPSB — BLOCKED INTEGRITY
```


### MMCRG-T-004 OPS3 to OPS4

Required:

- G-class known；
- highest-class composition applied；
- G4 and G5 absent；
- transfer permitted for the resulting class；
- minimal disclosure established。


### MMCRG-T-005 OPS4 to OPS5

Required:

- Packet materialization separately authorized；
- Packet prepared and sealed；
- scope、questions、gates and prohibitions fixed；
- no hidden or unclassified attachment。

Any Packet change invalidates seal.


### MMCRG-T-006 OPS5 Internal Branches

```text
INTERNAL PASS
→ CONTINUE ELIGIBILITY EVALUATION

INTERNAL FAIL
→ REVISION REQUIRED

INTERNAL BLOCKED
→ OPSB

INTERNAL STALE / UNBOUND
→ BLOCKED — INTEGRITY
```


### MMCRG-T-007 OPS5 to OPS6

External eligibility may be evaluated only if:

- applicable external authority exists；
- reviewer eligibility established；
- Cross-Vendor or authorized human independence established；
- transfer mode authorized；
- data eligible；
- cost and quota known；
- no active blocker。


### MMCRG-T-008 OPS6 to OPS7

Queue admission requires current authorization、sealed Packet、exact SHA、eligible data、eligible reviewer and known cost.

Queue admission creates no authority.


### MMCRG-T-009 OPS7 to OPS8

Immediately before dispatch, revalidate:

- authorization；
- expiry、revocation and suspension；
- Packet and asset SHA；
- data class；
- provider and model；
- quota、cost and retry ceiling；
- duplicate dispatch；
- kill state。


### MMCRG-T-010 OPS8 to OPS9

Receipt of a response only starts binding evaluation.

```text
RESPONSE RECEIVED
≠
GOVERNING RESPONSE
```


### MMCRG-T-011 Response Binding Branches

Response Binder 必须按以下顺序执行 first-match-wins 判定；后一分支不得覆盖前一分支：

```text
1. EXACT REQUEST CANCELLED
→ CANCELLED

2. IDENTITY / SHA / PACKET / REVIEWER / ACTUAL SCOPE
   MISSING, AMBIGUOUS, UNIDENTIFIABLE OR UNBINDABLE
→ REJECTED — UNBOUND RESPONSE

3. BOUND + REVIEWER OUTCOME FAIL
→ EXTERNAL FAIL

4. BOUND + REVIEWER OUTCOME BLOCKED
→ BLOCKED — REVIEW COULD NOT VALIDLY PROCEED

5. BOUND + REVIEWER OUTCOME PENDING
→ PENDING — GOVERNING OUTCOME NOT YET AVAILABLE

6. BOUND + REVIEWER OUTCOME LIMITED
→ LIMITED — SCOPE RESTRICTED

7. BOUND + REVIEWER OUTCOME PASS + IDENTIFIABLE NARROWER SCOPE
→ LIMITED — SCOPE RESTRICTED

8. BOUND + REVIEWER OUTCOME PASS + FULL REQUIRED SCOPE
→ EXTERNAL PASS
```

For branches 3–6, actual scope and limitations remain recorded, but scope breadth does not change the explicit FAIL、BLOCKED、PENDING or LIMITED disposition.


### MMCRG-T-012 LIMITED / UNBOUND Separation

```text
PASS WITH ACTUAL SCOPE IDENTIFIABLE AND BOUND, BUT NARROW
OR
EXPLICIT LIMITED OUTCOME WITH IDENTIFIABLE BOUND ACTUAL SCOPE
→ LIMITED

ACTUAL SCOPE MISSING, AMBIGUOUS, UNIDENTIFIABLE OR UNBINDABLE
→ UNBOUND
```

`LIMITED` 不得映射为 PASS；`UNBOUND` 不得映射为 FAIL。明确的 FAIL、BLOCKED 或 PENDING 在完成 binding 后分别优先映射为 FAIL、BLOCKED 或 PENDING，不因 scope 较窄而改写为 LIMITED。


### MMCRG-T-013 OPS9 to OPS10

Only current bound response may enter reconciliation.

Stale、superseded、cancelled 或 post-kill in-flight response remains historical and non-governing.


### MMCRG-T-014 Reconciliation Branches

本规则是 component-local reconciliation projection，仅在全局 current governing priority 已确认不存在 active kill、withdrawal、stale / superseded、request cancellation 或 OWNER HOLD 后适用。

Local branches 按以下顺序 first-match-wins：

```text
1. EXTERNAL UNBOUND OR INTEGRITY MISMATCH
→ BLOCKED — INTEGRITY

2. INTERNAL BLOCKED OR EXTERNAL BLOCKED
→ CORRESPONDING BLOCKED STATE

3. PASS / FAIL CONFLICT OR ANY SUBSTANTIVE DISAGREEMENT
→ HUMAN REVIEW REQUIRED

4. INTERNAL FAIL + EXTERNAL FAIL / LIMITED / PENDING / MISSING
   + NO SUBSTANTIVE DISAGREEMENT
→ REVISION REQUIRED — INTERNAL BLOCKER

5. INTERNAL PENDING / MISSING + EXTERNAL FAIL
   + NO SUBSTANTIVE DISAGREEMENT
→ REVISION REQUIRED — EXTERNAL BLOCKER

6. EXTERNAL LIMITED
→ SCOPE COMPLETION REQUIRED

7. EXTERNAL PENDING / UNAVAILABLE / QUOTA
→ EXTERNAL REVIEW PENDING

8. INTERNAL PENDING / MISSING + EXTERNAL PASS / MISSING
→ INTERNAL REVIEW PENDING

9. INTERNAL PASS + EXTERNAL PASS + NO DISAGREEMENT
→ OWNER DECISION READINESS EVALUATION
```


### MMCRG-T-015 OPS10 to OPS11

Human Review entry triggers:

- verdict disagreement；
- blocker or severity disagreement；
- scope disagreement；
- identity or SHA disagreement；
- authority interpretation disagreement；
- reviewer classification disagreement；
- data classification disagreement；
- limitation disagreement。


### MMCRG-T-016 Human Review Resolution

Human Review must produce exactly one:

```text
REVIEWS GOVERNING AND CONSISTENT
→ RETURN TO RECONCILIATION

BLOCKER CONFIRMED
→ REVISION REQUIRED

SUPPLEMENTAL REVIEW REQUIRED
→ RETURN TO APPLICABLE REVIEW PENDING

SCOPE OR AUTHORITY INVALID
→ BLOCKED — AUTHORIZATION / DATA / INTEGRITY

UNRESOLVED
→ HUMAN REVIEW REQUIRED
```

No Human Review resolution directly produces acceptance.

`OWNER HOLD` 不得由 Human Review 自动产生。只有 Project Owner 另行作出绑定 exact asset SHA 和 exact request profile 的明确 `HOLD` 决定，才可从 `HUMAN REVIEW REQUIRED` 或其他未关闭状态进入 `OPSH — OWNER HOLD`。


### MMCRG-T-017 OPS10 to OPS12

Required:

- authorization valid；
- exact SHA match；
- data eligible；
- Internal PASS；
- eligible External PASS；
- no disagreement；
- no active blocker；
- no active kill；
- current evidence complete。

Output:

```text
OWNER DECISION READY
```


### MMCRG-T-018 OPS12 to OPS13

Project Owner may:

```text
ACCEPT
REJECT
AUTHORIZE LIMITED REVISION
REQUEST HUMAN REVIEW
HOLD
WITHDRAW
```

Each decision must bind exact asset SHA and scope.


### MMCRG-T-019 Owner Decision Effects

```text
ACCEPT
→ ACCEPTED & SHA BOUND

REJECT
→ REJECTED & SHA BOUND

AUTHORIZE LIMITED REVISION
→ REVISION AUTHORIZED — SCOPED
→ NEW SHA AND RE-REVIEW REQUIRED

REQUEST HUMAN REVIEW
→ HUMAN REVIEW REQUIRED

HOLD
→ OPSH — OWNER HOLD

WITHDRAW
→ WITHDRAWN
```

Only `ACCEPT` creates acceptance.

Owner Hold Entry:

- 仅由 Project Owner 明确 `HOLD` 决定触发；
- 必须绑定 exact asset SHA、request profile and hold scope；
- 仅适用于未关闭状态；
- Hold active 时原 authorization、integrity、review、pending and disagreement axes 保留为 non-governing evidence；
- dispatch、retry、reconciliation progression and Owner Decision Ready 均停止。

Owner Hold Exit:

```text
PROJECT OWNER RELEASE HOLD AND RESUME EVALUATION
→ FULL REVALIDATION
→ RETURN TO THE EARLIEST APPLICABLE ELIGIBILITY / REVIEW STAGE

PROJECT OWNER AUTHORIZE LIMITED REVISION
→ REVISION AUTHORIZED — SCOPED

PROJECT OWNER REQUEST HUMAN REVIEW
→ HUMAN REVIEW REQUIRED

PROJECT OWNER REJECT
→ REJECTED & SHA BOUND

PROJECT OWNER WITHDRAW
→ WITHDRAWN
```

`OWNER HOLD` 不得因时间经过、服务恢复、quota 恢复、operator action 或 Runtime default 自动解除。`RELEASE HOLD` 不构成 ACCEPT；若未来希望 ACCEPT，必须在完整 revalidation 后重新达到 `OWNER DECISION READY`，再由 Project Owner 作出独立 ACCEPT 决定。


### MMCRG-T-020 Request Cancellation

Request cancellation:

```text
REVIEW REQUEST:
CANCELLED

ASSET:
NOT ACCEPTED / NOT REJECTED BY CANCELLATION ALONE
```

Request cancellation is not asset withdrawal.


### MMCRG-T-021 Stale / Superseded

Asset SHA、Packet、baseline、reviewer eligibility or response scope change causes current review evidence to become stale or superseded.


### MMCRG-T-022 Quota / Availability

```text
QUOTA EXHAUSTED
→ PENDING — QUOTA

EXTERNAL UNAVAILABLE / TIMEOUT
→ PENDING — UNAVAILABLE
```

Recovery requires complete revalidation and does not silently resume.


### MMCRG-T-023 Kill Activation

Activation requires:

- Project Owner direct action；or
- Project Owner exact-scope delegation to protective operator。

Effect:

```text
OPSK — PAUSED/BLOCKED BY KILL
```


### MMCRG-T-024 Kill Recovery

Re-enable requires:

- Project Owner explicit non-delegable decision；
- cause review；
- authorization revalidation；
- SHA、Packet、Queue、provider、model、quota and security revalidation。

Re-enable does not restore stale or cancelled work.


### MMCRG-T-025 Downstream Separation

Asset acceptance only permits evaluation of a separately authorized next action.

```text
ACCEPTED
≠
DOWNSTREAM AUTHORIZED
```


## Transition Matrix

| Current | Trigger / Condition | Next | Forbidden Interpretation |
|---|---|---|---|
| OPS0 | No authority | OPS0 | Queue allowed |
| OPS0 | Valid scoped Owner authorization | OPS1 | Runtime started |
| OPS1 | Authority invalid | OPSB — AUTHORIZATION | Warning-only |
| OPS2 | SHA mismatch | OPSB — INTEGRITY | Semantic FAIL |
| OPS3 | G4 or G5 | OPSB — DATA | Redaction assumed |
| OPS3 | UNKNOWN / MIXED unresolved | OPSB — DATA | Lowest class selected |
| OPS4 | Packet sealed | OPS5 | Dispatch authorized |
| OPS5 | Internal FAIL | REVISION REQUIRED | External PASS overrides |
| OPS10 | Internal FAIL + External LIMITED / PENDING / MISSING, no substantive disagreement | REVISION REQUIRED — INTERNAL BLOCKER | Limited/Pending overrides Internal blocker |
| OPS10 | Internal PENDING / MISSING + External FAIL, no substantive disagreement | REVISION REQUIRED — EXTERNAL BLOCKER | External FAIL ignored |
| OPS6 | External authority missing | OPSB — AUTHORIZATION | Standing assumed |
| OPS7 | Quota exhausted | PENDING — QUOTA | Provider switch |
| OPS7 | Kill active | OPSK | OWNER HOLD |
| Any operational state | Kill active + integrity mismatch | OPSK; integrity mismatch retained as non-governing axis evidence | Integrity replaces active kill as current governing status |
| OPS8 | Response received | OPS9 | Response governing |
| OPS9 | Bound full PASS | OPS10 | Asset accepted |
| OPS9 | Bound PASS with identifiable narrow scope or explicit bound LIMITED | LIMITED | Full PASS |
| OPS9 | Bound FAIL / BLOCKED / PENDING with identifiable narrow scope | FAIL / BLOCKED / PENDING respectively | Narrow scope forces LIMITED |
| OPS9 | Scope unbindable | UNBOUND | Reviewer FAIL |
| OPS10 | PASS / FAIL conflict | OPS11 | Majority resolution |
| OPS10 | Both PASS, no conflict | OPS12 | Acceptance |
| OPS11 | Blocker confirmed | REVISION REQUIRED | Automatic revision |
| OPS12 | Owner ACCEPT exact SHA | OPS14 — ACCEPTED | Downstream started |
| Any non-closed state | Explicit Owner HOLD bound to exact profile | OPSH — OWNER HOLD | Human Review or Runtime creates Hold |
| OPSH | Explicit Owner RELEASE HOLD | Full revalidation, then earliest applicable stage | Prior pending state auto-resumes |
| OPSH | Owner AUTHORIZE LIMITED REVISION / REQUEST HUMAN REVIEW / REJECT / WITHDRAW | Corresponding scoped branch | Runtime chooses branch |
| Any pre-decision | Request cancelled | OPSC | Asset withdrawn |
| Any current | SHA changes | OPSS | Old PASS carried |
| Any operational | Kill active | OPSK | History deleted |
| OPSK | Owner re-enable + full revalidation | Applicable prior eligibility stage | Stale request resumed |


## Abstract Component Governance Contracts

All contracts in this section define responsibilities and prohibitions only.

They do not define fields、methods、protocols、classes、files、tables、services or deployment units.


### Authorization Resolver

Must:

- evaluate current Project Owner authority；
- distinguish per-asset and Standing paths；
- apply expiry、revocation、suspension and supersession；
- bind action、asset、SHA、reviewer、provider、model、transfer、cost、time and retry scope；
- output eligible or protective blocked disposition。

Must Not:

- create authority；
- infer missing scope；
- broaden authorization；
- accept asset；
- re-enable kill state。


### Integrity Verifier

Must:

- compare exact asset SHA；
- verify Packet identity and seal status；
- verify response、review、Human Review and Owner decision binding；
- mark mismatch、stale or superseded。

Must Not:

- judge semantic correctness；
- downgrade mismatch to warning；
- reuse old-SHA evidence。


### Data Classifier

Must:

- classify G0–G5；
- apply highest-class composition；
- detect unknown and mixed content；
- block G4 / G5 external eligibility；
- preserve classification provenance。

Must Not:

- rely only on filename；
- silently downgrade after redaction；
- create redaction tool under this Spec；
- expose prohibited content in classification evidence。


### Review Packet

Abstract Obligations:

- bind project、asset、SHA、authorization、scope、reviewer class、provider/model scope、data class、questions、gates and prohibitions；
- enforce minimal disclosure；
- preserve manual / connector provenance；
- become immutable after seal；
- expire or supersede predictably。

Must Not:

- contain G4 or G5；
- create authority；
- mutate after seal；
- act as a concrete Schema under this Spec。


### Review Queue

Must:

- admit only eligible requests；
- preserve exact request identity；
- deduplicate only equivalent request profiles；
- enforce retry ceiling；
- apply cancellation、revocation、supersession and kill；
- distinguish quota pending、unavailable pending、OWNER HOLD and kill pause。

Must Not:

- grant authority；
- choose provider beyond scope；
- increase cost；
- revive cancelled work；
- interpret response；
- convert priority into eligibility。


### External Connector

Must in Future:

- transmit only an authorized sealed Packet；
- target only authorized provider and model；
- verify authority again at dispatch；
- expose transport provenance；
- stop on kill；
- receive response without declaring it governing。

Must Not:

- read repository broadly；
- receive G4 or G5；
- store credential in Packet or log；
- switch provider silently；
- retry outside scope；
- act as Project Owner or reviewer。

Current:

```text
NOT CREATED
NOT AUTHORIZED
NOT TESTED
```


### Response Binder

Must:

- bind response to request、Packet、asset SHA、reviewer、provider、model、scope and transport；
- distinguish PASS、FAIL、BLOCKED、LIMITED、PENDING and UNBOUND；
- reject stale and superseded response；
- preserve limitations。

Must Not:

- convert LIMITED to PASS；
- convert UNBOUND to FAIL；
- select favorable duplicate；
- accept asset。


### Review Reconciler

Must:

- compare internal and external evidence without merging provenance；
- detect substantive disagreement；
- route unresolved conflict to Human Review；
- preserve BLOCKED、LIMITED、PENDING and UNBOUND semantics。

Must Not:

- majority-vote；
- prefer same-family count；
- suppress blocker；
- create Owner decision。


### Review Ledger

Must:

- preserve append-only governance history；
- record identity、authorization status、classification、review provenance、response disposition、state changes and Owner decisions；
- distinguish current from historical；
- preserve manual-attested and connector-observed provenance。

Must Not:

- store G5；
- store unauthorized G4；
- store full prohibited prompt or attachment；
- silently overwrite history；
- produce acceptance。

The listed obligations are not a Ledger Schema.


### Decision Gate

Must:

- evaluate current authority；
- evaluate SHA integrity；
- evaluate data eligibility；
- evaluate internal and external status；
- evaluate disagreement、kill and revocation；
- emit protective status or `OWNER DECISION READY`。

Must Not:

- emit `PROJECT OWNER ACCEPTED`；
- waive external review；
- waive SHA or G-class；
- start downstream；
- treat Owner silence as decision。


### Human Review Router

Must:

- route exact-SHA disagreement；
- preserve original reviewer outputs；
- identify resolution authority；
- await human resolution。

Must Not:

- auto-select verdict；
- convert recommendation to acceptance；
- route around an active kill or revocation。


### Project Owner Decision Interface

Must:

- present exact asset and SHA；
- present current internal / external evidence separately；
- present blockers、limitations、disagreement and provenance；
- present no preselected positive decision；
- bind explicit Owner decision to scope and SHA。

Must Not:

- infer silence；
- hide protective states；
- create downstream authority from acceptance。


### Kill Switch

Authority Source:

```text
PROJECT OWNER ONLY
```

Activation Executor:

```text
PROJECT OWNER
OR
EXACT-SCOPE PROTECTIVE OPERATOR EXPLICITLY DELEGATED BY PROJECT OWNER
```

Re-Enable Authority:

```text
PROJECT OWNER ONLY — NON-DELEGABLE
```

Activation Effects:

- stop new dispatch；
- prevent retry；
- cancel eligible undispatched request or mark `PAUSED/BLOCKED BY KILL`；
- block in-flight response from current Decision Gate；
- preserve history；
- notify Project Owner。

`PAUSED/BLOCKED BY KILL`:

- is a protective Queue pause；
- is not `OWNER HOLD`；
- creates no Owner decision；
- cannot automatically resume。


## G0–G5 Runtime Data Governance

### Classification Composition

Mixed content inherits the highest applicable class.

UNKNOWN or disputed classification:

```text
EXTERNAL ELIGIBILITY:
BLOCKED
```


### G0 — Public / Non-Sensitive Governance

Potentially eligible only with applicable authorization.


### G1 — Internal Governance Without Real Matter

Potentially eligible only with valid per-asset or Standing Authorization.

Repository membership does not create transfer authority.


### G2 — Schema Without Instances

Potential eligibility requires:

- no instance；
- no real or simulated matter example；
- no credential；
- no hidden restricted identifier；
- exact SHA；
- explicit Schema transfer authority。


### G3 — Source Code / Operational Configuration

Default:

```text
EXTERNAL TRANSFER:
DENIED
```

Any future exception requires a separate exact-scope Project Owner decision plus Security and Privacy prerequisites.

No exception is authorized here.


### G4 — Real Matter / Evidence / PII / Privileged Material

```text
EXTERNAL PATH:
PROHIBITED

GENERAL STANDING AUTHORIZATION:
INELIGIBLE
```

No automated downgrade or redaction assumption is permitted.


### G5 — Credential / Secret

```text
PACKET:
PROHIBITED

PROMPT:
PROHIBITED

QUEUE / LEDGER CONTENT:
PROHIBITED

LOG / RESPONSE EVIDENCE / MODEL CONTEXT:
PROHIBITED
```


### Transfer Eligibility Matrix

| Class | Default External Eligibility | Additional Rule |
|---|---|---|
| G0 | Conditional | Applicable authorization required |
| G1 | Conditional | Per-asset or Standing authorization |
| G2 | Conditional | Explicit Schema transfer authority; no instances |
| G3 | Denied | Separate future exception and security gate |
| G4 | Prohibited | Not eligible for general Standing Authorization |
| G5 | Absolutely prohibited | Never enters content path |
| UNKNOWN / MIXED unresolved | Blocked | Human classification resolution required |


## API, Connector and Credential Isolation

### API Boundary

Future API design requires separate authorization.

This Spec defines no endpoint、method、payload、authentication scheme、rate limit、SDK or vendor client.


### Connector Scope

Any future Connector must be:

- project-scoped；
- provider-scoped；
- model-scoped；
- data-class-scoped；
- asset / action scoped；
- transfer-mode scoped；
- cost and retry scoped；
- revocable；
- observable；
- kill-switchable。


### Credential Boundary

Future credential governance must require:

- credential outside project assets and Packets；
- least privilege；
- provider and project scope；
- no plaintext log；
- no model-context exposure；
- rotation、expiry and revocation；
- audit without secret content；
- failure without secret disclosure。

Current:

```text
CREDENTIAL CREATION / STORAGE / USE:
NOT AUTHORIZED
```


### Provenance

Must distinguish:

```text
MANUAL — PROJECT OWNER ATTESTED
```

from:

```text
CONNECTOR — SYSTEM OBSERVED
```

Manual history cannot be relabeled as connector-observed evidence.


## External Review Outcome Governance

### Bound Outcome Requirements

A governing response must be conceptually bound to:

- exact asset SHA；
- exact request and Packet；
- reviewer identity and classification；
- provider and model；
- actual reviewed scope；
- transfer mode；
- outcome and limitations。

This list is not a response Schema.


### Unique Outcome Mapping

Outcome mapping uses mandatory first-match-wins order:

1. request cancellation；
2. binding / identity validity；
3. explicit reviewer verdict；
4. scope sufficiency only for PASS or explicit LIMITED。

| Response Condition | External Disposition | Governing Effect |
|---|---|---|
| Cancelled request | CANCELLED | Request ends; asset undecided |
| Missing/ambiguous/unidentifiable/unbindable identity or actual scope | UNBOUND | Integrity blocked; not reviewer FAIL |
| Bound explicit FAIL, any identifiable scope breadth | FAIL | Revision required, subject to disagreement routing |
| Bound explicit BLOCKED, any identifiable scope breadth | BLOCKED | Review could not validly proceed |
| Bound explicit PENDING, any identifiable scope breadth | PENDING | No governing outcome yet |
| Bound explicit LIMITED with identifiable actual scope | LIMITED | Scope completion required |
| Bound PASS with identifiable narrower scope | LIMITED | Scope completion required |
| Bound PASS with full required scope | PASS | Reconciliation eligible |

The branches are mutually exclusive. A narrow-scope FAIL、BLOCKED or PENDING remains FAIL、BLOCKED or PENDING; scope breadth is preserved as limitation evidence but does not replace the explicit verdict.


## Review Reconciliation and Human Review

### Reconciliation Priority

Global current governing status must first apply the `Unique Current Governing Status` priority. Reconciliation runs only if no active kill、withdrawal、stale / superseded、request cancellation or OWNER HOLD controls the exact profile.

Within that local reconciliation scope:

1. integrity mismatch / UNBOUND；
2. authorization or data blocker；
3. review BLOCKED；
4. substantive disagreement；
5. Internal FAIL or External FAIL branch；
6. LIMITED；
7. External PENDING；
8. Internal PENDING；
9. both PASS。

This local list produces axis evidence and Decision Gate input only; it cannot override global current governing priority.


### Reconciliation Matrix

| Internal | External | Integrity | Disagreement | Current Gate |
|---|---|---|---|---|
| Any | Any | MISMATCH / UNBOUND | Any | BLOCKED — INTEGRITY |
| BLOCKED | Any | MATCH | Any | BLOCKED — REVIEW |
| Any | BLOCKED | MATCH | Any | BLOCKED — REVIEW |
| PASS | FAIL | MATCH | DETECTED | HUMAN REVIEW REQUIRED |
| FAIL | PASS | MATCH | DETECTED | HUMAN REVIEW REQUIRED |
| FAIL | FAIL | MATCH | NONE | REVISION REQUIRED |
| FAIL | LIMITED | MATCH | NONE | REVISION REQUIRED — INTERNAL BLOCKER |
| FAIL | PENDING / UNAVAILABLE / QUOTA / MISSING | MATCH | NONE | REVISION REQUIRED — INTERNAL BLOCKER |
| PENDING / MISSING | FAIL | MATCH | NONE | REVISION REQUIRED — EXTERNAL BLOCKER |
| PASS | LIMITED | MATCH | NONE | SCOPE COMPLETION REQUIRED |
| PASS | PENDING / UNAVAILABLE / QUOTA | MATCH | NONE | PENDING — EXTERNAL |
| PENDING / MISSING | PASS | MATCH | NONE | INTERNAL REVIEW PENDING |
| PENDING / MISSING | LIMITED | MATCH | NONE | SCOPE COMPLETION REQUIRED |
| PENDING / MISSING | PENDING / MISSING | MATCH | NONE | INTERNAL / EXTERNAL REVIEW PENDING |
| PASS | CANCELLED | MATCH | NONE | NOT READY / REQUEST CANCELLED |
| PASS | PASS | MATCH | DETECTED | HUMAN REVIEW REQUIRED |
| PASS | PASS | MATCH | NONE | OWNER DECISION READY |


### Prohibited Tie-Breakers

No automated resolution by:

- majority；
- number of agents；
- model confidence；
- token count；
- response speed；
- cost；
- popularity；
- same-family third opinion；
- favorable outcome。


## Decision Gate Governance

### Pre-Owner Readiness Formula

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
NO ACTIVE BLOCKER
AND
NO ACTIVE KILL
=
OWNER DECISION READY
```


### Post-Owner Proceed Formula

```text
OWNER DECISION READY
AND
PROJECT OWNER ACCEPTED EXACT SHA
AND
SEPARATE NEXT-ACTION AUTHORIZATION VALID
=
MAY PROCEED ONLY WITHIN THAT NEXT-ACTION SCOPE
```

Acceptance alone does not authorize downstream.


### Owner Decision Matrix

| Readiness / State | Owner Decision | Governing State |
|---|---|---|
| Ready | ACCEPT exact SHA | ACCEPTED & SHA BOUND |
| Ready | REJECT exact SHA | REJECTED & SHA BOUND |
| Revision Required or Ready | AUTHORIZE LIMITED REVISION | REVISION AUTHORIZED — SCOPED |
| Any active review | REQUEST HUMAN REVIEW | HUMAN REVIEW REQUIRED |
| Any non-closed state | HOLD | OWNER HOLD |
| OWNER HOLD | RELEASE HOLD — exact SHA and request profile | HOLD RELEASED — REVALIDATION REQUIRED; full eligibility revalidation |
| Any current asset | WITHDRAW exact SHA | WITHDRAWN |
| Not ready | ACCEPT without exact SHA | REJECTED AS UNBOUND DECISION |
| Stale | Prior ACCEPT | STALE — RE-REVIEW REQUIRED |


## Fail-Closed Conditions

Any of the following blocks dispatch or Owner Decision Ready:

1. current action not authorized；
2. authorization scope incomplete；
3. neither valid per-asset nor valid Standing Authorization exists；
4. relied authorization expired、revoked、suspended or superseded；
5. asset identity outside scope；
6. SHA missing or mismatch；
7. Packet missing、unsealed、stale、cancelled or superseded；
8. data class unknown or mixed unresolved；
9. G4 detected；
10. G5 detected；
11. reviewer identity unknown；
12. provider or model unknown；
13. same-family reviewer labeled external；
14. transfer mode unauthorized；
15. quota、cost or retry boundary unknown；
16. duplicate active dispatch；
17. response unbound；
18. actual scope LIMITED；
19. Internal FAIL or BLOCKED；
20. External FAIL or BLOCKED；
21. external outcome PENDING；
22. disagreement unresolved；
23. Human Review unresolved；
24. Project Owner decision missing；
25. Owner decision SHA mismatch；
26. kill active；
27. OWNER HOLD active；
28. request cancelled；
29. asset withdrawn；
30. stale or superseded baseline；
31. attempted automatic acceptance；
32. attempted provider、model、cost or scope expansion；
33. attempted unauthorized asset transfer；
34. attempted unauthorized API、Connector、MCP、Code or Credential；
35. attempted Real Matter、Test、Runtime、Pilot、Implementation or Deployment。


## Revocation, Withdrawal and Recovery

### Authorization Revocation

Effect:

- new dispatch blocked；
- queued request cancelled or blocked；
- retry blocked；
- in-flight response non-governing pending disposition；
- history preserved。

Revocation does not erase prior history.


### Request Cancellation

Cancels only the exact current request profile.

It does not by itself withdraw or reject the asset.


### Asset Withdrawal

Requires Project Owner decision bound to exact asset SHA.

Effect:

```text
ASSET:
WITHDRAWN
```


### Supersession

New candidate SHA may supersede an older candidate only through explicit provenance.

Historical review remains visible but non-governing.


### Recovery

Recovery requires:

- cause resolved；
- authorization current；
- SHA current；
- Packet and Queue revalidated；
- reviewer and provider revalidated；
- data class current；
- quota and cost current；
- kill re-enable, if applicable；
- no stale response reuse。

Availability recovery alone never resumes work.

Owner Hold is not a technical recovery state:

```text
OWNER HOLD ACTIVE
+ NO NEW PROJECT OWNER DECISION
→ REMAIN OWNER HOLD
```

Only a new Project Owner decision bound to the exact asset SHA and request profile may release or redirect `OWNER HOLD`. After `RELEASE HOLD`, all recovery prerequisites above must be revalidated and the request returns to the earliest applicable eligibility or review stage; it never resumes from the prior pending step by default.


## Threat Review Preconditions

Future Threat Review requires separate authorization and must evaluate at least:

1. confused-deputy risk；
2. prompt injection；
3. indirect prompt injection；
4. data exfiltration；
5. credential and log leakage；
6. provider substitution；
7. model identity spoofing；
8. response replay；
9. stale SHA reuse；
10. Packet tampering；
11. Queue poisoning；
12. duplicate dispatch and retry amplification；
13. cost exhaustion and denial of service；
14. kill-switch bypass；
15. authorization and revocation race；
16. Ledger tampering；
17. Human Review bypass；
18. Owner decision spoofing；
19. deployment privilege escalation；
20. rollback failure；
21. dependency and supply-chain risk。

Current:

```text
THREAT REVIEW:
NOT AUTHORIZED
```


## Privacy Review Preconditions

Future Privacy Review requires separate authorization and must evaluate at least:

- data minimization；
- G-class correctness；
- PII detection；
- Real Matter isolation；
- retention and deletion；
- provider data use；
- cross-border transfer；
- prompt、response、log and metadata handling；
- model training opt-out boundary；
- operator access；
- manual transfer provenance；
- data subject impact；
- incident response；
- audit without content overcollection。

Current:

```text
PRIVACY REVIEW:
NOT AUTHORIZED
```


## Security Review Preconditions

Future Security Review requires separate authorization and must evaluate at least:

- credential storage、rotation and revocation；
- authentication and authorization enforcement；
- least privilege；
- network egress；
- provider and model allowlists；
- dependency integrity and code signing；
- secret scanning；
- audit integrity and tamper evidence；
- environment isolation and sandbox；
- incident kill、recovery and rollback；
- monitoring and alerting；
- data at rest and in transit；
- backup and access review；
- production change control。

Current:

```text
SECURITY REVIEW:
NOT AUTHORIZED
```


## Future Test and Validation Gates

### Separate Authorization Units

Each requires separate Project Owner authorization:

1. test plan；
2. test environment；
3. test data class；
4. provider sandbox；
5. credential scope；
6. cost ceiling；
7. network access；
8. destructive-test boundary；
9. evidence retention；
10. validation execution。


### Future Deterministic Test Domains

Potential domains:

- SHA mismatch；
- stale Packet；
- authorization expiry and revocation race；
- duplicate Queue request；
- retry ceiling；
- provider unavailable and quota exhausted；
- malformed or unbound response；
- LIMITED / UNBOUND separation；
- same-family misclassification；
- G4 / G5 detection；
- kill activation and in-flight response；
- cancellation / withdrawal separation；
- OWNER HOLD / kill pause separation；
- disagreement routing；
- no automatic acceptance or downstream；
- rollback history preservation。

This list is not a test plan, test case or test data.


### Validation Semantics

Future validation must distinguish:

```text
PASS
FAIL
BLOCKED
NOT RUN
PARTIAL
STALE
```

Validation PASS does not authorize Pilot or Deployment.


## Pilot, Deployment and Rollback Gates

### Future Sandbox Pilot Preconditions

- accepted Runtime Governance Spec and Result；
- accepted Threat / Privacy / Security Reviews；
- separately accepted component designs；
- Code authorization and review；
- test plan and test data authorization；
- validation evidence；
- connection test authorization and evidence；
- sandbox boundary；
- credential scope；
- cost ceiling；
- operational kill readiness；
- rollback plan；
- Project Owner Pilot authorization。


### Future Production Deployment Preconditions

- Pilot accepted；
- production-specific Security and Privacy confirmation；
- current accepted exact SHAs；
- production change control；
- monitoring and alerting；
- backup and incident response；
- rollback evidence；
- Project Owner Deployment authorization。


### Future Rollback Governance

Rollback must:

- stop new dispatch；
- preserve history；
- revoke unsafe version；
- restore only explicitly accepted version；
- revalidate credential、provider、Queue and Packet scope；
- block stale response reuse；
- require Project Owner decision for production re-enable。

This Spec creates no rollback tool.


## Future Authorization Sequence

```text
R0  Runtime Governance Handoff Materialized
R1  Handoff Review Authorized
R2  Handoff Reviewed
R3  Handoff Accepted
R4  Runtime Governance Design Spec Authorized
R5  Runtime Governance Design Spec Materialized
R6  Runtime Governance Design Spec Review Authorized
R7  Internal Design Review Completed
R8  External Design Review Authorized
R9  External Design Review Completed
R10 Runtime Governance Design Spec Accepted
R11 Runtime Governance Result Authorized
R12 Runtime Governance Result Materialized
R13 Runtime Governance Result Reviewed
R14 Runtime Governance Result Accepted
R15 Threat / Privacy / Security Reviews Authorized
R16 Component Handoffs and Designs Authorized
R17 Code and Test Authorization
R18 Connection Test and Sandbox Pilot Authorization
R19 Pilot Review and Acceptance
R20 Production Deployment Authorization
```

Current:

```text
R5 — RUNTIME GOVERNANCE DESIGN SPEC MATERIALIZED

R6–R20:
NOT AUTHORIZED
```


## Design Review Questions

If separately authorized, Design Review must evaluate at least:

1. Spec 是否仅物化唯一授权资产；
2. bound Runtime Governance Handoff SHA 是否匹配；
3. 三个 accepted Automation baseline SHA 是否匹配；
4. acceptance snapshot 是否保真且未回写 accepted assets；
5. normative precedence 是否明确且 Fail-Closed；
6. Spec 是否保持 Design Spec Only；
7. Project Owner 是否独占 Positive Authority；
8. Codex、Architecture Coordinator、External Consultant、Human Reviewer 和 operator 是否分离；
9. same-family internal 是否不能替代 Cross-Vendor external；
10. per-asset 与 Standing Authorization 是否作为 alternative authority paths；
11. 当前是否未授予 Standing Authorization；
12. revocation、expiry、suspension、supersession 和 kill 是否优先；
13. exact SHA change 是否使既有 Review 对新候选失效；
14. 多轴状态是否保留且未压缩为单一事实；
15. unique current governing status 是否具有唯一全局优先级，且 local reconciliation 不得覆盖 kill、OWNER HOLD 或其他全局控制；
16. Spec lifecycle 是否无自动升级；
17. conceptual Runtime lifecycle 是否具有完整 transition rules，尤其 OWNER HOLD 是否仅由 Owner 进入和解除并在解除后完整重验证；
18. Transition Matrix 是否保留 FAIL、BLOCKED、LIMITED、PENDING 和 UNBOUND；
19. Packet 是否保持 abstract 且不是 authority；
20. Queue 是否不能授权、扩权或自动恢复；
21. Connector 是否保持未创建、未授权且 provider/model scoped；
22. Credential 是否与 project asset、Packet、log 和 model context 隔离；
23. Response Binder 是否分离 LIMITED 与 UNBOUND；
24. External outcome 是否按 binding、explicit verdict 和 PASS-scope 顺序 first-match-wins，并保证唯一互斥映射；
25. Ledger 是否 append-only 且不能产生 acceptance；
26. Decision Gate 是否只产生 readiness 或 protective states；
27. Owner Interface 是否不预选 ACCEPT 或推定 silence；
28. substantive disagreement 是否必须进入 Human Review；
29. Human Review 是否不能直接产生 acceptance；
30. kill authority source、delegated executor 与 re-enable authority 是否分离；
31. kill pause 是否与 OWNER HOLD 分离且不自动恢复；
32. request cancellation 是否与 asset withdrawal 分离；
33. recovery 是否要求完整 revalidation；
34. G0–G5 composition 和 UNKNOWN fail-closed 是否完整；
35. G4 是否禁止进入 external path；
36. G5 是否绝对禁止进入任何 content path；
37. minimal disclosure 与 manual / connector provenance 是否保留；
38. Fail-Closed 是否覆盖 authority、integrity、data、review、availability and kill；
39. Threat Review 是否仅为未来前置条件；
40. Privacy Review 是否仅为未来前置条件；
41. Security Review 是否仅为未来前置条件；
42. test、validation、Pilot、Deployment 和 rollback 是否逐阶段分离；
43. 是否未创建 concrete Schema、Packet、Queue、Ledger、Gate 或 Connector；
44. 是否未创建 API、MCP、Code、Credential、Test Data、Runtime 或 Real Matter；
45. 是否未创建 Result、未启动 Review、未调用 external model、未自动授权 downstream。


## Design Spec Acceptance Gates

### MMCRG-DS-001 Authorization Fidelity

本次仅执行 Project Owner 已授权的 Runtime Governance Design Spec materialization。


### MMCRG-DS-002 Sole Artifact

唯一新资产必须是本 Spec。


### MMCRG-DS-003 Bound Handoff Integrity

Runtime Governance Handoff SHA 必须精确匹配。


### MMCRG-DS-004 Accepted Baseline Integrity

Automation Handoff、Spec 和 Result 三个 SHA 必须精确匹配。


### MMCRG-DS-005 Acceptance Snapshot Fidelity

状态快照必须保真且不得改写 accepted assets。


### MMCRG-DS-006 Normative Precedence

Project Owner current decision 和 accepted baselines 的优先级必须明确。


### MMCRG-DS-007 Design / Implementation Separation

本 Spec 不得成为 component、Schema、API、Code、Configuration 或 Runtime。


### MMCRG-DS-008 Four-Party Separation

Codex、Architecture Coordinator、External Consultant 和 Project Owner 必须保持分离。


### MMCRG-DS-009 Positive Authority

Project Owner 必须独占 Positive Authority。


### MMCRG-DS-010 Protective Operator Boundary

Protective operator 只能执行 exact delegated kill action，不能创造 authority 或 re-enable。


### MMCRG-DS-011 No Standing Authorization

本 Spec 不得授予 Standing External Review Authorization。


### MMCRG-DS-012 Alternative Authorization

有效 per-asset 或有效 Standing Authorization 均可成为未来 external authority；二者均无时阻断。


### MMCRG-DS-013 Revocation Dominance

Revocation、expiry、suspension、supersession 和 kill 必须优先。


### MMCRG-DS-014 Exact SHA Enforcement

Asset、Packet、response、Review、resolution 和 decision 必须 exact-bound。


### MMCRG-DS-015 Current / Historical Separation

历史证据不得作为新 SHA 的 current governing evidence。


### MMCRG-DS-016 Multi-Axis State Preservation

Authorization、integrity、data、review、disagreement、decision、kill 和 history 必须分离。


### MMCRG-DS-017 Unique Governing Status

每个 exact request profile 必须只导出一个 current governing status；global priority 必须覆盖 component-local reconciliation projection。


### MMCRG-DS-018 Transition Completeness

Lifecycle、transition rules 与 matrix 必须覆盖正常、失败、阻断、等待、kill、OWNER HOLD、解除重验证和撤回路径。


### MMCRG-DS-019 Packet Abstractness

Packet 仅为抽象治理契约，不定义 concrete field Schema。


### MMCRG-DS-020 Queue Is Not Authority

Queue 不得授权、扩权、选 provider、提高成本或恢复 cancelled work。


### MMCRG-DS-021 Connector Isolation

Connector 必须保持未创建、未授权且受 provider、model、data、cost 和 kill scope 约束。


### MMCRG-DS-022 Credential Isolation

Credential 不得进入 project asset、Packet、log 或 model context。


### MMCRG-DS-023 Response Binding

Response 必须可绑定 exact identity、scope and provenance。


### MMCRG-DS-024 External Outcome Fidelity

PASS、FAIL、BLOCKED、LIMITED、PENDING 和 UNBOUND 必须按 first-match-wins mapping 保持唯一且互不替代；narrow scope 不得覆盖明确 FAIL、BLOCKED 或 PENDING。


### MMCRG-DS-025 Ledger Boundary

Ledger 必须 append-only，且不得产生 acceptance。


### MMCRG-DS-026 Decision Gate Boundary

Decision Gate 只能产生 protective states 或 `OWNER DECISION READY`。


### MMCRG-DS-027 Owner Interface Neutrality

Owner Interface 不得预选 ACCEPT、推定 silence 或自动授权 downstream。


### MMCRG-DS-028 Human Review Preservation

实质分歧必须进入 Human Review，且 Human Review 不得直接接受资产。


### MMCRG-DS-029 Kill Authority Separation

Project Owner 必须是 activation authority 与 delegation 的唯一来源；re-enable authority 必须不可委托。


### MMCRG-DS-030 Kill Effect Fidelity

Kill 必须停止 dispatch、retry and Decision Gate progression，并保留历史。


### MMCRG-DS-031 No Silent Recovery

`PAUSED/BLOCKED BY KILL` 必须与 `OWNER HOLD` 分离，且任何恢复必须重新验证。


### MMCRG-DS-032 G0–G5 Classification

最高等级组合与 UNKNOWN / MIXED Fail-Closed 必须明确。


### MMCRG-DS-033 G4 Exclusion

G4 必须禁止进入 external path。


### MMCRG-DS-034 G5 Absolute Prohibition

G5 必须禁止进入所有 collaboration content paths。


### MMCRG-DS-035 Minimal Disclosure and Provenance

Minimal disclosure 及 manual / connector provenance 必须保留。


### MMCRG-DS-036 Fail-Closed Completeness

Authority、identity、data、review、availability、kill and downstream 风险必须阻断。


### MMCRG-DS-037 Threat Preconditions

Threat Review 仅可作为未来单独授权前置条件。


### MMCRG-DS-038 Privacy Preconditions

Privacy Review 仅可作为未来单独授权前置条件。


### MMCRG-DS-039 Security Preconditions

Security Review 仅可作为未来单独授权前置条件。


### MMCRG-DS-040 Test Boundary

Test domains 与 validation semantics 不得成为 test plan、test data 或 execution。


### MMCRG-DS-041 Pilot / Deployment Separation

Validation、Pilot、Deployment and rollback 必须逐阶段单独授权。


### MMCRG-DS-042 No Concrete Components

不得创建 Packet、Queue、Ledger、Gate、Connector、Resolver、Verifier、Classifier、Binder、Router、Interface 或 Kill Switch。


### MMCRG-DS-043 No API / Code / Credential

不得创建 API、MCP、Webhook、Agent、Skill、Script、Code、Configuration 或 Credential。


### MMCRG-DS-044 No Data / Runtime / Real Matter

不得创建 instance、example、test data、Runtime 或处理 Real Matter。


### MMCRG-DS-045 No Result / Review / Escalation

不得创建 Result、启动 Design Review、调用 external model、传输资产或自动授权 downstream。


## Authorized Scope

本次仅允许：

1. 创建本 Runtime Governance Design Spec；
2. 绑定 accepted Runtime Governance Handoff；
3. 继承 accepted Automation baselines；
4. 定义角色和 authority matrix；
5. 定义 conceptual multi-axis states；
6. 定义 governance lifecycle、transitions and matrices；
7. 定义 abstract component contracts；
8. 定义 G0–G5、external and credential isolation；
9. 定义 Human Review、kill、revocation and recovery；
10. 定义 future Threat、Privacy、Security、Test、Pilot、Deployment and rollback gates；
11. 定义 Review Questions and Acceptance Gates；
12. 计算 candidate SHA and report。


## Not Authorized

以下行为均未获授权：

1. 启动本 Spec Design Review；
2. 调用 Architecture Coordinator 对本 Spec Review；
3. 调用 Gemini 或其他 External Model；
4. 传输项目资产；
5. 创建 Runtime Governance Result；
6. 授予 Standing Authorization；
7. 创建 Standing Authorization Policy；
8. 创建 Packet 或 Packet Schema；
9. 创建 Queue；
10. 创建 Ledger；
11. 创建 Decision Gate；
12. 创建 Authorization Resolver；
13. 创建 Integrity Verifier；
14. 创建 Data Classifier；
15. 创建 Response Binder or Reconciler；
16. 创建 Human Review Router；
17. 创建 Project Owner Interface；
18. 创建 Kill Switch；
19. 创建 API；
20. 创建 Connector；
21. 创建 MCP or Webhook；
22. 创建 Agent or Skill；
23. 创建 Script or Source Code；
24. 创建 executable configuration；
25. 创建、存储或使用 Credential；
26. 定义 concrete field Schema；
27. 创建 instance、example or sample；
28. 创建 test plan；
29. 创建 test case or test data；
30. 执行 validation or connection test；
31. 执行 Threat Review；
32. 执行 Privacy Review；
33. 执行 Security Review；
34. 导入 Real Matter；
35. 处理 Evidence、PII or privileged material；
36. 创建 Runtime；
37. 启动 Pilot；
38. 启动 Implementation；
39. 执行 Deployment；
40. 创建 rollback tool；
41. 自动接受本 Spec；
42. 自动启动 downstream。


## Artifact Boundary

Authorized New Asset:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_RUNTIME_GOVERNANCE_SPEC.md
```

Bound Read-Only Assets:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_RUNTIME_GOVERNANCE_HANDOFF.md
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_HANDOFF.md
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_SPEC.md
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_RESULT.md
```

Explicitly Not Created:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_RUNTIME_GOVERNANCE_RESULT.md
Standing Authorization Policy
Review Packet
Packet Schema
Review Queue
Review Ledger
Decision Gate
Authorization Resolver
Integrity Verifier
Data Classifier
External Connector
Response Binder
Review Reconciler
Human Review Router
Project Owner Interface
Kill Switch
API
MCP
Webhook
Agent
Skill
Script
Code
Executable Configuration
Credential
Test Plan
Test Data
Runtime
Pilot
Deployment
Rollback Tool
```


## Current System State

```text
Runtime Governance Handoff:
ACCEPTED & SHA BOUND

Runtime Governance Design Spec:
MATERIALIZED — DESIGN REVIEW NOT AUTHORIZED

Runtime Governance Design Result:
NOT CREATED / NOT AUTHORIZED

Standing External Review Authorization:
NOT GRANTED

External Invocation / Asset Transfer:
NOT AUTHORIZED

Packet / Queue / Ledger / Decision Gate:
NOT CREATED / NOT AUTHORIZED

API / Connector / MCP / Code / Credential:
NOT CREATED / NOT AUTHORIZED

Threat / Privacy / Security Review:
NOT AUTHORIZED

Test Plan / Test Data / Validation:
NOT AUTHORIZED

Runtime / Pilot / Implementation / Deployment:
NOT AUTHORIZED

Real Matter:
NOT AUTHORIZED

Automatic State Transition:
BLOCKED
```


## Review Submission

Review Object:

```text
TASK_ACOS_MULTI_MODEL_COLLABORATION_AUTOMATION_RUNTIME_GOVERNANCE_SPEC.md
```

Proposed Internal Reviewer:

```text
Architecture Coordinator
```

Current Review Authority:

```text
NOT GRANTED
```

Future Review Mode:

```text
READ-ONLY
FIXED-SHA
45 QUESTIONS
45 ACCEPTANCE GATES
```

Future Review must not:

- edit this Spec；
- edit accepted baselines；
- invoke external model；
- transfer project assets；
- create Result；
- create component or concrete Schema；
- create API、Code or Credential；
- create test data；
- start Runtime、Pilot、Implementation or Deployment；
- accept this Spec；
- activate downstream。


## Next Authorized Action

当前不存在自动获准的下一动作。

本 Spec 物化后必须停留在：

```text
RUNTIME GOVERNANCE DESIGN SPEC MATERIALIZED
DESIGN REVIEW NOT AUTHORIZED
EXTERNAL REVIEW NOT AUTHORIZED
RESULT NOT AUTHORIZED
COMPONENTS NOT AUTHORIZED
API / CONNECTOR / CODE / CREDENTIAL NOT AUTHORIZED
TEST / RUNTIME / IMPLEMENTATION / DEPLOYMENT NOT AUTHORIZED
```

任何 Design Review、limited revision、external review、acceptance、Result 或 downstream action 均需 Project Owner 单独决定。
