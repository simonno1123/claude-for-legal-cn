# DSP-004 FA-06 剩余 LIMITED 登记候选 REV1 — 独立静态复核

本记录是路径 B 筹备增量 REV6 之后的在库只读复核。对象是已经在 `main` 上的 FA-06 剩余 LIMITED 登记候选 REV1。复核确认它的字节，并核对 61 行的条目、证据状态和来源指针是否落在已经在库的文件上。它不处置任何一行，不把登记的 SHA 接受为正式合同，不准入来源，不完成 `DSP004-FA-06`，也不关闭 B-01、B-02 或 DSP-004。

依据仍是已经记入的路径 B 原句：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

## 1. 复核基准

| 项目 | 本记录的事实 |
| --- | --- |
| 复核时 `HEAD` | `cbebe00a1d7557ab47a8052dbba7221f94073637` |
| FA-06 登记物化提交 | `cbebe00a1d7557ab47a8052dbba7221f94073637`（PR #10） |
| 登记自述形成时 `HEAD` | `2a9636f45aa12bcfd9edefb045f6e764b6acfc29` |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV6.md` |
| 前一增量说明 SHA-256 | `4FFE7A40F5307EE6F2485F26ECA6719F0671E075843C18A5586D43B338B1518C`（4301 字节） |
| 前一增量 JSON SHA-256 | `48AB526A92412AFCD3CDB982E7A68FB936D5D6325C26C7506C83428A16799FDA`（2845 字节） |
| 机器可读结果 | `validation/route_b_c03/wp_008/DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.json` |
| 该结果 SHA-256 | `1EDA163811CB0EF31E32898B968C39C7A464B55C1DD73D1EC83F30F68F6415BA` |
| 该结果字节 | 59047 |
| 受测模块导入或执行 | 未进行 |
| `identity_gate` 调用 | 未进行 |
| Fixture 执行或写入 | 未进行 |
| 场景运行器 | 未运行 |
| 商业 P0 | 未执行，未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 标准库只做字节散列和 JSON 与文本结构读取。读集是这份登记的说明与机器结果、登记点名的十五个来源、两份虚拟环境缺失记录、静态核对见证、FA-03 候选里三个实际侧与七个捕获候选的字节、两份 REV3 文本的字节，以及 ORDERED 清点里 `AP-006` 与 `AP-009` 的已写状态。未导入 `identity_gate`、合同模块、捕获候选或场景运行器，未执行 Fixture，未写入 Fixture，未编译 C#，未重放业务场景，未生成 Manifest。未读取 `ENVIRONMENT_MANIFEST.md`，未读取历史 Windows 虚拟环境，未读取工具缓存。`attempt_02_result.json` 里写出的运行路径没有被打开。

这是同仓库内的后续静态复核，不是跨供应商外审，也不是 Project Owner 对这份登记的接受。结论只是所见。`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。

## 2. 两个物理文件

复核前 REV6 以及 PR #10 记下的身份，与当前 `HEAD` 上的字节一致。物化提交就是当前 `HEAD`，其后没有新提交。十五个来源、两份缺失记录和见证文件在形成时 `HEAD` 与当前 `HEAD` 上是同一个 git blob。

