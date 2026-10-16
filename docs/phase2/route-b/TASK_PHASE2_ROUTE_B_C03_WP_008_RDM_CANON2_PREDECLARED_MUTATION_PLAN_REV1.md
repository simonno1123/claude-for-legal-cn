# WP-008 CANON-2 预声明错误版本敏感性本地批次计划 REV1

## 1. 目的与范围

本轮根据本项目已授权的仅本地合成实现/验证批次及“继续项目操作”，核对既有测试对八种预声明编码错误的识别能力。目标是补强现有测试的敏感性证据，不新增产品功能，不修改任何既有物理源码，也不把错误版本当作新的业务候选。

错误版本仅在进程内存中从固定原字节作唯一一次固定替换。未修改磁盘源文件；不修改预期字节、验证载体、断言或原测试计数，不以错误版本通过为目标。

不授权来源准入、正式 Manifest、业务捕获、集成、部署、外部模型或独立 ACOS 项目操作。DSP-004 仍 OPEN / HOLD，B-01、B-02 仍 OPEN，全部 LIMITED 与历史失败记录保留。当前主执行者的结果核对不冒称独立审查。

## 2. 固定来源与新入口

| 角色 | 本项目路径 | SHA-256 | bytes |
| --- | --- | --- | --- |
| scalar | validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py | 532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4 | 8234 |
| scalar_validation | validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_VALIDATION_REV1.py | 1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485 | 10002 |
| tree | validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_CANDIDATE_REV1.py | F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87 | 9953 |
| tree_validation | validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_VALIDATION_REV1.py | 182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39 | 11526 |
| 本批新增固定运行器 | validation/route_b_c03/wp_008/RDM_CANON2_PREDECLARED_MUTATION_SENSITIVITY_REV1.ps1 | 70B28D732BCB5FF1B34673E6A23835469FF981D2A15AB719A6960D9A3C225140 | 24249 |

引用既有标量/条目与结构布局候选，不转移其尚未建立的正式接受/来源权限。原标量与结构测试分别仍是 93/81 个局部断言、各 12 个字节向量；本批基线复跑不新增这些场景或合并成项目覆盖率。

固定 Python 可执行文件为 C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe，107312 bytes，SHA-256 为 B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8。这不代表标准库/PE/OS 的完整正式依赖闭包已接受。

## 3. 事先固定的八种错误版本

下列元数据在任何错误版本执行之前由只读字节计算得到。每个原片段必须恰好出现一次；每个错误版本均直接来自原版，而不是叠加前一个错误版本。

| ID | 修改主题 | 目标角色 | 内存错误版本 SHA-256 | bytes | 必须观察的 AssertionError 标识 |
| --- | --- | --- | --- | --- | --- |
| MU-S01 | 控制字符十六进制大小写 | scalar | 331377B2D0678C91EEFABAD42A3D52494F2D5967ED72A4E6B50FD0F8C58043D9 | 8234 | S-ALL-CONTROLS.BYTES |
| MU-S02 | 布尔编码反转 | scalar | C9F9C737304298F8CA907FE9F70172D1860E856F8A2E2089E61AE0B5F16C4BC3 | 8234 | B-TRUE.BYTES |
| MU-S03 | 重复键防线移除 | scalar | FAC557DD990C9E3976F809D7806F0E234059B6670081952F68973F1AB0748BA3 | 8226 | P-DECODED-DUPLICATE-0 |
| MU-S04 | 条目排序防线移除 | scalar | 78DF7AB168C383010E78EF447151D51C9E14071F5BA47711E7E60C0B9A487D9B | 8199 | E-UTF16-ORDER-REFUSED |
| MU-T01 | 对象键倒序 | tree | 70FA9086D6DA1C5CA8A9BD834A9C1814D13018BC5C67E53C57D8DFC7583BC5C3 | 9967 | T-MIXED.BYTES |
| MU-T02 | 数组同 key 防线移除 | tree | 4B34FB7D711D6E83A1ABC42192418F2D8D25C57B693B7C064E11BFE2260A3195 | 9930 | N-SORT-TIE |
| MU-T03 | 文档最终 LF 移除 | tree | 6F27BA03EB704C858A5F82F2752C75E79D17444DF7E78C7E4C98C28F63912783 | 9951 | T-EMPTY.BYTES |
| MU-T04 | 原始字节一致性防线移除 | tree | E0A55AFCF1E10155F17900CB0521C12B0CE08117325B6C9A7DFF925E26CEEF60 | 9942 | R-KEY-ORDER |

