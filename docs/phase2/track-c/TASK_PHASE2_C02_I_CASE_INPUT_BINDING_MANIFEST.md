# TASK_PHASE2_C02_I_CASE_INPUT_BINDING_MANIFEST

## 0. Document Control

| Field | Value |
|---|---|
| Track | Phase 2 / Track C / TASK_PHASE2_C02 |
| Stage | C02-I — Case Input Binding and Manifesting |
| Status | **COMPLETED WITH GAPS (BLOCKED)** |
| Verification Date | 2026-07-20 |
| Reference Handoff SHA-256 | `3007CDC928D2B30A3A76169079094D82D4EA8F9828D643BB962D666D4CD3D16B` |

This document serves as the formal Input Binding Manifest. The workspace was thoroughly audited to catalog raw materials for the three validation cases.

Due to the absence of physical documents in the workspace, all cases are marked as **MISSING**, and the validation execution remains blocked.

---

## 1. Case Input Inventory

All fields below are explicit. `NOT_FOUND` means no authorized workspace path exists; `UNKNOWN` means no file type can be identified; `NOT_AVAILABLE` means no file exists from which a SHA-256 can be computed; and `NONE` means no material is authorized for reading.

### 1.1 CASE-A: Muxi Shoes (C02-CASE-A-001)

- **Matter Name**: 沐希鞋业买卖合同纠纷
- **Status**: **MISSING / NOT FOUND**

| Material Name | Path | Type | SHA-256 | Access Scope | Validation Boundary | Status |
|---|---|---|---|---|---|---|
| Raw contract | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |
| Correspondence / WeChat files | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |
| Billing statements | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |
| Payment vouchers | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |

- **Material Count**: `4 required / 4 missing / 0 bound`
- **Validation Execution Status**: **BLOCKED**.

### 1.2 CASE-B: Subofang (C02-CASE-B-001)

- **Matter Name**: 塑博坊人格否认责任
- **Status**: **MISSING / NOT FOUND**

| Material Name | Path | Type | SHA-256 | Access Scope | Validation Boundary | Status |
|---|---|---|---|---|---|---|
| Judicial decisions | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |
| Corporate registration records | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |
| Shareholder lists | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |
| Financial-flow records | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |
| Enforcement documents | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |

- **Material Count**: `5 required / 5 missing / 0 bound`
- **Validation Execution Status**: **BLOCKED**.

### 1.3 CASE-C: Zhang Chengqi (C02-CASE-C-001)

- **Matter Name**: 张成棋执行衍生案件
- **Status**: **MISSING / NOT FOUND**

| Material Name | Path | Type | SHA-256 | Access Scope | Validation Boundary | Status |
|---|---|---|---|---|---|---|
| Enforcement documents | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |
| Asset-tracking clues | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |
| Property records | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |
| Derivative-litigation materials | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ / NO_FACT_EXTRACTION / NO_REQUEST_RIGHT_ANALYSIS` | `MISSING` |

- **Material Count**: `4 required / 4 missing / 0 bound`
- **Validation Execution Status**: **BLOCKED**.

---

## 2. Input Boundary Compliance

As per AC-C02-BIND-003, no mock facts or virtual case documents have been synthesized to compensate for the missing assets. The analytical framework will remain blocked until the physical source materials are provided in the workspace.

## 3. Correction Control

| Field | Value |
|---|---|
| Correction Handoff | `.codex-coordination/inbox/TASK_PHASE2_C02_I_CASE_INPUT_BINDING_CORRECTION_HANDOFF.md` |
| Correction Handoff SHA-256 | `1658D71C493CDA6A2AC7D7144A02D33DFE89EF260D8D02C184F651C512D9D6DD` |
| Corrected counts | `CASE-A 4 / CASE-B 5 / CASE-C 4` |
| Validation execution | `BLOCKED` |
