# DSP-004 FA-05 选项表候选 REV1 — 独立静态复核

本记录是路径 B 筹备增量 REV11 之后的在库只读复核。对象是已经在 `main` 上的 FA-05 选项表候选 REV1。复核确认它的字节，并核对三个选项的标识、次序、`Selected`、`Opened`，以及 `KEEP_REV1_RECORD` 下四个文件的字节，是否与已经在库的 REV7、REV8、REV9 和 REV1 记录一致。它不接受这些 SHA，不选中任何一个选项，不打开任何一个选项，不接受 Harness SHA，不准入输入候选，不调用 `identity_gate`，不执行 Fixture，不修复任何 BLOCK，也不关闭 B-01、B-02 或 DSP-004。

依据仍是已经记入的路径 B 原句：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

新增筹备事实的名称是 `FA05_OPTIONS_SHEET_INDEPENDENT_STATIC_REVIEW_NOT_ACCEPTED`。选项表自己的筹备事实名称仍是 `FA05_OPTIONS_SHEET_NOT_SELECTED_NOT_ADMITTED`。本复核不改写那个名称。

## 1. 复核基准

| 项目 | 本记录的事实 |
| --- | --- |
| 复核时 `HEAD` | `13320d0292092cd9e0b99cc0012b63fc08689145` |
| 选项表物化提交 | `9cfc1e8b4ed4b6494c330e6c8950856ed9bf2c70`（PR #13） |
| 选项表自述形成时 `HEAD` | `7d73f50ede1b5e4ec8aa55f85270eb50b9cafa92` |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV11.md` |
| 前一增量说明 SHA-256 | `455917864A70F5D8A0A861A57A1AEC8F2F6FF6C9FF8EDF2A1DBCBA344F7DEA33`（11359 字节） |
| 前一增量 JSON SHA-256 | `77B3812FFF704A4F9F71F93592372049E30C9CB140D18EC01B888B3E1C5ECC5D`（9550 字节） |
| 机器可读结果 | `validation/route_b_c03/wp_008/DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.json` |
| 该结果 SHA-256 | `3BEC8B6BE1173C4A22374F21C3726218F8F16AA7C520C9391D10B1752889755A` |
| 该结果字节 | 35336 |
| 受测模块导入或执行 | 未进行 |
| `identity_gate` 导入或调用 | 未进行 |
| Fixture 执行或写入 | 未进行 |
| 场景运行器 | 未运行 |
| 捕获代码 | 未导入，未执行 |
| 商业 P0 | 未执行，未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 标准库只做字节散列和 JSON 结构读取。读集是这份选项表的说明与机器结果、REV11 增量的说明与机器结果、REV9、REV8、REV7、REV1 的说明与机器结果、运行根缺口注记的说明与机器结果、四个被点名文件的字节、FA-03 候选里三个实际侧与七个捕获候选的字节，以及两个 REV3 文本和来源与根候选的字节。散列只固定文本身份。散列不是调用，也不是执行。`identity_gate.py` 没有被导入，也没有被调用。Fixture 文件没有被执行。未重跑 REV1 的两层结果，未导入捕获候选或场景运行器，未编译 C#，未重放业务场景，未生成 Manifest。未读取 `ENVIRONMENT_MANIFEST.md`，未读取历史 Windows 虚拟环境，未读取工具缓存。

这是同仓库内的后续静态复核，不是跨供应商外审，也不是 Project Owner 对这份选项表的接受。结论只是所见。`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。三个选项的准入状态都是 `NOT_ADMITTED`。

## 2. 两个物理文件

复核前 REV9 以及 PR #13 记下的身份，与当前 `HEAD` 上的字节一致。物化提交是 `9cfc1e8b4ed4b6494c330e6c8950856ed9bf2c70`。当前 `HEAD` 是 `13320d0292092cd9e0b99cc0012b63fc08689145`。选项表在这两处是同一个 git blob。选项表在形成时 `HEAD` `7d73f50ede1b5e4ec8aa55f85270eb50b9cafa92` 上还不存在。REV1、REV7、REV8 与运行根缺口注记在那个形成时 `HEAD` 与当前 `HEAD` 上是同一个 git blob。