| 文件 | 路径 | 字节 | SHA-256 |
| --- | --- | --- | --- |
| 登记说明 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE.md` | 22701 | `AAF90D311F2C85C48EF652E903D4B430D1F339F1FA465527DE679087F30B2305` |
| 登记 JSON | `validation/route_b_c03/wp_008/DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE.json` | 38377 | `500015848949A8B789E0E44F2BB21AE0676D50B9440EA89124BB30CDC8B06254` |

两份文件均为 UTF-8、无 BOM、无 CR、无行尾空白。说明文件嵌入自己配套 JSON 的 SHA-256。本复核的 SHA 不在那份说明里。

点名一个 SHA 只固定文本身份。本复核不把这两个 SHA 接受为正式合同、Manifest 或来源准入。

## 3. 说明与机器结果的 61 行

说明里的表与 JSON 的 `Rows` 一致：61 行，同一来源顺序，同一条目标识、标题、来源所写状态和证据状态。`Disposed` 全部为 false。登记自己的 `Signed` 与 `Accepted` 均为 false，准入状态是 `NOT_ADMITTED`，`FA06Completed` 为 false。关卡 `DSP004-FA-06` 仍是 `未建立充分前提`。

| 证据状态 | 行数 | 行号 |
| --- | --- | --- |
| `EVIDENCE_PRESENT_UNACCEPTED` | 35 | 其余各行 |
| `EVIDENCE_ABSENT` | 16 | 3、4、8、9、13、14、26、37、38、41、43、44、46、56、57、59 |
| `REQUIRES_RUNTIME_ROOT` | 10 | 2、5、7、10、12、15、48、55、60、61 |

跨来源重复的条目标识仍各占一行，没有合并。`full_dependency_provenance` 仍是两行，分别对应 `runtime_after` 与 `runtime_before`。

## 4. 来源指针

每一行的来源路径都在 `main` 上。行内字节与 SHA-256 等于该文件。条目标识、标题和来源所写状态都出现在该文件正文里。没有一行的来源是 `DSP_004_CAPTURE_RESULT_*`。

| 来源 | 字节 | SHA-256 | 行数 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_CANDIDATE.md` | 36436 | `F3C3DCA20F5FC0AB22A38F61B5A6C2EE9B437AD949C18E93E27CB0D550AF0B4C` | 5 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_1_CANDIDATE.md` | 38995 | `07FD553F641CF52EF54FABFCFAD448CC2D432C8A0279082E6DB899EB8C900910` | 5 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md` | 54703 | `6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA` | 7 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_TRUSTED_IMPORT_AND_INPUT_BINDING_LIMITED_REVISION_PROPOSAL.md` | 27557 | `AC90F5DA143256FBC4F9409F0130FCB11D187E97DA550C72931B9209C3E71516` | 18 |
| `validation/route_b_c03/wp_008/V003_LIMITED_COMPARISON_RULE_DRAFT.md` | 17452 | `9A856FCC23FEAC15A32CB7CD68BF3A33B33801B6D3947AB646CB6FD2AD7E08C9` | 1 |
| `validation/route_b_c03/wp_008/V003_LIMITED_COMPARISON_RULE_STATIC_CHECK.md` | 14449 | `A46CCD928EE8CC4EB46D6BEBCBCF7CF53176EF2BF6ACC1116BDCDFBB9309A1D5` | 2 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_DSP_002_AUTHORITY_COMPARISON_REACHABILITY_LIMITED_SUBJECT_DESIGN_PROPOSAL.md` | 19838 | `85D7A4029D9667EFF7922CEDAA19570A7C6A68F36C2D6A66401F291B5F135A24` | 4 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FORMAL_ACCEPTANCE_OWNER_DECISION_PACKET_REV1.md` | 8630 | `9B0A3C048E479B714083952E76CF6620A2AE046EA23D2CC95192D967CF5A6736` | 3 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REMAINING_WORK_HANDOFF_REV1.md` | 14774 | `538283D7E48520B56B90ACA42A705A43AFEA468AF6DE8B7A46AE34636A3805AA` | 2 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SOURCE_ROOT_ADMISSION_PREPARATION_REV1_CANDIDATE.md` | 21257 | `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` | 1 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_1_CANDIDATE.md` | 49702 | `3432D99D22AA288668C8D4E2CF58975A794ED545B62EB05FCA9E0B41525AEDDB` | 1 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_2_CANDIDATE.md` | 54109 | `87EE2451298189FDDED9F49AC8106B902290A2AA38CD58158B5972F0BE4463BD` | 3 |
| `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/README.md` | 5952 | `BBAD8F847687531313C42F188AFDB24A2B9DAF645D9D7BDD6CFEFC06F19A0F64` | 1 |
| `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/RESUMPTION_RESULT.md` | 7419 | `2705BBDF9AAFC580DF6AE09EC51BC887011D54496E1296A8C243B367BAA8658A` | 1 |
| `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/attempt_02_result.json` | 50434 | `967B146EA3DECC79106DE191D83C79934BF16CDB8161B6230DBB8EECCF53D148` | 7 |

两份虚拟环境缺失记录的散列与登记所记一致，正文没有 LIMITED 条目，所以没有入行。`LR-06` 至 `LR-12` 仍在可信导入提案原文里，没有入行。`RDM-V2-01` 至 `RDM-V2-05` 仍在 Plan V2.2 原文里，没有入行。

四项已经点名的 LIMITED 审查项仍各占一行，证据状态都是 `EVIDENCE_PRESENT_UNACCEPTED`，`Disposed` 为 false。本复核不把它们标成消除。

| 条目 | 行号 |
| --- | --- |
| `C03-WP008-RDM-V2-RQ-018` | 16 |
| `C03-WP008-RDM-V2-G-014` | 17 |
| `C03-WP008-V3-RQ-021` | 51 |
| `C03-WP008-V3-G-017` | 52 |

`RDM-DSP-002` 在提案标题和文首也出现。第 42 行取的是 `DSP002-G-018` 之后的结果状态：标题是 `OPEN — PROPOSED LIMITED DESIGN ROUTE ONLY`，来源所写状态是 `MATERIALIZED — REVIEW NOT AUTHORIZED / NOT PERFORMED`。这不是把文首那一行挪到门禁之后。

## 5. 需要单独记下的所见

这些所见不改变任何一行的证据状态，也不处置任何一行。

### 5.1 见证文件用的是短名

`SCENARIO_INPUT_BINDING_V3_2_V2_2_STATIC_CHECK.md` 为 5420 字节，`D8263E8CCFBCF7892FB4BE5EBE8B34CFD32A25F12CD29606CC562D4803EEC668`。文件里没有四个完整条目号。原文是：V3.2 `RQ-021`、`G-017` 与 V2.2 `RQ-018`、`G-014` 的 LIMITED 条目不因此消除。顺序与登记见证所列一致。四个完整条目号已经分别写在 Plan V2.2 与 V3.2 的既有行里。见证文件没有因此多出第五行。

### 5.2 attempt_02 的状态是分类，不是合成通过的回填

第 55 至 61 行的来源是 `attempt_02_result.json`。该文件的 `scope` 是 `LOCAL_SYNTHETIC_ONLY`，`status` 是 `PASS`，`formal_acceptance` 是 `NOT_ESTABLISHED_BY_THIS_RUN`。文件没有 `expected` 字段。登记没有把 `PASS` 或 `LOCAL_SYNTHETIC_ONLY` 写进行内标题或来源所写状态，也没有写入运行散列或可执行文件路径。本复核没有打开那个路径。

第 55 至 59 行共用数组 `remaining_limited`。来源所写状态是这个键名，不是每一项旁边的另一套状态字。分类是：

| 行 | 分类依据 |
| --- | --- |
| 55 | 标签是完整依赖来源与检查到使用；同一文件的 `runtime_before` 与 `runtime_after` 里 `full_dependency_provenance` 均为 `LIMITED` |
| 56 | 标签写明 `UNOBSERVED` |
| 57 | 标签是强制终止后的持久保存，数组里没有另附观察 |
| 58 | 189 项计划的标签在库，没有被接受为 FA-06 的完成 |
| 59 | 同一文件的 `formal_acceptance` 是 `NOT_ESTABLISHED_BY_THIS_RUN` |
| 60、61 | `full_dependency_provenance` 的值是 `LIMITED`，父键分别是 `runtime_after` 与 `runtime_before` |

`SYNTHETIC-PROJECT-001`、`SYNTHETIC-SESSION-001`、`SYNTHETIC-PROVIDER-001` 都没有进入这 61 行。

### 5.3 Manifest 一词仍是来源引文

若干行的标题或来源所写状态引自含有 Manifest 一词的句子。这些行保留来源自己的写法：`NOT AUTHORIZED`、`BLOCKED`、`NOT ESTABLISHED`、设计要求条目、`no PASS is asserted`、提案门禁标题，或不创建 `PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。`validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json` 仍不存在。本复核没有创建它。没有任何一行表示 Manifest 已经生成。

