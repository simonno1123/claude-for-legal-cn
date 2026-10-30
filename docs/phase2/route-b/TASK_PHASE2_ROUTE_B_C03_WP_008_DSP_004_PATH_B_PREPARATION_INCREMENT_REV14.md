# DSP-004 路径 B 筹备增量 REV14

本增量只记录路径 B 下的下一项筹备事实：所有者资产决定登记候选 REV1 已经写下。登记列出 15 项仍须 Project Owner 行动的决定。每一项的 `Selected`、`Decided`、`Opened` 都是 false。`Signed` 与 `Accepted` 都是 false。它不接受资产，不准入来源，不选中 FA-05 选项，不处置 FA-06 行，不修复 BLOCK，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本批授权是：REV13 合并之后，写下一项、且本批最后一份墙前筹备文档。文档是所有者资产决定登记。登记只列出仍须所有者行动的决定，不作出这些决定。本批停在资产墙前。

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV13.md` |
| 前一增量说明 | `8871255CD154EB6748CA3B28C0A8A2F6C9629D72AF9AD38C1BF3A5A3E1950EB9`（14474 字节） |
| 前一增量 JSON | `C27EA37C75D1735B0DE5309EA7C8712C78F28C7FEF9443F53796678C26BAF04B`（14201 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV14.json` |
| 本增量 JSON SHA-256 | `0F664D02C19F89C68609D85B9A97457A0D911A4B25A93F7030FADAC8463879EC` |
| 本增量 JSON 字节 | 11918 |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。REV1 至 REV13 已经记下的筹备事实保持原样。本增量不改它们。

## 1. 新增筹备事实：所有者资产决定登记