| 文件 | 路径 | 字节 | SHA-256 |
| --- | --- | --- | --- |
| 选项表说明 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE.md` | 10924 | `6C6F505258E30C1A31033E35C85797969CD387D79357E312830DF17DB785BEC4` |
| 选项表 JSON | `validation/route_b_c03/wp_008/DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE.json` | 12147 | `88F4B087169910561F51874E83C4B41A4D7873916136048F1A3DFF30E287CAF8` |

两份文件均为 UTF-8、无 BOM、无 CR、无行尾空白。说明文件嵌入自己配套 JSON 的 SHA-256。本复核的 SHA 不在那份说明里。

点名一个 SHA 只固定文本身份。本复核不把这两个 SHA 接受为正式合同、Manifest 或来源准入。

选项表自己的 `Signed` 与 `Accepted` 均为 false，准入状态是 `NOT_ADMITTED`。`AnyOptionSelected` 与 `AnyOptionOpened` 均为 false。`HarnessShaAccepted` 为 false。输入候选未被准入。

## 3. 已经绑定、仍未接受的来源

REV11 说明本次重新散列是 11359 字节，`455917864A70F5D8A0A861A57A1AEC8F2F6FF6C9FF8EDF2A1DBCBA344F7DEA33`。REV11 JSON 是 9550 字节，`77B3812FFF704A4F9F71F93592372049E30C9CB140D18EC01B888B3E1C5ECC5D`。该 JSON SHA 就是 REV11 说明里写下的 SHA。这次重新散列不把 REV11 接受为正式合同或来源准入。

| 文件 | 字节 | SHA-256 | 本复核后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV11.md` | 11359 | `455917864A70F5D8A0A861A57A1AEC8F2F6FF6C9FF8EDF2A1DBCBA344F7DEA33` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV11.json` | 9550 | `77B3812FFF704A4F9F71F93592372049E30C9CB140D18EC01B888B3E1C5ECC5D` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV9.md` | 9220 | `AB7D4233FBDF41A362BFD0360AC9BCB82C7C45D280BB55FECB801ABD0C18D159` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV9.json` | 8091 | `80A76D83CE91B012608F784712F76B329F37AA7B93A5A3073C5DDE3122165C09` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV8.md` | 10123 | `5D90088CA5FE820FD766DAB37CB4AC8502F612EF4F5101F5718B9AB85B31DAA2` | 已引用，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV8.json` | 9629 | `E512F379D32634F5F6C25DE3980BA1CE9D0DAB35BEB9837AECB43A5EC2C98B2B` | 已引用，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE.md` | 15149 | `E6ED064272226185FCD10A5FDBE3AA192B742A5E728B0D55A973251AE3A9E474` | 已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_AP006_AP009_RUNTIME_ROOT_GAP_NOTE_REV1_CANDIDATE.json` | 17687 | `26C2C5C308570ACE020CD628D5E517BCEEFE2A96E04BFC57CE38F905163B0C26` | 已引用，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV7.md` | 8112 | `1167FB1144495AF0BE11D7D172E889E675918785759D2D27B149EF4913BF42FB` | 选项次序已引用，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV7.json` | 7310 | `21FC18821036AB38C7855766B93236865EDE0DDE03795834ABA848F8A122A3C1` | 选项次序已引用，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV1.md` | 7595 | `F612F938B9F7897DFE71D4B9E5668D98C9C83B89368C18309E12963A22AE6ED0` | 四文件身份已引用，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV1.json` | 5737 | `045D2DC6C9ED53CB8F795E670A35653576095AE4D2224139F426CFF01C39CA4B` | 四文件身份已引用，未接受 |

REV9 JSON 的 8091 字节与 `80A76D83CE91B012608F784712F76B329F37AA7B93A5A3073C5DDE3122165C09` 与 REV9 说明所记一致。选项表的字节与 REV9 以及 PR #13 所记身份一致。本复核不把它们接受为来源准入。

## 4. 三个选项对照

对照只读已经在 `main` 上的 JSON：选项表、REV7、REV8、REV9。一致表示选项标识与次序相同，并且每一项的 `Selected` 与 `Opened` 都是 false。四个文件的路径、字节和 SHA-256 相同。说明文字没有被当成逐字节相同。一致不表示某个选项已被选中，也不表示来源已准入。本复核没有调用 `identity_gate`，也没有执行 Fixture。

说明与 JSON 一致。三个选项保持原次序。本复核不重排、不增项、不选中。

### 4.1 `KEEP_REV1_RECORD`

选项表、REV7、REV8、REV9 的第一项都是 `KEEP_REV1_RECORD`。`Selected` 为 false。`Opened` 为 false。输入候选仍是 `NOT_ADMITTED`。没有 Harness SHA 被接受。四个文件的当前字节与选项表、REV1、REV7、REV8、REV9 所记身份相同：

| 文件 | 字节 | SHA-256 | REV1 已经记下的状态 |
| --- | --- | --- | --- |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | 107849 | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` | `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | 68768 | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | 未覆盖 |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json` | 770 | `9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` | 仍要求 `BLOCKED_ISOLATED` / `BOUNDARY_MISMATCH` |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | 4555 | `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445` | 仍被记为返回 `REJECTED — ISOLATION FAILURE` |

