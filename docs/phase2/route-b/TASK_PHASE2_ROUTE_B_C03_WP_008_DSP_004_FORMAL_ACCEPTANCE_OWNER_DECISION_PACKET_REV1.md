# DSP-004 正式验收筹备 — 未签署决定包 REV1

本包把已经记录的复核和本工作区两文件缺失，收成 Project Owner 仍要逐项决定的清单。写入建议句不会使任何一项生效。

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。没有 Manifest，没有来源准入，没有最终接受。

“继续推”只作为正式验收筹备方向的工作授权。它不是交接文件第 6 节路径 A 或路径 B 的签署，也不接受任何固定 SHA。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_FORMAL_ACCEPTANCE_OWNER_DECISION_PACKET_REV1.json` |
| 机器记录 SHA-256 | `3E6773EF54B6F6F1E253B42FAF92D5714C4BDE36EA6B7CFCF4E5A73359AC3BDC` |
| 机器记录字节 | 15824 |
| 生效状态 | 全部 `Signed: false` / `Accepted: false` |

## 1. 已记录、但尚未被 Owner 接受的事实

独立静态复核已经在库，提交 `bb69dc2d96103e99a308dbe9eddaeebfa88e07d3`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FORMAL_ACCEPTANCE_PREPARATION_REV1_INDEPENDENT_STATIC_REVIEW.md` | 10208 | `AA06168C4E128B33A488D1FCBF905EAD421BAAA3129EE9844B962AED71FCBB25` |
| `validation/route_b_c03/wp_008/DSP_004_FORMAL_ACCEPTANCE_PREPARATION_REV1_INDEPENDENT_STATIC_REVIEW.json` | 11573 | `459BAB3E2D5C06395E7AF2E5AF89BB556311C2B16846053964AF5A1AE47902D5` |

筹备 JSON `127521BAF310DDF57C33336B8A17B29D40002E4419A5E5CCB0ED029562DB24E2` 里的 `DSP004-FA-01` 仍然 `completed: false`。Owner 没有接受 FA-01。本决定包不改该字段。

## 2. 第 4 节两文件清点已经停止

