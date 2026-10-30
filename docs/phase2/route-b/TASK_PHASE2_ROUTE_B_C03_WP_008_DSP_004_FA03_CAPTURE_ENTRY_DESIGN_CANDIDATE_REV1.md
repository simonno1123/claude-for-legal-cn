# DSP-004 FA-03 捕获入口设计候选 REV1

本文件是路径 B 下的 FA-03 捕获入口设计候选。它只写设计。它不准入捕获入口，不执行捕获代码，不从预期回填实际侧，也不完成 `DSP004-FA-03`。

依据仍是路径 B 原句：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写 FA-03 捕获设计候选，不准入、不执行、不从预期回填.`

`Signed` 与 `Accepted` 均为 false。本候选的准入状态是 `NOT_ADMITTED`。

## 1. 形成基准

| 项目 | 本候选的事实 |
| --- | --- |
| 形成时 `HEAD` | `7c23f63cb11345fd7a405a8ee6ee5bf009517881` |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV2.md` |
| 前一增量说明 SHA-256 | `618A913DED00C719FABF6D4AB37AEFAA1F9A604FF10EB08276D5CEF18A3DDBFD`（3121 字节） |
| 前一增量 JSON SHA-256 | `BFAFB7A0867156E164EACD8FEB76DF9655F658B6F33FF42A892675BB6356EBED`（2578 字节） |
| 机器可读候选 | `validation/route_b_c03/wp_008/DSP_004_FA03_CAPTURE_ENTRY_DESIGN_CANDIDATE_REV1.json` |
| 该候选 SHA-256 | `73DCBAB6AC60E79955C8755D820D9377DCEF1D2F32CABB01EA279DA9B81D859A` |
| 该候选字节 | 12081 |
| 受测模块导入或执行 | 未进行 |
| `identity_gate` 调用 | 未进行 |
| Fixture 写入 | 未进行 |
| 商业 P0 | 未执行，未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次只用本机 Python 对点名文件做字节散列，并只读既有捕获候选开头的设计说明。没有把那些文件当作已准入入口装载。没有导入 `identity_gate`、捕获候选、合同模块或场景运行器，没有编译 C#，没有重放业务场景，没有生成 Manifest。

这是设计候选，不是捕获实现，不是来源准入，也不是 Project Owner 对任何固定 SHA 的接受。点名一个 SHA 只固定文本身份。

## 2. 产生者与捕获入口分开

产生者准备获准调用的本地实际上下文。捕获入口是将来读取实际引用的那一个职责。二者不是同一个职责。产生者不能代替入口填写实际侧，再用填写结果证明自己。

| 职责 | 角色 | 本候选是否绑定入口 | 对冻结预期 |
| --- | --- | --- | --- |
| 预期维护 | `BASELINE_PREPARER` | 不新绑具体人 | 不能改写已经冻结的预期 |
| 实际上下文产生者 | `CONTROLLED_INVOCATION_CONTEXT_PRODUCER` | 未绑定 | 不能改写冻结预期 |
| 捕获入口 | `FIXED_ACTUAL_CAPTURE_ADAPTER` | 未绑定；`capture_entry` 为 null | 不能改写冻结预期 |
| 独立复核 | 与本文件物化者分开 | 本文件不把复核写成接受 | 不能改写冻结预期 |

预期维护者维护的是预期侧记录。预期一旦冻结，维护者也不能在原载体上改写。变更只能是另行授权的新载体和新 SHA。待审调用、产生者和捕获入口同样不能改写冻结预期。同一未获信任的调用方不能两侧自填再自证。

预期基线载体仍是 `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SYNTHETIC_EXPECTED_BASELINE_REV1.md`，10820 字节，`BE8C55796587BBA65E22B048291E1688A8B076D02DA2A48DE412919BEB10F368`。本候选不修改它，也不把它接受为资产。读取器 `AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727` 与调用侧候选 `EF554C3051318BD305EDE6B8511C433C1BB9E20B10E93E5FB5F71C9AFF7A7E63` 仍只是预期读取的局部候选，不是实际侧捕获入口。本候选不装载它们。

## 3. 实际引用只在另一次获准调用时读取

实际引用只在另一次获准的未来调用发生时读取。读取者是已经与产生者分开的捕获入口。本候选本身不读取。

那一次读取须同时做到：

- 保留原生类型。保留实际类型对象。类型名字符串、JSON 往返、`repr`、规范化、子类或同名异装载类都不能代替原生值。
- 保留来源。来源身份、定位、产生者职责和捕获入口归属随该次观察留下。本候选不预填这些事实。
- 未观察到的实际值保持空缺。不补一条记录。JSON null 在本候选里只表示未绑定、未观察，不表示已经取得的原生 None。真正取得的原生 None 与“没有观察”不是同一件事。本候选两种都不填写。

不得把 `SYNTHETIC-PROJECT-001`、`SYNTHETIC-SESSION-001` 或 `SYNTHETIC-PROVIDER-001` 写入实际侧。这三个字符串只留在预期侧记录里。预期侧身份仍是 `DSP004-EXPECTED-PROJECT-V1`、`DSP004-EXPECTED-SESSION-V1`、`DSP004-EXPECTED-PROVIDER-V1`。它们不是实际侧身份。

## 4. 不是实际侧身份的事实

