# WP-008 CANON-2 标量与条目编码本地候选结果 REV1

## 1. 结论与限定

本批新增纯编码候选、合成验证载体和固定本地运行器，首轮观察得到 LOCAL_SYNTHETIC_SCALAR_ENTRY_ENCODING_CHECKS_PASS：93 项局部断言、12 组独立字节预期向量通过。

这是一轮仅本地合成验证，不是正式十五场景运行、来源准入、Manifest 生成、B-02 关闭或整体项目完成。没有修改已接受文件，没有调用真实业务门禁、Provider、外部模型或独立 ACOS。候选没有因测试通过而自动被接受。

DSP-004 保持 OPEN / HOLD；B-01、B-02 保持 OPEN；全部 LIMITED、历史失败版本和后续验证记录保留。

本批由当前主执行者完成实施及只读结果复核，未另行调用独立子审查员或跨供应商审查。核对结果不得表述为独立外审通过。

## 2. 固定新增资产

| 路径（本项目内） | SHA-256 | bytes |
| --- | --- | --- |
| validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py | 532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4 | 8234 |
| validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_VALIDATION_REV1.py | 1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485 | 10002 |
| validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_LOCAL_RUN_REV1.ps1 | 378CBCDACFBEFD9CBD39D19994BEB909455D1AD885816FFD1ED0FE128D0545DA | 8294 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_CANON2_SCALAR_ENTRY_ENCODING_PLAN_REV1.md | 3E73D244A5F8AECF0DD77E0D8509BFFAEE2C28FA1A537BADD0AEFEE19F47942A | 7489 |
| validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_REV1_OBSERVED_RESULT.json | 18F9B9068B319D37B5547339A738A27DB71FE53A350992F7D85E01E1AF81B7B0 | 6370 |

本报告不嵌入自己的 SHA，交付时按实际字节计算并由阶段提交绑定。

要求参考是历史 Plan V2.2 candidate 的第 7、8、12 节，完整文件 SHA-256 为 6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA。它提供历史设计要求，不独立供应当前执行权、正式类型合同或完整数组排序登记的接受。

## 3. 实际观察记录

| 观察项 | 实际值 |
| --- | --- |
| 本地候选验证批次数 | 1 |
| Python 进程观察退出码 | 0 |
| stderr bytes | 0 |
| 外侧观察耗时 ms | 498 |
| 输入等待 / 进程等待 / 流等待预算 ms | 5000 / 30000 / 5000 |
| WaitTimedOut | false |
| 严格 UTF-8 / JSON 解析失败 | null |
| 原始 stdout bytes | 9334 |
| 原始 stdout SHA-256 | 35B052E41828479E6FF65146DC8E6F263E67EC8ABD34DECE73F414A15DBCCAF2 |
| 原始 stdout gzip bytes | 1675 |
| 完整 LF 规范化记录 bytes | 9334 |
| 完整 LF 规范化记录 SHA-256 | 35B052E41828479E6FF65146DC8E6F263E67EC8ABD34DECE73F414A15DBCCAF2 |
| 完整记录 gzip bytes | 1675 |
| Bootstrap UTF-8 SHA-256 | 86F4835158F6F5B4534520D21C096D893A4DD32542315B61C9AC5F37CF4E5508 |
| 局部断言 / 字节预期向量 | 93 / 12 |
| WholeManifestCanonicalization | NOT_IMPLEMENTED |
| FormalManifestGenerated / SourceAdmission | false / false |

Python 输出采用 LF，因此本轮 raw 与 LF 规范化完整记录的字节长度和 SHA 相同；两种表示仍分别保留。记录中的字节向量散列只绑定合成输出，不等于 entry.sha256 所指称的任何真实文件已被核验。

实际 Python 可执行文件身份为 B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8，107312 bytes。子进程记录 -I、-S、-B 均生效；这不是完整解释器/标准库/PE/OS 闭包接受，也不是操作系统级安全沙箱证明。

## 4. 已验证的局部行为

