# DSP-004 路径 B 一致的所有者决定批次 REV17

本记录一次记下 Project Owner 张纯熙在路径 B 下作出的一批决定。OD-01、OD-02、OD-03 选中 `RETAIN`。OD-04 没有已关闭选项表，批次选择键是 `DEFER_WITHOUT_EVIDENCE`，状态是 `OWNER_HELD_OPEN_NO_CLOSED_OPTIONS`。OD-06 选中 `LEAVE_UNREPAIRED`。OD-07 与 OD-08 选中 `REFUSE`。OD-09 选中 `DO_NOT_AUTHORIZE`。OD-10、OD-11、OD-12 选中 `REFUSE`。OD-13 选中 `RETAIN`。OD-15 的 `AUTHORIZE_MANIFEST`、`AUTHORIZE_FORMAL_RUN`、`COMPLETE_FA08`、`CLOSE_DSP004` 都是 Selected false，立场是 `UNAUTHORIZED` / `DO_NOT_AUTHORIZE`。每一行 `Decided` 是 true，`Opened` 是 false，`Signed` 与 `Accepted` 都是 false，准入是 `NOT_ADMITTED`。

OD-05 仍是 `REFUSE_LOCATOR`。OD-14 仍是 `KEEP_REV1_RECORD`。这两项由本批重新散列后绑定，决定文件没有改写。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本批授权原句是：`2026-10-30：批量完成后续项目进度，减少人为干预。` 记录范围只包括与路径 B 一致的拒绝、保留、保持未修复和不授权。不发明资产。不关闭 DSP-004。

新增筹备事实的名称是 `PATH_B_CONSISTENT_OWNER_DECISIONS_BATCH_REV17_RECORDED_NOT_ADMITTED`。

形成时 `HEAD` 是 `9c3e7ca03f76606484d53d30f3b01813cae6b6aa`（PR #20）。本决定记录在这个 `HEAD` 上还不存在。REV1 登记文件没有被改写。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_PATH_B_CONSISTENT_OWNER_DECISIONS_BATCH_REV17.json` |
| 机器记录 SHA-256 | `0049114F55C4636E631FA62E4C09A277D53DB0B274C74516E81A3B829EA1D67C` |
| 机器记录字节 | 78109 |
| 决定行 | 15 |
| 本批新记下 | OD-01、OD-02、OD-03、OD-04、OD-06、OD-07、OD-08、OD-09、OD-10、OD-11、OD-12、OD-13、OD-15 |
| 重新散列后未改写 | OD-05 `REFUSE_LOCATOR`；OD-14 `KEEP_REV1_RECORD` |
| 已决定 / 已打开 | 15 / 0 |
| OD-15 行 Selected | false |
| Signed / Accepted | false / false |
| 准入 | `NOT_ADMITTED` |
| 机器核对 | 12 项通过 |
| 通过的含义 | 字段与已记录筹备状态相符 |

行 `Selected` 为 true，只因为该行被选中的那一个选择键是 true。OD-15 没有被选中的动作，所以该行 `Selected` 是 false，`Decided` 仍是 true。`Opened` 沿用 REV1 登记的字段含义：true 表示随后打开了交付物。本批没有打开任何交付物。

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 标准库只做字节散列和 JSON 结构读取。散列只固定文本身份。散列不是调用，也不是执行。未导入受测模块，未调用 `identity_gate`，未执行 Fixture，未运行场景运行器，未执行捕获代码。未读取 `ENVIRONMENT_MANIFEST.md`，未读取历史 Windows 虚拟环境，未读取工具缓存。未生成 Manifest。

## 1. 十五行

| 决定 | 选中项 | Selected | Decided | Opened | Signed | Accepted | 准入 | 效力 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `OD-01` | `RETAIN` | true | true | false | false | false | `NOT_ADMITTED` | 35 行保留，DISPOSE false，登记未准入 |
| `OD-02` | `RETAIN` | true | true | false | false | false | `NOT_ADMITTED` | 16 行保留，DISPOSE false，登记未准入 |
| `OD-03` | `RETAIN` | true | true | false | false | false | `NOT_ADMITTED` | 10 行保留，DISPOSE false，运行根仍未提供 |
| `OD-04` | `DEFER_WITHOUT_EVIDENCE` | true | true | false | false | false | `NOT_ADMITTED` | 无已关闭选项表，未供给证据 |
| `OD-05` | `REFUSE_LOCATOR` | true | true | false | false | false | `NOT_ADMITTED` | 先前 REV15，本批未改写 |
| `OD-06` | `LEAVE_UNREPAIRED` | true | true | false | false | false | `NOT_ADMITTED` | REPAIR false，BLOCK 未修复 |
| `OD-07` | `REFUSE` | true | true | false | false | false | `NOT_ADMITTED` | ADMIT false，实际序列定位仍是 null |
| `OD-08` | `REFUSE` | true | true | false | false | false | `NOT_ADMITTED` | ADMIT false，三侧仍是 UNBOUND |
| `OD-09` | `DO_NOT_AUTHORIZE` | true | true | false | false | false | `NOT_ADMITTED` | AUTHORIZE_CALL false，未读取实际引用 |
| `OD-10` | `REFUSE` | true | true | false | false | false | `NOT_ADMITTED` | ACCEPT false，不是正式 B-02 合同 |
| `OD-11` | `REFUSE` | true | true | false | false | false | `NOT_ADMITTED` | ACCEPT false，含 57BAF161 未接受 |
| `OD-12` | `REFUSE` | true | true | false | false | false | `NOT_ADMITTED` | ACCEPT false，Harness 未接受 |
| `OD-13` | `RETAIN` | true | true | false | false | false | `NOT_ADMITTED` | ELIMINATE false，四项保留 |
| `OD-14` | `KEEP_REV1_RECORD` | true | true | false | false | false | `NOT_ADMITTED` | 先前 REV16，本批未改写，FA-05 未完成 |
| `OD-15` | `（无）` | false | true | false | false | false | `NOT_ADMITTED` | 四个动作 Selected false，DSP-004 仍 OPEN / HOLD |

