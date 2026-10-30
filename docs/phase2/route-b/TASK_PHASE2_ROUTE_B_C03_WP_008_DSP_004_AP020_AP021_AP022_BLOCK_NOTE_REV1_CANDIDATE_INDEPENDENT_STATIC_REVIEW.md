# DSP-004 AP-020、AP-021、AP-022 BLOCK 注记候选 REV1 — 独立静态复核

本记录是路径 B 筹备增量 REV10 之后的在库只读复核。对象是已经在 `main` 上的 `AP-020`、`AP-021`、`AP-022` BLOCK 注记候选 REV1。复核确认它的字节，并核对该注记列出的 BLOCK 代码是否与已经在库的 ORDERED 清点、以及 REV5 独立静态复核所记的代码表一致。它不接受这两个 SHA，不修复任何 BLOCK，不准入任何定位，不合并候选序列，不挑选其中一份，也不关闭 B-01、B-02 或 DSP-004。

依据仍是已经记入的路径 B 原句：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

新增筹备事实的名称是 `AP020_AP021_AP022_BLOCK_NOTE_INDEPENDENT_STATIC_REVIEW_NOT_ACCEPTED`。注记自己的筹备事实名称仍是 `AP020_AP021_AP022_BLOCK_NOTE_NOT_ADMITTED`。本复核不改写那个名称。

## 1. 复核基准

| 项目 | 本记录的事实 |
| --- | --- |
| 复核时 `HEAD` | `8a4e67da27594e33a8f323b763e00ba0ccaef3e8` |
| BLOCK 注记物化提交 | `8a4e67da27594e33a8f323b763e00ba0ccaef3e8`（PR #14） |
| 注记自述形成时 `HEAD` | `9cfc1e8b4ed4b6494c330e6c8950856ed9bf2c70` |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV10.md` |
| 前一增量说明 SHA-256 | `F27B5298638183DE96A313FB01FB7A0E565593D2E4337987087F6F8C720076F7`（9927 字节） |
| 前一增量 JSON SHA-256 | `A4A1B268B3DD1E7BAE4DCC2C729B931AF9E554F552E0FF8CA1EF3F63E7F59188`（8376 字节） |
| 机器可读结果 | `validation/route_b_c03/wp_008/DSP_004_AP020_AP021_AP022_BLOCK_NOTE_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.json` |
| 该结果 SHA-256 | `80C4D8DB6946E08A2A5287CC3D2075AF1E968AE9FE98AA8C8CC7B29019E93ABB` |
| 该结果字节 | 33478 |
| 受测模块导入或执行 | 未进行 |
| `identity_gate` 导入或调用 | 未进行 |
| Fixture 打开、执行或写入 | 未进行 |
| 绑定文件打开 | 未进行 |
| 场景运行器 | 未运行 |
| 捕获代码 | 未导入，未执行 |
| 商业 P0 | 未执行，未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 标准库只做字节散列和 JSON 结构读取。读集是这份注记的说明与机器结果、REV10 增量的说明与机器结果、ORDERED 清点的说明与机器结果，以及 REV5 对 FA-03 与 ORDERED 清点的独立静态复核。两个 REV3 文本和来源与根候选只重新散列，用来确认身份。七个 `DSP_004_CAPTURE_RESULT_*` 只重新散列。未重跑 REV5 的 21 项核对，未打开十五个 Fixture 文件，未打开两份绑定文件，未导入 `identity_gate`、合同模块、捕获候选或场景运行器，未执行 Fixture，未写入 Fixture，未编译 C#，未重放业务场景，未生成 Manifest。未读取 `ENVIRONMENT_MANIFEST.md`，未读取历史 Windows 虚拟环境，未读取工具缓存。

这是同仓库内的后续静态复核，不是跨供应商外审，也不是 Project Owner 对这份注记的接受。结论只是所见。`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。

## 2. 两个物理文件

复核前 REV10 以及 PR #14 记下的身份，与当前 `HEAD` 上的字节一致。物化提交就是当前 `HEAD`，其后没有新提交。注记在形成时 `HEAD` `9cfc1e8b4ed4b6494c330e6c8950856ed9bf2c70` 上还不存在。ORDERED 清点与 REV5 复核在那个形成时 `HEAD` 与当前 `HEAD` 上是同一个 git blob。

