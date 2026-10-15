# DSP-004 本地合成证据覆盖与执行准备差距 REV1

## 1. 本批结论与效力边界

本批完成六组既有本地合成观察归档的只读一致性核对。修正新增核对器的已知记录字段适配后，结果为 FIXED_ARCHIVE_RECONCILIATION_PASS：6 组归档、71 项归档核对检查通过，新增受测对象执行次数为 0。

这不是 71 个新增业务测试，不是 DSP-004 整体通过，不是正式运行验证或来源准入。核对器读取既有记录及文件身份，没有重放原受测源码、编译 C#、运行 Python、装载候选程序集或启动 child 测试阶段。核对器自身由固定 PowerShell 进程运行，不应将“无新增受测执行”误写为“没有运行任何代码”。

本报告及其结果复核由本项目当前协调执行者完成，未另行调用独立子审查员、Gemini 或第三方模型；不得将本批复核称作独立外审。

DSP-004 保持 OPEN / HOLD；B-01、B-02 保持 OPEN；全部 LIMITED、旧失败版本及后续验证记录保留。没有接受任何新候选，也没有修改任何已接受文件。

## 2. 六组记录的覆盖单位

| 组 | 既有观察归档文件名 | 原记录覆盖单位 | 原记录检查数 | 本测试进程原始 stdout |
| --- | --- | --- | --- | --- |
| AR-001 | DSP_004_LOCAL_COMPOSITION_REV2_OBSERVED_RESULT.json | 189 已记录计划项 ID | 2027 | 仅规范化结构记录 |
| AR-002 | DSP_004_REV2_STAGE_TRANSPORT_FAULT_REV1_OBSERVED_RESULT.json | 8 本地合成案例 | 89 | 仅规范化结构记录 |
| AR-003 | DSP_004_CLOSED_RECORD_JSON_REV1_OBSERVED_RESULT.json | 24 本地合成案例 | 94 | 仅规范化结构记录 |
| AR-004 | DSP_004_JSON_GATE_CONVERSION_BOUNDARY_REV1_OBSERVED_RESULT.json | 24 本地合成案例 | 137 | 独立保留并核对 |
| AR-005 | DSP_004_BOUNDED_READ_BOUNDARY_REV1_OBSERVED_RESULT.json | 20 本地合成案例 | 187 | 独立保留并核对 |
| AR-006 | DSP_004_EXCEPTION_RETENTION_REPRESENTATION_REV1_OBSERVED_RESULT.json | 13 本地合成案例 | 77 | 独立保留并核对 |

上述六个文件均位于 validation/route_b_c03/wp_008/。不同层次的计划项、私有阶段案例、单元案例及断言可能重叠，不能相加为项目覆盖总数、独立场景数或完成百分比。

AR-001 的 189 是已记录计划项 ID。其 RW、PURE、D007 子记录分别记录 96、92、1 个计划项 ID；本批核对其并集与主记录 189 个 ID 一致。对应子记录检查数为 390、373、815；主记录 2027 项属于父级断言，不是同一层级的独立案例。

AR-002 至 AR-006 的数字仅描述各自固定本地合成记录。归档记载的通过、退出码和检查布尔值经一致性核对，不等于在本批中独立重新证明每项原断言。

## 3. 归档身份与记录身份

归档文件散列绑定磁盘文件；完整记录散列绑定 gzip 解压后的规范化 UTF-8 LF 文本。这两层不可混同。

