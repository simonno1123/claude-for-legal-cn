# DSP-004 路径 B 筹备增量 REV7

本增量只记录路径 B 下的下一项筹备事实：FA-06 剩余 LIMITED 登记候选 REV1 的在库独立静态复核。它不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV6.md` |
| 前一增量说明 | `4FFE7A40F5307EE6F2485F26ECA6719F0671E075843C18A5586D43B338B1518C`（4301 字节） |
| 前一增量 JSON | `48AB526A92412AFCD3CDB982E7A68FB936D5D6325C26C7506C83428A16799FDA`（2845 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV7.json` |
| 本增量 JSON SHA-256 | `21FC18821036AB38C7855766B93236865EDE0DDE03795834ABA848F8A122A3C1` |
| 本增量 JSON 字节 | 7310 |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。REV1 至 REV6 已经记下的筹备事实保持原样。本增量不改它们。

## 1. 新增筹备事实：FA-06 登记的在库复核

REV6 写入了 FA-06 剩余 LIMITED 登记候选。该登记当时还没有独立复核。该复核现已写入仓库。复核结论是身份、61 行追溯和六项所见，`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。没有任何一行被处置。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.md` | 14868 | `776FE8B24D6F0DFD31EC577393C66A84C16A99C1494CE8BF060A4AA59D814928` |
| `validation/route_b_c03/wp_008/DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.json` | 59047 | `1EDA163811CB0EF31E32898B968C39C7A464B55C1DD73D1EC83F30F68F6415BA` |

被复核的登记仍是：

| 文件 | 字节 | SHA-256 | 本增量后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE.md` | 22701 | `AAF90D311F2C85C48EF652E903D4B430D1F339F1FA465527DE679087F30B2305` | 已复核，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE.json` | 38377 | `500015848949A8B789E0E44F2BB21AE0676D50B9440EA89124BB30CDC8B06254` | 已复核，未准入 |

这些字节与 REV6 以及 PR #10 所记身份一致。当前 `HEAD` 在写入本增量之前是 `cbebe00a1d7557ab47a8052dbba7221f94073637`。

复核所见：

- 说明与 JSON 都是 61 行。`EVIDENCE_PRESENT_UNACCEPTED` 35 行，`EVIDENCE_ABSENT` 16 行，`REQUIRES_RUNTIME_ROOT` 10 行。`Disposed` 全部为 false。
- 每一行的来源、字节、SHA-256、条目标识、标题和来源所写状态都能落到已经在 `main` 上的文件。
- 见证文件点的是短名 `RQ-021`、`G-017`、`RQ-018`、`G-014`，没有四个完整条目号，也没有多出第五行。四项完整条目仍是 `EVIDENCE_PRESENT_UNACCEPTED`。
- `attempt_02_result.json` 的 `LOCAL_SYNTHETIC_ONLY` 与 `PASS` 没有被写进登记行。七个 `DSP_004_CAPTURE_RESULT_*` 仍是 `NOT_SELECTED` / `NOT_ADMITTED`。
- 点到 Manifest 的行仍保留来源自己的写法，没有表示该文件已经生成。`PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json` 仍不存在。
- 第 48 行只引用 `RUNTIME_ROOT` 单元格。本增量不是来源与根候选 SHA 的第二份设计复核。

`DSP004-FA-06` 仍是 `未建立充分前提`。`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

三个实际侧仍为 null / `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。REV1 点名的七个既有捕获候选仍是 `NOT_SELECTED` / `NOT_ADMITTED`。

## 2. 剩余筹备缺口的次序

这一节只给仍留着的筹备缺口排次序。它不打开任何交付物，不修复任何 BLOCK，也不选择 FA-05 的任何一个选项。

1. `DSP004-FA-06` 仍是 `未建立充分前提`。登记和本复核都未接受。最近的资产决定是哪些 LIMITED 可以保留。本增量不写处置文件。
2. `AP-006` 与 `AP-009` 在已经在库的 ORDERED 清点里仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。BLOCK 代码仍是 `NO_RUNTIME_ROOT_LOCATOR`，且未修复。登记里的 10 行 `REQUIRES_RUNTIME_ROOT` 与这一缺口是同一道运行根障碍。本增量不打开定位交付物，也不读取 `ENVIRONMENT_MANIFEST.md`、历史 Windows 虚拟环境或工具缓存。
3. `DSP004-FA-05` 仍停在 REV1 已经记下的事实。下面三个选项都没有被选中，本增量也不打开它们。
   - 维持 REV1。输入候选仍是 `NOT_ADMITTED`。没有 Harness SHA 被接受。下列四个文件的字节仍与 REV1 所记相同；散列不是调用，也不是执行。
   - 若日后另有授权，可以只做字节身份注记。本增量不写那份注记。
   - 路径 B 下不可用的做法是：准入输入候选、接受 Harness SHA，或运行 `identity_gate` 与 Fixture。
4. `AP-020`、`AP-021`、`AP-022` 的已准入唯一序列仍留在 REV5 已经记下的 BLOCK 之后。本增量不修复这些代码。
5. Manifest、正式运行、`DSP004-FA-08` 和 DSP-004 关闭仍无授权，排在最后。

维持 REV1 时仍核对到的四个文件是：

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | 107849 | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | 68768 | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json` | 770 | `9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | 4555 | `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445` |

## 3. 本增量故意不做的事

- 不准入任何来源，不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不把两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 接受为正式 B-02 合同。
- 不把 FA-06 登记的 SHA `AAF90D311F2C85C48EF652E903D4B430D1F339F1FA465527DE679087F30B2305` 与 `500015848949A8B789E0E44F2BB21AE0676D50B9440EA89124BB30CDC8B06254` 接受为正式合同或来源准入。
- 不完成 `DSP004-FA-03`，也不完成 `DSP004-FA-04`。B-01 与 B-02 保持 `OPEN`。
- 不完成 `DSP004-FA-06`。它仍是 `未建立充分前提`。本增量不处置任何 FA-06 行。
- 不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。
- 不改商业 P0。

## 4. 仍须以后的资产级决定

路径 B 没有代替下列决定：

- 哪些依赖、启动、隔离、停止与清理 LIMITED 可以保留
- 导入闭包、两侧调用身份、检查到使用的防替换，以及 T0 / PE / OS 证据
- `AP-006` 与 `AP-009` 在运行根确立之后的实际定位
- 三个实际侧的来源身份、版本、载体、定位、产生者职责、授权和已经绑定的捕获入口
- 另一次获准调用；只有那次调用发生时才允许读取实际引用
- 是否对两个 REV3 SHA 作固定 SHA 接受
- 是否对 FA-03、ORDERED 清点或 FA-06 登记的固定 SHA 作接受或准入
- 是否消除或继续保留四项已经点名的 LIMITED 审查项
- 是否在 FA-05 的三个未选选项里另作授权
- Manifest、正式运行和 DSP-004 关闭
