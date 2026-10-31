# DSP-004 OD-05 运行根定位决定记录 REV1

本记录只记下 Project Owner 张纯熙对 OD-05 的选择。选中的是 `REFUSE_LOCATOR`。`PROVIDE_LOCATOR` 未选中。`Decided` 是 true。`Opened` 是 false。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。运行根没有被准入。`NO_RUNTIME_ROOT_LOCATOR` 没有被修复。AP-006 与 AP-009 仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

所有者本步选择是：拒绝提供 AP-006 与 AP-009 的运行根定位。没有给出定位路径，没有给出启动序列，没有给出导入查询顺序。本记录不补写这三项。

新增筹备事实的名称是 `OD05_RUNTIME_ROOT_LOCATOR_REFUSED_RECORDED_NOT_ADMITTED`。

形成时 `HEAD` 是 `a3685c8641661de8118bba3021f1520cee6d57d8`（PR #18）。本决定记录在这个 `HEAD` 上还不存在。REV1 登记文件没有被改写。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_OD05_RUNTIME_ROOT_LOCATOR_DECISION_REV1.json` |
| 机器记录 SHA-256 | `96CD4504DF67A06F00968024F5877F685B99FE43B4144BFFA747FAEA054E62B0` |
| 机器记录字节 | 14234 |
| 决定 | `OD-05` |
| 事项 | 提供或拒绝 AP-006 与 AP-009 的运行根定位 |
| 选中 | `REFUSE_LOCATOR` Selected true |
| 未选中 | `PROVIDE_LOCATOR` Selected false |
| 行 Selected / Decided / Opened | true / true / false |
| Signed / Accepted | false / false |
| 准入 | `NOT_ADMITTED` |
| RuntimeRootAdmitted | false |
| 机器核对 | 12 项通过 |
| 通过的含义 | 字段与已记录筹备状态相符 |

行 `Selected` 为 true，只因为 `REFUSE_LOCATOR` 是被选中的那一项。`Opened` 沿用 REV1 登记的字段含义：true 表示随后打开了定位、修复或其他交付物。拒绝定位没有打开其中任何一项，所以 `Opened` 保持 false。

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 标准库只做字节散列和 JSON 结构读取。散列只固定文本身份。散列不是调用，也不是执行。未导入受测模块，未调用 `identity_gate`，未执行 Fixture，未运行场景运行器，未执行捕获代码。未读取 `ENVIRONMENT_MANIFEST.md`，未读取历史 Windows 虚拟环境，未读取工具缓存。未生成 Manifest。

## 1. 记下的选择

| 字段 | 值 |
| --- | --- |
| Owner | 张纯熙 |
| DecisionId | `OD-05` |
| Subject | `RUNTIME_ROOT_LOCATOR_AP006_AP009` |
| `REFUSE_LOCATOR` | Selected true |
| `PROVIDE_LOCATOR` | Selected false |
| Selected | true |
| Decided | true |
| Opened | false |
| Signed | false |
| Accepted | false |
| Admission | `NOT_ADMITTED` |
| LocatorPath | null |
| StartupSequence | null |
| ImportQueryOrder | null |
| RuntimeRootAdmitted | false |
| BlockCode | `NO_RUNTIME_ROOT_LOCATOR` |
| BlockRepaired | false |

AP-006 与 AP-009 的状态仍取自已经在库的缺口注记，本记录不改写该注记：

| 政策 | LocatorStatus | ActualLocator | 候选行数 | BLOCK | Repaired | 准入 |
| --- | --- | --- | --- | --- | --- | --- |
| `AP-006` | `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` | null | 0 | `NO_RUNTIME_ROOT_LOCATOR` | false | `NOT_ADMITTED` |
| `AP-009` | `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` | null | 0 | `NO_RUNTIME_ROOT_LOCATOR` | false | `NOT_ADMITTED` |

这两行的定位不是本决定提供的。`SuppliedByThisDecision` 是 false。

## 2. 已重新散列、仍未接受的身份

下表只固定指针文件的文本身份。点名一个 SHA 不构成接受或准入。REV1 登记里的 OD-05 仍是未决定。本记录是后来的选择，不改写那份登记。

| 文件 | 字节 | SHA-256 | 状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV14.md` | 13011 | `BE4292DCDE963D0657D038132ACD5197A0BAF64E1A32233E7539C5B2C5B7BE9D` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV14.json` | 11918 | `0F664D02C19F89C68609D85B9A97457A0D911A4B25A93F7030FADAC8463879EC` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.md` | 37989 | `0821B18800B4FC9FF008160A80DA6E6D0DAD38273415CF6A62CADF05AD65AB91` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.json` | 82247 | `EC5233D541108CF59EF1DF7BCAA3E9E64F9CE61D1B29A05D8F40DC900789CFF3` | 已绑定，未改写，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV13.md` | 14474 | `8871255CD154EB6748CA3B28C0A8A2F6C9629D72AF9AD38C1BF3A5A3E1950EB9` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV13.json` | 14201 | `C27EA37C75D1735B0DE5309EA7C8712C78F28C7FEF9443F53796678C26BAF04B` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE.md` | 15149 | `E6ED064272226185FCD10A5FDBE3AA192B742A5E728B0D55A973251AE3A9E474` | 已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE.json` | 17687 | `26C2C5C308570ACE020CD628D5E517BCEEFE2A96E04BFC57CE38F905163B0C26` | 已引用，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.md` | 20486 | `8BA8F456E528572A1EF758025BDF8698770B091399FDA3BB6718C0F1227CB4E6` | 已引用，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.json` | 43714 | `6230D1977D39702FB19B4498A0AB65CEE3564E33FE5AB712E8451D38E2B93B09` | 已引用，未接受 |

