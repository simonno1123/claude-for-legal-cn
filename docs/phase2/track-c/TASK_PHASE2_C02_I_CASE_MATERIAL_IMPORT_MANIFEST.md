# TASK_PHASE2_C02_I_CASE_MATERIAL_IMPORT_MANIFEST

## 0. Document Control

| Field | Value |
|---|---|
| Track | Phase 2 / Track C / TASK_PHASE2_C02 |
| Stage | C02-I — Case Material Import and Binding |
| Status | **COMPLETED WITH GAPS (BLOCKED)** |
| Verification Date | 2026-07-20 |
| Reference Handoff SHA-256 | `1EF6F7B8E820F0507546BAF0623BCECEA8CF30A2FE63EA928E6D3D010AADF7E9` |

This document catalogs the verified physical files located on the system during the import scan. Gaps in necessary materials remain, and validation execution remains **BLOCKED**.

---

## 1. Case Material Inventory

### 1.1 CASE-A: CASE-A party (C02-CASE-A-001)
- **Matter Name**: CASE-A 买卖合同纠纷
- **Total Scanned Files**: 2 unique files

| Material Name | Path | Type | SHA-256 | Access Scope | Validation Boundary | Status |
|---|---|---|---|---|---|---|
| CASE-A Bill (10-12) | `<OWNER-CLOUD-DOCS>\CASE-A\[A-D01 文件].xls` | `XLS` | `6B1E5ED87165576847EEBC67B50E048FBC7F8C2FD708172C492BEFBD5F526082` | `CASE_ONLY` | `READ_ONLY / STRUCTURE_FACTS` | `BOUND` |
| CASE-A Company Report | `<OWNER-IM-FILES>\[A-D02 文件].pdf` | `PDF` | `8A654E4F136240496AE0EC3602CC1A7099CB546C3B6BD4AFFEDD0C90A5A2A898` | `CASE_ONLY` | `READ_ONLY / STRUCTURE_FACTS` | `BOUND` |
| WeChat chat logs | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ` | `MISSING` |
| Payment vouchers | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ` | `MISSING` |

- **Validation Status**: **BLOCKED** (Missing core interactive WeChat evidence and payment vouchers).

### 1.2 CASE-B: CASE-B party (C02-CASE-B-001)
- **Matter Name**: CASE-B 人格否认责任
- **Total Scanned Files**: 13 unique files

| Material Name | Path | Type | SHA-256 | Access Scope | Validation Boundary | Status |
|---|---|---|---|---|---|---|
| Court Judgment | `<OWNER-CLOUD-DOCS>\CASE-B\[B-D01 文件].pdf` | `PDF` | `FE0636347235BF3EBC800032BB075B2CC62F486279796FA6AB66A6EE5B412EA2` | `CASE_ONLY` | `READ_ONLY / STRUCTURE_FACTS` | `BOUND` |
| Bank Flow Records | `<OWNER-CLOUD-DOCS>\CASE-B\[B-D02 文件].xlsx` | `XLSX` | `85ACDB7FEC78A4FCB195844F229C470A8927B4B52698278B7CE501B7D52A8833` | `CASE_ONLY` | `READ_ONLY / STRUCTURE_FACTS` | `BOUND` |
| Corporate records (x11) | `<OWNER-CLOUD-DOCS>\CASE-B\[B-D03 目录]\` | `PDF/IMG` | *Bound Multiple* | `CASE_ONLY` | `READ_ONLY` | `BOUND` |

- **Validation Status**: **BLOCKED** (OCR unavailable; 80 files lack verified text layers).

### 1.3 CASE-C: CASE-C frozen-label party (C02-CASE-C-001)
- **Matter Name**: CASE-C 冻结标签执行衍生案件
- **Total Scanned Files**: 1 unique file

| Material Name | Path | Type | SHA-256 | Access Scope | Validation Boundary | Status |
|---|---|---|---|---|---|---|
| CASE-C current-label Fee Details | `<OWNER-CLOUD-DOCS>\CASE-C\[C-D01 文件].xlsx` | `XLSX` | `0A984697AA7B1EAA4157F8C8CF84B0E114AA7097118E0054023337BC2163764B` | `CASE_ONLY` | `READ_ONLY / STRUCTURE_FACTS` | `BOUND` |
| Property registration | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ` | `MISSING` |
| Enforcement logs | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ` | `MISSING` |
| Derivative lawsuit docs | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ` | `MISSING` |

- **Validation Status**: **BLOCKED** (Missing primary property registration and enforcement records).

---

## 2. Input Boundary Compliance

As per AC-C02-IMPORT-003, validation execution remains blocked due to the missing required records and unverified OCR text gaps. No mock facts or virtual case documents have been synthesized.