| 文件 | 路径 | 字节 | SHA-256 |
| --- | --- | --- | --- |
| 注记说明 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_AP020_AP021_AP022_BLOCK_NOTE_REV1_CANDIDATE.md` | 15543 | `01A98020D1E2524D1E6F953F028950A02BD317BE45A4E973E43B37B953FF5A27` |
| 注记 JSON | `validation/route_b_c03/wp_008/DSP_004_AP020_AP021_AP022_BLOCK_NOTE_REV1_CANDIDATE.json` | 19308 | `C1C00CEA5DF3D5EBE0BB7861308339B32007CC6FD97E5957981B49D1AEFBCA3D` |

两份文件均为 UTF-8、无 BOM、无 CR、无行尾空白。说明文件嵌入自己配套 JSON 的 SHA-256。本复核的 SHA 不在那份说明里。

点名一个 SHA 只固定文本身份。本复核不把这两个 SHA 接受为正式合同、Manifest 或来源准入。

注记自己的 `Signed` 与 `Accepted` 均为 false，准入状态是 `NOT_ADMITTED`。`BlocksRepaired`、`LocatorsAdmitted`、`SequencesMerged`、`SequencesSelected` 均为 false。`UniqueLocatorEstablished` 为 false。`AppearanceMatchIsPass` 与 `AppearanceMatchIsAdmission` 均为 false。`IndependentReviewChecksRerun` 为 false。

## 3. 已经绑定、仍未接受的来源

REV10 说明本次重新散列是 9927 字节，`F27B5298638183DE96A313FB01FB7A0E565593D2E4337987087F6F8C720076F7`。REV10 JSON 是 8376 字节，`A4A1B268B3DD1E7BAE4DCC2C729B931AF9E554F552E0FF8CA1EF3F63E7F59188`。该 JSON SHA 就是 REV10 说明里写下的 SHA。这次重新散列不把 REV10 接受为正式合同或来源准入。

| 文件 | 字节 | SHA-256 | 本复核后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV10.md` | 9927 | `F27B5298638183DE96A313FB01FB7A0E565593D2E4337987087F6F8C720076F7` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV10.json` | 8376 | `A4A1B268B3DD1E7BAE4DCC2C729B931AF9E554F552E0FF8CA1EF3F63E7F59188` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.md` | 15858 | `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5` | 已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.json` | 70228 | `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7` | 已引用，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA03_AND_ORDERED_INVENTORY_REV1_CANDIDATES_INDEPENDENT_STATIC_REVIEW.md` | 11092 | `3723F4A36E3EF9761AEE094A49D579DFAC22D317E2870FAB702B1D02A7FA51AC` | 所见已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_FA03_AND_ORDERED_INVENTORY_REV1_CANDIDATES_INDEPENDENT_STATIC_REVIEW.json` | 18456 | `48AB6F18FEEB43FD15EF342B5E5516655EB8EE619261AABAF367D227027FB6A1` | 所见已引用，未准入 |

清点与 REV5 复核的字节与注记所引身份一致，也与 REV4、REV5 所记身份一致。本复核不重跑那 21 项核对，也不把它们接受为来源准入。

## 4. BLOCK 代码对照

对照只读三份已经在 `main` 上的 JSON：注记、ORDERED 清点、REV5 复核的 `OrderedBlockGrounding`。代码表一致表示注记复述了清点里 `Disposition` 为 `BLOCK` 的代码，并且与 REV5 所记列表同序。一致不表示代码已修复，也不表示定位已准入。本复核没有打开 Fixture 文件，也没有打开绑定文件。

说明与 JSON 一致。行数保持：`AP-020` 17，`AP-021` 2，`AP-022` 30。清点形成记录里的 `Reordered`、`ItemsInvented`、`DuplicatesRemoved` 均为 false。注记的 `RowsReordered`、`RowsAdded`、`DuplicatesRemoved` 均为 false。本复核不重排、不去重、不补行。每一条 BLOCK 的 `Repaired` 都是 false。实际序列定位都是 null。`UniqueLocatorEstablished` 都是 false。每一行候选状态都是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。

### 4.1 AP-020

注记、清点里 `Disposition` 为 `BLOCK` 的所见、以及 REV5 条目 `IR-13` 的代码表同序，恰好三条，均未修复：

| 代码 | 注记与清点已经写下的状态 |
| --- | --- |
| `FIXTURE_CATALOG_ARTIFACT_ABSENT` | 未修复 |
| `FIXTURE_FILES_ARE_SEPARATE_OBJECTS` | 未修复 |
| `FIXTURE_IDENTITIES_IS_A_MAP` | 未修复 |

清点候选行是 17。其中 15 行位置是 `$.scenario_id`，2 行位置是 `$.fixture_identities`。选择器仍是 `manifest_identity.fixture_catalog`，政策路径仍是 `input_contract.fixtures`。实际序列定位是 null。`UniqueLocatorEstablished` 是 false。本复核不准入这 17 行，也不把十五个文件拼成目录。

### 4.2 AP-021

注记、清点里 `Disposition` 为 `BLOCK` 的所见、以及 REV5 条目 `IR-14` 的代码表同序，恰好两条，均未修复：

| 代码 | 注记与清点已经写下的状态 |
| --- | --- |
| `LOCATOR_NOT_UNIQUE` | 未修复 |
| `SOURCE_NOT_ADMITTED` | 未修复 |

另有一条处置 `OUT_OF_ARRAY_OCCURRENCE_NOT_MERGED`。清点的 `Disposition` 是 `RECORDED_NOT_INSERTED`。注记的 `IsBlock` 是 false，`InsertedByThisNote` 是 false。它不是第三条 BLOCK。本复核没有把它插入 `$.scenarios`。

两行候选仍是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。位置都是 `$.scenarios`。清点所记字段偏移是 24523 与 40336，计数都是 15。文内状态分别是 `MATERIALIZED_NOT_REVIEWED_NOT_ADMITTED` 与 `MATERIALIZED_NOT_FORMALLY_REVIEWED_NOT_ACCEPTED_NOT_ADMITTED`。两行都没有被挑选。两个数组没有合并。实际序列定位是 null。`UniqueLocatorEstablished` 是 false。

### 4.3 AP-022

注记、清点所见、以及 REV5 条目 `IR-15` 的代码表同序，恰好五条，均未修复：

| 代码 | 注记与清点已经写下的状态 |
| --- | --- |
| `POLICY_IDENTITY_FIELD_ABSENT` | 未修复 |
| `OBSERVED_FIELD_NAME_DIFFERS` | 未修复 |
| `LOCATOR_NOT_UNIQUE` | 未修复 |
| `SOURCE_NOT_ADMITTED` | 未修复 |
| `CANDIDATE_SEQUENCES_DIFFER` | 未修复 |

三十行仍是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。文件内项数仍是 25 与 28。`variant_id` 出现次数仍是 0。键 `variants` 出现次数仍是 0。`FieldRenamed` 是 false。`C03-TA-V-002` 保留两条顺序，计数是 2 与 5。其余十四个场景的外观相同，仍然是两行。两条顺序没有合并，也没有被挑选。实际序列定位是 null。`UniqueLocatorEstablished` 是 false。`AppearanceMatchIsPass` 是 false。

REV5 条目 `IR-16` 记下的行数仍是这 17、2、30。本复核不重跑 `IR-16`。

## 5. 需要单独记下的所见

这些所见不修复任何代码，也不准入任何定位。

### 5.1 三份代码表同序

`AP-020` 三条、`AP-021` 两条、`AP-022` 五条，在注记、清点的 BLOCK 所见和 REV5 的 `OrderedBlockGrounding` 里是同一顺序。每一条被对照的 `Repaired` 都是 false。代码表相同只说明注记复述了已经写下的代码。它不是修复，也不是准入。

### 5.2 数组外出现仍留在 BLOCK 表之外

`OUT_OF_ARRAY_OCCURRENCE_NOT_MERGED` 在清点的 `AP-021` 所见里，`Disposition` 是 `RECORDED_NOT_INSERTED`。注记把它标成不是 BLOCK，并且没有插入。本复核也没有插入。

### 5.3 外观相符仍不是通过

清点的两条 `AP-021` 候选行记下外观与 `C03-TA-V-001` 至 `C03-TA-V-015` 的具名范围相同，同时 `MatchIsNotAPass` 与 `MatchIsNotAdmission` 均为 true。注记的 `AppearanceMatchIsPass` 与 `AppearanceMatchIsAdmission` 均为 false。`AP-022` 的十四个场景外观相同，仍然是两行。`C03-TA-V-002` 的两条顺序都保留，计数是 2 与 5。清点里 `SB-002-UNREACHABLE-AUTHORITY-COMPARISON` 仍在原绑定的两项顺序上。五项顺序没有被抄到另一份文件。两条顺序都没有被挑选。

### 5.4 唯一序列定位仍未建立

注记和清点里三条政策的 `UniqueLocatorEstablished` 都是 false。实际序列定位都是 null。49 行候选都是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。本复核不准入其中任何一行。

### 5.5 注记没有重跑 REV5，本复核也不重跑

注记点名 REV5 的 `IR-13`、`IR-14`、`IR-15`、`IR-16`，并写下 `IndependentReviewChecksRerun` 为 false。本复核只把这些代码表与清点 JSON 对照。没有按 Fixture 字节重做那四项核对，没有打开 Fixture 或绑定文件，没有给出修复，也没有打开修复交付物。

### 5.6 七个捕获候选与三个实际侧仍保持原状

七个 `DSP_004_CAPTURE_RESULT_*` 的当前字节仍与 FA-03 所记散列相同。选择状态仍是 `NOT_SELECTED`，准入状态仍是 `NOT_ADMITTED`。本复核只做字节散列，没有导入，没有挑选，没有执行。

三个实际侧仍是 `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。身份与捕获入口仍是 null。本复核不绑定它们。

