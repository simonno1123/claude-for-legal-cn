# DSP-004 传入原生值投影比较核心 REV1 — 主审静态核对说明

本记录属于 `claude-for-legal-cn` 的本地新候选批次，只记录源码文字与结构核对。不是独立复核完成记录、Project Owner 接受决定、189 项测试结果、执行准入或 DSP-004 关闭记录。

## 1. 唯一新源码候选

- 文件：`validation/route_b_c03/wp_008/DSP_004_REPORTED_NATIVE_VALUE_COMPARER_CANDIDATE_REV1.cs`。
- 字节数：21186；385 个物理文本行；UTF-8、无 BOM、LF、最终 LF。
- SHA-256：`A48B1C45A6CD3EC5999FE183730AB727BC0C90F29E6957F97459CB2440F22F83`。
- 定位：调用侧传入的原生 `object[]` 值投影与独立提供预期之间的有限比较核心。
- 状态：`SOURCE CANDIDATE ONLY — PENDING INDEPENDENT STATIC REVIEW / OWNER ACCEPTANCE`。
- 未编译、未装载、未调用、未测试、未集成。没有入口、装载器、受测调用、文件/进程/网络操作或启用授权接口。

这不是 PowerShell 管道捕获器。它不认证传入对象、预期来源、真实完成事件或输出消费；不能将源码层的值关系转成实际项目状态。

## 2. 主审文本核对

主审完整阅读新候选，核对 P1 数据预期结构以及已接受控制端前八个函数的返回结构；没有调用 Parser / AST、编译器、装载接口、候选函数、Python、测试或环境探针。

| 核对项 | 源码文本观察 | 仍未证明的能力 |
| --- | --- | --- |
| 固定编号与形状 | M6 / RQ18 / D7 / F62 / RD52 / WR44 范围在 Item 中固定；不根据外部 ExpectedOutputKind 动态选型 | 没有执行 189 项，也不认证 ID 的外侧绑定 |
| 单次输出数量 | M-001/004 为 8，M-002/005 为 26，其余为 1；传入集合必须是原生 object[] | 真实管道计数、空管道与显式 null 的捕获区别未建立 |
| 字段与原生类型 | CaseRecord 三字段、FixedRecord 27 字段、D/F/RD/WR 分别 6/10/7/9 字段；名称按 ordinal 匹配，Int32 / Boolean / String 和 RD 可空 Int32 分开 | 编译兼容性、真实返回对象包装与实际类型未验证 |
| 集合顺序 | Cases8、Tuples26、Reasons6 固定数量；tuple/reason 明确允许 object[] 或 string[]，元素必须为原生 String，按顺序比较 | 不保证传入集合的来源、冻结、独占或并发安全 |
| 可见属性检查 | 对 exact PSObject / immediate PSCustomObject 的可见属性，先检查 exact instance PSNoteProperty、原名与数量，再读取 Value；不读取脚本、代码、别名或适配属性的 Value | Public Properties 是可见整合视图；隐藏成员、宿主 TypeTable / adapter 和框架内部分配未认证 |
| 字典检查 | 只接受 exact Hashtable / OrderedDictionary；枚举原生 String 键，不调用自定义键比较器做查找；记录结构固定 | 本地运行时实现身份、输入独占与枚举期间无并发修改未绑定 |
| 标量比较 | 直接 CLR 类型检查与 ordinal String 比较；没有自定义 Equals、ToString、格式化、JSON 或通用转换路径 | 不执行任意 PSObject scalar / Hashtable wrapper 的自动解包；未来捕获投影适配责任仍未实现 |
| 返回语义 | EQUAL / DIFFERENT / REFERENCE_NOT_COMPARABLE / ACTUAL_NOT_COMPARABLE / INSPECTION_FAILED 只是值关系；返回限定字段均保持未认证或未建立 | 不是 MATCH / NOT_MATCH / NOT_RUN / INCOMPLETE 项目状态，也不是第五项目状态或执行许可 |
| 异常 | 检查异常的原始对象仅作为私有引用保留，没有公开 message / trace accessor 或格式化输出 | 私有结果持有、进程损失、主失败与清理失败并存以及资源收束未建立 |
| 局部边界 | 名称 64 字符、值字符串 512 字符、固定集合数量与有限形状递归只在源码内规定 | 不是全框架内存上限、实际计时保证或可信运行证明 |

以上观察只能支持源码路径与声明的静态核对，不能支持“真实完整捕获比较已实现”或“可以运行”。

## 3. 独立复核状态

已向独立只读子审查员发出本轮源码复核任务，但该任务以账户使用额度限制错误终止，没有返回复核判定。

```text
Primary Check:
COMPLETED — SOURCE TEXT INSPECTION ONLY

Independent Static Review:
NOT COMPLETED — REVIEWER USAGE LIMIT

Independent PASS / Grade:
NOT ESTABLISHED

Candidate Acceptance / Execution Readiness:
NOT ESTABLISHED

This Batch Git Commit / Push:
NOT PERFORMED — REVIEW MILESTONE NOT COMPLETED
```

