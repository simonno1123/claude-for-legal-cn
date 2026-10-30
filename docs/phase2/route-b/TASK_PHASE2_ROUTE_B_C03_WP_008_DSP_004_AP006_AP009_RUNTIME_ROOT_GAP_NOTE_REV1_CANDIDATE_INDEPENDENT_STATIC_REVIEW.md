# DSP-004 AP-006 与 AP-009 运行根缺口注记候选 REV1 — 独立静态复核

本记录是路径 B 筹备增量 REV12 之后的在库只读复核。对象是已经在 `main` 上的 `AP-006` 与 `AP-009` 运行根缺口注记候选 REV1。复核确认它的字节，并核对该注记列出的两条政策字段是否与已经在库的 ORDERED 清点一致，以及十行 `REQUIRES_RUNTIME_ROOT` 是否与 FA-06 登记及该登记的独立静态复核所记行号一致。它不接受这些 SHA，不准入运行根，不发明路径，不补启动序列，不补导入查询顺序，不修复 `NO_RUNTIME_ROOT_LOCATOR`，不选中任何一个 FA-05 选项，不接受 Harness SHA，也不关闭 B-01、B-02 或 DSP-004。

依据仍是已经记入的路径 B 原句：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

新增筹备事实的名称是 `AP006_AP009_RUNTIME_ROOT_GAP_NOTE_INDEPENDENT_STATIC_REVIEW_NOT_ACCEPTED`。注记自己的筹备事实名称仍是 `AP006_AP009_RUNTIME_ROOT_GAP_NOTE_NOT_ADMITTED`。本复核不改写那个名称。

## 1. 复核基准

| 项目 | 本记录的事实 |
| --- | --- |
| 复核时 `HEAD` | `181f0de9d4ba49390e79ae33092958039fdeb5ba` |
| 缺口注记物化提交 | `7d73f50ede1b5e4ec8aa55f85270eb50b9cafa92`（PR #12） |
| 注记自述形成时 `HEAD` | `d2f8f62536cb2de3ab8c09e634281202a1e19487` |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV12.md` |
| 前一增量说明 SHA-256 | `E44A36331C3679C04B3923E000077F1AF83329B075AF5D27ECD19DD92D68D063`（12277 字节） |
| 前一增量 JSON SHA-256 | `1C84529D4746327835622CDCA713F6FC714D992CAC474A8425C322B6EAEDDB17`（10089 字节） |
| 机器可读结果 | `validation/route_b_c03/wp_008/DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.json` |
| 该结果 SHA-256 | `6230D1977D39702FB19B4498A0AB65CEE3564E33FE5AB712E8451D38E2B93B09` |
| 该结果字节 | 43714 |
| 受测模块导入或执行 | 未进行 |
| `identity_gate` 导入或调用 | 未进行 |
| Fixture 执行或写入 | 未进行 |
| 场景运行器 | 未运行 |
| 捕获代码 | 未导入，未执行 |
| 商业 P0 | 未执行，未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 标准库只做字节散列和 JSON 结构读取。读集是这份缺口注记的说明与机器结果、REV12 增量的说明与机器结果、REV8 与 REV7 的说明与机器结果、ORDERED 清点的说明与机器结果、FA-06 登记及其独立静态复核、FA-05 选项表的说明与机器结果、四个被点名文件的字节、FA-03 候选里三个实际侧与七个捕获候选的字节，以及两个 REV3 文本和来源与根候选的字节。散列只固定文本身份。散列不是调用，也不是执行。`identity_gate.py` 没有被导入，也没有被调用。Fixture 文件没有被执行。未重跑 FA-06 复核的 21 项核对，未导入捕获候选或场景运行器，未编译 C#，未重放业务场景，未生成 Manifest。未读取 `ENVIRONMENT_MANIFEST.md`，未读取历史 Windows 虚拟环境，未读取工具缓存。未发明启动序列，未发明导入查询顺序，未写入任何运行根路径。

这是同仓库内的后续静态复核，不是跨供应商外审，也不是 Project Owner 对这份注记的接受。结论只是所见。`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。运行根没有被准入。`NO_RUNTIME_ROOT_LOCATOR` 仍未修复。

