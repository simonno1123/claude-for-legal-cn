# DSP-004 FA-05 选项表候选 REV1

本选项表只记录路径 B 下 REV7 与 REV8 已经排好的三个 FA-05 选项。三个选项的 `Selected` 与 `Opened` 都是 false。它不选中任何选项，不准入输入候选，不接受任何 Harness SHA，不把 Fixture 或 `identity_gate.py` 的 SHA 接受为正式合同，不调用 `identity_gate`，不执行 Fixture，不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。新增筹备事实的名称是 `FA05_OPTIONS_SHEET_NOT_SELECTED_NOT_ADMITTED`。

## 1. 形成基准

| 项目 | 本选项表的事实 |
| --- | --- |
| 形成时 `HEAD` | `7d73f50ede1b5e4ec8aa55f85270eb50b9cafa92` |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV8.md` |
| 前一增量说明 SHA-256 | `5D90088CA5FE820FD766DAB37CB4AC8502F612EF4F5101F5718B9AB85B31DAA2`（10123 字节） |
| 前一增量 JSON SHA-256 | `E512F379D32634F5F6C25DE3980BA1CE9D0DAB35BEB9837AECB43A5EC2C98B2B`（9629 字节） |
| 机器可读选项表 | `validation/route_b_c03/wp_008/DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE.json` |
| 该选项表 SHA-256 | `88F4B087169910561F51874E83C4B41A4D7873916136048F1A3DFF30E287CAF8` |
| 该选项表字节 | 12147 |
| 受测模块导入或执行 | 未进行 |
| `identity_gate` 导入或调用 | 未进行 |
| Fixture 执行或写入 | 未进行 |
| 场景运行器 | 未运行 |
| 捕获代码 | 未执行 |
| 商业 P0 | 未执行，未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 标准库只做字节散列，并读取已经在 `main` 上的 REV8 与运行根缺口注记。散列只固定文本身份。散列不是调用，也不是执行。`identity_gate.py` 没有被导入，也没有被调用。Fixture 文件没有被执行。

REV8 JSON 的 9629 字节与 `E512F379D32634F5F6C25DE3980BA1CE9D0DAB35BEB9837AECB43A5EC2C98B2B` 与 REV8 说明所记一致，也与 PR #12 所记一致。REV8 说明本次重新散列是 10123 字节，`5D90088CA5FE820FD766DAB37CB4AC8502F612EF4F5101F5718B9AB85B31DAA2`。这次重新散列不把 REV8 接受为正式合同或来源准入。当前 `HEAD` 在写入本选项表之前是 `7d73f50ede1b5e4ec8aa55f85270eb50b9cafa92`。

已经在 `main` 上的运行根缺口注记本次重新散列。字节与 REV8 所记身份一致。不接受，不准入。

| 文件 | 字节 | SHA-256 | 本选项表后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV8.md` | 10123 | `5D90088CA5FE820FD766DAB37CB4AC8502F612EF4F5101F5718B9AB85B31DAA2` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV8.json` | 9629 | `E512F379D32634F5F6C25DE3980BA1CE9D0DAB35BEB9837AECB43A5EC2C98B2B` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE.md` | 15149 | `E6ED064272226185FCD10A5FDBE3AA192B742A5E728B0D55A973251AE3A9E474` | 已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE.json` | 17687 | `26C2C5C308570ACE020CD628D5E517BCEEFE2A96E04BFC57CE38F905163B0C26` | 已引用，未准入 |

点名一个 SHA 只固定文本身份。本选项表不把下列任何 SHA 接受为正式合同、Manifest 或来源准入。

## 2. FA-05 仍停在 REV1 已经记下的事实

`DSP004-FA-05` 未完成。输入候选保持 `NOT_ADMITTED`。没有 Harness SHA 被接受。189 项合成检查不是输入准入。REV1 已经把门禁的隔离失败与 Fixture 的 `BLOCKED_ISOLATED` 记成两层结果。本选项表不重跑这两层，也不把其中任何一层写成通过。

## 3. 三个已经排好的选项

这一节按 REV7 与 REV8 已经写下的次序记录三个选项。次序不是选择。三个选项的 `Selected` 都是 false，`Opened` 都是 false。本选项表不打开其中任何一个。

### 3.1 `KEEP_REV1_RECORD`

`Selected` 为 false。`Opened` 为 false。维持 REV1。输入候选仍是 `NOT_ADMITTED`。没有 Harness SHA 被接受。下列四个文件的字节仍与 REV1、REV7、REV8 所记身份相同。本次只用标准库重新散列。散列不是调用，也不是执行。

| 文件 | 字节 | SHA-256 | REV1 已经记下的状态 |
| --- | --- | --- | --- |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | 107849 | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` | `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | 68768 | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | 未覆盖 |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json` | 770 | `9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` | 仍要求 `BLOCKED_ISOLATED` / `BOUNDARY_MISMATCH` |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | 4555 | `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445` | 仍被记为返回 `REJECTED — ISOLATION FAILURE` |