## 6. 两个 REV3 SHA 与来源根 SHA 仍不是接受

类型合同 REV3 仍是 29240 字节，`AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F`。数组政策 REV3 仍是 16317 字节，`39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。本次重新散列只核对身份。两者都不是正式 B-02 合同。

来源与根候选仍是 21257 字节，`57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93`。本复核不是该 SHA 的第二份设计复核，也没有新增那样一份文件，也没有接受该 SHA。

## 7. 剩余筹备缺口的次序

这一节只给仍留着的筹备缺口排次序。它不打开任何交付物，不修复任何 BLOCK，不选中 FA-05 的任何一个选项，也不处置任何 FA-06 行。

1. `DSP004-FA-06` 的保留仍未接受。登记和独立复核都未接受。最近的资产决定是哪些 LIMITED 可以保留。本复核不写处置文件，也不处置任何一行。
2. `AP-006` 与 `AP-009` 仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。缺口注记已经写下，准入状态是 `NOT_ADMITTED`。BLOCK 代码仍是 `NO_RUNTIME_ROOT_LOCATOR`，且未修复。实际定位仍是 null。本复核不打开定位交付物，也不读取 `ENVIRONMENT_MANIFEST.md`、历史 Windows 虚拟环境或工具缓存。
3. `DSP004-FA-05` 的选项表已经写下，准入状态是 `NOT_ADMITTED`。`KEEP_REV1_RECORD`、`FUTURE_STATIC_IDENTITY_NOTE_ONLY`、`NOT_AVAILABLE_UNDER_PATH_B` 都没有被选中，也都没有被打开。本复核不选中任何一个选项。
4. `AP-020`、`AP-021`、`AP-022` 的 BLOCK 注记已经有本独立静态复核。复核未接受。准入状态仍是 `NOT_ADMITTED`。BLOCK 代码仍未修复。实际序列定位仍是 null。候选行仍是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。本复核不打开修复交付物。
5. Manifest、正式运行、`DSP004-FA-08` 和 DSP-004 关闭仍无授权，排在最后。

`DSP004-FA-06` 因此仍是 `未建立充分前提`。`DSP004-FA-05` 仍未完成。`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

