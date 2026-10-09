# DSP-004 M 引用观察候选 REV1：限定范围静态复核

## 1. 本批范围及结论

本批继续本项目获授权的自动候选准备与独立静态复核。唯一新源码是 `validation/route_b_c03/wp_008/DSP_004_REPORTED_M_REFERENCE_INSPECTOR_CANDIDATE_REV1.cs`；本文件只记录该批的静态核对，不是状态台账、接受决定或执行凭证。不涉及独立 ACOS 或其他项目。

主审完整读取最终源码、核对相关 M 原文并核验文件字节；独立源码审查员 `/root/dsp004_carrier_rev1_independent_static_review` 也完整读取同一最终源码。结论：`SCOPED STATIC PASS / LIMITED`，未发现本轮限定源码范围内的阻断性缺陷。没有编译、装载、调用、AST 解析、测试、环境探测、来源准入、实际捕获或集成。

本候选仅观察两份**调用侧提供的对象投影**。它不调用此前值比较器、不与 oracle 比较值、不修改首次副本，也不执行两次 DUT 调用。不建立 M-004 至 M-006 的完整核验。候选源码尚未被 Project Owner 接受；静态复核与 Git 备份均不构成接受。

## 2. 本地字节绑定与未变更保护

下表中的实际文件 SHA 由本地文件字节读取核验，不是外部纯文本模型计算或第三方执行事实证明。catalog 哈希是已恢复文本的记录绑定，本批不声称存在对应独立物理文件。

| 对象 | SHA-256 | 本批处置 |
| --- | --- | --- |
| 新 M 引用观察源码 | `2D7B6A65E54C29FFA90964256078CE46E1B9F59E37AFFE6A3E3DBE0FBDAD1D9F` | 新候选，18051 UTF-8 bytes、353 LF、无 CR/BOM、末尾 LF |
| A：已有限接受局部载体源码 | `46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C` | 未修改 |
| B：已接受唯一控制端源码 | `891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB` | 未修改；只核对前三 getter，不访问后两个函数 |
| P1：原生输入与独立预期源码候选 | `D585B3CE407B0D3BEAD2C2D5339E4EC1C66D0E768D2FB87B49F7BD053B50DB9D` | 未修改，未转移任何既有结论 |
| 分离的原生值比较源码候选 | `A48B1C45A6CD3EC5999FE183730AB727BC0C90F29E6957F97459CB2440F22F83` | 未修改、未调用 |
| 输入与预期清单 REV2 记录绑定 | `4BAED6E284C92A2403117C72CFBF419BD2B6FB478A55697CA2229201C8FB149E` | 189 项计数及原文不变 |

源码文本检查：0 行尾空白、未发现所扫描隐藏 Unicode；1 个 public static 方法 `CompareReferences`，14 个 get-only 结果字段。文本检查不是编译可用性或运行行为证明。

## 3. 原文、显式配对及补充观察的分离

范围设计先由 `/root/dsp004_gap_convergence_rev1_independent_readonly_review` 只读复核，结论 `LIMITED`，仅适用于范围设计语义，不冒充对最终源码的完整审查。随后最终源码由上述另一独立审查员完整复核。

| 项目 | 原文与 P1 的显式范围 | 新源码行为及限定 |
| --- | --- | --- |
| M-004 | A 第248行及 P1 第185/196行：两次首项 Hashtable 不同；仅修改首次副本的首项 CaseId | 只报告两个首项 Hashtable 的 shared/distinct；检查8项形状不增加其余7项 fresh 要求。没有副本修改或调用顺序证据。 |
| M-005 | A 第249行及 P1 第201/212行：捕获集合首槽变更不影响第二次值；无 String identity assertion | 明确 `STRING_IDENTITY_NOT_REQUIRED`；只检查投影形状，不要求 String 新引用，不声称 getter 直接返回数组。 |
| M-006 显式配对 | P1 第228行：包装器、CaseContract/StatusCombinations 集合、8个同索引 Hashtable | `P1ExplicitReferenceRelation` 单独记录这些配对，不能推导完整隐藏图不共享或两次值匹配。 |
| OuterReasons | A 第250行涉及可变嵌套集合；B 第85行有 OuterReasons 数组；P1 显式清单未列此项 | 单列补充可见数组关系；不修改 P1，不声称是 P1 原有显式断言。 |
| 调用侧投影容器 | 由调用侧提供，不等同于 DUT 直接返回数组 | 单列补充 container 关系，来源与持有责任仍未认证。 |
| 27个可见 NoteProperty | 可见实例存储站点，不是原文新增 fresh 条件 | 单列27×27跨组观察；不得变成 M-006 新强制通过条件或隐藏图证明。 |
| 跨索引 Hashtable | 原 P1 的8个同索引配对不能排除跨索引共享 | 单列8×8跨组补充观察，不增加189项用例、不改变值 oracle。 |

