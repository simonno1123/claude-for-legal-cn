# DSP-004 仅本地合成实现与验证批次 REV1

本目录为 Project Owner 本轮整批授权下的新增候选和测试记录，不是业务运行入口、来源准入决定或正式接受决定。不修改任何已接受文件，不涉及独立 ACOS 或其他项目。DSP-004 保持 **OPEN / HOLD**，B-01、B-02 保持 **OPEN**；全部历史记录和 LIMITED 保留。

## 范围与文件

- `carrier_rev4.py`：已接受载体 REV3 的新增后继。保留原 158 项 action/oracle 原文，新增本地原生管道与固定 B/A 字节绑定，以及 8 项真实异常身份/阶段/停止补充断言；不经 monkeypatch 启用旧候选。
- `bootstrap_rev2.py`：新增执行入口，固定接收 B/A/N 的完整字节与实际 EOF，随后仅注册一个 N。代码输入、控制命令和执行授权分离。
- `windows_scope.py`：仅管理本次创建的进程与句柄，使用 Windows Job、显式继承管道及独立外侧进程控制；不是完整安全沙箱。
- `supervisor_rev3.py`：新增 Python 监督候选，不冒充已接受 C# REV2 的实际实现。独立保存固定 158 项目录及逐案预期。
- `fault_fixture.py`：封闭的纯合成故障主体，不作为原生 158 项的替代 oracle。
- `run_batch.py`：外侧驱动与进程树观察者，固定项目、解释器、来源文件和结果目录；没有任意路径、回调或授权布尔开关。
- `candidate_pins.json`：本轮六份新增源码的完整 SHA-256/长度，属于字节身份绑定，不是签署、授权或完整环境可信证明。
- 固定输入能够读取并完成身份检查后，`attempt_NN_sources.json` 使用独占新建方式保存源码快照；`attempt_NN_result.json` 保存结果。前置权限失败可能只有结果、没有源码快照；不得补造快照冒充当时观察。失败记录不覆盖、不删除。

## 执行链与边界

外侧驱动 → 自有外层 Job 中的 host → 自有内层 Job 中的 bootstrap/N 或故障主体。子进程创建时通过 `PROC_THREAD_ATTRIBUTE_JOB_LIST` 归属 Job，无先创建后绑定的后备路径；只显式继承五个管道句柄。固定解释器使用 `-I -S -B`，不安装依赖、不修改环境、不使用 Shell 或网络。

源码必须经固定长度、完整 SHA-256 和实际 EOF 后装载。写任务与原始错误对象由本进程保留到结算；Event 置位不等同于线程退出。STOP、进程退出、Job 活跃数为零、写线程退出、私有报告 EOF、标准流实际 EOF 分别观察，不互相替代。stdout/stderr 的任何正文（包括日志、错误、ACK）均违背零正文要求；故障测试故意产生的一个字节仅用于验证保护性检测。

运行期元数据始终为 `UNVERIFIED_REPORT`。收到 READY、8 项补充报告或 158 条 PASS 帧，不能单独证明原生结果或正式接受；原生断言、父侧协议检查与外侧停止观察分开记录。

## 测试计划

计划 28 个独立进程场景：正常、提前 STOP、B 字节损坏、来源顺序错误、输入截断、多余来源字节、无代码 EOF、错误命令、重复 NEXT、STOP 后多余命令、挂起、stdout/stderr 正文、错误 READY、不完整帧、超长帧、提前 EOF、重复结果、乱序结果、SETUP/NOT_EVALUABLE、SUT/FAIL、STOPPED 后尾部、真实中断、存活后代、晚到 stdout/stderr、host 挂起和 host/主体同时存活的外侧停止。

正常场景计划执行 158 项目录的独立逐案比较和 8 项补充断言。持久结果仅保留计数、最后阶段等摘要，不逐条保存 158 个原始报告帧或原生返回。故障场景中的“测试 PASS”只表示观察到该场景预期的拒绝/停止/清理，不表示被审主体 PASS。启动失败、未到达受测阶段、非明确退出码、错误阶段或任何未结算资源都不能替代预期保护结果。

每批 T0 在第一次源码读取/哈希前观察，全批工作截止 T0+60 秒，硬截止 T0+70 秒；个案命令 2 秒，停止/清理最多 5 秒且受硬截止约束。外侧 host 上限 10 秒，专门挂起案例在标记后观察 0.3 秒再终止。它们是本次合成实验的保护上限，不证明任意原生同步调用可中断、既有设计的全部预算均已实现，或所有 OS 调度均已覆盖。

## 环境观察与未解除限制

本轮前置实际观察：固定现有解释器报告 Python 3.12.14，五个指定运行时文件 SHA 与此前记录一致。旧配置中的 3.12.13 仅为配置文本，不当作实际运行版本。`sys.path` 中列有但本地不存在的 `python312.zip` 不是已核验归档。DLLs/Lib 目录存在也不等于完整标准库及系统 DLL 来源均已证明。普通版本/配置变化按依赖与可证实时间范围评估，不自动推翻历史结果。

保留 LIMITED：完整依赖来源、检查到使用期间保护、未观察调度和同步原生调用、host 强制终止后的原生错误对象持久性、完整 189 项计划、D-007 业务来源路径、业务正向 SHA 分支、正式来源准入和后续集成/部署。不得把本地合成补充覆盖算作这些限制的自动解除。

本目录没有真实案卷、个人信息、凭据、外部模型调用或实际业务捕获。源码与结果备份仅是备份，不是治理接受。

## Windows 官方接口依据

- [CreateProcessW](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw)
- [UpdateProcThreadAttribute](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-updateprocthreadattribute)
- [Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects)

这些资料说明接口，不证明本地实现或运行结果。恢复后的运行观察、独立复核及限制见 `RESUMPTION_RESULT.md`；上轮权限和服务中断的快照保留在 `BATCH_STATUS.md`。结果不构成正式接受或来源准入。