这四条状态来自 REV1 记录。本复核没有调用 `identity_gate`，也没有执行 Fixture。四个 SHA 都没有被接受为正式合同。本复核没有选中 `KEEP_REV1_RECORD`。

### 4.2 `FUTURE_STATIC_IDENTITY_NOTE_ONLY`

选项表、REV7、REV8、REV9 的第二项都是 `FUTURE_STATIC_IDENTITY_NOTE_ONLY`。`Selected` 为 false。`Opened` 为 false。选项表的 `NoteWritten` 是 false。本复核不写那份日后的字节身份注记，也不打开这一项。

### 4.3 `NOT_AVAILABLE_UNDER_PATH_B`

选项表、REV7、REV8、REV9 的第三项都是 `NOT_AVAILABLE_UNDER_PATH_B`。`Selected` 为 false。`Opened` 为 false。REV7 与 REV8 已经把这一项写成路径 B 下不可用的做法：准入输入候选、接受 Harness SHA，或运行 `identity_gate` 与 Fixture。选项表只继续记录这一项。本复核不选中它，也不打开它。

## 5. 需要单独记下的所见

这些所见不选中任何选项，也不接受任何 SHA。

### 5.1 三份选项表同序，且都未选中

`KEEP_REV1_RECORD`、`FUTURE_STATIC_IDENTITY_NOTE_ONLY`、`NOT_AVAILABLE_UNDER_PATH_B` 在选项表、REV7、REV8、REV9 里是同一顺序。选项表的 `AlreadyRankedOrder` 是 1、2、3。每一项的 `Selected` 与 `Opened` 都是 false。次序相同只说明选项表复述了已经写下的三项。它不是选择，也不是准入。

### 5.2 四个文件身份相符，且都未接受

四个文件的路径、字节和 SHA-256 与选项表、REV1 的 `InputHarness`、REV7、REV8、REV9 以及当前磁盘一致。输入候选保持 `NOT_ADMITTED`。原始绑定在选项表里的状态是 `NOT_OVERWRITTEN`，对应 REV1 说明里的未覆盖。Fixture 仍被记为要求 `BLOCKED_ISOLATED` / `BOUNDARY_MISMATCH`。`identity_gate.py` 仍被记为返回 `REJECTED — ISOLATION FAILURE`。相符是字段对照。它不是调用，也不是执行。

### 5.3 FA-05 仍停在 REV1 记录

选项表的 `FA05` 状态是 `INCOMPLETE`。`StillAtRev1Record` 是 true。输入候选准入是 `NOT_ADMITTED`。`HarnessShaAccepted` 是 false。记在 REV1 的合成检查数是 189，并且这些检查不是输入准入。门禁的隔离失败与 Fixture 的 `BLOCKED_ISOLATED` 仍是两层结果。`ThisSheetReranThoseLayers` 是 false。本复核也没有重跑这两层，也没有把其中任何一层写成通过。

### 5.4 没有 Harness SHA 被接受

选项表、REV1、REV7、REV8、REV9 都记下没有 Harness SHA 被接受。REV1 的 `InputHarness.HarnessShaAccepted` 是 false。选项表没有记下任何一份已被接受的 Harness 摘要。本复核不接受 Harness SHA。

### 5.5 日后字节注记没有被写，路径 B 不可用项没有被打开

`FUTURE_STATIC_IDENTITY_NOTE_ONLY` 的 `NoteWritten` 是 false。本复核没有写那份注记。`NOT_AVAILABLE_UNDER_PATH_B` 仍是 `Selected` false、`Opened` false。把“路径 B 不准入输入候选、不接受 Harness SHA、不运行 `identity_gate` 或 Fixture”继续记下来，不是把这一项选成当前做法。

### 5.6 七个捕获候选与三个实际侧仍保持原状

七个 `DSP_004_CAPTURE_RESULT_*` 的当前字节仍与 FA-03 候选所记散列相同，也与 REV11 复核所记散列相同。选择状态仍是 `NOT_SELECTED`，准入状态仍是 `NOT_ADMITTED`。本复核只做字节散列，没有导入，没有挑选，没有执行。

