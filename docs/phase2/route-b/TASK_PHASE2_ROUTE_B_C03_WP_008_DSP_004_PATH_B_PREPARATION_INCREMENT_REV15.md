# DSP-004 路径 B 筹备增量 REV15

本增量只记录路径 B 下的下一项筹备事实：Project Owner 张纯熙对 OD-05 的选择已经写下。选中的是 `REFUSE_LOCATOR`。`PROVIDE_LOCATOR` 未选中。`Decided` 是 true。`Opened` 是 false。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。它不接受资产，不准入来源，不提供运行根定位，不修复 `NO_RUNTIME_ROOT_LOCATOR`，不选中 FA-05 选项，不处置 FA-06 行，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本批授权是：REV14 合并之后，记下张纯熙对 OD-05 的 `REFUSE_LOCATOR`，并继续正式验收筹备。没有提供定位路径、启动序列或导入查询顺序。本批停在资产墙前。

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV14.md` |
| 前一增量说明 | `BE4292DCDE963D0657D038132ACD5197A0BAF64E1A32233E7539C5B2C5B7BE9D`（13011 字节） |
| 前一增量 JSON | `0F664D02C19F89C68609D85B9A97457A0D911A4B25A93F7030FADAC8463879EC`（11918 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV15.json` |
| 本增量 JSON SHA-256 | `E3817F182B51460F7E8C59CF0104A6355A21CA3B8474970EECD3944670590DA9` |
| 本增量 JSON 字节 | 20253 |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。REV1 至 REV14 已经记下的筹备事实保持原样。本增量不改它们。REV1 登记文件没有被改写。

## 1. 新增筹备事实：OD-05 拒绝运行根定位

新增筹备事实的名称是 `OD05_RUNTIME_ROOT_LOCATOR_REFUSED_RECORDED_NOT_ADMITTED`。决定记录是候选。它记载所有者的选择，准入仍是 `NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD05_RUNTIME_ROOT_LOCATOR_DECISION_REV1.md` | 9876 | `30CA669C6EFE30EDDEE294CF2CAF2B9C3109E168E211753DDF62229EC3700192` |
| `validation/route_b_c03/wp_008/DSP_004_OD05_RUNTIME_ROOT_LOCATOR_DECISION_REV1.json` | 14234 | `96CD4504DF67A06F00968024F5877F685B99FE43B4144BFFA747FAEA054E62B0` |

决定记录重新散列 REV14、REV1 登记、REV13、缺口注记和 REV13 复核，并核对字段。相符不是接受。

| 字段 | 值 |
| --- | --- |
| Owner | 张纯熙 |
| `REFUSE_LOCATOR` | Selected true |
| `PROVIDE_LOCATOR` | Selected false |
| Selected / Decided / Opened | true / true / false |
| Signed / Accepted | false / false |
| Admission | `NOT_ADMITTED` |
| RuntimeRootAdmitted | false |
| LocatorPath / StartupSequence / ImportQueryOrder | null / null / null |
| `NO_RUNTIME_ROOT_LOCATOR` | 未修复 |
| AP-006 / AP-009 | `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` |

行 `Selected` 为 true，只因为 `REFUSE_LOCATOR` 被选中。`Opened` 为 false：没有打开定位、修复或其他交付物。