这四条状态来自 REV1 记录。本选项表没有调用 `identity_gate`，也没有执行 Fixture。四个 SHA 都没有被接受为正式合同。

### 3.2 `FUTURE_STATIC_IDENTITY_NOTE_ONLY`

`Selected` 为 false。`Opened` 为 false。若日后另有授权，可以只做字节身份注记。本选项表不写那份注记。

### 3.3 `NOT_AVAILABLE_UNDER_PATH_B`

`Selected` 为 false。`Opened` 为 false。REV7 与 REV8 已经把这一项写成路径 B 下不可用的做法：准入输入候选、接受 Harness SHA，或运行 `identity_gate` 与 Fixture。本选项表只继续记录这一项，不选中它，也不打开它。

## 4. 硬性边界

- 不选中任何选项。三个选项的 `Selected` 与 `Opened` 保持 false。
- 不准入 `SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json`，也不准入 `SCENARIO_INPUT_BINDING.json`。
- 不把任何 Harness SHA、Fixture SHA 或 `identity_gate.py` 的 SHA 接受为正式合同。
- 不调用 `identity_gate`。散列该文件只固定字节身份。
- 不执行 Fixture，也不把 Fixture 结果写成通过。
- 不运行场景运行器，不执行捕获代码。
- 不接受资产，不准入来源，不生成 Manifest，不授权正式运行，不关闭 DSP-004。
- 不处置任何 FA-06 行，不修复 `AP-006`、`AP-009`、`AP-020`、`AP-021`、`AP-022` 的 BLOCK。

## 5. 剩余筹备缺口的次序

这一节只给仍留着的筹备缺口排次序。它不打开任何进一步的交付物，不选中 FA-05 的任何一个选项，也不修复任何 BLOCK。本选项表已经记下三个未选选项。`DSP004-FA-05` 仍然未完成。

1. `DSP004-FA-06` 仍是 `未建立充分前提`。登记和独立复核都未接受。最近的资产决定是哪些 LIMITED 可以保留。本选项表不写处置文件，也不处置任何一行。
2. `AP-006` 与 `AP-009` 的缺口注记已经写下，准入状态是 `NOT_ADMITTED`。两条政策仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。BLOCK 代码仍是 `NO_RUNTIME_ROOT_LOCATOR`，且未修复。实际定位仍是 null。清点读集里的候选行数仍是 0。十行 `REQUIRES_RUNTIME_ROOT` 仍与这一缺口是同一道运行根障碍。本选项表不打开定位交付物。
3. `DSP004-FA-05` 的选项表已经写下，准入状态是 `NOT_ADMITTED`。三个选项都没有被选中，也都没有被打开。本选项表不打开进一步的 FA-05 交付物。
4. `AP-020`、`AP-021`、`AP-022` 的已准入唯一序列仍留在 REV5 已经记下的 BLOCK 之后。本选项表不修复这些代码。
5. Manifest、正式运行、`DSP004-FA-08` 和 DSP-004 关闭仍无授权，排在最后。

## 6. 仍保留的状态

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。`DSP004-FA-05` 仍未完成。`DSP004-FA-06` 仍是 `未建立充分前提`。

三个实际侧仍为 null / `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。

七个 `DSP_004_CAPTURE_RESULT_*` 仍是 `NOT_SELECTED` / `NOT_ADMITTED`：

- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1.py`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_FIXED_BOOTSTRAP_CANDIDATE_REV1.py`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV1.py`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV2.py`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV3.py`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_OUTER_SUPERVISOR_CANDIDATE_REV1.cs`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_OUTER_SUPERVISOR_CANDIDATE_REV2.cs`

两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 未接受为正式 B-02 合同。不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。

## 7. 本记录的效力

```text
FA-05 OPTIONS SHEET RECORDED — NONE SELECTED — NOT ADMITTED

KEEP_REV1_RECORD：Selected false / Opened false
FUTURE_STATIC_IDENTITY_NOTE_ONLY：Selected false / Opened false
NOT_AVAILABLE_UNDER_PATH_B：Selected false / Opened false
输入候选：NOT_ADMITTED
Harness SHA：未接受
identity_gate：未调用
Fixture：未执行
Signed / Accepted：false / false
准入：NOT_ADMITTED
DSP004-FA-05：未完成
DSP004-FA-06：未建立充分前提
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY
DSP004-FA-04：未完成
B-01：OPEN
B-02：OPEN
DSP-004：OPEN / HOLD
```

本选项表不接受 `5D90088CA5FE820FD766DAB37CB4AC8502F612EF4F5101F5718B9AB85B31DAA2`，也不接受 `E512F379D32634F5F6C25DE3980BA1CE9D0DAB35BEB9837AECB43A5EC2C98B2B`。本选项表不接受 `E6ED064272226185FCD10A5FDBE3AA192B742A5E728B0D55A973251AE3A9E474` 与 `26C2C5C308570ACE020CD628D5E517BCEEFE2A96E04BFC57CE38F905163B0C26`。本选项表不接受 `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430`、`92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5`、`9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` 与 `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445`。这些 SHA 都不是正式合同。