三个实际侧仍是 `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。身份与捕获入口仍是 null。FA-03 候选 JSON 仍是 12081 字节，`73DCBAB6AC60E79955C8755D820D9377DCEF1D2F32CABB01EA279DA9B81D859A`。本复核不绑定它们，也不接受该 SHA。

## 6. 两个 REV3 SHA 与来源根 SHA 仍不是接受

类型合同 REV3 仍是 29240 字节，`AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F`。数组政策 REV3 仍是 16317 字节，`39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。本次重新散列只核对身份。两者都不是正式 B-02 合同。

来源与根候选仍是 21257 字节，`57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93`。本复核不是该 SHA 的第二份设计复核，也没有新增那样一份文件，也没有接受该 SHA。

## 7. 剩余筹备缺口的次序

这一节只给仍留着的筹备缺口排次序。它不打开任何交付物，不选中 FA-05 的任何一个选项，不修复任何 BLOCK，也不处置任何 FA-06 行。

1. `DSP004-FA-06` 的保留仍未接受。登记和独立复核都未接受。最近的资产决定是哪些 LIMITED 可以保留。本复核不写处置文件，也不处置任何一行。
2. `AP-006` 与 `AP-009` 仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。缺口注记已经写下，准入状态是 `NOT_ADMITTED`。BLOCK 代码仍是 `NO_RUNTIME_ROOT_LOCATOR`，且未修复。实际定位仍是 null。本复核不打开定位交付物，也不读取 `ENVIRONMENT_MANIFEST.md`、历史 Windows 虚拟环境或工具缓存。
3. `DSP004-FA-05` 的选项表已经有本独立静态复核。复核未接受。准入状态仍是 `NOT_ADMITTED`。`KEEP_REV1_RECORD`、`FUTURE_STATIC_IDENTITY_NOTE_ONLY`、`NOT_AVAILABLE_UNDER_PATH_B` 都没有被选中，也都没有被打开。本复核不选中任何一个选项，也不打开进一步的 FA-05 交付物。
4. `AP-020`、`AP-021`、`AP-022` 的 BLOCK 注记已经有 REV11 的独立静态复核。那份复核未接受。准入状态仍是 `NOT_ADMITTED`。BLOCK 代码仍未修复。本复核不打开修复交付物。
5. Manifest、正式运行、`DSP004-FA-08` 和 DSP-004 关闭仍无授权，排在最后。

`DSP004-FA-06` 因此仍是 `未建立充分前提`。`DSP004-FA-05` 仍未完成。`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

## 8. 本记录的效力

```text
INDEPENDENT STATIC REVIEW RECORDED — FINDINGS ONLY

选项表的准入：NOT_ADMITTED
三个选项的准入：NOT_ADMITTED
Signed / Accepted：false / false
KEEP_REV1_RECORD：Selected false / Opened false
FUTURE_STATIC_IDENTITY_NOTE_ONLY：Selected false / Opened false
NOT_AVAILABLE_UNDER_PATH_B：Selected false / Opened false
输入候选：NOT_ADMITTED
Harness SHA：未接受
identity_gate：未调用
Fixture：未执行
DSP004-FA-05：未完成，选项未选中
DSP004-FA-06：未建立充分前提
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY
DSP004-FA-04：未完成
B-01：OPEN
B-02：OPEN
DSP004-FA-08：未完成
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

本记录不接受 `6C6F505258E30C1A31033E35C85797969CD387D79357E312830DF17DB785BEC4`，也不接受 `88F4B087169910561F51874E83C4B41A4D7873916136048F1A3DFF30E287CAF8`。本记录不接受 `455917864A70F5D8A0A861A57A1AEC8F2F6FF6C9FF8EDF2A1DBCBA344F7DEA33` 与 `77B3812FFF704A4F9F71F93592372049E30C9CB140D18EC01B888B3E1C5ECC5D`。本记录不接受 `AB7D4233FBDF41A362BFD0360AC9BCB82C7C45D280BB55FECB801ABD0C18D159` 与 `80A76D83CE91B012608F784712F76B329F37AA7B93A5A3073C5DDE3122165C09`。本记录不接受 `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430`、`92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5`、`9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` 与 `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445`。本记录也不接受 `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。这些 SHA 都不是正式合同。来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 也没有被接受。

本记录不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`，不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，也不关闭 DSP-004。不为来源与根候选新增第二份设计复核文件。商业 P0 保持原样。没有真实案件、个人信息、凭据或供应商调用。

21 项机器核对全部通过。通过表示身份与 REV9、REV11 所记一致，并且选项表里的三个选项与 REV7、REV8、REV9 的标识和次序一致，四个文件字段与 REV1 记录一致。通过不表示来源准入，不表示 SHA 接受，不表示某个选项已被选中，也不表示 DSP-004 关闭。
