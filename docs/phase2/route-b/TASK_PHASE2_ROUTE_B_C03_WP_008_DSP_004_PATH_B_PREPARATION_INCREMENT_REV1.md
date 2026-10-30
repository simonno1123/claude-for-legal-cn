# DSP-004 路径 B 筹备增量 REV1

本增量只做正式验收筹备。它不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

| 项目 | 值 |
| --- | --- |
| 签署说明 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_SCOPE_SIGNING_RECORD_REV1.md` |
| 签署说明 SHA-256 | `EBD2F1F000447F40EDF70342F68083E49A71D995DF139A0854A6241E9AF8B02C` |
| 签署 JSON | `E92CAD5CBA87D974430735B53491B85F837BF5FECCE0AEBF629ADE1BAB05E025`（2242 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV1.json` |
| 本增量 JSON SHA-256 | `045D2DC6C9ED53CB8F795E670A35653576095AE4D2224139F426CFF01C39CA4B` |
| 本增量 JSON 字节 | 5737 |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。

## 1. FA-02：缺失记录确认为筹备事实

路径 B 与决定包 FA-02 建议一致：确认的是两个路径不存在，不接受虚拟环境资产。因此缺失记录作为本次筹备事实被确认。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_FORMAL_ACCEPTANCE_VENV_TWO_FILE_ABSENCE_REV1.json` | 1965 | `D8142F5B8CFF55BE0AE26F652A7A09D86BC2E6172DC592D62D9230260A115E97` |

确认对象只有 `.venv-validation/pyvenv.cfg` 与 `.venv-validation/Scripts/python.exe` 在 `/workspace` 不存在这一事实。没有新的 SHA、配置字段或执行。`VENV_ROOT` 保持 `NOT_ESTABLISHED`。

`DSP004-FA-02` 仍未完成。还缺解析器及版本、大小写与重解析政策、检查到使用的完整性，以及 `PROJECT_ROOT`、`RUNTIME_ROOT`、`SYSTEM_ROOT` 的批准。历史 Windows 环境记录不改为这次观察。

## 2. FA-03：实际侧捕获入口大纲

这是设计大纲，不是源码，不是可导入模块，也不是捕获实现。不准入，不执行，不从预期回填。

三个实际侧仍为 null：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。

以后若另有授权，新的捕获候选才需要同时满足：

- 产生者与捕获入口分开；预期维护者不能改写冻结预期。
- 只在另一次获准调用发生时读取实际引用，保留原生类型和来源。
- 未观察到的实际值保持空缺。不得填入 `SYNTHETIC-PROJECT-001`、`SYNTHETIC-SESSION-001` 或 `SYNTHETIC-PROVIDER-001`。
- `audit_correlation_id` 相等、刺激帧本身、`NOT_SELECTED` 和禁止调用结果都不是实际侧身份。
- 不调用 `identity_gate`，不写 Fixture 结果，不预填 `variant_id`、`attempt_id` 或 `input_snapshot_sha256`。

下列已有文件只是先前候选。本大纲不挑选它们，不装载它们，也不把它们当作已准入的捕获入口。

| 路径 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1.py` | 18301 | `E9472328847617EBF629FB01A0A163C0805226690600E5E13EBE1209E2F6705C` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_FIXED_BOOTSTRAP_CANDIDATE_REV1.py` | 10678 | `4281385A8694C870A96E7EC7B98A9CB027A470C1AC2EE5F31BABCF9D56F46007` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV1.py` | 47292 | `2C03E9D87BB747A58491CB3B992780FE4252ABDDCF4F35B1A2BC4F0078C4E942` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV2.py` | 53568 | `634AC0CB18B0877B619A4FFAEFBBD4AA95C8DEBAACD7018FEBFB6A4C18B03365` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV3.py` | 57623 | `329EC4A1C12351667F9A52946E4E11F6B01E287796FBDE42211FE5861CC14845` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_OUTER_SUPERVISOR_CANDIDATE_REV1.cs` | 29736 | `36C90727CA87F6F6235546B8A380784CED13E40E94F2CA7799C01EE0FC094B35` |
| `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_OUTER_SUPERVISOR_CANDIDATE_REV2.cs` | 51610 | `D097CBC8DEFA521F0B19ED06FF8A355881F95DB251453B760E644C33271BBE6A` |

`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。

## 3. FA-04：B-02 剩余设计清单

REV3 两份文件仍是文档候选，不是正式合同。本清单不新增政策行，也不把它们的 SHA 接受为 B-02 关闭依据。

| 候选 | 字节 | SHA-256 |
| --- | --- | --- |
| 类型合同 REV3 | 29240 | `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` |
| 数组政策 REV3 | 16317 | `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` |

数组政策候选自己申报的组内计数是：`manifest_identity` 0，`root_bindings` 4，`runtime_identity` 4，`import_contract` 5，`trusted_operation_contract` 5，`input_contract` 6，`entries` 1，`excluded_sets` 3，`closure_evidence` 3，`aggregate_identity` 1，`governance` 0，合计 32。这是候选文本里的对应关系，不是已批准的正式合同。

五条 ORDERED 政策仍没有实际序列来源：`AP-006`、`AP-009`、`AP-020`、`AP-021`、`AP-022`。候选写明缺一项就不能因表格存在而通过。

仍未建立、且本增量不补上的事项：

- 这两个物理候选的固定 SHA 接受，以及在库独立复核
- 每条 ORDERED 路径的实际来源文件、唯一序列定位和逐场景登记行
- 四根、大小写、重解析和别名事实
- 具体输入、变体、观察与可达性的准入
- 排除类别的成员关系和装载分支分类依据
- 编码器、生成器和对政策的运行验证
- D-007、可信装载、输出隔离、计时和外侧停止

B-02 保持 `OPEN`。`DSP004-FA-04` 未完成。

## 4. FA-05：输入与 Harness 就绪说明

输入候选保持 `NOT_ADMITTED`。

| 对象 | 字节 | SHA-256 | 本增量后的状态 |
| --- | --- | --- | --- |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | 107849 | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` | `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | 68768 | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | 未覆盖 |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json` | 770 | `9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` | 仍要求 `BLOCKED_ISOLATED` / `BOUNDARY_MISMATCH` |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | 4555 | `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445` | 仍返回 `REJECTED — ISOLATION FAILURE` |

没有 Harness SHA 被接受。189 项合成检查不是输入准入。门禁的隔离失败与 Fixture 的 `BLOCKED_ISOLATED` 仍是两层结果。`DSP004-FA-05` 未完成。

## 5. 本增量故意不做的事

- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。`DSP004-FA-06` 仍是前提未建立。
- 不生成 Manifest，不授权正式运行。`DSP004-FA-07` 仍未授权。
- 不完成 `DSP004-FA-08`，DSP-004 不关闭。
- 不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。该 SHA 尚未被单独授权。

## 6. 仍须以后的资产级决定

路径 B 没有代替下列决定：

- 四根的解析、重解析和批准，以及 FA-02 完成
- 三个实际侧的来源身份、捕获入口和调用归属
- 是否对两个 REV3 SHA 做有限设计接受
- 当前输入、比较映射和 Harness 的固定 SHA 处置
- 哪些依赖、隔离、停止与清理 LIMITED 可以保留
- Manifest、正式运行和最终接受
