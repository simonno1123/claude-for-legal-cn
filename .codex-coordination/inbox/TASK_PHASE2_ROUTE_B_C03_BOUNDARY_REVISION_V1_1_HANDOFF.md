# TASK_PHASE2_ROUTE_B_C03_BOUNDARY_REVISION_V1_1_HANDOFF（范围交接，待确认）

| 字段 | 值 |
| --- | --- |
| 依据 | 所有者 2026-11-23 对 C03 可实现性的讨论，选择"先议边界"，并决定把 A 措施与期限、B 财产调查途径、C 变更追加当事人、D 异议与救济途径四项，参照 C01 的做法放开为"可供律师考虑的……（候选）" |
| 起草 | Claude（记录人），2026-11-23 |
| 状态 | **待所有者确认** |

## 〇、目的

C03 现在只出五类候选（争点矩阵、不利条件登记、冲突与缺口登记、依据核查请求、复核包）。执行实务中最常用的四类事项，因为落在禁止类别里，连"候选"都不能列。本次修订把这四项放开为**只列法定前提和所缺材料的候选**：不排先后，不提建议，不下结论。其余禁止类别不变。

本交接只改规格和经验文件，**不写技能、不写代码**。技能另行立项。

## 一、固定基线

| 文件 | 改动前 SHA-256 |
| --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_ENFORCEMENT_ADVERSARIAL_DOMAIN_PROFILE_SPEC.md` | `35C3F7E905D2D171301114C6AAF28DF4BCCC2609ADF528A466EC3661D4F44559` |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_ENFORCEMENT_MODULE_LESSONS_AND_AUTHORITY_CATALOG.md` | `4C77F434D3A10F6E1E7DC37DF1E031534E5307EFA735E248B70872E49F0A8332` |

## 二、授权范围（规格文件）

### 包 B1：版本

文档控制表中 Version 由 `v1.0` 改为 `v1.1`；表后增加一行说明：

> v1.1 (2026-11-23): Project Owner opened four record-bound lawyer-consideration candidate types (Section 10.1A). All other boundaries unchanged.

### 包 B2：第 4 节 permitted_operations

在 `RECORD_CONFLICTS_AND_INFORMATION_GAPS` 之后增加一行：

```yaml
    - ENUMERATE_RECORD_BOUND_LAWYER_CONSIDERATION_CANDIDATES
```

`prohibited_operations` 不变。

### 包 B3：第 7 节维度表

D02、D07、D08 三行的 "Required boundary" 列末尾，各加：`; except a Section 10.1A candidate`。

D06 一行末尾加：`; a Section 10.1A candidate may name statutory investigation tools only, and no search is performed`（D06 的"不主动查找"本身不放开）。

### 包 B4：新增第 10.1A 节（放在 10.1 与 10.2 之间）

```markdown
### 10.1A Record-Bound Lawyer-Consideration Candidates (v1.1)

Four additional candidate types are permitted. Each is a list of matters a
qualified lawyer may consider, bound to the record and to checked authorities:

    C03_MEASURE_AND_DEADLINE_CONSIDERATION_CANDIDATE          （A 可供律师考虑的措施与期限事项）
    C03_ASSET_INVESTIGATION_PATHWAY_CONSIDERATION_CANDIDATE   （B 可供律师考虑的财产调查途径）
    C03_PARTY_CHANGE_GROUND_CONSIDERATION_CANDIDATE           （C 可供律师考虑的变更追加当事人情形）
    C03_OBJECTION_AND_REMEDY_PATHWAY_CONSIDERATION_CANDIDATE  （D 可供律师考虑的异议与救济途径）

Scope of each type:

- A: for each recorded measure, its recorded scope, term, expiry and
  continuation requirement; for each statutory measure category not yet
  recorded as taken, the statutory preconditions.
- B: statutory investigation tools (such as investigation orders and the
  categories of institutions they may address, property-report orders, reward
  notices, audits) and their conditions. No search is performed.
- C: the statutory grounds in the applicable rules that recorded facts may
  touch, and the materials needed to establish each ground.
- D: the procedural remedies that may be available, with their time limits and
  preconditions.

Every item in these four types must:

1. cite only authorities whose status in the matter's authority freshness
   packet is "checked" or "lawyer-confirmed" and current; otherwise the item
   reads "authority not checked" and is blocked from use;
2. compare each statutory precondition with the record and mark it
   "present in record", "contradicted by record", or "no record", citing the
   record location;
3. list the materials missing for each precondition;
4. state time limits only as computed from recorded dates and checked
   authorities, showing the computation, and mark them [lawyer review];
5. not rank, order, time, prioritise, or recommend any item, and not use
   words of recommendation;
6. not state whether any measure, ground, or remedy would succeed, should be
   pursued, or is likely to be granted;
7. not perform, describe how to perform, or suggest any search of persons,
   assets, accounts, or third parties beyond naming the statutory tool; and
8. carry the four labels required by Section 10.1.

An item that violates any of rules 5 to 7 is reclassified under Section 10.2
and must be blocked.
```

