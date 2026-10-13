# DSP-004 所报读写记录分类：固定本地合成批次 REV1

## 1. 继续范围

Project Owner 回复“接受并继续”，仅有限接受原失败与清理失败并存候选 `06D2729B96BEBE2EB3A29CEF66B91982CD3ABE73B0491D6BEE37C903A4E830D9` 的固定源码，保留全部 LIMITED。本批次按既有仅本地合成实现与验证范围继续；该接受不扩大为集成、来源准入或实际捕获权限，也不接受上一批停止载体。

本批次只新增固定验证入口、实际观察 JSON 及结果记录。不得改动已接受文件、原清单、控制端或历史记录；不涉及独立 ACOS 或其他项目，不需要真实人物信息或案件材料。

## 2. 精确输入绑定与目标

| 角色 | 唯一文件 | SHA-256 |
| --- | --- | --- |
| 清单及独立预期来源，只读、不装载 | `validation/route_b_c03/wp_008/DSP_004_LOCAL_VALIDATION_CARRIER_CANDIDATE_REV1.ps1` | `46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C` |
| 固定控制端快照 | `validation/route_b_c03/wp_008/DSP_004_OUTER_CONTROLLER_CANDIDATE_REV1.ps1` | `891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB` |

仅调用 `Get-DSP004ReadObservationClassification` 与 `Get-DSP004WriteObservationClassification` 两个纯函数；其他函数虽随同一完整固定快照形成定义，但不调用。尤其不调用单案例入口、未来 Bootstrap、Driver 检查或任何 Python 代码。

先读每份唯一文件的一次字节快照，核验完整 SHA 和固定长度，以严格 UTF-8 解码。清单仅按固定表格语法提取 RD-001 至 RD-052、WR-001 至 WR-044 及其别名，绝不执行清单文本、`Invoke-Expression` 或未知 token。原清单关于当时 NOT_RUN 的历史文字不改写。

## 3. 原生输入与独立预期

- 按固定清单构造原生 Int32、Int64、String、Boolean 或 null；`string:0` 不转换成整数，`int64:20177` 不转换成 Int32，大小写和无效值按清单保留。
- 仅剥离 Markdown 表格分隔符外的格式空白，不归一化测试值；未知 token、重复/缺失 ID、列数错位或预期别名不匹配即拒绝本批次。
- 22 个本批次用到的任务状态、分类、检测/进度别名逐项核对清单原文；预期不从受测控制端或实际结果生成。
- RD 的 Expected After 必须逐项比较原生 Int32 或 null，并独立核对 Classification、DetectionByte。
- WR 逐项核对 Classification、ActualPartialProgress；WriteAsync 没有 bytecount，不能推断接受长度、实际部分进度、子端收到数据或 EOF。

## 4. 装载、调用和输出

在新的 PowerShell 进程内创建空白、独立 FullLanguage runspace。完整控制端快照经 AST 检查只能有十个已知顶层函数定义，不能有顶层执行语句；只装载一次。FullLanguage 不是 OS 安全沙箱或可信根证明。

装载及每次调用均核对输出数量与错误、警告、调试、详细、信息、进度通道。每个函数调用须返回且仅返回一个预期形状对象，先完成原生属性类型/值比较，再序列化展示。输入是人为构造的事件声明，不是真实任务、资源所有权、读取/写入或截止时间观察。

对 96 条清单逐条保留 ID、原始 token、原生参数类型、原生比较结果及受测返回的全部字段。一个失败不伪造后续通过；入口失败、已得部分结果及清理失败类型必须保留。关闭/Dispose runspace 的调用返回不等于全部引擎资源已收敛。

## 5. 覆盖和效力限制

仅覆盖原清单中的 RD 52 项、WR 44 项。M 6、RQ 18、D 7、F 62 仍不由本批次执行；96 项分类调用与此前其他载体的检查数不能相加冒充完整 189 项验证。保护性输入被正确拒绝不等于正常 I/O 成功。

不启动 Driver、测试子进程或真实案件操作，不读四个上游业务资产，不准入来源、不实际捕获、不集成、不修改已接受文件，不调用其他模型。全部 LIMITED 保留；DSP-004 仍 OPEN / HOLD，B-01、B-02 仍 OPEN。测试通过、候选有限接受和 GitHub 备份都不关闭这些缺口。
