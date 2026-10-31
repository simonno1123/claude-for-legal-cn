# DSP-004 OD-04 仓库现有证据盘点候选 REV1

本候选只盘点 GitHub 仓库里已经记下的、与 OD-04 有关的记录，并逐项列出缺口。OD-04 的内容是：导入闭包、两侧调用身份、检查到使用的防替换，以及 T0 / PE / OS 证据。

本候选不补造证据。盘点已有记录不是新证据，也不满足 OD-04。OD-04 仍是 `DEFER_WITHOUT_EVIDENCE`，状态是 `OWNER_HELD_OPEN_NO_CLOSED_OPTIONS`。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本次授权是：2026-10-31，Project Owner 张纯熙选择"改变某项决定"中的 OD-04 补充证据。所有者无法提供 Windows 验证机，因此指示：只盘点 GitHub 仓库已有的 OD-04 相关记录，列出缺口，不准入，不改 OD-04，不关闭 DSP-004。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_OD04_EVIDENCE_INVENTORY_REV1_CANDIDATE.json` |
| 形成前 Git HEAD | `e9d4a54fcf5b5de04da7272c8684a09a6497c5fe` |
| 形成方法 | Python 标准库只读：SHA-256、JSON 解析、Markdown 表格解析、AST 解析 |
| 形成主机 | 云端 Linux 容器，不是验证机 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 0. 形成边界

- 未访问验证机，未读取工具缓存，未读取历史 Windows 虚拟环境。
- 未导入或执行仓库中的任何模块。未调用 `identity_gate`，未执行 Fixture，未运行场景运行器。
- 未提供运行根定位。本文只用 EIR 行号引用路径，不重复写出路径。OD-05 `REFUSE_LOCATOR` 不变。
- 未发明路径、启动序列或导入查询顺序。
- 如实记载：记录人在摸查阶段对 `ENVIRONMENT_MANIFEST.md` 做过一次文本检索。本候选不使用、不引用、不绑定该文件内容。下文的环境身份全部取自准备计划、重绑定候选和 attempt_02 结果。机器记录里 `EnvironmentManifestRead` 因此写为 true，并附说明。

## 1. 绑定的来源

| 角色 | 文件 |
| --- | --- |
| 准备计划 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN.md` |
| 重绑定候选 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_ENVIRONMENT_IDENTITY_REBINDING_REV1_CANDIDATE.md` |
| 本地合成运行结果 | `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/attempt_02_result.json` |
| 批次恢复结果 | `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/RESUMPTION_RESULT.md` |
| 批次候选固定值 | `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/candidate_pins.json` |

各文件的字节数与 SHA-256 写在机器记录的 `BoundSources`。相符只是身份核对，不是接受。

## 2. OD-04 六个组成部分的现状

| 组成部分 | 仓库现状 | 仓库里有的 | 仍缺的 |
| --- | --- | --- | --- |
| 导入闭包 | 部分，仅文本 | 准备计划第 4 节：十个受测文件的直接导入文本清单；本候选第 4 节：六个批次 Harness 文件的直接导入 | 标准库递归闭包及每个文件的字节与 SHA；内置与冻结模块清单；非标准导入名到具体文件的解析；扩展模块闭包 |
| 两侧调用身份 | 无 | attempt_02 记下一次本地合成运行的解释器和 `sys.path`（LIMITED，`LOCAL_SYNTHETIC_ONLY`） | 已接受的调用方身份；已接受的被调用方身份；两侧绑定到同一个已接受运行时 |
| 检查到使用的防替换 | 无 | attempt_02 一次运行内五个文件前后一致；重绑定候选第 1.3 节的前后元数据与 ReparsePoint 观察 | 覆盖检查到使用区间的保护；冻结或不可变的运行根；运行之间不被替换的证据（记录显示字节变化过，见第 3 节） |
| T0 | 无 | 验证执行包 V3 定义了 T0，未记下任何 T0 观察 | Python 启动前对启动器与环境的已接受核验 |
| PE | 部分，仅身份 | 五个运行时文件三代 SHA（见第 3 节） | 这些文件的 PE 导入表；每个 PYD 的字节与 SHA；每个 PYD 的运行时 DLL 依赖；经审查的静态 PE 解析器及其限制 |
| OS | 无 | 重绑定候选第 3.2 节写明 SYSTEM_ROOT 及 OS 依赖闭包未取得 | 已接受主机身份；每个系统 DLL 的根、字节与 SHA；解析搜索顺序 |

## 3. 运行时文件身份的三代记录

本节只比较仓库里已经记下的数值，没有重新读取任何二进制文件。

| 文件 | 准备计划记录 | 此前会话观测 | 最近记录观测（EIR） | attempt_02 前后 | 不同身份数 |
| --- | --- | --- | --- | --- | --- |
| `python.exe` | `D8E3F0AD…` | `B847BB9F…` | `B07B03B9…`（EIR-003） | 与 EIR-003 相同 | 3 |
| `python3.dll` | `2D2330CE…` | `FE6A4470…` | `F91CA7E2…`（EIR-004） | 与 EIR-004 相同 | 3 |
| `python312.dll` | `64A1DAD0…` | `2B6FFFDE…` | `3B33D49D…`（EIR-005） | 与 EIR-005 相同 | 3 |
| `vcruntime140.dll` | `D5E4D9A3…` | 同计划 | `D5E4D9A3…`（EIR-006） | 与 EIR-006 相同 | 1 |
| `vcruntime140_1.dll` | `1F2D41C4…` | 同计划 | `1F2D41C4…`（EIR-007） | 与 EIR-007 相同 | 1 |

完整 SHA 与字节数写在机器记录的 `RuntimeIdentityGenerations`。

## 4. 批次 Harness 直接导入（AST 文本结果）

六个文件的字节与 SHA 与 `candidate_pins.json` 逐份相符。下表是 AST 解析出的直接导入名，不是解析后的文件，也不是执行得出的能力结论。

| 固定键 | 文件 | 模块级导入 | 函数内导入 |
| --- | --- | --- | --- |
| WIN | `windows_scope.py` | `__future__`、`ctypes`、`msvcrt`、`os`、`subprocess`、`threading`、`time` | 无 |
| SUP | `supervisor_rev3.py` | `__future__`、`dsp004_windows_scope`、`time` | `hashlib` |
| BOOT | `bootstrap_rev2.py` | `__future__`、`ctypes`、`hashlib`、`importlib.machinery`、`io`、`msvcrt`、`os`、`sys`、`types` | 无 |
| N | `carrier_rev4.py` | `__future__`、`dataclasses`、`hashlib`、`importlib.machinery`、`io`、`math`、`os`、`stat`、`sys`、`types` | 无 |
| FAULT | `fault_fixture.py` | `io`、`msvcrt`、`os`、`sys`、`time` | `subprocess` |
| DRIVER | `run_batch.py` | `__future__`、`hashlib`、`importlib.machinery`、`json`、`math`、`os`、`pathlib`、`sys`、`time`、`types` | 无 |

## 5. 所见

- `OD04-INV-F01`：`python.exe`、`python3.dll`、`python312.dll` 各有三个不同的已记录身份，两个 VC 运行库只有一个。运行根至少变化过两次。
- `OD04-INV-F02`：attempt_02 前后五个文件的 SHA 与 EIR-003 至 EIR-007 全部相同。那次本地合成运行用的是最近观测到的字节，不是准备计划记下的字节。
- `OD04-INV-F03`：`pyvenv.cfg` 的版本文本是 3.12.13（重绑定候选第 3.1 节），attempt_02 报告的解释器版本是 3.12.14。配置文本落后于实际运行的解释器。本候选不推断原因。
- `OD04-INV-F04`：重绑定候选第 3.1 节记下 `pyvenv.cfg` 的 home 指向一个由工具管理的运行时缓存。结合 F01，记录显示基础运行时的字节在多次观测之间发生变化，而项目侧没有对应的变更记录。在这种布局下，仅凭仓库记录无法建立检查到使用的防替换。
- `OD04-INV-F05`：批次 Harness 直接导入了 `ctypes`、`msvcrt`、`subprocess`、`threading`。非标准导入名是 `dsp004_windows_scope`，它不是标准库模块，要映射到哪个文件需要另行解析。
- `OD04-INV-F06`：仓库及其历史里没有任何 PYD 身份、系统 DLL 身份、PE 导入表、标准库文件 SHA 或 T0 观察。这些只能从验证机取得。

## 6. 本候选故意不做的事

- 不改 OD-04，不改其他 OD 记录，不改 REV1 登记或 REV2 至 REV4 叠层。
- 不把任何已记录 SHA 接受为运行根、来源或 Manifest 条目。
- 不提供运行根定位，不发明启动序列或导入查询顺序。
- 不生成 Manifest，不授权正式运行，不完成 FA-08，不关闭 DSP-004。
- 不执行任何仓库代码。不改商业 P0。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