### 5.4 七个捕获候选仍未挑选

七个 `DSP_004_CAPTURE_RESULT_*` 文件的当前字节仍与 FA-03 所记散列相同。选择状态仍是 `NOT_SELECTED`，准入状态仍是 `NOT_ADMITTED`。`attempt_02_result.json` 的 `protected_before` 与 `protected_after` 点了这些路径。登记没有把它们用作任何一行的来源。本复核只做字节散列，没有导入，没有挑选。

三个实际侧仍是 `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。身份与捕获入口仍是 null。

### 5.5 RUNTIME_ROOT 只是一个单元格

第 48 行来自来源与根候选里的这一格：`RUNTIME_ROOT` 与列 `不能据此认定` 相交，单元格文字是 `完整依赖来源、闭包或检查到使用保护`。来源所写状态是这一列表头。该文件仍是 21257 字节，`57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93`。本复核不是该 SHA 的第二份设计复核，也没有新增那样一份文件。

## 6. 两个 REV3 SHA 仍不是正式合同

类型合同 REV3 仍是 29240 字节，`AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F`。数组政策 REV3 仍是 16317 字节，`39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。本次重新散列只核对身份。两者都不是正式 B-02 合同。

## 7. 仍然缺少的事项

登记自己的未完成事项，加上本复核不能代替的接受，仍然包括：