## 2. 两个物理文件

复核前 REV8、PR #12 以及 REV12 记下的身份，与当前 `HEAD` 上的字节一致。物化提交是 `7d73f50ede1b5e4ec8aa55f85270eb50b9cafa92`。当前 `HEAD` 是 `181f0de9d4ba49390e79ae33092958039fdeb5ba`。缺口注记在这两处是同一个 git blob。注记在形成时 `HEAD` `d2f8f62536cb2de3ab8c09e634281202a1e19487` 上还不存在。ORDERED 清点、FA-06 登记、FA-06 复核与 REV7 在那个形成时 `HEAD` 与当前 `HEAD` 上是同一个 git blob。

| 文件 | 路径 | 字节 | SHA-256 |
| --- | --- | --- | --- |
| 注记说明 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE.md` | 15149 | `E6ED064272226185FCD10A5FDBE3AA192B742A5E728B0D55A973251AE3A9E474` |
| 注记 JSON | `validation/route_b_c03/wp_008/DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE.json` | 17687 | `26C2C5C308570ACE020CD628D5E517BCEEFE2A96E04BFC57CE38F905163B0C26` |

两份文件均为 UTF-8、无 BOM、无 CR、无行尾空白。说明文件嵌入自己配套 JSON 的 SHA-256。本复核的 SHA 不在那份说明里。

点名一个 SHA 只固定文本身份。本复核不把这两个 SHA 接受为正式合同、Manifest 或来源准入。

注记自己的 `Signed` 与 `Accepted` 均为 false，准入状态是 `NOT_ADMITTED`。`LocatorSuppliedByThisNote` 为 false。实际定位保持 null。候选行数保持 0。`BlockCodesRepaired` 为 false。`PathsInvented`、`StartupSequenceInvented`、`ImportSequenceInvented` 均为 false。十行的 `Disposed` 都是 false。

## 3. 已经绑定、仍未接受的来源

REV12 说明本次重新散列是 12277 字节，`E44A36331C3679C04B3923E000077F1AF83329B075AF5D27ECD19DD92D68D063`。REV12 JSON 是 10089 字节，`1C84529D4746327835622CDCA713F6FC714D992CAC474A8425C322B6EAEDDB17`。该 JSON SHA 就是 REV12 说明里写下的 SHA，也与 PR #16 所记身份一致。这次重新散列不把 REV12 接受为正式合同或来源准入。

| 文件 | 字节 | SHA-256 | 本复核后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV12.md` | 12277 | `E44A36331C3679C04B3923E000077F1AF83329B075AF5D27ECD19DD92D68D063` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV12.json` | 10089 | `1C84529D4746327835622CDCA713F6FC714D992CAC474A8425C322B6EAEDDB17` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV8.md` | 10123 | `5D90088CA5FE820FD766DAB37CB4AC8502F612EF4F5101F5718B9AB85B31DAA2` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV8.json` | 9629 | `E512F379D32634F5F6C25DE3980BA1CE9D0DAB35BEB9837AECB43A5EC2C98B2B` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.md` | 15858 | `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5` | 已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.json` | 70228 | `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7` | 已引用，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE.md` | 22701 | `AAF90D311F2C85C48EF652E903D4B430D1F339F1FA465527DE679087F30B2305` | 已引用，未准入，未处置 |
| `validation/route_b_c03/wp_008/DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE.json` | 38377 | `500015848949A8B789E0E44F2BB21AE0676D50B9440EA89124BB30CDC8B06254` | 已引用，未准入，未处置 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.md` | 14868 | `776FE8B24D6F0DFD31EC577393C66A84C16A99C1494CE8BF060A4AA59D814928` | 所见已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.json` | 59047 | `1EDA163811CB0EF31E32898B968C39C7A464B55C1DD73D1EC83F30F68F6415BA` | 所见已引用，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV7.md` | 8112 | `1167FB1144495AF0BE11D7D172E889E675918785759D2D27B149EF4913BF42FB` | 已引用，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV7.json` | 7310 | `21FC18821036AB38C7855766B93236865EDE0DDE03795834ABA848F8A122A3C1` | 已引用，未接受 |

