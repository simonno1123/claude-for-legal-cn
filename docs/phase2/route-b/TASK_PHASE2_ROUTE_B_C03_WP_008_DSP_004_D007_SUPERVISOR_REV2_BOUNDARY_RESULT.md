# DSP-004 局部监督器 REV2：超时优先级与输入说明边界验证

## 1. 授权和变更范围

Project Owner 对“仅新增监督器 REV2 和本地合成边界测试，保留 REV1、全部已接受文件和 LIMITED，不进行来源准入、实际捕获或集成”明确回复“授权继续”。本批次仅新增本项目的监督器源码、固定合成测试、测试入口及观察/结果记录。没有修改 REV1、原私有槽候选、固定控制端或其他已接受文件，没有访问独立 ACOS 或其他项目，也没有调用外部模型。

本记录不是 Project Owner 接受决定、独立双审结论、总体安全/法律结论或执行放行。REV2 仍是待单独处置的新候选；已有接受范围不自动转移至 REV2。

| 新资产 | 本地系统计算的实际 SHA-256 | 格式 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_D007_LOCAL_SYNTHETIC_HANDOFF_SUPERVISOR_REV2.cs` | `FA6625FA2917B056801A598B445C3A68E86A147C2A237260893A784B4449A066` | 16018 UTF-8 bytes / 297 LF |
| `validation/route_b_c03/wp_008/DSP_004_D007_LOCAL_SYNTHETIC_HANDOFF_REV2_BOUNDARY_TESTS.cs` | `B76082A7285261603CE559082F84CA3B340DE03FDD20ED201BC3FF305CE9BCCC` | 5250 bytes / 87 LF |
| `validation/route_b_c03/wp_008/DSP_004_D007_LOCAL_SYNTHETIC_HANDOFF_REV2_BOUNDARY_VALIDATION.ps1` | `214F6C98C7237A356776955A23FB9817D6D46109070518861ECECBD049A604CA` | 10795 bytes / 111 LF |
| `validation/route_b_c03/wp_008/DSP_004_D007_LOCAL_SYNTHETIC_HANDOFF_REV2_OBSERVED_RESULT.json` | `450BB40528FE2909DF4F2B3877D16186D14DF49747CB53E56142D39C19B5FAAD` | 40074 bytes / 820 LF |

四份文件均无 BOM、CR 和尾随空白，并以 LF 结束。观察 JSON 保存实际工具输出的完整父侧解析对象，以两空格和仓库 LF 排版；不是未修改的原始控制台 transcript。旧失败记录没有改写。

## 2. 两项实现修订

### 2.1 超时先于完成判断

REV1 在接受“进程已退出、输入关闭、双流结束”分支之后才检查 120000 ms 阈值，可能接受逾期完成。REV2 将阈值判定置于循环最前、进程启动前后、输入 close 前后，并在完成分支和解析确认标记后的最终决策样本处再次检查。

生产路径使用自己的 Stopwatch 样本与持有的任务状态，没有新增公共时间注入、回调、路径替换、布尔启用开关或计数器重置接口。内部共享纯分类方法先拒绝负数或达到阈值的样本，再判断是否完成；超时/失败后丢弃正常返回体并取消合格 ACK 标记。记录 `CompletionDecisionElapsedMilliseconds` 是该次局部决策样本，不是治理时间戳或整段操作硬实时保证。

### 2.2 输入说明由观察生成

REV1 的固定说明无条件宣称子进程已核验快照，包括根本没有启动子进程的重复拒绝结果。REV2 的固定 bootstrap 在接收完整载体、核验长度/SHA 和输入 EOF 后输出精确 ASCII 标记 `DSP004-SNAPSHOT-ACK-V2` 加 LF。父侧只有在预算内、正常 EOF、正文非空且严格 UTF-8、时间样本未过期时，才记录合格 ACK 并剥离前缀交给外侧 JSON 解析。

有合格 ACK 时说明为 `FIXED BOOTSTRAP SNAPSHOT ACK OBSERVED; NOT TRUSTED ROOT OR AUTHORITY`；否则为 `NO QUALIFIED CHILD SNAPSHOT ACK OBSERVATION`。这只陈述固定 bootstrap 的确认报告被观察到，不把 ACK 等同于可信根、独立来源验证或任何授权。重复拒绝以及失败路径不再无条件声称子进程核验已经发生。

## 3. 实际验证

固定测试入口先对 REV2 与测试源码的完整同份字节快照核验 SHA/长度，严格 UTF-8 解码，再将两份新源码内存编译到同一程序集。内部纯方法仅用于分类测试；监督器的公共入口仍是唯一无参 `RunSingleLocalBatch`。没有 SDK 安装、依赖下载、restore 或持久 DLL 输出。

本批次测试入口运行一次，退出码 0，结果 `LOCAL_BOUNDARY_BATCH_PASS`，没有主失败类型。源码静态语法核对及结果计数核对由主协调员进行；本轮未调用独立子审查员或 Gemini。

| 检查层 | 数量 | 本次结果 | 证据限定 |
| --- | --- | --- | --- |
| D：共享截止分类 | 12 | 12 PASS | 人工样本为 -1、0、119999、120000、120001、long.MaxValue；各配完成/未完成状态。阈值及逾期完成均拒绝；不是实际等待 120 秒 |
| A：ACK 分帧/解码 | 10 | 10 PASS | 空输入、缺失/不完整/错误标记、仅标记、正确标记与正文、空白正文、前置杂项、CRLF 标记、非法 UTF-8；全为固定合成输出样本 |
| Q：条件说明 | 2 | 2 PASS | true/false 的精确限定语；不是独立执行或可信根证明 |
| API、RUN、REFUSE：接口及真实局部运行记录 | 12 | 12 PASS | 1 项入口形状、8 项正常运行记录、3 项同程序集重复拒绝记录 |
| 既有固定载体在新子进程中的检查 | 85 | 85 PASS / 0 FAIL | 本次新执行的 85 个唯一 ID；不是引用上轮 PASS，不是完整 189 项计划 |

上述三层分别是 24 项合成边界、12 项接口/运行记录和 85 项子进程局部检查，不合并宣称一个完整 121 项治理或端到端覆盖结果。

真实正常调用：一次子进程启动，退出码 0，观察到进程退出、输入 close 返回，stdout 12493 bytes、stderr 0；监督器返回时样本 2619 ms，完成决策样本 2619 ms。固定 ACK 为 23 bytes；剥离后解析出同一固定载体的 JSON。`ChildSnapshotAckQualified=true`，其限定语是“观察到固定确认报告”，没有将其升级为来源准入或可信状态。

同一已编译监督器的第二次实际请求返回 `REPEATED_BATCH_REFUSED`，未尝试启动子进程，返回体为空，`ChildSnapshotAckQualified=false`，决策时间样本为 -1，stdout/stderr 长度为 -1（无该次流观察，不能写为测得零字节），说明明确为 `NO QUALIFIED CHILD SNAPSHOT ACK OBSERVATION`。没有重新编译以绕过门或执行第二个正常子进程。

新子进程中的原私有槽候选准备一次、请求两次并仍拒绝；固定控制端 helper 调用一次、正常返回一次。六字段保持 `TextCheck=FIXED_DRIVER_SHA_MISMATCH`、`Authority=NOT ESTABLISHED`、`SourceAdmission=NOT ESTABLISHED`、`FrozenHandoff=NOT IMPLEMENTED`、`ChildLengthEofShaVerification=NOT OBSERVED`、`CaseCompletion=NOT ESTABLISHED`。新的监督器观察不移转为原私有槽候选的交接能力。

## 4. 固定资产保留与未覆盖项

批次前后核对 23 份既有保护源码/记录的完整 SHA，均保持不变，包括上一轮四份载体/监督器/观察/结果记录。原监督器 REV1 SHA 为 `8AACC28D45F9BCFE14DD143116D1861819EAFCDE7B733B75400530216835CD54`；固定既有测试载体仍为 `49D058C495432D6028ED32D33A356CCA0D0F7B02FC8A162FBFB607266C643749`。历史版本及其中已记录的缺陷/失败不追溯改写为已修复。

本批次没有真实超时路径、实际启动失败注入、超量输出/资源耗尽、复杂取消、恶意 ACK 伪造、跨进程原异常保留、完整后代终止或原失败与清理失败并存测试。对样本的截止拒绝和 ACK 解码覆盖不等于实际停止能力。

同步读取、启动、close、kill 等操作本身仍没有可证明的硬时限；120/5/5 秒参数不是成熟平台能力证明。决策样本到实际返回之间也不是原子硬实时边界。进程退出、EOF、Dispose/kill 返回不证明全部资源/后代结束。临时目录保留，未递归清理。

正向 driver SHA 分支、callee 引用/独占冻结、可信宿主和完整依赖、完整 D-007 准入与 189 项计划继续未建立/未覆盖。没有读取真实 driver 或案件材料，没有来源准入、实际业务捕获或集成。

全部 LIMITED 保留；DSP-004 为 **OPEN / HOLD**；B-01、B-02 为 **OPEN**。本结果不接受 REV2，不关闭总缺口，不建立任何下游权限。仅这五份新增本项目合成验证文件可按既有阶段备份授权普通提交/推送；备份不等于接受。
