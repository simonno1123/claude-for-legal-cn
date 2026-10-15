# WP-008 CANON-2 标量与条目编码本地候选批次计划 REV1

## 1. 授权解释与范围

本批依据 Project Owner 的“自动完成后续项目操作”及此前仅本地合成后续实现/验证批次授权，推进本项目已有 WP008-RDM-CANON-2 要求中的纯编码候选。它是新增候选与局部验证，不修改任何已接受文件，不接受自身，不建立正式运行资格。

这是 B-02 的局部技术准备，不是来源准入、正式 Manifest 生成或 B-02 关闭。B-01、B-02 继续 OPEN，DSP-004 OPEN / HOLD，全部 LIMITED 保留。不得因已有自动操作授权推断此前明确排除的来源准入、实际业务捕获、集成、部署或外部供应商调用已获批准。

本批由当前主执行者实施并只读复核；不冒称独立子代理审查或跨供应商审查，不涉及独立 ACOS 或其他项目。

## 2. 固定参考与新增源码

| 角色 | 本项目路径 | SHA-256 | bytes |
| --- | --- | --- | --- |
| 历史编码要求参考，主要核对第 7、8、12 节 | docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md | 6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA | 54703 |
| 最新覆盖差距说明 | docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_EVIDENCE_COVERAGE_AND_READINESS_REV1.md | C4C49EEAA12A9D725CD1F98DE509988025D272AA59FEBD6F94DEDD332109CEE9 | 14476 |
| 新增纯编码候选 | validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py | 532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4 | 8234 |
| 新增本地合成验证载体 | validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_VALIDATION_REV1.py | 1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485 | 10002 |
| 新增固定本地运行器 | validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_LOCAL_RUN_REV1.ps1 | 378CBCDACFBEFD9CBD39D19994BEB909455D1AD885816FFD1ED0FE128D0545DA | 8294 |

历史参考中的状态及创建时禁令只描述其形成时权限，不自动建立或撤销本批授权；新候选不继承正式合同接受效力。准备设计记录中的来源角色方案仅作上下文参考，不能补成真实来源已绑定。

实际 Python 可执行文件为 C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe，107312 bytes，SHA-256 为 B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8。这只绑定本地可执行文件，不是完整解释器/标准库/PE/OS 依赖闭包接受。

## 3. 实现与非实现范围

| 项 | 本候选的行为 | 不建立的能力 |
| --- | --- | --- |
| 字符串 | UTF-8；引号/反斜杠固定转义；32 个控制字符固定小写六字符转义；其他 Unicode 标量保留；拒绝代理码点 | 不修复错误 Unicode，不作规范化、大小写折叠或来源验证 |
| 整数/布尔/null | 原生精确类型；整数显式范围参数；布尔不可替代整数；null 需显式允许 | 不推断正式类型合同的每字段数值上界或可空性 |
| 原始标量字节 | JSON 数字词法在转换前校验；拒绝 -0、指数、小数、NaN/Infinity；严格 UTF-8；重编码不一致则拒绝原字节，不归一化后复用旧凭证 | 不是任意 JSON 的完整类型/范围/资源预算验证器 |
| 重复键 | 在 object_pairs_hook 中检查解码后的键，包含转义同名键与嵌套重复键 | 未取得通用 JSON 验证器认证或正式数据准入权 |
| 十五字段投影 | 类型/字段集合、分类枚举、loader、SHA 语法、DIRECT 子集路径与 phase 字符串检查；预排序条目、连续 ordinal、唯一 ID/root-path | 不解析实际文件，不证明 role/root/import/required_by 获准，不证明大小写或 reparse 别名完整排除 |
| 排序与聚合 | 检查四字段 tuple 已严格递增；原字段顺序以十四个原始 US 分隔，末尾 LF；字符串内 US/LF 保持转义 | 不重新排序或改写 ordinal，不建立全 Manifest 数组排序登记，不生成全文件/aggregate_identity |
| 散列 | 验证载体对纯合成输出字节计算 SHA-256 | 合成 entry.sha256 为虚构测试数据，不是任何物理文件的真实绑定 |

候选处理本地内存参数；无文件读写、网络调用、Provider/Gate 调用或正式 Manifest 文件输出。标准库导入、解释器活动及本地运行器读取固定源码仍是本批实际操作，不能声称整个进程零 I/O、完全隔离或完整可信闭包。

## 4. 合成验证与预期

验证载体预置 12 组独立字节向量，计划登记 93 项检查；这些数字是预定局部断言，不是独立业务场景数，不与旧批次相加为覆盖率。

- 字符串：空串、引号/反斜杠/斜杠、中文/非 BMP/分隔符标量、32 个控制字符、无 Unicode 合并、代理码点拒绝。
- 整数：Int64 两端及大于 Int64 的精确合成整数；布尔/float/字符串替代和范围违例拒绝。
- 原始字节：严格 canonical 标量、非法数字形式、可解析但非 canonical 转义/空白、无效 UTF-8/BOM、重复键及 null 边界。
- 条目：单条/双条完整字面量预期、字典插入顺序不影响字段流、US/LF 注入防护、码点排序而非 UTF-16 排序、字段缺失/未知、SHA、phase、路径、标识/路径重复等拒绝。
- 正向输出由字面量预期比较；拒绝用例必须捕获本候选 EncodingRejected，意外异常或错误拒绝原因不能冒充预期通过。

载体中合成角色、root、相对路径和 A 字符重复构成的 SHA 仅作测试刺激，不传入真实来源或业务门禁。

## 5. 本地运行与保留方法

运行器先在外侧读取并核对两个新 Python 文件的长度/SHA/严格 UTF-8。固定 Python 使用 -I -S -B；经 stdin 交接源码快照，子进程再核对 SHA，并对同一份字节作 AST 解析、编译与受控 namespace 装载。没有普通导入本项目候选或重开文件执行的回退。

外侧固定等待参数：输入等待 5000ms、进程等待 30000ms、流结清等待 5000ms。原始 stdout 以字节捕获后再严格 UTF-8/JSON 解析，独立保留 raw 与 LF 规范化记录 gzip/base64、长度和 SHA。

本私有载体在捕获后检查 262144 bytes 输出上限及空 stderr；它不是在线内存上限、防恶意源码沙箱或物理硬停止实现。等待预算不等于端到端硬时间保证，标准库/PE/OS 闭包、并发修改/恶意调用、资源耗尽及极端中断仍 LIMITED。

任何编译/测试失败均保留当轮原始输出、源码版本身份和后续修正，不回写旧成功记录或未通过记录。候选异常、检查失败或外侧捕获边界违例，不得输出总体 PASS。

## 6. 静态复核与交付边界

- 核对本批未改变旧 47 份固定保护文件、两个历史参考，以及上轮七个已备份新增文件。
- 核对新 Python/PowerShell 源码结构、最终换行、无行尾空白、Markdown 列数、常见密钥模式、观察归档完整性及断言 ID/计数。
- 标准 Python 标量/字节语义按实际载体观察，不声称跨语言或跨实现可重现性已经验证。
- 仅本批新文件可进入普通阶段提交/推送；备份和 CI 通过不是候选接受或来源准入。
- 未解决正式类型合同、完整数组路径/排序登记及外部绑定，不执行 Manifest 生成；B-01/B-02 均不关闭。