这些字节与缺口注记所引身份一致。本复核不重跑 FA-06 那 21 项核对，也不把它们接受为来源准入。

## 4. 政策字段与十行对照

对照只读已经在 `main` 上的 JSON：缺口注记、ORDERED 清点、FA-06 登记、FA-06 复核的 `EvidenceStateOrders`。一致表示注记复述了清点里 `AP-006` 与 `AP-009` 的字段，并且十行与登记里 `EvidenceState` 为 `REQUIRES_RUNTIME_ROOT` 的行同序。一致不表示运行根已准入，也不表示 BLOCK 已修复。本复核没有读取 `ENVIRONMENT_MANIFEST.md`，也没有打开历史虚拟环境或工具缓存。

说明与 JSON 一致。本复核不补行、不重排、不发明路径。

### 4.1 AP-006

注记与清点的字段一致，且未修复：

| 字段 | 注记与清点已经写下的值 |
| --- | --- |
| 路径 | `runtime_identity.declared_startup_sequence` |
| 选择器 | `runtime_identity.startup_contract` |
| 模式 | `ORDERED` |
| 状态 | `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` |
| 实际定位 | null |
| 候选行数 | 0 |
| 准入 | `NOT_ADMITTED` |
| BLOCK | `NO_RUNTIME_ROOT_LOCATOR`，未修复 |

清点明细仍是：读集里没有启动序列工件、SHA 或唯一定位，实际定位保持 null。本复核不补启动步骤，也不给出新的路径。

### 4.2 AP-009

注记与清点的字段一致，且未修复：

| 字段 | 注记与清点已经写下的值 |
| --- | --- |
| 路径 | `import_contract.lookup_order` |
| 选择器 | `import_contract.origin_policy` |
| 模式 | `ORDERED` |
| 状态 | `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` |
| 实际定位 | null |
| 候选行数 | 0 |
| 准入 | `NOT_ADMITTED` |
| BLOCK | `NO_RUNTIME_ROOT_LOCATOR`，未修复 |

清点明细仍是：读集里没有搜索序列工件、SHA 或唯一定位，实际定位保持 null。本复核不补查询身份，也不发明导入顺序。

### 4.3 十行 `REQUIRES_RUNTIME_ROOT`

登记的 `REQUIRES_RUNTIME_ROOT` 计数是 10。FA-06 复核记下的行号，与注记、与登记，是同一列表：2、5、7、10、12、15、48、55、60、61。每一行的 `Order`、`ItemId`、`Title`、`SourcePath`、`WrittenState`、`EvidenceState`、`Disposed` 都与登记相同。`Disposed` 都是 false。

| 行 | 条目 | 对照 |
| --- | --- | --- |
| 2 | `RDM-V2-06` | 字段相符，未处置 |
| 5 | `RDM-V2-09` | 字段相符，未处置 |
| 7 | `RDM-V2-06` | 字段相符，未处置 |
| 10 | `RDM-V2-09` | 字段相符，未处置 |
| 12 | `RDM-V2-06` | 字段相符，未处置 |
| 15 | `RDM-V2-09` | 字段相符，未处置 |
| 48 | `RUNTIME_ROOT` | 字段相符，未处置 |
| 55 | `FULL_DEPENDENCY_PROVENANCE_AND_CHECK_TO_USE` | 字段相符，未处置 |
| 60 | `full_dependency_provenance` | 字段相符，未处置 |
| 61 | `full_dependency_provenance` | 字段相符，未处置 |

这十行与 `AP-006`、`AP-009` 的未修复 BLOCK `NO_RUNTIME_ROOT_LOCATOR` 仍是同一道运行根障碍。本复核不把这一句写成定位，也不把 BLOCK 标成已修复。

## 5. 需要单独记下的所见

这些所见不准入运行根，不修复任何代码，也不选中任何 FA-05 选项。

### 5.1 两条政策字段相符，且都未定位

`AP-006` 与 `AP-009` 在缺口注记和 ORDERED 清点里是同一字段。状态都是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。实际定位都是 null。候选行数都是 0。BLOCK 代码都是 `NO_RUNTIME_ROOT_LOCATOR`，`Repaired` 都是 false。字段相同只说明注记复述了已经写下的障碍。它不是定位，也不是准入。

