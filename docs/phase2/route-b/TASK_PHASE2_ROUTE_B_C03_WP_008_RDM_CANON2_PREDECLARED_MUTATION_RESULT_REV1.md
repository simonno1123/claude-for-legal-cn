# WP-008 CANON-2 预声明错误版本敏感性本地结果 REV1

## 1. 结论与范围

本批两个原版基线通过；八种事先固定的内存单点错误版本，全部在预定断言处被现有测试识别。批次观察为 LOCAL_PREDECLARED_MUTATION_SENSITIVITY_PASS。

这里的通过是“本轮预声明检测条件得到观察”，不是错误源码通过，也不是原版源码没有任何缺陷。仅支持对这八种错误的有限敏感性；不宣称通用 mutation score、任意缺陷检出率、独立审查、正式 Manifest 或整项目完成。

没有修改四份受检源码或其他已接受文件。错误字节仅在内存运行，压缩快照作为归档数据保留，不替换物理候选。DSP-004 OPEN / HOLD，B-01、B-02 OPEN，全部 LIMITED 和旧失败记录保持。

本批是本项目内部主执行者的本地合成验证与只读结果复核，未调用独立子审查员、Gemini 或其他外部模型，不涉及独立 ACOS 或其他项目。

## 2. 新增资产身份

| 本项目路径 | SHA-256 | bytes |
| --- | --- | --- |
| validation/route_b_c03/wp_008/RDM_CANON2_PREDECLARED_MUTATION_SENSITIVITY_REV1.ps1 | 70B28D732BCB5FF1B34673E6A23835469FF981D2A15AB719A6960D9A3C225140 | 24249 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_CANON2_PREDECLARED_MUTATION_PLAN_REV1.md | 815DA0809D473E8E33AA6EE711586C07BD9D6DA2A7D73A1AE06496F8B0EF6D8E | 7852 |
| validation/route_b_c03/wp_008/RDM_CANON2_PREDECLARED_MUTATION_REV1_OBSERVED_RESULT.json | C3297E81CF3A69662F045E5C074CF48DA3F390B157A246757695A3A5B7797425 | 44253 |

本报告自身的 SHA 在交付核对时计算，不在自身正文嵌入。

四个原版来源身份、八份预声明错误字节身份与断言在上述计划中完整绑定。来源分别为固定标量候选/验证载体及结构候选/验证载体；没有把未接受候选自动转为正式接受，也没有把代码身份核对作为来源准入。

## 3. 实际进程观察

| 案例 | 预定断言（基线不适用） | 实际观察 | SubjectValidationPassed | 包装进程退出码 | 外侧观察 ms |
| --- | --- | --- | --- | --- | --- |
| BASE-SCALAR | 不适用 | BASELINE_VALIDATOR_PASS | true | 0 | 623 |
| BASE-TREE | 不适用 | BASELINE_VALIDATOR_PASS | true | 0 | 424 |
| MU-S01 | S-ALL-CONTROLS.BYTES | EXPECTED_ASSERTION_OBSERVED | false | 0 | 327 |
| MU-S02 | B-TRUE.BYTES | EXPECTED_ASSERTION_OBSERVED | false | 0 | 214 |
| MU-S03 | P-DECODED-DUPLICATE-0 | EXPECTED_ASSERTION_OBSERVED | false | 0 | 166 |
| MU-S04 | E-UTF16-ORDER-REFUSED | EXPECTED_ASSERTION_OBSERVED | false | 0 | 213 |
| MU-T01 | T-MIXED.BYTES | EXPECTED_ASSERTION_OBSERVED | false | 0 | 181 |
| MU-T02 | N-SORT-TIE | EXPECTED_ASSERTION_OBSERVED | false | 0 | 198 |
| MU-T03 | T-EMPTY.BYTES | EXPECTED_ASSERTION_OBSERVED | false | 0 | 351 |
| MU-T04 | R-KEY-ORDER | EXPECTED_ASSERTION_OBSERVED | false | 0 | 224 |

十个案例各使用独立的新 Python 进程。两个基线完整返回原先 93/81 个局部断言、各 12 个字节向量；本轮基线结果与之前固定观察的 Result 内容一致，不计为新增业务场景。

八个负向案例均记录：

- FailureType 为 AssertionError，FailurePhase 为 RUN_CLOSED_VALIDATOR。
- FailureAssertion 与计划预声明的标识逐字一致。
- SubjectValidationPassed=false，ValidatorResult=null；原载体在该断言处停止，没有完整返回其他检查。
- 包装进程退出 0 仅表示预期负向观察被正确记录，不表示错误源码通过。
- 编译/导入失败、错误断言标识、任意异常、超时或错误源码仍返回通过，都不被本批计入预定检出。

所有 stdout 均严格解析，stderr 字节均为 0，未观察到等待超时。没有把八个故意注入错误登记为原版的正式缺陷或任何隐私/安全 Finding。

## 4. 八种错误的实际证据定位