| 范围 | 本轮合成观察支持的结论 |
| --- | --- |
| Unicode 与字符串 | 空串、中文、非 BMP、U+2028/U+2029、斜杠保留；引号/反斜杠及全部 32 个控制字符按固定字节转义；代理码点拒绝；不合并不同 Unicode 标量序列 |
| 整数及布尔 | Int64 两端与一个 51 位合成整数精确输出；拒绝 bool/float/字符串替代整数及显式范围违例；布尔仅原生 bool |
| null | 必须显式允许，默认拒绝 |
| 原始标量字节 | 拒绝 -0、小数、指数、NaN/Infinity、非法 JSON、非法 UTF-8/BOM、非 canonical 空白/可选转义及代理码点；不归一化后复用原始字节身份 |
| 解码重复键 | 同名、转义同名和嵌套同名键在折叠为 dict 之前拒绝 |
| 十五字段合成投影 | 字段类型、集合、分类/loader 枚举、SHA 语法、DIRECT 子集路径、T1–T4 字符串顺序等检查；固定字段流字节及结尾 LF |
| 条目顺序与唯一性 | 既定四元组码点升序、连续 ordinal、唯一 entry ID 和精确 root/path；不重排或合并不合法输入 |
| 分隔符 | 两行各十四个原始 US 和一处 LF；字符串内 US/LF 转义不能生成额外字段/记录 |
| 预期独立性 | 十二组预期由载体内字面量字节构造，不调用被测编码器产生 expected；记录全部检查 ID、通过布尔及向量长度/SHA |

93 个检查包括类型、成功字节和拒绝分支，不是 93 个独立业务场景。它们不与旧批次叠加计算项目完成百分比。

## 5. 只读复核与保留事实

本轮交付前只读复核范围：

- 原有 47 份固定保护文件、两个历史参考及上轮七个备份文件身份保持一致；即 54 份固定项目文件加两个历史参考未变，不声称它们接受状态相同。
- 新源码长度/SHA、固定运行器身份、PowerShell 语法、源文件换行及格式。
- 观察归档 gzip、原始与规范化字节、完整记录/摘要关系、93 个预置唯一断言 ID、12 个预期向量身份及原生启动标志。
- 常见密钥模式与本批合成内容人工范围核对；模式未命中不能证明任意敏感数据均不存在。

本候选运行首轮通过，无本批编译或测试失败记录。此前其他候选的失败归档不被移除、改写或宣称已由本批修复。工具依赖定位中一个旧工具入口不可用，随后使用可用的本机依赖清单取得路径；这不是测试失败或外部代理调用。

## 6. 不得据此宣称完成的事项

| 未建立项 | 原因与保留边界 |
| --- | --- |
| 正式类型合同 | 没有生成/接受完整字段、每字段数值上界/可空性与来源绑定；显式整数参数是合成合同，不是正式政策 |
| 全部数组排序登记 | 未实现完整 Manifest 的所有数组路径及 ORDERED/SET_SORTED 政策；条目投影不替代完整登记 |
| 全 Manifest canonical JSON | 未实现递归对象/数组的两空格布局、全组身份和 detached 全文件绑定；不生成正式文件 |
| 根与来源可信性 | 不读取合成 entry 所称文件；root/role/import/required_by 的语义接受与来源可信性未建立；B-01 OPEN |
| 文件系统别名 | 精确 root/path 去重不证明大小写、重解析或系统别名完整排除；只接受本地 DIRECT 语法子集 |
| 完整规范再现性 | 单一 Python 候选加字面量预期不是跨语言/跨实现重现性证据；未系统性覆盖任意 JSON 资源耗尽、并发或恶意调用 |
| 装载与执行资格 | 固定源码同字节装载只见证本轮私有验证；不补成正式环境/载体/Manifest/输入接受或来源准入 |
| 物理硬停止与完整结清 | 运行器等待预算和捕获后大小检查不等于在线内存防护、端到端硬停止或所有资源结清证明 |
| 治理接受与下游权力 | 测试、只读复核、备份及 CI 不自动接受新候选；实际捕获、集成、部署和外部调用未授权 |

## 7. 后续动作界线

本批把 B-02 的标量/条目流编码从纯要求推进到可重核的本地候选证据，但 B-02 整体仍 OPEN。后续若要生成 Manifest，必须先有完整且单独接受的类型合同、数组排序登记、准备根绑定、输入/环境/载体身份与对应授权；缺少任何一项都不能以此候选的哈希一致或局部通过替代。

在当前自主操作范围内，可以继续本地合成实现准备与候选验证；不得为取得“项目完成”而擅自准入来源、生成正式 Manifest、执行实际业务捕获、修改已接受文件或调用外部代理。