### 5.2 十行相符，且都未处置

十行的七个对照字段与 FA-06 登记相同，行号也与 FA-06 复核的 `REQUIRES_RUNTIME_ROOT` 列表相同。每一行的 `Disposed` 都是 false。相符是字段对照。它不是处置，也不是运行根准入。

### 5.3 注记引用的 FA-06 所见没有重跑

注记点名 FA-06 复核的 `F-02`、`F-03`、`F-05`，并写下自己没有重跑那 21 项核对。`F-02` 仍是：第 55、60、61 行是分类，`LOCAL_SYNTHETIC_ONLY` 与 `PASS` 没有被写进登记行。`F-03` 仍是：若干行的标题引自含有 Manifest 一词的句子，其中包括第 2、7、12、15 行，这些句子不表示 Manifest 已经生成。`F-05` 仍是：第 48 行只是来源与根候选里 `RUNTIME_ROOT` 与列 `不能据此认定` 相交的单元格，不是 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 的第二份设计复核。本复核也没有重跑那三项，也没有新增一份会处置这些行的所见。

### 5.4 没有运行根定位被准入

注记的 `LocatorSuppliedByThisNote` 是 false。两条实际定位都是 null。本复核没有打开定位交付物，没有尝试实际定位，没有发明启动序列，没有发明导入查询顺序，也没有写入任何运行根路径。`ENVIRONMENT_MANIFEST.md`、历史 Windows 虚拟环境和工具缓存都没有被读取。`NO_RUNTIME_ROOT_LOCATOR` 保持未修复。`NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` 保持原样。

### 5.5 FA-05 三个选项仍未选中

缺口注记的 JSON 与已经在库的 FA-05 选项表，三项 `OptionId` 同序：`KEEP_REV1_RECORD`、`FUTURE_STATIC_IDENTITY_NOTE_ONLY`、`NOT_AVAILABLE_UNDER_PATH_B`。每一项的 `Selected` 与 `Opened` 都是 false。注记说明用中文记下这三项都没有被选中，也没有被打开。选项表的 `NoteWritten` 仍是 false。没有 Harness SHA 被接受。本复核不选中任何一项，也不写日后的字节身份注记。

四个文件的当前字节仍与注记、选项表以及 REV1 所记身份相同。散列不是调用，也不是执行。四个 SHA 都没有被接受：

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | 107849 | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | 68768 | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json` | 770 | `9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | 4555 | `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445` |

### 5.6 七个捕获候选与三个实际侧仍保持原状

七个 `DSP_004_CAPTURE_RESULT_*` 的当前字节仍与 FA-03 候选所记散列相同，也与 REV12 复核所记散列相同。选择状态仍是 `NOT_SELECTED`，准入状态仍是 `NOT_ADMITTED`。本复核只做字节散列，没有导入，没有挑选，没有执行。

三个实际侧仍是 `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。身份与捕获入口仍是 null。FA-03 候选 JSON 仍是 12081 字节，`73DCBAB6AC60E79955C8755D820D9377DCEF1D2F32CABB01EA279DA9B81D859A`。本复核不绑定它们，也不接受该 SHA。

## 6. 两个 REV3 SHA 与来源根 SHA 仍不是接受

类型合同 REV3 仍是 29240 字节，`AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F`。数组政策 REV3 仍是 16317 字节，`39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。本次重新散列只核对身份。两者都不是正式 B-02 合同。

来源与根候选仍是 21257 字节，`57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93`。本复核不是该 SHA 的第二份设计复核，也没有新增那样一份文件，也没有接受该 SHA。第 48 行仍只是登记里已经写下的单元格。

## 7. 剩余筹备缺口的次序

这一节只给仍留着的筹备缺口排次序。它不打开任何交付物，不修复任何 BLOCK，不选中 FA-05 的任何一个选项，也不处置任何 FA-06 行。