伴随的加性状态叠层不改写 REV1。它的筹备事实是 `OWNER_ASSET_DECISION_STATUS_OVERLAY_REV2_NOT_ADMITTED`。OD-05 在叠层里已决定为 `REFUSE_LOCATOR`。OD-01 至 OD-04 与 OD-06 至 OD-15 仍未决定。叠层本身的 `Signed` 与 `Accepted` 是 false，准入是 `NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 | 状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV2_STATUS_OVERLAY_CANDIDATE.md` | 6210 | `A069DE20BEE610B0FF4E7DD3FBC4F02654C3469C0F673DEC1421F75B52870A3A` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV2_STATUS_OVERLAY_CANDIDATE.json` | 16111 | `8BFE26CAF66524E43B4D11AE8909ED7F1ADDE13BCF8FA7B1DD852137A89B55CF` | 已绑定，未准入 |

REV1 登记仍是未决定快照。它的 OD-05 在磁盘上仍是 `Selected` false、`Decided` false，两个选择都未选中。

| 文件 | 字节 | SHA-256 | 本增量后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.md` | 37989 | `0821B18800B4FC9FF008160A80DA6E6D0DAD38273415CF6A62CADF05AD65AB91` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.json` | 82247 | `EC5233D541108CF59EF1DF7BCAA3E9E64F9CE61D1B29A05D8F40DC900789CFF3` | 已绑定，未改写，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV14.md` | 13011 | `BE4292DCDE963D0657D038132ACD5197A0BAF64E1A32233E7539C5B2C5B7BE9D` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV14.json` | 11918 | `0F664D02C19F89C68609D85B9A97457A0D911A4B25A93F7030FADAC8463879EC` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV13.md` | 14474 | `8871255CD154EB6748CA3B28C0A8A2F6C9629D72AF9AD38C1BF3A5A3E1950EB9` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV13.json` | 14201 | `C27EA37C75D1735B0DE5309EA7C8712C78F28C7FEF9443F53796678C26BAF04B` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE.md` | 15149 | `E6ED064272226185FCD10A5FDBE3AA192B742A5E728B0D55A973251AE3A9E474` | 已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE.json` | 17687 | `26C2C5C308570ACE020CD628D5E517BCEEFE2A96E04BFC57CE38F905163B0C26` | 已引用，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.md` | 20486 | `8BA8F456E528572A1EF758025BDF8698770B091399FDA3BB6718C0F1227CB4E6` | 已引用，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.json` | 43714 | `6230D1977D39702FB19B4498A0AB65CEE3564E33FE5AB712E8451D38E2B93B09` | 已引用，未接受 |

REV14 JSON 的 11918 字节与 `0F664D02C19F89C68609D85B9A97457A0D911A4B25A93F7030FADAC8463879EC` 与 REV14 说明所记一致，也与 PR #18 所在的 `HEAD` `a3685c8641661de8118bba3021f1520cee6d57d8` 上的文件一致。筹备事实仍是 `OWNER_ASSET_DECISION_REGISTER_REV1_NOT_ADMITTED`。REV13 JSON 的 14201 字节与 `C27EA37C75D1735B0DE5309EA7C8712C78F28C7FEF9443F53796678C26BAF04B` 与 REV13 说明所记一致。筹备事实仍是 `AP006_AP009_RUNTIME_ROOT_GAP_NOTE_INDEPENDENT_STATIC_REVIEW_NOT_ACCEPTED`。缺口注记与复核的两条政策仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`，实际定位仍是 null，候选行数仍是 0，BLOCK 仍是 `NO_RUNTIME_ROOT_LOCATOR`，`Repaired` 仍是 false。

OD-03 仍未决定。十行 `REQUIRES_RUNTIME_ROOT` 的行号仍是 2、5、7、10、12、15、48、55、60、61。OD-05 的拒绝是这十行的上下文。这十行未被处置，也未被写成保留决定。

决定记录的 12 项核对与叠层的 8 项核对都通过。本增量的 12 项核对也通过。通过表示字段与已记录筹备状态相符。通过不表示接受这些 SHA。