| ID | 单点错误 | 已观察断言 | 内存错误版本 SHA-256 |
| --- | --- | --- | --- |
| MU-S01 | 控制字符十六进制大小写 | S-ALL-CONTROLS.BYTES | 331377B2D0678C91EEFABAD42A3D52494F2D5967ED72A4E6B50FD0F8C58043D9 |
| MU-S02 | 布尔编码反转 | B-TRUE.BYTES | C9F9C737304298F8CA907FE9F70172D1860E856F8A2E2089E61AE0B5F16C4BC3 |
| MU-S03 | 重复键防线移除 | P-DECODED-DUPLICATE-0 | FAC557DD990C9E3976F809D7806F0E234059B6670081952F68973F1AB0748BA3 |
| MU-S04 | 条目排序防线移除 | E-UTF16-ORDER-REFUSED | 78DF7AB168C383010E78EF447151D51C9E14071F5BA47711E7E60C0B9A487D9B |
| MU-T01 | 对象键倒序 | T-MIXED.BYTES | 70FA9086D6DA1C5CA8A9BD834A9C1814D13018BC5C67E53C57D8DFC7583BC5C3 |
| MU-T02 | 数组同 key 防线移除 | N-SORT-TIE | 4B34FB7D711D6E83A1ABC42192418F2D8D25C57B693B7C064E11BFE2260A3195 |
| MU-T03 | 文档最终 LF 移除 | T-EMPTY.BYTES | 6F27BA03EB704C858A5F82F2752C75E79D17444DF7E78C7E4C98C28F63912783 |
| MU-T04 | 原始字节一致性防线移除 | R-KEY-ORDER | E0A55AFCF1E10155F17900CB0521C12B0CE08117325B6C9A7DFF925E26CEEF60 |

每个错误版本均从固定原版独立产生，唯一匹配一次替换；不叠加前一个错误，不修改测试载体或 expected。完整记录保留原 SHA、Before/After、匹配次数、修改后字节长度/SHA 及完整源码压缩快照。

只读复核从原字节及补丁重建八份快照，均与归档逐字节身份一致。源码快照是测试数据，不是经接受的候选、修订方案、来源或工程实现。

## 5. 完整归档与运行身份

| 项 | 记录值 |
| --- | --- |
| 批次完整规范化记录 bytes | 95049 |
| 批次完整规范化记录 SHA-256 | 4D52D97AB34E1862927FDA5CB85B0E68A22B7702691FD58AF53E30F417A6885A |
| 批次 gzip bytes | 32678 |
| 批次外侧观察 ms | 3265 |
| Python 版本（十个进程） | 3.12.14 |
| Python -I / -S / -B | 1 / 1 / 1 |
| Python 可执行文件 SHA-256 | B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8 |
| Bootstrap UTF-8 SHA-256 | 951BB9DF58283CFA1955E092574B11E0839DF91BA8D776F72513E24745B9B045 |
| 基线 / 内存错误版本 / 新 Python 进程 | 2 / 8 / 10 |
| 批次意外错误记录 | null |
| GeneralizedMutationScore | NOT CLAIMED |

外层归档绑定由运行器构造的完整 LF 批次记录，不把它当作整段 PowerShell 原始 stdout 的独立见证。完整记录内另含十份真正从子进程流捕获的原始 stdout/stderr 字节及各自长度/SHA/gzip，并逐项与解析结构核对。

树案例的五个私有模块条目清理观察均为 OWNED_ENTRY_REMOVED；标量案例未登记此依赖。删除条目不证明模块/内存销毁、原子冻结或完整资源结清。

本地进程等待参数与逻辑批次预算仅是本批观察/检查，不是物理硬停止、在线内存上限或安全沙箱。解释器文件身份及同字节编译不等于完整标准库/PE/OS 闭包接受。实际活动包括固定源码读取、Python 启动和标准库导入，不宣称整体零 I/O。

## 6. 交付只读复核

交付复核 PASS，限定范围如下：

- 66 份固定项目文件和两个历史参考身份未变；不声称这些文件具有相同治理接受状态。
- 四份原版源码身份及记录一致；八份错误快照与唯一补丁可重建。
- 十个预置案例的顺序、角色集合和实际字节身份与计划一致，未混入其他错误或来源。
- 十份 stdout/stderr 的长度、散列、gzip 和解析关系一致；基线完整 Result 与旧归档一致。
- 负向案例的错误类型、阶段、精确断言和 SubjectValidationPassed=false 一致；不把任意失败当作预期检出。
- 完整记录/摘要、入口、运行身份、UTF-8/LF、表格列数、PowerShell 语法及常见密钥模式核对。对解压后的源码和原始输出亦做模式检查；模式未命中不保证任意敏感数据均不存在。

首次未物化的交付核对脚本在读取 PSObject.Properties.Count 时得到枚举属性，而非源角色总数，触发 CASE_SOURCE_COUNT。改用显式数组计数 @(...).Count 后复核通过。没有改变受测入口、四份源码、任何预期、错误版本或原始运行记录，也没有为此重跑十个受测进程。这属于交付检查器的计数表达式修正，不追溯改写实际观察。

本轮没有测试入口编译失败、错误版本无效或意外案例失败；原有历史失败归档全部保留。八个预定 AssertionError 是有意观察的测试反应，不应隐去或写作零失败/零缺陷。

## 7. 后续界线

本批补强的是“已有测试确实对选定关键错误敏感”的有限证据，没有增加业务功能。两个编码候选仍未因本结果获得自动接受。

进入正式类型合同、完整数组排序来源、准备根绑定、来源准入或 Manifest 生成前，仍须分别明确对象、完整 SHA、范围与相应接受/授权。本批不能代为签署决定，也不能用合成角色、自填两侧引用或局部通过补成可信来源。

保持 DSP-004 OPEN / HOLD、B-01/B-02 OPEN；不准入来源、不实际业务捕获、不集成、不部署、不调用外部供应商。按既定阶段备份仅普通提交/推送本轮四个新文件；Git 和 CI 均不构成治理接受或缺口关闭。