1. `DSP004-FA-06` 的保留仍未接受。登记和独立复核都未接受。最近的资产决定是哪些 LIMITED 可以保留。本复核不写处置文件，也不处置任何一行。
2. `AP-006` 与 `AP-009` 的缺口注记已经有本独立静态复核。复核未接受。准入状态仍是 `NOT_ADMITTED`。两条政策仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。BLOCK 代码仍是 `NO_RUNTIME_ROOT_LOCATOR`，且未修复。实际定位仍是 null。清点读集里的候选行数仍是 0。十行 `REQUIRES_RUNTIME_ROOT` 仍未处置。本复核不准入运行根，也不打开定位交付物。
3. `DSP004-FA-05` 的选项表已经有 REV12 的独立静态复核。那份复核未接受。准入状态仍是 `NOT_ADMITTED`。`KEEP_REV1_RECORD`、`FUTURE_STATIC_IDENTITY_NOTE_ONLY`、`NOT_AVAILABLE_UNDER_PATH_B` 都没有被选中，也都没有被打开。本复核不选中任何一个选项。
4. `AP-020`、`AP-021`、`AP-022` 的 BLOCK 注记已经有 REV11 的独立静态复核。那份复核未接受。准入状态仍是 `NOT_ADMITTED`。BLOCK 代码仍未修复。本复核不打开修复交付物。
5. Manifest、正式运行、`DSP004-FA-08` 和 DSP-004 关闭仍无授权，排在最后。

`DSP004-FA-06` 因此仍是 `未建立充分前提`。`DSP004-FA-05` 仍未完成。`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

## 8. 本记录的效力

```text
INDEPENDENT STATIC REVIEW RECORDED — FINDINGS ONLY

缺口注记的准入：NOT_ADMITTED
Signed / Accepted：false / false
AP-006 / AP-009：NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT
实际定位：null / null
候选行数：0 / 0
BLOCK：NO_RUNTIME_ROOT_LOCATOR，未修复
运行根：未准入
FA-06 十行 REQUIRES_RUNTIME_ROOT：未处置
FA-05 三个选项：未选中，未打开
Harness SHA：未接受
DSP004-FA-06：未建立充分前提
DSP004-FA-05：未完成，选项未选中
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY
DSP004-FA-04：未完成
B-01：OPEN
B-02：OPEN
DSP004-FA-08：未完成
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

本记录不接受 `E6ED064272226185FCD10A5FDBE3AA192B742A5E728B0D55A973251AE3A9E474`，也不接受 `26C2C5C308570ACE020CD628D5E517BCEEFE2A96E04BFC57CE38F905163B0C26`。本记录不接受 `E44A36331C3679C04B3923E000077F1AF83329B075AF5D27ECD19DD92D68D063` 与 `1C84529D4746327835622CDCA713F6FC714D992CAC474A8425C322B6EAEDDB17`。本记录不接受 `5D90088CA5FE820FD766DAB37CB4AC8502F612EF4F5101F5718B9AB85B31DAA2` 与 `E512F379D32634F5F6C25DE3980BA1CE9D0DAB35BEB9837AECB43A5EC2C98B2B`。本记录不接受 `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5` 与 `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7`。本记录不接受 `AAF90D311F2C85C48EF652E903D4B430D1F339F1FA465527DE679087F30B2305` 与 `500015848949A8B789E0E44F2BB21AE0676D50B9440EA89124BB30CDC8B06254`。本记录不接受 `776FE8B24D6F0DFD31EC577393C66A84C16A99C1494CE8BF060A4AA59D814928` 与 `1EDA163811CB0EF31E32898B968C39C7A464B55C1DD73D1EC83F30F68F6415BA`。本记录不接受 `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430`、`92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5`、`9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` 与 `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445`。本记录也不接受 `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。这些 SHA 都不是正式合同。来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 也没有被接受。

本记录不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`，不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，也不关闭 DSP-004。不为来源与根候选新增第二份设计复核文件。商业 P0 保持原样。没有真实案件、个人信息、凭据或供应商调用。

21 项机器核对全部通过。通过表示身份与 REV8、REV12 所记一致，并且注记里 `AP-006`、`AP-009` 的字段与 ORDERED 清点一致，十行 `REQUIRES_RUNTIME_ROOT` 与 FA-06 登记一致。通过不表示来源准入，不表示 SHA 接受，不表示运行根已准入，不表示 BLOCK 已修复，也不表示 DSP-004 关闭。