`DSP004-FA-05` 仍未完成。三个选项都没有被选中。`DSP004-FA-06` 仍是 `未建立充分前提`。`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。`DSP004-FA-08` 仍未完成。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

## 2. 剩余筹备缺口的次序

这一节只给仍留着的筹备缺口排次序。OD-05 的拒绝已经记下。本增量不打开下一项修复、定位或 Manifest。

1. `DSP004-FA-06` 仍是 `未建立充分前提`。OD-01、OD-02、OD-03、OD-04、OD-13 都未决定。OD-05 的拒绝只给 OD-03 提供上下文。十行 `REQUIRES_RUNTIME_ROOT` 仍未处置。本增量不写处置文件。
2. `AP-006` 与 `AP-009` 的 OD-05 已记下 `REFUSE_LOCATOR`。`PROVIDE_LOCATOR` 未选中。没有运行根路径、启动序列或导入查询顺序。BLOCK 代码仍是 `NO_RUNTIME_ROOT_LOCATOR`，且未修复。两条政策仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。缺口注记与 REV13 复核仍未接受。
3. `DSP004-FA-05` 的选项表已经有 REV12 的独立静态复核。复核未接受。OD-14 没有选中 `KEEP_REV1_RECORD`、`FUTURE_STATIC_IDENTITY_NOTE_ONLY` 或 `NOT_AVAILABLE_UNDER_PATH_B`，也没有打开它们。
4. `AP-020`、`AP-021`、`AP-022` 的 BLOCK 注记已经有 REV11 的独立静态复核。复核未接受。OD-06 与 OD-07 仍未决定。这些 BLOCK 没有被修复。实际序列定位仍是 null。`OUT_OF_ARRAY_OCCURRENCE_NOT_MERGED` 仍是 `RECORDED_NOT_INSERTED`。
5. 三个实际侧仍是 `UNBOUND`。OD-08 与 OD-09 仍未决定。七个捕获候选仍是 `NOT_SELECTED` / `NOT_ADMITTED`。
6. OD-10、OD-11、OD-12 仍未决定。两个 REV3 SHA、此前候选 SHA、来源与根候选 SHA 和任何 Harness SHA 都没有被接受。
7. Manifest、正式运行、`DSP004-FA-08` 和 DSP-004 关闭仍无授权。OD-15 没有选中其中任何一项。

## 3. 本增量故意不做的事

- 不准入任何来源，不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不改写 REV1 登记。那份文件的 15 行仍都未决定。
- 不把 `REFUSE_LOCATOR` 写成对资产 SHA 的接受。决定已经记下，准入仍是 `NOT_ADMITTED`。
- 不提供运行根定位，不发明启动序列，不发明导入查询顺序，不写入任何运行根路径。
- 不修复 `NO_RUNTIME_ROOT_LOCATOR`。`NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` 保持原样。实际定位保持 null。
- 不修复 `AP-020`、`AP-021`、`AP-022` 的 BLOCK，也不准入它们的实际序列定位。
- 不选中 `KEEP_REV1_RECORD`、`FUTURE_STATIC_IDENTITY_NOTE_ONLY` 或 `NOT_AVAILABLE_UNDER_PATH_B`。
- 不处置任何 FA-06 行。OD-03 保持未决定。
- 不绑定 `SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。
- 不把两个 REV3 SHA 接受为正式 B-02 合同，不接受来源与根候选，不接受任何 Harness SHA。
- 不把本增量、决定记录或状态叠层的 SHA 接受为正式合同或来源准入。
- 不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不改商业 P0。

## 4. 仍须以后的资产级决定

路径 B 没有代替下列决定。OD-05 已经记下为 `REFUSE_LOCATOR`，该记载的 `Signed` 与 `Accepted` 仍是 false。其余每一项仍是 `Decided` false：

- `OD-01` 保留或处置 FA-06 里证据状态为 EVIDENCE_PRESENT_UNACCEPTED 的行
- `OD-02` 保留或处置 FA-06 里证据状态为 EVIDENCE_ABSENT 的行
- `OD-03` 保留或处置 FA-06 里证据状态为 REQUIRES_RUNTIME_ROOT 的行。OD-05 的拒绝只是上下文，本行仍未决定
- `OD-04` 导入闭包、两侧调用身份、检查到使用的防替换，以及 T0 / PE / OS 证据
- `OD-05` 已记下 `REFUSE_LOCATOR`。`PROVIDE_LOCATOR` 未选中。运行根未准入。BLOCK 未修复
- `OD-06` 是否以及如何修复 AP-020、AP-021、AP-022 的 BLOCK
- `OD-07` 准入或拒绝 AP-020、AP-021、AP-022 的实际序列定位
- `OD-08` 准入或拒绝三个实际侧及其捕获入口
- `OD-09` 是否另作一次获准调用，以便读取实际引用
- `OD-10` 是否把两个 REV3 SHA 接受为正式 B-02 合同
- `OD-11` 是否接受或准入此前候选的固定 SHA
- `OD-12` 是否接受任何 Harness SHA
- `OD-13` 四项已经点名的 LIMITED 审查项是消除还是继续保留
- `OD-14` 在三个未选的 FA-05 选项中选择一项
- `OD-15` Manifest、正式运行、FA-08 与关闭 DSP-004

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