本工作区没有 `.venv-validation/pyvenv.cfg`，也没有 `.venv-validation/Scripts/python.exe`。父目录 `.venv-validation` 同样不存在。因此没有 SHA、大小、时间或 `pyvenv.cfg` 字段。未执行解释器，未改虚拟环境，未改查其他路径。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FORMAL_ACCEPTANCE_VENV_TWO_FILE_ABSENCE_REV1.md` | 2536 | `8272F12D37A625455B9CC80962C504285D47E67794BB2CAC750E9684A6B72AAE` |
| `validation/route_b_c03/wp_008/DSP_004_FORMAL_ACCEPTANCE_VENV_TWO_FILE_ABSENCE_REV1.json` | 1965 | `D8142F5B8CFF55BE0AE26F652A7A09D86BC2E6172DC592D62D9230260A115E97` |

这是缺失记录，不是 `VENV_ROOT` 绑定，也不是 FA-02 完成。

## 3. 来源与根候选的在库设计复核本次不新增

候选 `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SOURCE_ROOT_ADMISSION_PREPARATION_REV1_CANDIDATE.md` 为 21257 字节，SHA-256 `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93`，提交 `25a65aae4212823c09e0b6acb0287cb933148468`。

该文件第 A 节写明本批复核通过会话交付，不新增第二份复核文件。第 E 节写明不生成另一份复核文件，并且本批只新增那一份候选。现在补一份复核文件会违反该批约束。会话复核没有留在仓库里，本次也不根据记忆补写。

未签署建议：在单独写明“允许为 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增一份复核文件”之前，不补写该候选的在库设计复核。

## 4. 关卡 FA-02 至 FA-08

建议句都未签署。Owner 若采用，需要在后续消息里原样复述对应句子。

| ID | 仍缺的事实 | 固定 SHA | 未签署建议 |
| --- | --- | --- | --- |
| `DSP004-FA-02` | 准备根范围未决定。两个拟清点文件在本工作区不存在，解析器、大小写/重解析和防替换证据仍缺。 | 筹备 JSON `127521BA…24E2` | 确认两文件 ABSENT 记录有效，VENV_ROOT 继续 NOT ESTABLISHED，并禁止改扫其他解释器。 |
| `DSP004-FA-03` | 三个实际侧身份、载体和捕获观察仍为 null。预期侧的 variant、attempt、输入快照和批准记录仍为 null。 | 基线 `BE8C5579…F368`；读取器 `AE1389ED…0727`；调用侧 `EF554C30…7E63` | 三项实际侧保持 UNBOUND；下一次至多授权新的捕获设计候选，不准入、不执行、不从预期回填。 |
| `DSP004-FA-04` | REV3 类型合同与数组政策已物化，但没有在库独立复核，也没有固定 SHA 接受。五类 ORDERED 实际序列来源未填。 | 类型合同 `AAD3921D…DE1F`；数组政策 `39F0FDC3…8123`；Plan V2.2 `6AD0CFD1…00BA` | 不把上述两个 REV3 SHA 当作正式合同；若继续，先单独授权对这两个字节的在库只读复核。 |
| `DSP004-FA-05` | V3.2/V2.2 输入候选未准入。原生门禁结果还不是 Fixture 比较映射。没有已接受的 Harness SHA。 | 输入候选 `A8AB66D7…3430`；旧绑定 `92303974…EEA5`；Fixture `9DAE8B93…46D8`；`identity_gate.py` `9E57E16C…F445`；Package V3.2 `87EE2451…63BD` | 输入候选保持 NOT ADMITTED；不覆盖旧绑定文件；不把 ISOLATION FAILURE 记成 Fixture 通过。 |
| `DSP004-FA-06` | 导入闭包、两侧调用身份和检查到使用的保护未建立。运行依赖 Manifest 仍不存在。 | Plan V2.2 `6AD0CFD1…00BA` | 依赖与隔离 LIMITED 全部保留，不创建 PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json。 |
| `DSP004-FA-07` | 没有已授权的 detached Manifest，也没有精确运行授权。 | 无新 Manifest | 不生成 Manifest，不授权正式运行。 |
| `DSP004-FA-08` | 没有已接受的正式验证记录，也没有 Owner 最终接受。 | 交接 `538283D7…05AA` | 不作出最终接受，DSP-004 保持 OPEN / HOLD。 |

`identity_gate.py` 仍只比较事项 ID、版本和 actor，并返回 `REJECTED — ISOLATION FAILURE`。Fixture `C03-TA-V-004` 仍要求 `BLOCKED_ISOLATED` / `BOUNDARY_MISMATCH`。这两项不能并成一次通过。

## 5. 剩余项 R-01 至 R-08

| ID | 仍缺的事实 | 固定 SHA | 未签署建议 |
| --- | --- | --- | --- |
| `DSP004-R-01` | 六侧仍缺各自的预期/实际身份、版本、SHA、产生者职责、授权、位置和范围。同一未获信任的调用方不能两侧自填再自证。 | 来源使用候选 `F4B995D8…4A2F` | 六侧继续 UNBOUND / HOLD；关联字符串相等不算实际证据。 |
| `DSP004-R-02` | 四根都没有 Manifest 生成前的批准。历史 Windows 定位不是本工作区，两个拟清点文件在这里不存在。 | 环境身份候选 `DC6DAA71…29EA`；`ENVIRONMENT_MANIFEST.md` `EFCF1A78…A531`（本次未重读） | 四根继续 OPEN；历史环境记录不改为本次观察，也不追认准备资格。 |
| `DSP004-R-03` | 正式成员的类型、可空性、范围、数组路径和 detached 外部权威仍未批准。 | 类型合同 `AAD3921D…DE1F`；数组政策 `39F0FDC3…8123` | B-02 继续 OPEN；不把玩具投影或未接受的 REV3 文本宣布为正式全合同。 |
| `DSP004-R-04` | 没有指向来源使用候选 SHA 的在库 Owner 接受。提交 `f3a41bca5d6857f2bb22a6a51c10895ea84ef076` 的标题写了 accepted，文件仍写明复核待完成且未接受。 | 来源使用候选 `F4B995D8…4A2F` | 以该文件字节为状态来源；提交标题中的 accepted 不构成接受，且不改写历史。 |
| `DSP004-R-05` | 当前完整输入、原生到 Fixture 的映射和 Harness 接受都未处置。189 项合成检查不是输入准入。 | 输入候选 `A8AB66D7…3430` | 不覆盖 SCENARIO_INPUT_BINDING.json，不从输入数据导入任意模块或函数。 |
| `DSP004-R-06` | 引用/冻结语义、完整解析、导入闭包、T0 / PE / OS 证据和检查到使用的防替换依据仍缺。 | 无新清单 | 保持 LIMITED；私有子进程和模块槽位删除不等于生产可信装载。 |
| `DSP004-R-07` | Owner 尚未写明哪些停止与清理 LIMITED 可以保留。同步读取、启动、Kill、Close、Dispose 和后代清理都未证明。 | 无新证据 | 保留全部既有停止与清理 LIMITED，不宣告零 I/O、零残留或物理硬停止。 |
| `DSP004-R-08` | Manifest 的生成、审查和接受缺少已授权准备来源。运行授权、运行证据审查和关闭决定都不存在。 | 无 Manifest | 未授权来源准入、实际业务捕获、集成或部署；不自动触发任何阶段。 |

## 6. 若要签署路径，使用新的一句

本文件不代选。若 Owner 要明确交接文件里的路径 B，需要另发一句，例如：

`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

该句出现在本包里只是可复述的文本，不是已经签署的选择。路径 A 仍是只确认本地合成阶段交付并继续保留 OPEN / HOLD；本次没有走那条签署。

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。