| 事实 | 本候选的判定 |
| --- | --- |
| `audit_correlation_id` 相等 | 不是实际侧身份，也不证明同一次调用 |
| 刺激帧 | `frame.project_reference`、`frame.session_reference`、`frame.provider_reference` 只是拟议逻辑位置上的刺激。刺激帧本身不是观察，也不是实际侧身份 |
| `NOT_SELECTED` | 不是实际侧身份，也不是 Provider 身份 |
| 禁止调用结果 | 不是实际侧身份，也不能代替 Provider 身份观察 |

`scripts/phase2_runtime/route_b_c03/provider_port.py` 为 870 字节，`66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381`。本候选不导入该文件。文内的 `NOT_SELECTED` 只作为既有文本被点名，不成为本次观察，也不被接受。

## 5. 本候选禁止的动作

- 不调用 `identity_gate`。`scripts/phase2_runtime/route_b_c03/identity_gate.py` 仍是 4555 字节，`9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445`。既有筹备记录里的隔离失败结果不被本候选重跑，也不被写成 Fixture 或实际侧身份。
- 不写 Fixture 结果。`validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json` 仍是 770 字节，`9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8`。本候选不改它。
- 不预填 `variant_id`、`attempt_id` 或 `input_snapshot_sha256`。这三项与 `authority_record` 保持 null。
- 不执行捕获代码，不把任一既有捕获候选装载为入口，不从预期回填。

## 6. 三个实际侧保持 UNBOUND

| 角色 | 绑定 | 身份 | 版本 | 载体 | 定位 | 记录引用 | 捕获入口 | 观察 SHA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SRC004-A-PROJECT` | `UNBOUND` | null | null | null | null | null | null | null |
| `SRC004-A-SESSION` | `UNBOUND` | null | null | null | null | null | null | null |
| `SRC004-A-PROVIDER` | `UNBOUND` | null | null | null | null | null | null | null |

使用绑定 `variant_id`、`attempt_id`、`input_snapshot_sha256`、`authority_record` 均为 null。

## 7. 七个既有文件保持未选

路径 B 筹备增量 REV1 已经点名这七个文件，并且没有挑选它们。本候选只复核字节，并只读开头的设计说明。它们仍是 `NOT_SELECTED` / `NOT_ADMITTED`。

| 路径 | 字节 | SHA-256 | 开头文本所示职责 | 本候选后的状态 |
| --- | --- | --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1.py` | 18301 | `E9472328847617EBF629FB01A0A163C0805226690600E5E13EBE1209E2F6705C` | 校验调用者给出的结构元数据；不读取来源，不捕获引用 | `NOT_SELECTED` / `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_FIXED_BOOTSTRAP_CANDIDATE_REV1.py` | 10678 | `4281385A8694C870A96E7EC7B98A9CB027A470C1AC2EE5F31BABCF9D56F46007` | 固定字节接收与单次装载候选，不是捕获入口 | `NOT_SELECTED` / `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV1.py` | 47292 | `2C03E9D87BB747A58491CB3B992780FE4252ABDDCF4F35B1A2BC4F0078C4E942` | 结构校验载体，执行关闭 | `NOT_SELECTED` / `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV2.py` | 53568 | `634AC0CB18B0877B619A4FFAEFBBD4AA95C8DEBAACD7018FEBFB6A4C18B03365` | 校验载体，执行关闭 | `NOT_SELECTED` / `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV3.py` | 57623 | `329EC4A1C12351667F9A52946E4E11F6B01E287796FBDE42211FE5861CC14845` | 校验载体，执行关闭 | `NOT_SELECTED` / `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_OUTER_SUPERVISOR_CANDIDATE_REV1.cs` | 29736 | `36C90727CA87F6F6235546B8A380784CED13E40E94F2CA7799C01EE0FC094B35` | 公开入口拒绝 | `NOT_SELECTED` / `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_OUTER_SUPERVISOR_CANDIDATE_REV2.cs` | 51610 | `D097CBC8DEFA521F0B19ED06FF8A355881F95DB251453B760E644C33271BBE6A` | 公开入口拒绝 | `NOT_SELECTED` / `NOT_ADMITTED` |

合同候选的开头文本把 `variant_id`、`attempt_id`、`input_snapshot_sha256` 写成调用者提供的结构字段。本候选不采用该文件为捕获入口，也不为了迎合该字段而预填这三个值。

没有导入这些文件，没有编译 C#。

## 8. 关卡仍未完成

`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`completed` 为 false。

设计文本写下来，不等于入口已经绑定，也不等于实际侧已经有观察。仍缺：

- 三个实际侧的来源身份、版本、载体、定位、产生者职责、授权、位置和范围
- 与产生者分开且已经绑定的捕获入口
- `variant_id`、`attempt_id`、`input_snapshot_sha256` 和授权记录
- 另一次获准调用。只有那次调用发生时才允许读取实际引用

## 9. 本候选的效力

```text
DESIGN CANDIDATE RECORDED — NOT ADMITTED

捕获入口准入：未建立
三个实际侧：UNBOUND / null
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY / 未完成
DSP004-FA-04：未完成
DSP004-FA-08：未完成
B-01：OPEN
B-02：OPEN
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

本候选不接受任何固定 SHA 为正式合同、Manifest 或来源准入。两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 不是正式 B-02 合同。

本候选不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`，不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，也不关闭 DSP-004。不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。商业 P0 保持原样。没有真实案件、个人信息、凭据或供应商调用。