## 8. 本记录的效力

```text
INDEPENDENT STATIC REVIEW RECORDED — FINDINGS ONLY

BLOCK 注记的准入：NOT_ADMITTED
Signed / Accepted：false / false
AP-020 BLOCK：未修复
AP-021 BLOCK：未修复
AP-022 BLOCK：未修复
实际序列定位：null / null / null
UniqueLocatorEstablished：false
外观相符：不是通过，也不是准入
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

本记录不接受 `01A98020D1E2524D1E6F953F028950A02BD317BE45A4E973E43B37B953FF5A27`，也不接受 `C1C00CEA5DF3D5EBE0BB7861308339B32007CC6FD97E5957981B49D1AEFBCA3D`。本记录不接受 `F27B5298638183DE96A313FB01FB7A0E565593D2E4337987087F6F8C720076F7` 与 `A4A1B268B3DD1E7BAE4DCC2C729B931AF9E554F552E0FF8CA1EF3F63E7F59188`。本记录不接受 `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5` 与 `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7`。本记录不接受 `3723F4A36E3EF9761AEE094A49D579DFAC22D317E2870FAB702B1D02A7FA51AC` 与 `48AB6F18FEEB43FD15EF342B5E5516655EB8EE619261AABAF367D227027FB6A1`。本记录也不接受 `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。这些 SHA 都不是正式合同。来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 也没有被接受。

本记录不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`，不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，也不关闭 DSP-004。不为来源与根候选新增第二份设计复核文件。商业 P0 保持原样。没有真实案件、个人信息、凭据或供应商调用。

21 项机器核对全部通过。通过表示身份与 REV10 所记一致，并且注记里 `AP-020`、`AP-021`、`AP-022` 的 BLOCK 代码表与 ORDERED 清点及 REV5 复核所记列表一致。通过不表示来源准入，不表示 SHA 接受，不表示 BLOCK 已修复，也不表示 DSP-004 关闭。