| 组 | 归档文件 SHA-256 | 归档 bytes | 完整规范化记录 SHA-256 | 完整记录 bytes |
| --- | --- | --- | --- | --- |
| AR-001 | 3DB42CBCAA7C361B78CC1C29719BE6A76009A79DAE4FB0304FF4A93D45D672A4 | 45615 | CB06EC4381F57F19B5C043B60935104D9C4AB0A6AA99FD395321750A387D09F5 | 391606 |
| AR-002 | 8F36D01BBCA45333A147C7E6901ECA1755A6528852A6A5C40E6185198686AB54 | 25734 | BB5FCB40C5B45B90982E7ED96E645D6CC2382F12E6084A39B59BB6F8B904D94D | 22038 |
| AR-003 | 081F5C2D2A42F2C693555C57875769F996FB4BDD65163EA7213446E9F96FB693 | 5410 | 17B31E7FD9B73DE9C1C8232C45AF1E406DB7924893E11C6EF5D200C279187F01 | 20041 |
| AR-004 | 5462F44C2E9F463C104FFC83FC83ADDA021DBC9EFA842775A2B8CE22C3CDFB93 | 11614 | E7EE623FA1E10A4A88F4942418ADDE41B1BBD695AD33B85DD6DBB61D36A7041F | 27650 |
| AR-005 | 6FDAB9BC2DCD79A8D290D0E417311CD5FCA79E199DA83E42F1AB2A09AE596B52 | 11272 | B3655E83D38933D921C8F692B7F33F5F5138F9FFA68B3305CEDBFD6146A4C174 | 40004 |
| AR-006 | 2E0D13BEED92826DA17957D897499B6E04D3EAB7E31BDAEE9F46AB713BB397A0 | 7304 | 7F344983F8DCC104C5658D651B065AEDC6CE405B8E2ED37F1F61F7E17ACD32C6 | 18809 |

AR-004 至 AR-006 另保留本次旧测试进程输出的原始 stdout 字节，本批核对其散列及与规范化记录之间的 CRLF/LF 关系：

| 组 | 原始 stdout bytes | 原始 stdout SHA-256 |
| --- | --- | --- |
| AR-004 | 28672 | 14E88EAC0A74783E04CE7F922FA817CD7A19EFDCC4B4E627F4AE2E3DA2DD5CDF |
| AR-005 | 41488 | C11F70D002618F378DDC896318740296034EF1E5BE0A3024B9DB08508664ACC5 |
| AR-006 | 19417 | F7F205728BBFFC22702F8DED2AAA5DC96D60DF013161244A2763B7028A473ACD |

这些字节只见证相应测试进程自身的输出，不是正式生产 child 的输出体。AR-001、AR-002、AR-003 没有分别留存该层原始 stdout；本批准确登记为结构记录限定，不补造“原始”字节。

AR-001、AR-002 中部分 child 记录保留解析结构及散列元数据，但未保存 ChildJsonBody 原始体。因此不能从现有原始字节独立重算这些 child body 的历史散列。重新序列化或重新执行均不能追溯修复当时缺失的见证。

## 4. 本批实际核对内容

71 个核对检查由三个前置检查、六组各 11 个检查以及两个后置检查组成：

- 前置：47 份固定保护文件身份、固定核对运行器身份、两个历史要求参考身份。
- 每组：归档文件身份、JSON 重复键、完整记录字节身份、gzip 长度、记录退出码、记录 Outcome、带类型摘要投影、检查 ID 与布尔值、记录覆盖单位、记录源码绑定、原始见证可用性分类。
- 后置：输入身份未变、核对检查总数与预置一致。

“原始见证可用性分类”通过，表示缺失或存在被准确区分，不表示缺失的原始见证已通过真实性检验。“记录源码绑定”只核对既有记录中的散列与固定文件清单，不新增来源准入或权限。

各格式分别核对：

| 格式 | 处理边界 |
| --- | --- |
| AR-001 组合记录 | 扁平根结构；摘要 Stages 对 ActualStageRecords 作明确投影，RW/PURE 计 Cases，D007 计 NewPlanItemIds；其余摘要字段逐项比较 |
| AR-002 阶段故障记录 | 扁平根结构；外层摘要按其既有显式投影核对，保留 Cases 数组顺序 |
| AR-003 至 AR-006 | 完整记录的嵌套 Summary 与外层摘要按原生 JSON 类型核对 |
| 大整数与数组 | 数字按原生 JsonElement 原文核对，不经 JavaScript Number 往返；字符串区分大小写，数组保留顺序，对象按字段名对应 |
| 布尔检查字段 | RW、PURE 与顶层使用 Passed；D007 使用 Pass；缺字段、非原生 bool、非 true 或 ID 缺失/重复均不作为通过 |

JSON 的数值文本及结构核对不能恢复已丢失的 CLR Int32/Int64 身份或历史来源。核对器拒绝分支没有在本批系统性变异测试，不能据此宣称其为经认证的通用解析器或完整验证环境。

## 5. 首次失败及有限适配