REV14 的筹备事实仍是 `OWNER_ASSET_DECISION_REGISTER_REV1_NOT_ADMITTED`。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。`AnyDecisionTaken` 仍是 false，因为那份增量写下登记时还没有作出决定。REV13 的筹备事实仍是 `AP006_AP009_RUNTIME_ROOT_GAP_NOTE_INDEPENDENT_STATIC_REVIEW_NOT_ACCEPTED`。缺口注记的筹备事实仍是 `AP006_AP009_RUNTIME_ROOT_GAP_NOTE_NOT_ADMITTED`。复核的 `RuntimeRootAdmitted` 仍是 false。十条 `REQUIRES_RUNTIME_ROOT` 行的行号仍是 2、5、7、10、12、15、48、55、60、61，`RowsDisposed` 仍是 0。

登记 JSON 里 OD-05 的 `Selected`、`Decided`、`Opened` 仍是 false。`PROVIDE_LOCATOR` 与 `REFUSE_LOCATOR` 在那份文件里的 `Selected` 仍是 false。这是未改写的登记快照。所有者后来的选择写在本记录。

## 3. 对 OD-03 的上下文

OD-03 仍是：保留或处置 FA-06 里证据状态为 `REQUIRES_RUNTIME_ROOT` 的行。10 行的行号仍是 2、5、7、10、12、15、48、55、60、61。`Disposed` 是 false。

OD-05 拒绝提供运行根定位，只构成这 10 行的上下文。拒绝不把这 10 行写成保留，也不把它们写成处置。OD-03 的 `Selected`、`Decided`、`Opened` 仍是 false。`Signed` 与 `Accepted` 仍是 false。准入仍是 `NOT_ADMITTED`。

OD-01、OD-02、OD-04，以及 OD-06 至 OD-15，本记录都不作决定。

## 4. 本记录故意不做的事

- 不改写 REV1 所有者资产决定登记。那份文件的 OD-05 仍是未决定。
- 不准入任何来源，不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不提供运行根定位，不写入定位路径，不发明启动序列，不发明导入查询顺序。
- 不修复 `NO_RUNTIME_ROOT_LOCATOR`。AP-006 与 AP-009 保持 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。实际定位保持 null。
- 不修复 AP-020、AP-021、AP-022 的 BLOCK，也不准入它们的实际序列定位。
- 不处置任何 FA-06 行。OD-03 保持未决定。
- 不选中 `KEEP_REV1_RECORD`、`FUTURE_STATIC_IDENTITY_NOTE_ONLY` 或 `NOT_AVAILABLE_UNDER_PATH_B`。
- 不绑定 `SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。
- 不把两个 REV3 SHA 接受为正式 B-02 合同，不接受来源与根候选，不接受任何 Harness SHA。
- 不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不把本记录的 SHA 接受为正式合同或来源准入。
- 不改商业 P0。

## 5. 本记录的效力

```text
OD-05 DECISION RECORDED — FINDINGS ONLY

Owner：张纯熙
REFUSE_LOCATOR：Selected true
PROVIDE_LOCATOR：Selected false
Selected / Decided / Opened：true / true / false
Signed / Accepted：false / false
准入：NOT_ADMITTED
RuntimeRootAdmitted：false
LocatorPath / StartupSequence / ImportQueryOrder：null / null / null
NO_RUNTIME_ROOT_LOCATOR：未修复
AP-006 / AP-009：NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT
OD-03：未决定，十行未处置
OD-01、OD-02、OD-04、OD-06 至 OD-15：未决定
REV1 登记：未改写，其 OD-05 仍未决定
DSP004-FA-05：未完成，选项未选中
DSP004-FA-06：未建立充分前提
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY
DSP004-FA-04：未完成
DSP004-FA-08：未完成
B-01：OPEN
B-02：OPEN
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

12 项机器核对全部通过。通过表示所引身份与当前磁盘相符，并且本记录的字段就是上面的筹备状态。通过不表示来源准入，不表示 SHA 接受，不表示运行根已经定位，也不表示 DSP-004 关闭。

本记录不接受 `96CD4504DF67A06F00968024F5877F685B99FE43B4144BFFA747FAEA054E62B0`。该 SHA 只固定机器记录的文本身份。