各补充字段可以与显式配对字段呈现不同关系；这种区分不能合并成 PASS/FAIL、MATCH 或新增 M 通过标准。缓存、伪造或非真实调用来源的投影同样可能满足此 API。

## 4. 独立最终源码复核记录

| 复核项 | 判定 | 最终源码依据与限定 |
| --- | --- | --- |
| M-004 范围 | PASS | 第323–328行仅首项 Hashtable 配对，未要求其余项 fresh。 |
| M-005 范围 | PASS | 第330–332行无 String 或 getter 返回数组身份断言。 |
| M-006 显式引用对 | PASS | 第281–288行包装器、两类集合、8个同索引 Hashtable 配对，与 P1 所列范围对应。 |
| 补充观察分离 | PASS | 第333–345行分离四类补充字段，无合并通过判定、无新增 M 强制条件。 |
| 原生形状与字段 | PASS | 27字段、9个 Int32 字段、8/26/6集合形状及19/20/21索引与 B 前三 getter 一致。只核对形状，不核对值正确性。 |
| 元数据先于 Value | PASS / LIMITED | 第219–235行先检查全部可见成员类型、实例属性、名称与唯一性，第239行才开始读 Value。隐藏成员及框架内部行为未证明。 |
| 只读与引用关系 | PASS / LIMITED | 没有输入 setter、字典键查询、未知对象转换或自定义 Equals/GetHashCode/ToString；私有记录赋值不是输入副本写入。框架整合视图、宿主及并发行为仍 LIMITED。 |
| 资源及异常 | LIMITED | 每投影最多40引用站点，不是40唯一对象；27×27及8×8循环有限不保证框架内部资源或时间。原异常仅私有持有，完整异常寿命与进程存活未证明。 |

引用比较使用 `Object.ReferenceEquals`，不代替值相等判断；其 API 语义见 [Microsoft 官方文档](https://learn.microsoft.com/en-us/dotnet/api/system.object.referenceequals?view=net-10.0)。Hashtable 支持自定义 comparer，因此本候选不实现可能进入该路径的键查询或副本写入；实现背景见 [.NET 官方源码](https://raw.githubusercontent.com/dotnet/runtime/main/src/libraries/System.Private.CoreLib/src/System/Collections/Hashtable.cs)。这些公开参考不绑定本机程序集版本、环境可信度或运行行为。查询只涉及通用公开 API，未传送本项目源码、哈希或案件数据。

## 5. 保留的实现缺口与不建立的资格

下列项目不是本轮源码缺陷的零缺陷抵销项；它们是尚未建立的完整 M/载体实现能力，必须继续保留：

- 可信装载、程序集/TypeTable/adapter 绑定及装载前输出闭合；
- 首次真实调用、完整原值捕获、与独立预期的值比较；
- 仅许可首次副本修改、可信私有所有权及安全写入路径；Hashtable 的精确类型不能单独证明写入不会进入自定义 comparer；
- 第二次真实调用及 first → mutation → second 顺序；本 API 的两个参数不证明时间或来源；
- 第二次完整值匹配、全部隐藏可变状态、冻结及防并发写；
- 受控返回、四状态结算、外侧计时/停止、资源清理和完整异常寿命。

`FirstAndSecondValueMatches`、`ActualCallSequence`、`FullCaptureEvidence`、`Authority` 保持 `NOT ESTABLISHED`；`FirstCopyMutation` 保持 `NOT PERFORMED BY THIS API / NOT ESTABLISHED`；`HiddenMutableState` 保持 `NOT ATTESTED`。

全部上游 LIMITED 保留。D-007 保持 `UNBOUND / NOT_RUN`；真实 driver 正向 SHA 分支保持 `NOT COVERED`；120/5/5秒仅设计提议，不认定实现能力。DSP-004 保持 `OPEN / HOLD`，B-01、B-02 保持 `OPEN`。

## 6. 发布备份边界

允许备份范围仅本次新引用观察源码及本静态复核记录。此记录不声明备份已完成；实际提交和远端核验回执在执行后单独报告，避免自引用提交编号。不得加入其他未审查文件、案件数据、凭据、其他项目资产或变更已接受文件。

没有扩大任何执行资格，不把本轮静态复核解释为 Project Owner 接受、总体项目完成、完整 M 验证、来源准入或实际捕获授权。后续仍须保持上述全部 LIMITED 与边界。
