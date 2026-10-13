# DSP-004 本地合成异常与停止路径 REV1：观察结果

## 1. 授权和版本归属

Project Owner 对前述固定 SHA 源码有限接受及下一批本地合成异常/停止路径设计、必要新测试准备、隔离运行、结果复核和阶段备份明确回复“授权”。有限接受仅绑定监督器 REV2 源码 `FA6625FA2917B056801A598B445C3A68E86A147C2A237260893A784B4449A066`，不接受成熟停止能力，不关闭 DSP-004、B-01 或 B-02。

本批次新增一个封闭测试载体，以七个固定合成情景运行子进程。它复用 REV2 的内部纯截止分类/分帧方法，但没有调用 REV2 的公共执行入口；进程/流/停止实现属于新载体。测试结果不转移为 REV2 实际异常路径覆盖。既有文件保持原样，没有修改路径、启用测试模式、反射私有成员或替换固定载体。

| 新资产 | 实际 SHA-256（本地系统计算） | 格式 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SYNTHETIC_STOP_PATH_PLAN_REV1.md` | `BCBCE883B3F6EC93ABEF512DEC41AD74C6365D1DD66985551E1F3A66590C6873` | 4516 UTF-8 bytes / 38 LF |
| `validation/route_b_c03/wp_008/DSP_004_LOCAL_SYNTHETIC_STOP_PATH_CARRIER_REV1.cs` | `14A50ABB4AF415316A862572197162BB1A4DA5C79C277FD255587E3D84C4041B` | 15590 bytes / 291 LF |
| `validation/route_b_c03/wp_008/DSP_004_LOCAL_SYNTHETIC_STOP_PATH_VALIDATION_REV1.ps1` | `91DBF24718B6989912C3118C0FFB91FD564B1C65B1A01BB80E314B2F7D0778F0` | 12218 bytes / 112 LF |
| `validation/route_b_c03/wp_008/DSP_004_LOCAL_SYNTHETIC_STOP_PATH_REV1_OBSERVED_RESULT.json` | `8397995E010580B07E0769EC6660CB1F2B0B4DC63F750585EAFFFA5E4B6F4E16` | 20294 bytes / 528 LF |

四份文件均无 BOM、CR 和尾随空白，并以 LF 结束。JSON 保存实际工具输出的完整父侧解析对象，按仓库两空格/LF 排版；不是未修改的原始控制台 transcript。本结果不是新载体的 Owner 接受决定。

## 2. 装载和隔离范围

先只读核验已有限接受 REV2 的完整 SHA，再对新载体进行内存编译检查（零子进程）。新载体在执行前仅补充重复拒绝的未计时说明，编译/运行使用的最终指纹如上；已接受文件没有参与修改。

测试入口运行一次，先对两份源码的同份字节快照核验 SHA/长度，严格 UTF-8 解码并在同一内存程序集编译。没有 SDK 安装、restore、下载依赖或写出 DLL。每个实际 child 使用固定 pwsh 路径、无 profile、非交互、隐藏窗口和新临时工作目录，清空继承环境后仅补七个必要路径/遥测关闭项。固定 child 语句只写合成字符串或进行 .NET 等待，没有读取业务文件、访问网络或调用其他模型。

pwsh 文件指纹为 `362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139`，仅作为实际启动前本地文件身份观察，不证明可信根、执行期间不可替换或完整依赖闭包。这些进程/环境措施不是 OS 安全沙箱证明。

stdout 预算 65536 bytes 加一个检测字节；stderr 零正文预算加一个检测字节。使用并发、正数、有界请求读取，检测超量后不无限排空；正常/异常公开记录均不含原始失败流、异常 Message、堆栈或合成字节数组。原异常和次级异常只在本进程私有对象中保留，类型元数据不代表跨进程原对象留存。

## 3. 实际结果

本批次退出码 0，`LOCAL_SYNTHETIC_STOP_CHECKS_PASS`。47 个检查 ID 唯一，47 个布尔 true，0 个 false，无入口级验证失败类型。这里的 PASS 表示预期保护反应与局部记录相符，不表示七个情景均正常成功，也不表示零缺陷或总体安全通过。

| 情景 | 实际首要原因 | 情景总耗时 ms | stdout / stderr 读取数 | 已观察 child 退出 | 本情景终止请求 | 正常正文保留 |
| --- | --- | --- | --- | --- | --- | --- |
| S-01 控制 | SYNTHETIC_CONTROL_CAPTURED_ONLY | 480 | 52 / 0 | true，exit 0 | false | true，仅固定控制记录 |
| S-02 短时超时 | SYNTHETIC_TEST_DEADLINE | 5024 | 52 / 0 | true，退出数值 -1 | true，kill 调用返回 | false |
| S-03 stdout 超量 | STDOUT_OVER_BUDGET | 447 | 65537 / 0 | true，退出数值 -1 | true，kill 调用返回 | false |
| S-04 stderr 检测 | UNEXPECTED_STDERR | 434 | 0 / 1 | true，退出数值 -1 | true，kill 调用返回 | false |
| S-05 确认缺失 | ACK_ABSENT | 477 | 29 / 0 | true，exit 0 | false，已自行退出 | false |
| S-06 非零退出 | NONZERO_CHILD_EXIT | 484 | 52 / 0 | true，exit 7 | false，已自行退出 | false |
| S-07 启动失败 | START_FAILURE | 3 | -1 / -1，无流观察 | false，没有已启动 child | false | false |

总计七次启动尝试、六个实际启动的固定合成 child。S-02/03/04 的 -1 伴随 `ChildExitObserved=true`，是该已结束 child 的实际退出数值；S-07 的 -1 是默认未观察值，不能将两者混为同一种状态。

S-02 输出合成确认/正文后仍存活，实际短时 5000 ms 预算触发保护反应；5024 ms 是包括停止收尾的情景总耗时，没有单独记录锁定瞬间。停止后读取任务均结束、双流 EOF 被观察到，但正常正文和确认资格没有恢复。52 bytes 是 23-byte 合成标记加 29-byte 固定控制正文，不涉及输入 SHA 验证。

S-03 的 65537 读取数包含一检测字节，stdout 未被标记为正常 EOF；S-04 的 1-byte stderr 同样未被标记为正常 EOF。停止读检测流与观测 child 退出是不同事实。S-05 的 exit 0/EOF 不修复缺失确认；S-06 根据**新测试载体**的严格拒绝策略丢弃正文，不追溯改写 REV2 保留非零退出诊断正文的既有策略。

S-07 保留实际 `System.ComponentModel.Win32Exception` 类型，未虚构进程退出、EOF、kill 或计时完成。负面情景均有相应实际主异常；每个情景的 Process Dispose 调用均返回，未观察次级失败。这些局部事实不等于完整资源或后代结束。

同一编译程序集的第二次批次请求返回 `BATCH-REPEAT / REPEATED_TEST_BATCH_REFUSED`，未启动任何新 child，没有正文或确认资格，时间为 -1，并明确说明 `NOT TIMED; REPEATED TEST BATCH REFUSED`。没有重新编译以绕过本地门。

| 断言组 | 数量 | 本次限定 |
| --- | --- | --- |
| API / SET | 2 | 固定无参入口、七个唯一情景 |
| 七情景的原因、范围、状态、读取、清理记录 | 35 | 每情景 5 项；只核对局部记录，不把 Dispose 返回等同完全收敛 |
| 七情景专有的字节/时间/异常对照 | 7 | 预期另写于固定入口，不使用结果生成 oracle |
| 实际重复批次拒绝 | 3 | 同一程序集；不是跨进程/会话的一次性权限服务 |
| 合计 | 47 | 47 / 47 局部观察对照通过 |

本轮由主协调员进行静态核对和结果交叉核对；未调用独立子审查员或 Gemini，不能称为独立双审结论。

## 4. 保留状态与下一边界

既有 28 份保护源码/记录与其完整绑定 SHA 对照均保持一致，包括原私有槽/控制端、REV1 和本次已有限接受的 REV2；新增代码不改写任何既有文件。历史记录中的当时未接受、未执行或失败状态不被追溯改写。

该新载体采用 5000 ms **实际短时预算**，通过加 115000 ms 映射到 REV2 的 120000 ms **纯分类阈值**。本轮不声称运行了 REV2 的实际 120 秒公共入口或证明其所有异常路径。停止后的退出/读取等待设计参数各为 2000 ms；同步 start/kill/close/dispose 等调用自身仍没有可证明的硬界限。单个 child 退出/任务结束不证明全部资源和后代结束。

仍未覆盖：REV2 实际 120 秒路径、复杂取消/资源耗尽、原失败与清理失败并存注入、完整后代和资源收敛、同步调用硬时限、可信根/完整依赖、正向 driver SHA、callee 引用/冻结、完整 189 项计划。临时目录保留，未做递归删除。本批次未调用既有 DUT、未读取真实 driver 或案件材料、未准入来源、未实际业务捕获、未集成。

全部 LIMITED 保留；DSP-004 保持 **OPEN / HOLD**，B-01、B-02 保持 **OPEN**。本结果不接受新载体，不建立总体结论或下游权限。五份新增本项目文件可按已授权阶段备份执行普通提交/推送；备份不等于治理接受。