OD-01 的 35 行、OD-02 的 16 行、OD-03 的 10 行，行号都与未改写的 FA-06 登记和 REV1 登记所记相同。`DISPOSE` 是 false。这些行没有被处置。保留不是准入，也不是接受。

OD-03 的上下文是 OD-05 的 `REFUSE_LOCATOR`。十行行号仍是 2、5、7、10、12、15、48、55、60、61。保留这些行不提供运行根，不修复 `NO_RUNTIME_ROOT_LOCATOR`。

OD-04 在 REV1 登记里的 `Choices` 仍是空数组。本批不把那份登记改成有选项表。`DEFER_WITHOUT_EVIDENCE` 只是本批机器记录使用的选择键。它的 `Selected` 是 true，含义是所有者明确把这项留在没有新证据的状态。导入闭包、两侧调用身份、检查到使用的防替换，以及 T0、PE、OS 证据都没有供给，也没有被准入。

OD-06 不修复 AP-020、AP-021、AP-022 的 BLOCK。`REPAIR` 是 false。`OUT_OF_ARRAY_OCCURRENCE_NOT_MERGED` 仍是 `RECORDED_NOT_INSERTED`。OD-07 不准入实际序列定位。三条政策的实际序列定位仍是 null。

OD-08 不绑定 `SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。七个捕获候选仍是 `NOT_SELECTED` / `NOT_ADMITTED`。OD-09 不授权读取实际引用的调用。

OD-10 不把两个 REV3 SHA 接受为正式 B-02 合同。OD-11 不接受此前候选的固定 SHA，包括来源与根候选 `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93`。不为它新增第二份设计复核文件。OD-12 不接受任何 Harness SHA。`identity_gate.py` 没有被导入，也没有被调用。

OD-13 的四项是 `C03-WP008-RDM-V2-RQ-018`（行 16）、`C03-WP008-RDM-V2-G-014`（行 17）、`C03-WP008-V3-RQ-021`（行 51）、`C03-WP008-V3-G-017`（行 52）。`ELIMINATE` 是 false。FA-06 文件没有被写入新的消除字段。

OD-15 确认路径 B 的不授权。`CLOSE_DSP004` 的 Selected 是 false。DSP-004 保持 `OPEN / HOLD`。`validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json` 仍不存在。

## 2. 已重新散列、仍未接受的身份

下表只固定本批直接绑定的文本身份。点名一个 SHA 不构成接受或准入。另外 59 条已在先前机器记录里被点名的路径，本批逐一重新散列，与磁盘相符，`Accepted` 与 `Admitted` 都是 false。相符不是接受。

| 文件 | 字节 | SHA-256 | 状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV16.md` | 13470 | `217CA6A36DB3EED5518DA99209B958EBB291B5058BC9750AFAA65F23BF386B3C` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV16.json` | 24280 | `EFB6C33952C36B700CAE294CC61DD9A6D66D870162F43D7A6DC4D015E04CD570` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD05_RUNTIME_ROOT_LOCATOR_DECISION_REV1.md` | 9876 | `30CA669C6EFE30EDDEE294CF2CAF2B9C3109E168E211753DDF62229EC3700192` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OD05_RUNTIME_ROOT_LOCATOR_DECISION_REV1.json` | 14234 | `96CD4504DF67A06F00968024F5877F685B99FE43B4144BFFA747FAEA054E62B0` | 已绑定，未改写，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD14_FA05_OPTION_DECISION_REV1.md` | 11599 | `DA0871EBAAE92B48C40043AA9CDAF3387EC447610F9DD7BA6BA4DE5953F756E9` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OD14_FA05_OPTION_DECISION_REV1.json` | 17592 | `E382AE8D8AD6F6033A7526C79559BE641AC0A2AED51D3500523A76A0C0E7982A` | 已绑定，未改写，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV3_STATUS_OVERLAY_CANDIDATE.md` | 9306 | `972F15B5E1C4BAE478DFD1BD2BAA3271DB5D47C0CDA47ADCA7FF7920F5DC0C4A` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV3_STATUS_OVERLAY_CANDIDATE.json` | 25452 | `F93F3CFD7E7342D301D722D9978734FCF7BFA8B53EB747D525D9881B98C67800` | 已绑定，未改写，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV2_STATUS_OVERLAY_CANDIDATE.md` | 6210 | `A069DE20BEE610B0FF4E7DD3FBC4F02654C3469C0F673DEC1421F75B52870A3A` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV2_STATUS_OVERLAY_CANDIDATE.json` | 16111 | `8BFE26CAF66524E43B4D11AE8909ED7F1ADDE13BCF8FA7B1DD852137A89B55CF` | 已绑定，未改写，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.md` | 37989 | `0821B18800B4FC9FF008160A80DA6E6D0DAD38273415CF6A62CADF05AD65AB91` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.json` | 82247 | `EC5233D541108CF59EF1DF7BCAA3E9E64F9CE61D1B29A05D8F40DC900789CFF3` | 已绑定，未改写，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SOURCE_ROOT_ADMISSION_PREPARATION_REV1_CANDIDATE.md` | 21257 | `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` | 已重新散列，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_TYPED_CONTRACT_REV3_CANDIDATE.md` | 29240 | `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` | 已重新散列，未接受为正式 B-02 合同 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ARRAY_POLICY_REGISTRY_REV3_CANDIDATE.md` | 16317 | `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` | 已重新散列，未接受为正式 B-02 合同 |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | 107849 | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` | 已重新散列，未接受，未执行 |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | 68768 | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | 已重新散列，未接受，未执行 |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json` | 770 | `9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` | 已重新散列，未接受，未执行 |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | 4555 | `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445` | 已重新散列，未接受，未导入，未调用 |

