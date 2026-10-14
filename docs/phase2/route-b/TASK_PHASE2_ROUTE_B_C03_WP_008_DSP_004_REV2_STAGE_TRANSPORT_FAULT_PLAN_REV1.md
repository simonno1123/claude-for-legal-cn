# DSP-004 REV2 私有阶段传输故障验证计划 REV1

## 1. 本轮范围与依据

Project Owner 已在本对话有限接受本地合成贯通监督器 REV2 的固定源码，并要求“自动完成后续批量任务”。本批次将后续工作限定为本项目新增的封闭本地合成测试：只核对接受身份、编译同份源码、构造固定内存脚本、调用其私有阶段方法、观察保护性拒绝与本地子进程退出、归档结果并按既有授权阶段备份。

不修改任何已接受文件，不自动签署新的接受或关闭决定，不开展来源准入、真实 Driver、真实案件材料、实际业务捕获、业务集成、部署或独立 ACOS／其他项目操作。既有文档中的 PENDING 字面量保留为生成时记录，不追溯改写本次会话层接受。

## 2. 固定身份与新输出

| 角色 | 资产 | SHA-256 |
| --- | --- | --- |
| 已有限接受的受测源码 | validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV2.cs | 9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E |
| 本批次新增固定核对入口 | validation/route_b_c03/wp_008/DSP_004_REV2_STAGE_TRANSPORT_FAULT_VALIDATION_REV1.ps1 | AF4BD16ADA55C264711E5045FF05672F2C5DB5DF442524174105417F642825B9 |
| 固定已有 PowerShell 运行文件 | C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe | 362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139 |

另外只新增本计划、OBSERVED_RESULT.json 和 RESULT.md。入口开始前必须复核固定源码和运行文件 SHA；本批次前后保护 REV1、REV2、原有依赖及记录共 20 份既有文件。

## 3. 测试入口和权限边界

新增入口在新 PowerShell 进程内编译同份受测源码，以固定非公开 SourceSpec 构造器与 RunStage 方法做八次单元层调用。只有受控脚本字节传给该私有方法，伪文件名只作为元数据，不从该名字读取文件。没有新增公共参数、回调、时钟替换、Provider 或测试模式到受测源码。

公开 RunFixedLocalCompositionBatch 不调用，其运行前八项依赖预检查与程序集公开单次门均不属于本批次覆盖。测试入口自行核对源文件与运行文件身份；不把私有方法调用包装成公开批次成功或正式 WP-008 场景。

## 4. 八个预置合成场景

| ID | 合成输入／行为 | 独立预期 | 输出边界 |
| --- | --- | --- | --- |
| TF-001 | 写出固定小 JSON | 阶段传输通过、退出 0、无失败、ACK/EOF 成立 | 正文和散列精确匹配固定合成字符串 |
| TF-002 | 写出不带 JSON 对象括号的文本 | InvalidOperationException；ACK_AND_BODY；退出 0 | 正文、正文散列和已合格 ACK 标志清除 |
| TF-003 | 子进程 exit 9 | InvalidOperationException；OWNED_STREAM_TASKS；退出 9 | 正文及合格 ACK 不公开 |
| TF-004 | stderr 写一个字节后长等待 | InvalidOperationException；OWNED_STREAM_TASKS；停止路径 | 只记录 1 个检测字节计数，不输出错误正文 |
| TF-005 | stdout 写超预算文本后长等待 | InvalidOperationException；OWNED_STREAM_TASKS；停止路径 | 只读取到 262145 字节的预算加检测字节，不无限排空 |
| TF-006 | stdout 正文写无效 UTF-8 字节 | DecoderFallbackException；ACK_AND_BODY；退出 0 | 无效正文与散列不公开 |
| TF-007 | 内存脚本声明错误 SHA | bootstrap 在 ACK 前拒绝；InvalidOperationException；OWNED_STREAM_TASKS | 不生成合格 ACK，不公开失败正文 |
| TF-008 | 子进程实际长等待 | 真实单调计时达到原固定 120000 ms；TimeoutException；OWNED_STREAM_TASKS；停止路径 | 正文及合格 ACK 不公开，记录本地退出与任务结束 |

TF-004、TF-005 和 TF-008 的固定等待脚本上限为 180000 ms；预期由受测方法停止其自己新建的测试 child。只允许该 child 的停止／kill，不查找或终止其他用户进程，不删除临时目录。

八个场景均核对本地子进程启动与退出、输入/输出/错误流关闭及 Process.Dispose 返回、读取任务结束、次级清理异常计数，以及传输成功/拒绝与失败阶段的一致性。任一意外情况停止后续场景并保留不完整结果，不修改预期以迎合受测输出。

## 5. 时间、资源与证据限定

TF-008 使用真实 Stopwatch 和受测源码原有 120000 ms 期限，不缩短阈值、不直接调用标量门代替计时、不注入时钟或篡改已接受源码。它仍不验证最后一次依赖文件读取发生跨期限停滞，也不证明外侧 watchdog、同步 Start/Kill/Close/Dispose 硬时限、恶意后代或完整资源收敛。

本批次没有人为制造父侧 Close/Dispose 本身失败。保护性拒绝后的正常本地清理返回，不等于异常清理能力已全部覆盖。异常类型/阶段和布尔观察可公开；原失败流、异常 Message/堆栈、进程句柄及字节载荷不归档。

新增八项是私有阶段故障单元检查，不增加或替代原 189 项清单，不把检查数量当作独立业务场景数量。本批次由主协调员执行和复核，不冒称独立双审或 Cross-Vendor 审查。

全部 LIMITED 保留；DSP-004 OPEN / HOLD，B-01/B-02 OPEN。任何新结果接受、来源准入、正式 WP-008 验证、集成或部署均不由本计划或测试成功自动产生。