不得借用 P1 候选、旧载体或控制端的复核结论，填补本轮缺失的独立结论。主审核对不代替独立复核，不据此登记零缺陷总判定或阶段关闭。

## 4. 保留的 LIMITED 与缺口

1. 比较对象是调用侧传入的 native value projection；真实管道捕获、输出闭合、私有所有权、预期认证和完整观察事件未实现。
2. 提供空数组、单个 null 槽和 null 字段可以表示不同输入，但不证明真实捕获器保留了区别。没有对捕获 API 或包装转换作运行验证。
3. M-004/005/006 只支持分别比较一份传入值；首次检查、仅修改首次捕获副本、第二次调用以及引用身份/可变状态隔离仍未实现。
4. PSObject.Properties 仅核对可见成员投影；隐藏元数据与框架内整合/分配不受这里的循环上限证明。宿主、程序集、TypeTable、adapter 和私有域须另行绑定。
5. 输入与 oracle 必须由外侧独占持有；本候选不证明冻结、防并发修改、可信来源或预期清单归属。摘要字面量不是对象认证。
6. 同份受控源码字节装载、完整十定义/八函数与 helper 归属、启动前全部输出封锁、受控提交与首次停止的原子裁决、外侧监督未实现或未绑定。
7. D-007 的独立准备与同份私有输入摘要门仍未实施，保持 `UNBOUND / NOT_RUN`；真实 driver SHA 正向分支保持 `NOT COVERED`。本批没有访问 driver / caller / reader / baseline 四份上游资产。
8. 120/5/5 秒是设计提议，不是已实现能力。真实单调计时、原操作/后代资源停止确认与主/次异常保留仍未建立。
9. 所有上游 `LIMITED` 保留；`DSP-004 OPEN / HOLD`、`B-01 OPEN`、`B-02 OPEN`。
10. 不准入真实来源，不实际捕获，不安装软件或 OCR，不集成，不接入第三方模型，不涉及独立 ACOS 或其他项目。

## 5. 固定文件完整性

本批物化与文本核对后，下列文件的实际本地摘要保持原值；没有修改它们：

| 文件 | 字节数 | SHA-256 |
| --- | --- | --- |
| DSP_004_LOCAL_VALIDATION_CARRIER_CANDIDATE_REV1.ps1 | 70284 | 46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C |
| DSP_004_OUTER_CONTROLLER_CANDIDATE_REV1.ps1 | 25573 | 891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB |
| DSP_004_NATIVE_INPUT_ORACLE_CANDIDATE_REV1.ps1 | 286568 | D585B3CE407B0D3BEAD2C2D5339E4EC1C66D0E768D2FB87B49F7BD053B50DB9D |

P1 仍是未接受的新候选，不在此记录中升格。清单原文记录身份仍为 `4BAED6E284C92A2403117C72CFBF419BD2B6FB478A55697CA2229201C8FB149E`。四处既有 manifest description 不一致及已接受文档、源码、历史决定均未改写。

## 6. 通用 API 参考限定

Microsoft 的公开文档说明 PSNoteProperty 的值属性及 PSObject 的 Properties / ImmediateBaseObject 接口；这些只用于编写有限 API 路径，不能证明本地程序集身份或运行安全。[PSNoteProperty](https://learn.microsoft.com/en-us/dotnet/api/system.management.automation.psnoteproperty?view=powershellsdk-7.4.0)、[Properties](https://learn.microsoft.com/en-us/dotnet/api/system.management.automation.psobject.properties?view=powershellsdk-7.4.0)、[ImmediateBaseObject](https://learn.microsoft.com/en-us/dotnet/api/system.management.automation.psobject.immediatebaseobject?view=powershellsdk-7.4.0)。

公开 PowerShell / .NET 源码也只支持 API 设计核对，不能转移为当前宿主、枚举资源上限或并发安全证据。[PowerShell MshMemberInfo.cs](https://raw.githubusercontent.com/PowerShell/PowerShell/v7.6.5/src/System.Management.Automation/engine/MshMemberInfo.cs)、[.NET Hashtable.cs](https://raw.githubusercontent.com/dotnet/runtime/main/src/libraries/System.Private.CoreLib/src/System/Collections/Hashtable.cs)。只查询通用 API 文档，没有提交项目源码、资产、摘要或案件资料。

## 7. 下一步与备份限定

本批两个新文件仅保存在本地。须先获得针对本候选固定 SHA 的实际独立静态复核，再处理候选中的真实问题；不预填复核结论、提交 SHA 或推送成功状态。本批 GitHub 备份因复核未完成而暂停；上一个已核实备份提交是 `c86eb81e8878ccf2653c079fa81b4a97d4458506`，不是本批备份。

等待独立审查恢复，或由 Project Owner 单独决定新的外审路径，不能把账户错误解释为接受、通过、授权失效或技术测试结果。
