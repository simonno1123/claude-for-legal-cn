# TASK_PHASE3_TRACK_A_FACT_CONSTRUCTION_GOVERNANCE_HANDOFF

## Status

MATERIALIZED — PENDING ARCHITECTURE REVIEW


## Phase Identification

Phase:
PHASE 3

Track:
Track A

Name:
FACT CONSTRUCTION GOVERNANCE


## Objective

建立法律 AI 系统中的事实构建治理层。

本阶段目标不是进行案件分析，而是建立从证据到事实、从事实到法律事实的受控转换机制。


## Architectural Position

本阶段位于：

Evidence Governance Layer

与

Request Right Engine

之间。


Architecture:

Evidence
    |
    v
Fact Construction Governance
    |
    v
Legal Fact Layer
    |
    v
Request Right Foundation


## Relationship With Previous Phase

Phase 2 Track C:

Evidence Governance
- 
Execution Boundary Control


Phase 3 Track A:

Fact Construction Governance


Phase 2 负责保证：

"输入真实"

Phase 3 Track A 负责保证：

"事实形成过程可验证"


## Core Principles


### FC-G-001 Evidence ≠ Fact

原始证据不得直接等同于事实。

任何事实必须具有：

- 来源证据；
- 形成过程；
- 验证状态；
- 争议状态。


### FC-G-002 Fact ≠ Legal Fact

客观事件与法律评价必须分离。

禁止：

事实层直接生成法律结论。


### FC-G-003 Fact Traceability

任何事实必须可以追溯：

Fact

↓

Evidence Source

↓

Human Verification


### FC-G-004 Dispute Preservation

争议事实不得被模型自动消除。

事实状态必须支持：

- Confirmed
- Disputed
- Unknown


### FC-G-005 Human Validation Gate

涉及法律事实形成的关键节点必须保留人工确认。


## Authorized Scope

本 Handoff 仅授权：

1. Architecture Review
2. Fact Construction Governance Design Preparation


## Not Authorized


以下行为禁止：

- 创建 Fact Schema；
- 修改 Evidence Registry；
- 导入真实案件材料；
- 自动提取案件事实；
- 生成法律关系判断；
- 生成请求权基础；
- 生成诉讼策略。


## Expected Future Artifacts

经授权后，仅允许创建：

TASK_PHASE3_TRACK_A_FACT_CONSTRUCTION_GOVERNANCE_SPEC.md

TASK_PHASE3_TRACK_A_FACT_CONSTRUCTION_GOVERNANCE_RESULT.md


## Acceptance Gates


FC-H-001:
Phase 3 Boundary Confirmation


FC-H-002:
Evidence / Fact Separation


FC-H-003:
Fact / Legal Fact Separation


FC-H-004:
No Automatic Legal Reasoning


FC-H-005:
Human Validation Preservation


FC-H-006:
No Real Matter Pollution


## Current System State


Phase 2 Track C:

FINAL CLOSED & ARCHIVED


Phase 3 Track A:

FACT CONSTRUCTION GOVERNANCE

Status:

HANDOFF MATERIALIZATION PENDING REVIEW


Fact Construction Design:

NOT STARTED


Request Right Foundation:

NOT STARTED


Legal Reasoning:

NOT AUTHORIZED