REV16 的筹备事实仍是 `OD14_FA05_KEEP_REV1_RECORD_RECORDED_NOT_ADMITTED`。REV1 登记的 15 行在那份文件里仍都未决定。本记录是后来的批次，不改写那份登记。

## 3. 本记录故意不做的事

- 不改写 REV1 所有者资产决定登记，不改写 REV2 或 REV3 叠层。
- 不改写 OD-05 与 OD-14 的决定记录。
- 不准入任何来源，不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不处置任何 FA-06 行。`DISPOSE` 保持 false。
- 不供给 OD-04 的导入闭包、两侧调用身份、防替换或 T0 / PE / OS 证据。
- 不提供运行根定位，不发明启动序列，不发明导入查询顺序。
- 不修复 `NO_RUNTIME_ROOT_LOCATOR`，也不修复 AP-020、AP-021、AP-022 的 BLOCK。
- 不准入 AP-020、AP-021、AP-022 的实际序列定位。
- 不绑定三个实际侧，不挑选七个捕获候选，不授权读取实际引用的调用。
- 不把两个 REV3 SHA 接受为正式 B-02 合同。
- 不接受来源与根候选 SHA，也不为它新增第二份设计复核文件。
- 不接受任何 Harness SHA。
- 不消除四项 LIMITED 审查项。
- 不选中 OD-15 的四个动作。不关闭 DSP-004。
- 不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`。
- 不把本记录的 SHA 接受为正式合同或来源准入。
- 不改商业 P0。

## 4. 本记录的效力

```text
PATH B OWNER DECISIONS BATCH RECORDED — FINDINGS ONLY

Owner：张纯熙
OD-01 / OD-02 / OD-03：RETAIN，DISPOSE false
OD-04：DEFER_WITHOUT_EVIDENCE，OWNER_HELD_OPEN_NO_CLOSED_OPTIONS，未供给证据
OD-05：REFUSE_LOCATOR，未改写，运行根未准入
OD-06：LEAVE_UNREPAIRED，REPAIR false
OD-07：REFUSE，ADMIT false，实际序列定位 null
OD-08：REFUSE，三侧 UNBOUND
OD-09：DO_NOT_AUTHORIZE，AUTHORIZE_CALL false
OD-10 / OD-11 / OD-12：REFUSE，ACCEPT false
OD-13：RETAIN，ELIMINATE false
OD-14：KEEP_REV1_RECORD，未改写，FA-05 未完成
OD-15：四个动作 Selected false，UNAUTHORIZED / DO_NOT_AUTHORIZE
CLOSE_DSP004：Selected false
Selected 行 / Decided / Opened：14 / 15 / 0
Signed / Accepted：false / false
准入：NOT_ADMITTED
REV1 登记：未改写，15 行仍未决定
DSP004-FA-06：未建立充分前提
DSP004-FA-05：未完成
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY
DSP004-FA-04：未完成
DSP004-FA-08：未完成
B-01：OPEN
B-02：OPEN
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

12 项机器核对全部通过。通过表示所引身份与当前磁盘相符，并且本记录的字段就是上面的筹备状态。通过不表示来源准入，不表示 SHA 接受，不表示运行根已经定位，也不表示 DSP-004 关闭。

本记录不接受 `0049114F55C4636E631FA62E4C09A277D53DB0B274C74516E81A3B829EA1D67C`。该 SHA 只固定机器记录的文本身份。
