# WP-008 CANON-2 结构布局本地合成批次计划 REV1

## 1. 本批授权解释

根据本项目已有仅本地合成实现与验证批次授权，以及本轮“自动完成后续项目操作”，继续补足 B-02 的纯编码候选：显式合成类型合同、对象键排序、数组政策、递归字节布局和原始规范字节拒绝路径。

本批不修改任何已接受文件，不自动接受新候选，不生成正式 Manifest，不准入来源，不进行实际业务捕获、集成、部署、Provider/Gate 调用或外部代理审查。不涉及独立 ACOS 或其他项目。

本计划是本批执行范围的记录，不是 Project Owner 新签署的接受、准入或关闭决议。DSP-004 仍 OPEN / HOLD；B-01、B-02 仍 OPEN；全部 LIMITED 保留。

## 2. 固定来源与新增候选

| 角色 | 本项目路径 | SHA-256 | bytes |
| --- | --- | --- | --- |
| 上轮未自动接受的标量候选，仅私有合成依赖 | validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py | 532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4 | 8234 |
| 新结构布局候选 | validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_CANDIDATE_REV1.py | F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87 | 9953 |
| 新合成验证载体 | validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_VALIDATION_REV1.py | 182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39 | 11526 |
| 新固定本地运行器 | validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_LOCAL_RUN_REV1.ps1 | CB489E8BA6F262C0E71AA025E1C3DDEF25D74ED5D8DB845C84D1D28CA140B33C | 9554 |

历史要求参考：docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md，第 12.1–12.6 节；SHA-256 为 6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA。只采用已记录要求，不将形成时状态、接受或授权转移至新 SHA。

上轮结果参考：docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_CANON2_SCALAR_ENTRY_ENCODING_RESULT_REV1.md，SHA-256 为 086492C798DD3F5EA113DA7AA8AD9FE5F9052390AAEB2451A61C5BB207019CCD。上轮 93 项断言不在本批重跑或相加为业务覆盖率。

固定 Python：C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe；107312 bytes；SHA-256 为 B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8。仅绑定本地解释器文件，不声明完整解释器/标准库/PE/OS 闭包已经接受。

## 3. 新候选的合成合同语法

合同是验证载体内的原生嵌套 tuple；不物化正式 schema 或数组登记，不建立任何真实来源权威。

| 合同形式 | 明确含义 |
| --- | --- |
| string / boolean / null | 固定标量种类；null 仅允许 None |
| integer，显式下界/上界 | 只允许原生 int，bool 不可替代；不推断正式字段范围 |
| nullable，单一非 null/nullable 子合同 | 显式可空；非空分支完整执行子合同 |
| object，唯一字段名/子合同 tuple | 全字段必需，未知与缺失均拒绝；键按 Unicode 标量码点排序 |
| array，元素合同，ORDERED 政策 | 必须提供确切 key tuple 序列与是否明确允许重复 key；保持给定顺序，不自行排序 |
| array，元素合同，SET_SORTED 政策 | 必须提供明确 selector；标量仅 string/int；对象只支持直接 string/int 字段构成的 key；精确排序，同 key 拒绝 |

每个数组合同只能有一种明确政策；未知、多余或缺失政策参数均拒绝。该内嵌结构避免本合成合同的同一路径出现两条政策，但不证明正式 Manifest 的所有数组路径已经在独立接受的登记中覆盖。

selector 和 ORDERED 序列只规定本批合成元数据的选定 key，不独立证明真实身份、完整排序键或来源授权。允许重复 key 仅是合成显式规则，不是正式重复身份豁免。

## 4. 字节与拒绝边界

- 同字节标量依赖按上轮固定 SHA 装载，不复制修改原源码。
- 文档接口要求根 object；递归非空容器采用两空格缩进、LF、逗号/冒号规则；空容器为 {} 或 []；完整文档恰好一个最终 LF。
- compact 接口没有无意义空白和最终 LF；不替代十五字段条目聚合流或其政策。
- 已提供原始字节先作严格 JSON/UTF-8/数字/重复键处理，再按显式合同重算；不相等直接拒绝，不修复输入后保留旧凭证。
- 不把 SHA、权限或未来接受记录嵌入文档自身；测试散列仅在外侧观察记录中产生。
- 不强制排序 ORDERED，不把未提供的政策解释为 SET_SORTED，不静默忽略未知字段，不用 JSON bool/float 冒充整数。

局部逻辑上限：合同和值分别深度最多 32、节点最多 4096；字符串最多 32768 个 Python 字符；规范投影标量字节与输出字节各最多 262144。上限违例拒绝；它们不是正式 Manifest 容量规格、OS 内存隔离或硬时限保证。

调用方已有对象的原子冻结、并发修改、恶意上下文/运行器替换、所有资源耗尽和完整环境可信性均未由本候选解决。

## 5. 合成验证计划

预置 12 组新字节向量、81 项局部断言，首轮结果未观察前不登记通过。向量 expected 为独立字面量，不调用被测编码器生成。

包括：

- 空对象/嵌套空容器、对象插入顺序、码点排序与转义键、紧凑布局及精确最终 LF。
- SET_SORTED 标量/复合 key、ORDERED 不排序、嵌套数组逐层政策、显式重复 key 与精确大整数。
- 合同未绑定、种类/arity/范围/字段重复、原生字符串子类键、未知/缺失字段、bool/float/null 类型违例。
- 缺失/重叠形状/未知数组政策、错误序列/成员/重复 key、缺失或重复 selector、非 string/int 排序键、同 key 冲突。
- 原始非规范 key/set 顺序、compact/双 LF/CRLF、解码重复键、非法数字/BOM/UTF-8、代理码点拒绝。
- 值循环、深度、节点、字符串、原始字节、规范投影字节及最终布局字节限制。

局部断言数不是独立业务场景数，不和之前任何批次叠加为项目完成率。

## 6. 固定运行及保留方法

运行器在外侧读取三个固定源码快照，校验长度、SHA 和严格 UTF-8。Python 使用 -I -S -B，经 stdin 接收快照，再次核对后对同一字节作 AST 解析及编译。

标量依赖只在该一次性子进程的 sys.modules 中以 rdm_canon2_scalar_fixed_dependency_rev1 名称登记；预先占用即拒绝。结构候选从此已装载模块取得固定函数，不能通过文件搜索替换。执行后只有仍由本轮拥有的条目才删除，登记实际清理结果。不要求真实人物信息，也不建立系统级注册、正式来源准入或可信根。

输入/进程/流等待预算为 5000/30000/5000ms；沿用本地私有捕获器，原始 stdout 字节与 LF 规范化完整记录分别以 gzip/base64、长度和 SHA 留存。262144 bytes 输出上限在捕获后检查，不宣称在线内存上限或物理硬停止。

任何编译/测试失败须保留实际观察、原版本及修正说明，不追溯修改成功或失败记录。

## 7. 交付复核与持续限制

复核旧 60 个固定项目文件及两个历史参考身份不变；新文件只做本项目格式、PowerShell 语法、断言/向量、完整观察及常见密钥模式核对。复核由当前主执行者完成，不冒称独立审查或 Gemini 结论。

仅本批新增文件可作为阶段性备份提交/推送。备份、CI 或本地通过不接受新候选，不补成正式类型合同/完整数组排序登记、准备根、正式来源或完整 Manifest 接受。B-01/B-02 保持 OPEN。
