# TASK_PHASE2_C02_III_REQUEST_RIGHT_VALIDATION_ENHANCEMENT_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Validation Enhancement Handoff

GOVERNANCE LAYER: Task Authorization Request

TARGET MODULE: `litigation-legal` / Request Right Validation

---

## 1. Task Purpose

本 Handoff 用于授权启动：
`C02-III Request Right Validation Enhancement`

目标是开展请求权基础验证增强阶段：
- 采用 C02-II 中设计的请求权要素体系框架对真实案件输入进行增强验证；
- 建立并固化包含访问和 OCR 解析状态的文件清单库（Case Material Registry）；
- 基于要件缺口映射（Evidence Gap Validation）而非脑补来判定事实和证明责任。

本阶段为 **只读增强验证**，不授权修改任何既有代码或 Skill。

---

## 2. Governance Position

```text
C02-II Request Right Framework Design (CLOSED / DONE)
        ↓
C02-III Validation Enhancement (This Task, AUTHORIZED)
        ↓
C03 Enforcement Strategy Layer (NOT AUTHORIZED)
```

No file under `litigation-legal/` may be created or modified.

---

## 3. Fixed Baseline Inputs

Before execution, the executor must verify:

### 3.1 C02-II Design Spec
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_SPEC.md`
- Required SHA-256: `BB4C2A1B8977A99EB46E4854BDDCF7F4B6759523F6E926654BED365F71C55FE1`

### 3.2 C02-II Design Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_RESULT.md`
- Required SHA-256: `3BCE75F664CECB079AACBBAB622F71915DEAF15DC81B335CB8E1BBE51FC2B047`

---

## 4. Enhancement Validation Scope and Rules

- **Allowed**: Map elements and verify gaps for located materials under Muxi, Subofang, and Zhang Chengqi cases; construct the Case Material Registry; log OCR layer verified states.
- **Prohibited**: Editing Skill prompts, Agents, or code under `litigation-legal/`; generating final win rates, strategy choices, or merits predictions.

---

## 5. Authorized Outputs

The executor is authorized to create exactly **2 files**:

### Output A: Request-Right Validation Enhancement Spec
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_III_REQUEST_RIGHT_VALIDATION_ENHANCEMENT_SPEC.md`

### Output B: Execution Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C02_III_REQUEST_RIGHT_VALIDATION_ENHANCEMENT_RESULT.md`

---

## 6. Acceptance Criteria

- **AC-C02-III-001**: Registry verifies document hashes and OCR statuses.
- **AC-C02-III-002**: Traces the elements-evidence mapping.
- **AC-C02-III-003**: Structures gaps based on element prerequisites.
- **AC-C02-III-004**: Prohibit win predictions or automated merits evaluation.
- **AC-C02-III-005**: Zero prompt changes or code regressions under `litigation-legal/`.
- **AC-C02-III-006**: `git diff --check` passes and staging remains empty.