### 包 B5：第 10.2 节末尾增加一段

```markdown
The categories above remain prohibited. A Section 10.1A candidate is not an
`ENFORCEMENT_STRATEGY_OR_TACTIC`, `ASSET_SEARCH_OR_TRACING_INSTRUCTION`,
`ADDITIONAL_PARTY_OR_LIABILITY_CONCLUSION`, or `OBJECTION_OR_REMEDY_CONCLUSION`
only while it complies with every rule in Section 10.1A.
```

### 包 B6：第 16 节验收门增加一行

| `C03-DG-016` — Consideration-Candidate Boundary | Section 10.1A items are record-bound and authority-checked, and contain no ranking, recommendation, timing, success assessment, or search |

## 三、授权范围（经验文件）

第六节第二点：

> - 维持现有边界：C03 只出五类候选（争点矩阵、不利条件登记、冲突与缺口登记、依据核查请求、复核包）。策略、文书、财产查找、追加当事人结论、救济结论都不在 C03 内产生。

改为：

> - 边界（规格 v1.1）：C03 出五类候选（争点矩阵、不利条件登记、冲突与缺口登记、依据核查请求、复核包），另有第 10.1A 节四类"可供律师考虑的……（候选）"（措施与期限、财产调查途径、变更追加当事人情形、异议与救济途径），只列法定前提、卷内对照和所缺材料。策略、文书、实际查找财产、追加当事人结论、救济结论、结果预测仍不在 C03 内产生。

第六节第三点"建议在操作说明中加一条：记录人提议下一份输出时，先对照第 10.1 节的允许类别"中的"第 10.1 节"，改为"第 10.1 节和第 10.1A 节"。

### 不授权

- 以上所列以外的任何改动；
- 写 C03 技能或任何代码；
- 改动 C01 技能；
- 处理任何真实案件材料。

## 四、验证（静态）

| 编号 | 输入（虚构） | 应有表现 |
| --- | --- | --- |
| B01 | 卷内记录某查封措施及到期日 | A 类列出到期日和续行要求，期限算式可见，标 `[lawyer review]`；不写"应及时续封" |
| B02 | 卷内无限制消费的记录 | A 类列出该措施类别及法定前提，逐项标"present / contradicted / no record" |
| B03 | 候选写"建议先申请调查令，再申请悬赏" | 违反第 5 条，按第 10.2 节阻断 |
| B04 | B 类列出调查令可指向的机构类别 | 符合；若写明具体查询步骤或检索某人账户，违反第 7 条，阻断 |
| B05 | C 类：卷内有股东出资未到位的线索 | 列出可能涉及的法定情形和所缺材料；不写"可以追加" |
| B06 | D 类：列出执行异议及期限 | 期限由已核对规范和卷内日期算出并标注；不写"异议能够成立" |
| B07 | 候选引用的规范在时效包中为"待核对" | 该项标"authority not checked"，阻断 |
| B08 | 候选写"成功可能性较高" | 违反第 6 条，阻断 |
| B09 | 五类原有候选 | 不受影响，照旧 |

结果写入 `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_BOUNDARY_REVISION_V1_1_RESULT.md`，评审记录写入 `.codex-coordination/outbox/`。

## 五、回滚与验收

- 改动前另存两个文件的原始字节。
- 验收条件：
  1. 改动前 SHA 与第一节一致；
  2. 差异只在第二、三节所列位置；
  3. B01–B09 静态核查通过；
  4. 隐私检查无发现，CI 通过；
  5. Codex 评审无重大问题，所有者确认后合并。

## 六、请所有者确认

确认本交接，即授权按第二、三节修订 C03 规格至 v1.1。