首次新增核对器在 AR-001 子检查表读取处发生 PropertyNotFoundException。退出码为 1，Outcome 为 FIXED_ARCHIVE_RECONCILIATION_INCOMPLETE。此前登记的 11 个检查均为 true，但全组未完成，GroupCount 为 0。

FailedAuditChecks 为 0 仅表示已登记布尔项中无 false；非空 PrimaryExceptionType、退出码和 INCOMPLETE 共同阻止登记通过。不能把该首次观察改写为成功或据此判定旧归档损坏。

原因是新增核对器错误假设 D007 也使用 Passed。只对尚未接受的新核对器增加固定的 Passed/Pass 字段选择；仅 D007 选择 Pass。未修改原记录、预置通过条件、固定散列或计数。原入口快照、首轮完整失败观察、原计划和适配说明均保留。

| 观察 | 外侧耗时 ms | 退出码 | stderr bytes | 等待超时 | 核对结果 |
| --- | --- | --- | --- | --- | --- |
| 首次入口 | 3047 | 1 | 0 | false | INCOMPLETE；AR-001；11 个已登记检查 |
| 字段适配后 | 3645 | 0 | 0 | false | 6 组、71 项核对通过 |

以上是核对进程的本次观察，不是受测对象性能预算或硬停止保证。

## 6. 最终观察归档

| 字段 | 记录值 |
| --- | --- |
| ArchiveVersion | DSP004-ARCHIVE-RECONCILIATION-REV1-OBSERVED |
| 核对入口 SHA-256 | 2AF0A8E2902AF838FC5A60DBAE92DA0D47C211A2F1CAC45BA4CEEA6BDF1CD035 |
| 外侧等待预算 ms | 60000 |
| 观察退出码 / stderr bytes | 0 / 0 |
| 原始 stdout bytes | 24432 |
| 原始 stdout SHA-256 | 62802FB58DF0605D6DBE3C686D3B1BA0863AF05F69BE8D26D0B9A65AD25B1A06 |
| 原始 stdout gzip bytes | 5167 |
| 完整规范化记录 bytes | 23751 |
| 完整规范化记录 SHA-256 | BA2411E426851FB34AC74840527679CDEDBE8CA730A0678759D3CD5BD5A7FC75 |
| 完整规范化记录 gzip bytes | 5148 |
| 严格 UTF-8 / JSON 失败类型 | null |
| 新增受测对象执行 | 0 |

另行只读复核检查了完整观察的散列、原始/规范化关系、六组预置、71 个唯一核对 ID、47 份保护清单、首轮失败记录及源码版本身份，复核结果 PASS。该结果不扩展为原历史执行事实的独立外部验证。

## 7. 仍未建立的执行准备条件

| 事项 | 已有证据边界 | 仍未建立或本批未建立的条件 | 状态 |
| --- | --- | --- | --- |
| 本地合成组合与单位边界 | 已有组合、JSON、读取预算、异常表示和任务观察等固定记录；本批只核对它们的一致性 | 不等于全项目覆盖、所有异常分支或实际来源贯通 | LIMITED |
| Project / Session / Provider 来源角色 | 已有设计要求分别绑定预期侧和实际侧 | 可信角色、准确来源身份及使用范围不能由调用者同时自填两侧后宣告可信；本批未建立真实来源绑定 | UNBOUND / HOLD |
| B-01 准备根绑定 | 历史要求是先在准备授权及接受记录下绑定，运行阶段再引用复核 | 硬编码路径/SHA 的合成检查不替代 Manifest 生成前的可信准备根绑定 | OPEN |
| B-02 规范字节与外部绑定 | 历史规格标识 WP008-RDM-CANON-2，要求标量、Unicode、空白、完整数组顺序及外部绑定 | 本地 JSON 比较不等于已准入规范来源字节；不得复用旧散列替代新绑定 | OPEN |
| 跨 child 引用、冻结与依赖闭包 | 有局部记录和摘要投影 | 全部依赖的同引用/冻结语义、装载可信边界及完整闭包未由归档一致性建立 | LIMITED |
| 清理失败与硬停止 | 有异常并存表示、读取边界及私有超时观察 | 真实清理失败、同步调用的物理硬停止及资源全部结清仍不能由表示结构或单个超时样本证明 | LIMITED |
| 正式运行与结果权限 | 本批限既有归档核对 | 本批不建立正式执行授权、来源准入、环境/载体/Manifest 的正式接受或运行结果接受；不推断仓库中不存在其他历史记录 | NOT ESTABLISHED BY THIS BATCH |

