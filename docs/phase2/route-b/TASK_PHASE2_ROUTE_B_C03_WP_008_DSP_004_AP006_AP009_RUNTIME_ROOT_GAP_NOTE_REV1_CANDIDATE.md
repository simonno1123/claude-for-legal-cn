# DSP-004 AP-006 与 AP-009 运行根缺口注记候选 REV1

本注记只记录路径 B 下已经在 `main` 上的一道运行根障碍。对象限于 ORDERED 清点里的 `AP-006` 与 `AP-009`，以及 FA-06 剩余 LIMITED 登记里已经写成 `REQUIRES_RUNTIME_ROOT` 的十行。它不打开定位，不发明路径，不补启动序列，不补导入查询顺序，不修复 BLOCK，不接受资产，不准入来源，不处置任何 FA-06 行，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。新增筹备事实的名称是 `AP006_AP009_RUNTIME_ROOT_GAP_NOTE_NOT_ADMITTED`。

## 1. 形成基准

| 项目 | 本注记的事实 |
| --- | --- |
| 形成时 `HEAD` | `d2f8f62536cb2de3ab8c09e634281202a1e19487` |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV7.md` |
| 前一增量说明 SHA-256 | `1167FB1144495AF0BE11D7D172E889E675918785759D2D27B149EF4913BF42FB`（8112 字节） |
| 前一增量 JSON SHA-256 | `21FC18821036AB38C7855766B93236865EDE0DDE03795834ABA848F8A122A3C1`（7310 字节） |
| 机器可读注记 | `validation/route_b_c03/wp_008/DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE.json` |
| 该注记 SHA-256 | `26C2C5C308570ACE020CD628D5E517BCEEFE2A96E04BFC57CE38F905163B0C26` |
| 该注记字节 | 17687 |
| 受测模块导入或执行 | 未进行 |
| `identity_gate` 调用 | 未进行 |
| Fixture 执行或写入 | 未进行 |
| 场景运行器 | 未运行 |
| 捕获代码 | 未执行 |
| 商业 P0 | 未执行，未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 标准库只做字节散列，并读取已经在 `main` 上的 REV7、ORDERED 清点、FA-06 登记和该登记的独立静态复核。REV7 JSON 的 7310 字节与 `21FC18821036AB38C7855766B93236865EDE0DDE03795834ABA848F8A122A3C1` 与 REV7 说明所记一致。这次重新散列不把 REV7 接受为正式合同或来源准入。

点名一个 SHA 只固定文本身份。本注记不把下列任何 SHA 接受为正式合同、Manifest 或来源准入。

## 2. ORDERED 清点里已经写下的 AP-006 与 AP-009

清点说明与 JSON 本次重新散列。字节与 REV4 所记身份一致。不接受，不准入。

| 文件 | 字节 | SHA-256 | 本注记后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.md` | 15858 | `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5` | 已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.json` | 70228 | `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7` | 已引用，未准入 |

本注记只引用这两条政策。清点里的其余政策不在本注记里重写，也不修复。

| Policy ID | 路径 | 选择器 | 状态 | 实际定位 | 候选行数 | BLOCK |
| --- | --- | --- | --- | --- | --- | --- |
| `AP-006` | `runtime_identity.declared_startup_sequence` | `runtime_identity.startup_contract` | `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` | null | 0 | `NO_RUNTIME_ROOT_LOCATOR`，未修复 |
| `AP-009` | `import_contract.lookup_order` | `import_contract.origin_policy` | `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` | null | 0 | `NO_RUNTIME_ROOT_LOCATOR`，未修复 |

两行的模式都是 `ORDERED`。准入状态都是 `NOT_ADMITTED`。`CandidateRows` 为空。清点读集里的候选行数是 0。实际定位保持 null。

清点说明已经写明：读集里没有启动序列文件，也没有搜索序列文件。两份绑定文件里没有 `startup_contract`、`origin_policy`、`declared_startup_sequence` 或 `lookup_order`。缺项的 BLOCK 代码是 `NO_RUNTIME_ROOT_LOCATOR`。`Repaired` 为 false。清点对 `AP-006` 写下的明细是：读集里没有启动序列工件、SHA 或唯一定位，实际定位保持 null。对 `AP-009` 写下的明细是：读集里没有搜索序列工件、SHA 或唯一定位，实际定位保持 null。

本注记不补启动步骤，不补查询身份，不发明启动序列，不发明导入顺序，也不给出任何新的路径。

## 3. FA-06 登记里的十行 REQUIRES_RUNTIME_ROOT

登记说明与 JSON 本次重新散列。字节与 REV6、REV7 所记身份一致。不接受，不处置。`DSP004-FA-06` 仍是 `未建立充分前提`。

| 文件 | 字节 | SHA-256 | 本注记后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE.md` | 22701 | `AAF90D311F2C85C48EF652E903D4B430D1F339F1FA465527DE679087F30B2305` | 已引用，未准入，未处置 |
| `validation/route_b_c03/wp_008/DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE.json` | 38377 | `500015848949A8B789E0E44F2BB21AE0676D50B9440EA89124BB30CDC8B06254` | 已引用，未准入，未处置 |