REV13 把仍须以后的资产级决定留在第 4 节，并把缺口排到 Manifest、正式运行、FA-08 和 DSP-004 关闭。本批的最后一份墙前文档把这些决定收成登记。登记是候选，只记所见。新增筹备事实的名称是 `OWNER_ASSET_DECISION_REGISTER_REV1_NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.md` | 37989 | `0821B18800B4FC9FF008160A80DA6E6D0DAD38273415CF6A62CADF05AD65AB91` |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.json` | 82247 | `EC5233D541108CF59EF1DF7BCAA3E9E64F9CE61D1B29A05D8F40DC900789CFF3` |

登记重新散列 REV13，并核对字段。相符不是接受。

| 文件 | 字节 | SHA-256 | 本增量后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV13.md` | 14474 | `8871255CD154EB6748CA3B28C0A8A2F6C9629D72AF9AD38C1BF3A5A3E1950EB9` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV13.json` | 14201 | `C27EA37C75D1735B0DE5309EA7C8712C78F28C7FEF9443F53796678C26BAF04B` | 已绑定，未接受 |

REV13 JSON 的 14201 字节与 `C27EA37C75D1735B0DE5309EA7C8712C78F28C7FEF9443F53796678C26BAF04B` 与 REV13 说明所记一致，也与 PR #17 所在的 `HEAD` `f281cf8c253d4c79bdcd217f31da84a520f05fd6` 上的文件一致。筹备事实仍是 `AP006_AP009_RUNTIME_ROOT_GAP_NOTE_INDEPENDENT_STATIC_REVIEW_NOT_ACCEPTED`。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 仍是 `OPEN / HOLD`。B-01 与 B-02 仍是 `OPEN`。三个 FA-05 选项仍未选中，也未打开。运行根仍未准入。Manifest、正式运行和 FA-08 仍无授权。REV13 JSON 里 20 组已记录身份与当前磁盘相同。

登记共 15 行。已决定 0 行。已选择 0 行。已打开 0 行。

| 决定 | 事项 | Selected | Decided | Opened |
| --- | --- | --- | --- | --- |
| `OD-01` | 保留或处置 FA-06 里证据状态为 EVIDENCE_PRESENT_UNACCEPTED 的行 | false | false | false |
| `OD-02` | 保留或处置 FA-06 里证据状态为 EVIDENCE_ABSENT 的行 | false | false | false |
| `OD-03` | 保留或处置 FA-06 里证据状态为 REQUIRES_RUNTIME_ROOT 的行 | false | false | false |
| `OD-04` | 导入闭包、两侧调用身份、检查到使用的防替换，以及 T0 / PE / OS 证据 | false | false | false |
| `OD-05` | 提供或拒绝 AP-006 与 AP-009 的运行根定位 | false | false | false |
| `OD-06` | 是否以及如何修复 AP-020、AP-021、AP-022 的 BLOCK | false | false | false |
| `OD-07` | 准入或拒绝 AP-020、AP-021、AP-022 的实际序列定位 | false | false | false |
| `OD-08` | 准入或拒绝三个实际侧及其捕获入口 | false | false | false |
| `OD-09` | 是否另作一次获准调用，以便读取实际引用 | false | false | false |
| `OD-10` | 是否把两个 REV3 SHA 接受为正式 B-02 合同 | false | false | false |
| `OD-11` | 是否接受或准入此前候选的固定 SHA | false | false | false |
| `OD-12` | 是否接受任何 Harness SHA | false | false | false |
| `OD-13` | 四项已经点名的 LIMITED 审查项是消除还是继续保留 | false | false | false |
| `OD-14` | 在三个未选的 FA-05 选项中选择一项 | false | false | false |
| `OD-15` | Manifest、正式运行、FA-08 与关闭 DSP-004 | false | false | false |

OD-01、OD-02、OD-03 分别对应 `EVIDENCE_PRESENT_UNACCEPTED` 35 行、`EVIDENCE_ABSENT` 16 行、`REQUIRES_RUNTIME_ROOT` 10 行。三桶都未处置。10 行的行号仍是 2、5、7、10、12、15、48、55、60、61。

OD-04 只复述 REV13 第 4 节已经记下的导入闭包、两侧调用身份、检查到使用防替换和 T0 / PE / OS 证据缺口。本增量不补这些证据，也不新造选项。

OD-05 的 `PROVIDE_LOCATOR` 与 `REFUSE_LOCATOR` 都未选中。AP-006 与 AP-009 仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。实际定位仍是 null。候选行数仍是 0。`NO_RUNTIME_ROOT_LOCATOR` 仍未修复。

OD-06 不修复 AP-020、AP-021、AP-022 的 BLOCK，也不写下修复做法。`OUT_OF_ARRAY_OCCURRENCE_NOT_MERGED` 仍是 `RECORDED_NOT_INSERTED`，不是 BLOCK。OD-07 不准入实际序列定位。三条实际序列定位仍是 null。候选行数仍是 17、2、30。行状态仍是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。

OD-08 不绑定三个实际侧。`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER` 仍是 `UNBOUND`。七个捕获候选仍是 `NOT_SELECTED` / `NOT_ADMITTED`。OD-09 不打开另一次获准调用。

OD-10 不把两个 REV3 SHA 接受为正式 B-02 合同。OD-11 不接受 REV13 第 4 节点名的候选 SHA，也不接受来源与根候选 `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93`。OD-12 不接受任何 Harness SHA。这三行的 `REFUSE` 也都未选中。

OD-13 不消除四项已经点名的 LIMITED 审查项，也不把继续保留写成决定。行号仍是 16、17、51、52。OD-14 不选中也不打开任何一个 FA-05 选项。OD-15 不授权 Manifest、正式运行、FA-08 或 DSP-004 关闭。

登记机器核对 16 项通过。通过表示字段与已记录筹备状态相符。通过不表示接受 `0821B18800B4FC9FF008160A80DA6E6D0DAD38273415CF6A62CADF05AD65AB91` 或 `EC5233D541108CF59EF1DF7BCAA3E9E64F9CE61D1B29A05D8F40DC900789CFF3`。

`DSP004-FA-05` 仍未完成。三个选项都没有被选中。`DSP004-FA-06` 仍是 `未建立充分前提`。`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。`DSP004-FA-08` 仍未完成。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

## 2. 剩余筹备缺口的次序

这一节只给仍留着的筹备缺口排次序。登记已经把它们列成未决定的行。本增量不打开下一项筹备文档，也不作出任何一行里的决定。

