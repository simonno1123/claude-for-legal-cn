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

### 1.1 CASE-A: Muxi Shoes (C02-CASE-A-001)
- **Matter Name**: 沐希鞋业买卖合同纠纷
- **Total Scanned Files**: 2 unique files

| Material Name | Path | Type | SHA-256 | Access Scope | Validation Boundary | Status |
|---|---|---|---|---|---|---|
| Muxi Bill (10-12) | `C:\Users\Administrator\WPSDrive\729282343\WPS云文档\wps个人云文档\私有\法律案件\沐希鞋业合同案\沐希10-12月账单.xls` | `XLS` | `6B1E5ED87165576847EEBC67B50E048FBC7F8C2FD708172C492BEFBD5F526082` | `CASE_ONLY` | `READ_ONLY / STRUCTURE_FACTS` | `BOUND` |
| Muxi Company Report | `C:\Users\Administrator\Documents\xwechat_files\simonno1123_a85c\msg\file\2026-06\温州沐希鞋业有限公司报告.pdf` | `PDF` | `8A654E4F136240496AE0EC3602CC1A7099CB546C3B6BD4AFFEDD0C90A5A2A898` | `CASE_ONLY` | `READ_ONLY / STRUCTURE_FACTS` | `BOUND` |
| WeChat chat logs | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ` | `MISSING` |
| Payment vouchers | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ` | `MISSING` |

- **Validation Status**: **BLOCKED** (Missing core interactive WeChat evidence and payment vouchers).

### 1.2 CASE-B: Subofang (C02-CASE-B-001)
- **Matter Name**: 塑博坊人格否认责任
- **Total Scanned Files**: 13 unique files

| Material Name | Path | Type | SHA-256 | Access Scope | Validation Boundary | Status |
|---|---|---|---|---|---|---|
| Court Judgment | `C:\Users\Administrator\WPSDrive\729282343\WPS云文档\wps个人云文档\私有\法律案件\塑博坊案\浙江塑博坊判决书.pdf` | `PDF` | `FE0636347235BF3EBC800032BB075B2CC62F486279796FA6AB66A6EE5B412EA2` | `CASE_ONLY` | `READ_ONLY / STRUCTURE_FACTS` | `BOUND` |
| Bank Flow Records | `C:\Users\Administrator\WPSDrive\729282343\WPS云文档\wps个人云文档\私有\法律案件\塑博坊案\资金流流水.xlsx` | `XLSX` | `85ACDB7FEC78A4FCB195844F229C470A8927B4B52698278B7CE501B7D52A8833` | `CASE_ONLY` | `READ_ONLY / STRUCTURE_FACTS` | `BOUND` |
| Corporate records (x11) | `C:\Users\Administrator\WPSDrive\729282343\WPS云文档\wps个人云文档\私有\法律案件\塑博坊案\工商调档资料\` | `PDF/IMG` | *Bound Multiple* | `CASE_ONLY` | `READ_ONLY` | `BOUND` |

- **Validation Status**: **BLOCKED** (OCR unavailable; 80 files lack verified text layers).

### 1.3 CASE-C: Zhang Chengqi (C02-CASE-C-001)
- **Matter Name**: 张成棋执行衍生案件
- **Total Scanned Files**: 1 unique file

| Material Name | Path | Type | SHA-256 | Access Scope | Validation Boundary | Status |
|---|---|---|---|---|---|---|
| Kangerda Fee Details | `C:\Users\Administrator\WPSDrive\729282343\WPS云文档\wps个人云文档\私有\法律案件\康尔达系列案\康尔达系列案件费用明细.xlsx` | `XLSX` | `0A984697AA7B1EAA4157F8C8CF84B0E114AA7097118E0054023337BC2163764B` | `CASE_ONLY` | `READ_ONLY / STRUCTURE_FACTS` | `BOUND` |
| Property registration | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ` | `MISSING` |
| Enforcement logs | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ` | `MISSING` |
| Derivative lawsuit docs | `NOT_FOUND` | `UNKNOWN` | `NOT_AVAILABLE` | `NONE` | `NO_READ` | `MISSING` |

- **Validation Status**: **BLOCKED** (Missing primary property registration and enforcement records).

---

## 2. Input Boundary Compliance

As per AC-C02-IMPORT-003, validation execution remains blocked due to the missing required records and unverified OCR text gaps. No mock facts or virtual case documents have been synthesized.