已经在 `main` 上的独立静态复核也本次重新散列。复核结论仍是所见。`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。本注记不重跑那 21 项核对，也不把复核接受为来源准入。

| 文件 | 字节 | SHA-256 | 本注记后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.md` | 14868 | `776FE8B24D6F0DFD31EC577393C66A84C16A99C1494CE8BF060A4AA59D814928` | 所见已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.json` | 59047 | `1EDA163811CB0EF31E32898B968C39C7A464B55C1DD73D1EC83F30F68F6415BA` | 所见已引用，未准入 |

复核已经写下的 `REQUIRES_RUNTIME_ROOT` 行号是 2、5、7、10、12、15、48、55、60、61。本注记按登记原文列出这十行。十行的 `Disposed` 都是 false。它们与 `AP-006`、`AP-009` 的未修复 BLOCK `NO_RUNTIME_ROOT_LOCATOR` 是同一道运行根障碍。本注记不把这一句写成定位，也不把 BLOCK 标成已修复。

| 行 | 条目 | 标题 | 来源 | 来源所写状态 | Disposed |
| --- | --- | --- | --- | --- | --- |
| 2 | `RDM-V2-06` | Authorize static Manifest generation with accepted input, harness, runtime roots and origin-policy evidence | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_CANDIDATE.md` | NOT AUTHORIZED | false |
| 5 | `RDM-V2-09` | Establish separately accepted environment/startup/network assurances and exact run authority | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_CANDIDATE.md` | BLOCKED | false |
| 7 | `RDM-V2-06` | Authorize static Manifest generation with accepted input, harness, runtime roots and origin-policy evidence | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_1_CANDIDATE.md` | NOT AUTHORIZED | false |
| 10 | `RDM-V2-09` | Establish separately accepted environment/startup/network assurances and exact run authority | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_1_CANDIDATE.md` | BLOCKED | false |
| 12 | `RDM-V2-06` | Before generation, separately authorize and accept exact preparation root-binding sources and the complete typed encoding/array-order policy; then authorize static Manifest generation with accepted input, harness, environment and origin-policy evidence | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md` | NOT AUTHORIZED / ROOT AND ENCODING PREREQUISITES NOT ESTABLISHED BY THIS DOCUMENT | false |
| 15 | `RDM-V2-09` | Establish separately accepted environment/startup/network assurances and exact run authority; reference and recheck the already accepted preparation root bindings and completed Manifest, not create the root source retroactively | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md` | BLOCKED | false |
| 48 | `RUNTIME_ROOT` | 完整依赖来源、闭包或检查到使用保护 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SOURCE_ROOT_ADMISSION_PREPARATION_REV1_CANDIDATE.md` | 不能据此认定 | false |
| 55 | `FULL_DEPENDENCY_PROVENANCE_AND_CHECK_TO_USE` | FULL_DEPENDENCY_PROVENANCE_AND_CHECK_TO_USE | `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/attempt_02_result.json` | remaining_limited | false |
| 60 | `full_dependency_provenance` | LIMITED | `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/attempt_02_result.json` | runtime_after | false |
| 61 | `full_dependency_provenance` | LIMITED | `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/attempt_02_result.json` | runtime_before | false |

复核里与这十行相关、且本注记只作引用的所见是：

- `F-02`：第 55、60、61 行是分类。第 55 行因完整依赖来源标签而为 `REQUIRES_RUNTIME_ROOT`。第 60、61 行分别是 `runtime_after` 与 `runtime_before` 下的 `full_dependency_provenance`。`LOCAL_SYNTHETIC_ONLY` 与 `PASS` 没有被写进登记行。
- `F-03`：若干行的标题引自含有 Manifest 一词的句子，其中包括第 2、7、12、15 行。这些句子不表示 Manifest 已经生成。`PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json` 仍不存在。
- `F-05`：第 48 行只是来源与根候选里 `RUNTIME_ROOT` 与列 `不能据此认定` 相交的单元格。标题是单元格文字。这不是 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 的第二份设计复核。