- 哪些依赖、启动、隔离、停止与清理 LIMITED 可以保留
- 导入闭包、两侧调用身份、检查到使用的防替换，以及 T0 / PE / OS 证据
- `AP-006` 与 `AP-009` 在运行根确立之后的实际定位
- 三个实际侧的来源身份、版本、载体、定位、产生者职责、授权和已经绑定的捕获入口
- 这份登记的固定 SHA 接受
- FA-03 候选与 ORDERED 清点的固定 SHA 接受
- 对两个 REV3 SHA 的固定 SHA 接受
- 四项保留的 LIMITED 审查项是消除还是继续保留
- Manifest、正式运行和 DSP-004 关闭

`DSP004-FA-06` 因此仍是 `未建立充分前提`。`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍是未完成。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

## 8. 本记录的效力

```text
INDEPENDENT STATIC REVIEW RECORDED — FINDINGS ONLY

FA-06 登记的准入：NOT_ADMITTED
Signed / Accepted：false / false
任何 FA-06 行：未处置
DSP004-FA-06：未建立充分前提
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY
DSP004-FA-04：未完成
B-01：OPEN
B-02：OPEN
DSP004-FA-08：未完成
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

本记录不接受 `AAF90D311F2C85C48EF652E903D4B430D1F339F1FA465527DE679087F30B2305`，也不接受 `500015848949A8B789E0E44F2BB21AE0676D50B9440EA89124BB30CDC8B06254`。本记录也不接受 `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。这些 SHA 都不是正式合同。

本记录不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`，不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，也不关闭 DSP-004。不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。商业 P0 保持原样。没有真实案件、个人信息、凭据或供应商调用。

21 项机器核对全部通过。通过表示身份与 REV6 所记一致，说明与 JSON 的 61 行一致，并且每一行都能追溯到已经在 `main` 上的文件。通过不表示来源准入，不表示 SHA 接受，不表示任何 FA-06 行已被处置，也不表示 DSP-004 关闭。