原片段、替换片段、唯一匹配次数、原版身份、修改后完整字节身份及压缩快照均保留在批次完整观察记录中。修改范围只用于负向合成验证，不生成或替换任何物理候选源码，不准许使用错误版本执行生产任务。

## 4. 顺序与成功条件

执行顺序为 BASE-SCALAR、BASE-TREE，再按上述八个 ID 的固定顺序；共计划十个新的私有 Python 进程，每个只运行一个案例，不重新使用同一进程的旧模块或测试结果。

| 类别 | 严格观察条件 | 不可当作成功的情况 |
| --- | --- | --- |
| 两个原版基线 | 原验证载体返回完整原检查与向量结果，计数分别 93/81、各 12；预置 Outcome 一致 | 基线失败、未完整返回、计数漂移 |
| 八个内存错误版本 | 必须先成功解析/装载固定错误字节，然后原验证载体在 RUN_CLOSED_VALIDATOR 阶段抛出精确 AssertionError，标识与表格逐字一致 | 编译/导入失败、任意异常、错误断言标识、崩溃、超时或仍返回通过 |
| 过程边界 | 私有输入/来源/启动参数匹配；stdout 严格可解析，stderr 为空；树案例只清理本轮拥有的模块条目 | 来源漂移、未知案例、模块条目失去所有权或捕获边界失效 |

负向案例的包装进程可退出 0，表示“如实观察到预期断言”，不表示错误源码通过验证。每个负向记录必须同时保留 SubjectValidationPassed=false、AssertionError 与具体失败标识。原验证载体会在该失败点停止，不能宣称其余原检查均已完成，也不能填 0 项失败冒充全通过。

只要基线或任一预定观察不符，立即停止本批，不自动重试或修正错误预期。编译无效的错误版本不计为已识别缺陷。

## 5. 执行与证据

固定运行器从四份原版源码读取同一批快照，逐项核对长度/SHA/严格 UTF-8；唯一字符串替换后的字节再次对照第 3 节预定 SHA 和长度。每个一次性子进程使用 -I -S -B，stdin 只传固定案例 ID 与固定源码字节；子进程独立核对所选角色集合/长度/SHA，并解析编译同一快照。

树案例仅在一次性子进程 sys.modules 中登记已核对标量依赖，且只有仍属于本轮对象时才删除；这不是系统级注册、正式来源准入或销毁保证。原版候选与验证文件不会被回写。

每个进程留存完整原始 stdout/stderr 字节、长度/SHA/压缩表示及解析结构。完整批次记录另外包含八份内存源码压缩快照和精确补丁，以及原始/变更身份。外层归档绑定规范化批次记录字节，不冒称整段 PowerShell 的原始 stdout 见证。

本地等待参数为每进程输入 5000ms、进程 30000ms、流结清 5000ms；循环前后检查 60000ms 批次逻辑预算。每案 262144 bytes stdout 与空 stderr 在捕获后核对。它们不是在线内存限额、端到端物理硬停止或极端资源清理保证。

## 6. 保留限定与交付

- 这只是八种预声明单点错误的有限检出证据；不计算或声称一般 mutation score、任意缺陷检出率、独立外审或总体质量保证。
- 既有验证载体不改，expected 不是从错误版本生成；但仍是同一供应商/主执行者的私有验证，不构成跨实现认证。
- 原 66 份固定项目文件及两个历史参考须前后身份一致。原新候选没有因本批被自动接受。
- 新增四个文件仅为固定运行器、此计划、观察归档和结果说明；无正式 schema、登记、Manifest、治理接受或准入文件。
- 常见密钥模式扫描与合成范围复核不能证明任意敏感信息均不存在；仅允许本项目安全的阶段性备份。
- B-01/B-02 不因本地检出结果关闭；实际来源、根绑定、正式合同/排序政策接受与运行权限仍需分别建立。