本注记不新增第七项所见，也不处置任何一行。

## 4. 本注记没有读取、没有做的事

- 未读取 `ENVIRONMENT_MANIFEST.md`。
- 未读取历史 Windows 虚拟环境。
- 未读取工具缓存。
- 未使用目录列举顺序。
- 未发明启动序列，也未发明导入查询顺序。
- 未打开定位交付物，未尝试实际定位，未写入任何新的运行根路径。
- 未修复 `NO_RUNTIME_ROOT_LOCATOR`，也未修复 `AP-020`、`AP-021`、`AP-022` 的 BLOCK。
- 未创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`，未生成 Manifest，未授权正式运行。
- 未调用 `identity_gate`，未执行 Fixture，未运行场景运行器，未执行捕获代码。
- 三个实际侧仍为 null / `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。
- 七个 `DSP_004_CAPTURE_RESULT_*` 仍是 `NOT_SELECTED` / `NOT_ADMITTED`。
- 两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 未接受为正式 B-02 合同。
- 不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。第 48 行仍只是登记里已经写下的单元格。
- 不改商业 P0。

## 5. 剩余筹备缺口的次序

这一节只给仍留着的筹备缺口排次序。它不打开下一项交付物，不修复任何 BLOCK，也不选择 FA-05 的任何一个选项。本注记已经记下运行根障碍。`AP-006` 与 `AP-009` 仍然不能定位。

1. `DSP004-FA-06` 仍是 `未建立充分前提`。登记和独立复核都未接受。最近的资产决定是哪些 LIMITED 可以保留。本注记不写处置文件，也不处置十行里的任何一行。
2. `AP-006` 与 `AP-009` 的缺口注记已经写下，准入状态是 `NOT_ADMITTED`。两条政策仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。BLOCK 代码仍是 `NO_RUNTIME_ROOT_LOCATOR`，且未修复。实际定位仍是 null。清点读集里的候选行数仍是 0。上面十行仍与这一缺口是同一道运行根障碍，`Disposed` 仍为 false。本注记不打开定位交付物。
3. `DSP004-FA-05` 仍停在 REV1 已经记下的事实。下面三个选项都没有被选中，本注记也不打开它们。
   - 维持 REV1。输入候选仍是 `NOT_ADMITTED`。没有 Harness SHA 被接受。下列四个文件的字节仍与 REV1 所记相同。本次只用标准库重新散列。散列不是调用，也不是执行。
   - 若日后另有授权，可以只做字节身份注记。本注记不写那份注记。
   - 路径 B 下不可用的做法是：准入输入候选、接受 Harness SHA，或运行 `identity_gate` 与 Fixture。
4. `AP-020`、`AP-021`、`AP-022` 的已准入唯一序列仍留在 REV5 已经记下的 BLOCK 之后。本注记不修复这些代码。
5. Manifest、正式运行、`DSP004-FA-08` 和 DSP-004 关闭仍无授权，排在最后。

维持 REV1 时仍核对到的四个文件是：

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | 107849 | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | 68768 | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json` | 770 | `9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | 4555 | `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445` |

## 6. 本记录的效力

```text
RUNTIME ROOT GAP NOTE RECORDED — NOT LOCATED — NOT ADMITTED

AP-006 / AP-009：NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT
实际定位：null / null
候选行数：0 / 0
BLOCK：NO_RUNTIME_ROOT_LOCATOR，未修复
FA-06 十行 REQUIRES_RUNTIME_ROOT：未处置
Signed / Accepted：false / false
准入：NOT_ADMITTED
DSP004-FA-06：未建立充分前提
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY
DSP004-FA-04：未完成
B-01：OPEN
B-02：OPEN
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。`DSP004-FA-06` 仍是 `未建立充分前提`。

本注记不接受 `1167FB1144495AF0BE11D7D172E889E675918785759D2D27B149EF4913BF42FB`，也不接受 `21FC18821036AB38C7855766B93236865EDE0DDE03795834ABA848F8A122A3C1`。本注记不接受 `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5` 与 `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7`。本注记不接受 `AAF90D311F2C85C48EF652E903D4B430D1F339F1FA465527DE679087F30B2305` 与 `500015848949A8B789E0E44F2BB21AE0676D50B9440EA89124BB30CDC8B06254`。本注记也不接受 `776FE8B24D6F0DFD31EC577393C66A84C16A99C1494CE8BF060A4AA59D814928` 与 `1EDA163811CB0EF31E32898B968C39C7A464B55C1DD73D1EC83F30F68F6415BA`。这些 SHA 都不是正式合同。