上游被有限接受的源码身份仍是固定 SHA 候选，有限接受不自动转成正式运行资格。归档一致性可以使后续决策更可追溯，但不能关闭 B-01/B-02 或取消其他 LIMITED。

## 8. 文件保护与历史参考

六份固定结果文档中的 41 条文件清单，加六份结果文档自身，共 47 个唯一受保护路径，核对前后 SHA-256 与长度保持一致。这是本批固定身份保护集合，不意味着其中每个文件具有相同接受状态。

另外两个历史参考身份保持不变：

| 参考 | SHA-256 | bytes |
| --- | --- | --- |
| TASK_PHASE2_ROUTE_B_C03_WP_008_OPERATIONAL_VALIDATION_PLAN.md | E9643D0993532A1E1603B66F95CD288F394BDDA621EFB6784B256CECFC915E6D | 23939 |
| TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md | 6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA | 54703 |

两个参考均位于 docs/phase2/route-b/，只用于辨识历史要求，不将旧候选中的生命周期措辞认作当前授权，不把受控替换后的源码与旧计划散列差异自动解释为违规。准备设计记录另作局部段落只读参考，不声称完成全文审查，也不将其计入上述两个参考的前后散列保护集合。

## 9. 本批新增资产身份

下表不列本报告自身散列，避免自引用。本报告的实际身份由阶段提交及交付核对记录绑定。

| 路径（本项目内） | SHA-256 | bytes |
| --- | --- | --- |
| validation/route_b_c03/wp_008/DSP_004_EVIDENCE_ARCHIVE_RECONCILIATION_REV1.ps1 | 2AF0A8E2902AF838FC5A60DBAE92DA0D47C211A2F1CAC45BA4CEEA6BDF1CD035 | 19604 |
| validation/route_b_c03/wp_008/DSP_004_EVIDENCE_ARCHIVE_RECONCILIATION_REV1_OBSERVED_RESULT.json | AA74E3F4E9471E15C98673DF4F4CA8BD10359FBB853D17D6A06F9CD424303DDB | 14972 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_EVIDENCE_ARCHIVE_RECONCILIATION_PLAN_REV1.md | 95952FFA66F9060B5FD466A627B1F566F9264CE97A1C7E7814AE45AD49489505 | 9075 |
| validation/route_b_c03/wp_008/DSP_004_EVIDENCE_ARCHIVE_RECONCILIATION_ATTEMPT1_ENTRY_SNAPSHOT.txt | FCEDC4752FDC490E0E82BC914781FF5B5EA4E5627391C91BE0DF3192035E29A9 | 19341 |
| validation/route_b_c03/wp_008/DSP_004_EVIDENCE_ARCHIVE_RECONCILIATION_ATTEMPT1_OBSERVED_FAILURE.json | 411D913751AD0529239E58FFBD12CD5EB680ADFC7A9767134B2A3A3FD0DD8838 | 11910 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_EVIDENCE_ARCHIVE_RECONCILIATION_READER_CLARIFICATION_REV1.md | 33E0FD0AD40DE341C1FF64AA2250992E32C7E6ADC2BA7884140B97B928DF2E65 | 2862 |

发布前只核对本批新增内容、固定身份、UTF-8/换行/表格结构和常见密钥模式；模式扫描未命中不等于证明不存在任何敏感信息。材料为本地合成及归档元数据，不含案件材料或外部来源正文。

## 10. 后续顺序与持续限制

下一项有效工作应优先收敛来源绑定和准入前置条件，而不是重复增加相同层次的合成断言计数。可以依据现有设计整理准确缺口，但实际来源准入、可信角色绑定及正式运行仍须各自明确的对象、范围和授权；本报告不代为签发这些权限。

持续保持：

- 不修改已接受文件；不追溯修复旧失败记录或缺失原始字节。
- 不准入来源、不做实际业务捕获、业务集成或部署。
- 不访问或修改独立 ACOS 或其他项目，不调用外部模型或供应商。
- 不把备份、提交、CI 通过或本批核对通过解释为治理接受、正式运行通过或项目完成。
- DSP-004 OPEN / HOLD；B-01 OPEN；B-02 OPEN；全部 LIMITED 保留。