1. `DSP004-FA-06` 仍是 `未建立充分前提`。OD-01、OD-02、OD-03 都未处置。OD-04 没有补上导入闭包、两侧调用身份、检查到使用防替换或 T0 / PE / OS 证据。OD-13 没有消除四项 LIMITED 审查项，也没有决定继续保留。本增量不写处置文件。
2. `AP-006` 与 `AP-009` 的缺口注记已经有 REV13 的独立静态复核。复核未接受。OD-05 没有提供运行根定位，也没有把拒绝写成决定。BLOCK 代码仍是 `NO_RUNTIME_ROOT_LOCATOR`，且未修复。实际定位仍是 null。十行 `REQUIRES_RUNTIME_ROOT` 仍未处置。
3. `DSP004-FA-05` 的选项表已经有 REV12 的独立静态复核。复核未接受。OD-14 没有选中 `KEEP_REV1_RECORD`、`FUTURE_STATIC_IDENTITY_NOTE_ONLY` 或 `NOT_AVAILABLE_UNDER_PATH_B`，也没有打开它们。
4. `AP-020`、`AP-021`、`AP-022` 的 BLOCK 注记已经有 REV11 的独立静态复核。复核未接受。OD-06 没有修复这些代码。OD-07 没有准入实际序列定位。`OUT_OF_ARRAY_OCCURRENCE_NOT_MERGED` 仍不是 BLOCK。
5. 三个实际侧仍是 `UNBOUND`。OD-08 没有绑定它们。OD-09 没有打开另一次获准调用。七个捕获候选仍是 `NOT_SELECTED` / `NOT_ADMITTED`。
6. OD-10、OD-11、OD-12 没有接受两个 REV3 SHA、REV13 第 4 节点名的候选 SHA、来源与根候选 SHA 或任何 Harness SHA。拒绝也同样未选中。
7. Manifest、正式运行、`DSP004-FA-08` 和 DSP-004 关闭仍无授权。OD-15 没有选中其中任何一项。

## 3. 本增量故意不做的事

- 不准入任何来源，不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不作出登记里的任何一项决定。15 行的 `Selected`、`Decided`、`Opened` 保持 false。
- 不准入运行根，不发明启动序列，不发明导入查询顺序，不写入任何运行根路径。
- 不修复 `NO_RUNTIME_ROOT_LOCATOR`。`NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` 保持原样。实际定位保持 null。
- 不修复 `AP-020`、`AP-021`、`AP-022` 的 BLOCK，也不准入它们的实际序列定位。
- 不选中 `KEEP_REV1_RECORD`、`FUTURE_STATIC_IDENTITY_NOTE_ONLY` 或 `NOT_AVAILABLE_UNDER_PATH_B`。
- 不准入 `SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json`，也不准入 `SCENARIO_INPUT_BINDING.json`。
- 不把任何 Harness SHA、Fixture SHA 或 `identity_gate.py` 的 SHA 接受为正式合同。
- 不把四个文件的 SHA `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430`、`92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5`、`9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` 与 `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445` 接受为正式合同。
- 不把本登记的 SHA `0821B18800B4FC9FF008160A80DA6E6D0DAD38273415CF6A62CADF05AD65AB91` 与 `EC5233D541108CF59EF1DF7BCAA3E9E64F9CE61D1B29A05D8F40DC900789CFF3` 接受为正式合同或来源准入。
- 不把 REV13 的 SHA `8871255CD154EB6748CA3B28C0A8A2F6C9629D72AF9AD38C1BF3A5A3E1950EB9` 与 `C27EA37C75D1735B0DE5309EA7C8712C78F28C7FEF9443F53796678C26BAF04B` 接受为正式合同或来源准入。
- 不把两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 接受为正式 B-02 合同。
- 不把来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 接受为来源准入，也不为它新增第二份设计复核文件。
- 不完成 `DSP004-FA-03`，也不完成 `DSP004-FA-04`。B-01 与 B-02 保持 `OPEN`。
- 不完成 `DSP004-FA-05`。三个选项保持未选中。
- 不完成 `DSP004-FA-06`。它仍是 `未建立充分前提`。本增量不处置任何 FA-06 行。
- 不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不打开任何进一步的交付物。
- 不改商业 P0。

## 4. 仍须以后的资产级决定

路径 B 没有代替下列决定。本增量只把它们记入登记，每一项仍是 `Decided` false：

- `OD-01` 保留或处置 FA-06 里证据状态为 EVIDENCE_PRESENT_UNACCEPTED 的行
- `OD-02` 保留或处置 FA-06 里证据状态为 EVIDENCE_ABSENT 的行
- `OD-03` 保留或处置 FA-06 里证据状态为 REQUIRES_RUNTIME_ROOT 的行
- `OD-04` 导入闭包、两侧调用身份、检查到使用的防替换，以及 T0 / PE / OS 证据
- `OD-05` 提供或拒绝 AP-006 与 AP-009 的运行根定位
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
