# DSP-004 封闭 JSON 记录解析局部验证 REV1 — 实际结果与范围

## 1. 本轮结论

结果为 **LOCAL_CLOSED_JSON_DECODER_CHECKS_PASS**。新增测试入口实际退出码为 0，stderr 观察为 0 UTF-8 bytes。

24 个独立合成场景、94 个唯一检查均符合运行前的字面量预期：12 项正常解析、12 项保护性拒绝，失败检查为 0。保护性拒绝不计为验证失败；ACCEPT/REJECT 仅指输入解码结果，不是 Project Owner 的治理接受。

本轮是对固定已有解析函数的局部检查，不是正式 WP-008 执行，不声明原 189 项清单、完整组合监督器、真实 Driver、来源准入、业务捕获或集成已经通过。DSP-004 保持 OPEN / HOLD；B-01、B-02 保持 OPEN；全部上游 LIMITED 和历史失败记录保留。

## 2. 固定身份与提取边界

| 角色 | SHA-256 | bytes |
| --- | --- | --- |
| 固定已有解析函数宿主 DSP_004_LOCAL_COMPOSITION_VALIDATION_REV2.ps1 | ADAB2850039C9A15C0A175F0028B751F983FC21EB218835102247F9CD50D5262 | 19481 |
| 固定已有 PowerShell 运行文件 | 362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139 | 本文不重复记录 |

宿主路径为 validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_VALIDATION_REV2.ps1。运行文件路径及完整调用范围见本轮计划。所有仓库内路径相对本项目根目录。

| 新资产 | SHA-256 | UTF-8 bytes |
| --- | --- | --- |
| validation/route_b_c03/wp_008/DSP_004_CLOSED_RECORD_JSON_VALIDATION_REV1.ps1 | 3072E3C5A452AF740197CDE8C86FAA9061C144F0F6A2F189564DE371B721EBC5 | 12022 |
| validation/route_b_c03/wp_008/DSP_004_CLOSED_RECORD_JSON_REV1_OBSERVED_RESULT.json | 081F5C2D2A42F2C693555C57875769F996FB4BDD65163EA7213446E9F96FB693 | 5410 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_CLOSED_RECORD_JSON_PLAN_REV1.md | BD4D4AC427756FF2CC39BA508F0F3BCB12B6E51113FCC99513109EC92E23F016 | 7263 |

本结果文档不在自身正文中自绑定散列。

实际从宿主语法树唯一提取以下两个函数定义的 Extent.Text，再次确认提取后只有两条函数定义、静态解析错误为 0。函数原文本未修改。表中是提取文本经严格 UTF-8 编码的身份，不是另行创建的源文件。

| 函数 | 宿主物理行 | 提取文本 SHA-256 | UTF-8 bytes |
| --- | --- | --- | --- |
| Check-JsonKeyUniqueness | 30–40 | E573D366827177B9178C3F87C79E383AE8F9E973C473ED42852E1F2428E382CC | 619 |
| Decode-ClosedJson | 41–48 | 458877E0C9AFD1E7E666A2CF23F8FF1722429C8CC3107F43A633EAE6ED2E8A59 | 439 |

只在新的固定 PowerShell 进程内建立这两段定义并调用解析函数。**没有执行原宿主的顶层入口、C# 编译、公开组合批次或私有 child 阶段。** InputText 从未作为脚本执行；CJ-012 中看似文件读取的表达式仅作为字符串解码和比较。

## 3. 逐项实际观察

正向输入均返回原生 PSCustomObject，异常类型为 null；其原生值或形状在序列化前逐项比较。负向输入均未返回对象，原生值检查为 null，异常类型存在。只留最内层异常类型，不保留错误 Message 或 StackTrace。

| ID | 场景 | 实际结果 | 值／异常类型观察 |
| --- | --- | --- | --- |
| CJ-001 | 空对象 | ACCEPT | 零属性对象 |
| CJ-002 | 布尔及字符串 | ACCEPT | 原生 true、local |
| CJ-003 | 嵌套对象 | ACCEPT | 嵌套对象值 x |
| CJ-004 | 对象数组 | ACCEPT | 顺序 A、B |
| CJ-005 | Unicode 转义 | ACCEPT | 中文 |
| CJ-006 | 引号与反斜线转义 | ACCEPT | 精确字符串相同 |
| CJ-007 | 整数与小数 | ACCEPT | 7、1.5 |
| CJ-008 | Int64 最大值 | ACCEPT | System.Int64；9223372036854775807 |
| CJ-009 | Int64 最小值 | ACCEPT | System.Int64；-9223372036854775808 |
| CJ-010 | null 与 false | ACCEPT | 保留两个属性及原生 null／false |
| CJ-011 | 对象外 CR/LF/tab | ACCEPT | 原生 ok=true |
| CJ-012 | 看似文件读取的字符串 | ACCEPT | 精确字符串保留，不求值 |
| CJ-013 | 缺少属性值 | REJECT | System.Text.Json.JsonReaderException |
| CJ-014 | 多根对象 | REJECT | System.Text.Json.JsonReaderException |
| CJ-015 | 数组根 | REJECT | System.InvalidOperationException |
| CJ-016 | 字符串根 | REJECT | System.InvalidOperationException |
| CJ-017 | 数字根 | REJECT | System.InvalidOperationException |
| CJ-018 | null 根 | REJECT | System.InvalidOperationException |
| CJ-019 | 根对象重复键 | REJECT | System.InvalidOperationException |
| CJ-020 | 嵌套对象重复键 | REJECT | System.InvalidOperationException |
| CJ-021 | 数组内对象重复键 | REJECT | System.InvalidOperationException |
| CJ-022 | 等价 Unicode 转义键重复 | REJECT | System.InvalidOperationException |
| CJ-023 | 更深层数组内重复键 | REJECT | System.InvalidOperationException |
| CJ-024 | 尾随逗号 | REJECT | System.Text.Json.JsonReaderException |

CJ-008、CJ-009 在 PowerShell 原生比较中分别匹配 Int64.MaxValue 与 Int64.MinValue。归档只将诊断值写为十进制字符串及类型名，未把两个边界值经 JavaScript Number 转换后回写。它们证明这两个值在本轮路径中的精确性，不代表所有数值格式或超 Int64 范围策略已经确定。

## 4. 检查计数与观察归档

| 检查组 | 数量 |
| --- | --- |
| 固定身份、函数唯一性／提取文本绑定、函数限定静态解析 | 7 |
| 24 项判定／结果返回／异常边界，各 3 项 | 72 |
| 12 个正向原生值检查 | 12 |
| 后置场景数、宿主 SHA 未变、检查总数 | 3 |
| 合计 | 94 |

94 项均为 true。检查 ID 与 24 个场景 ID 均唯一，按预期命名空间逐一核对，不把检查数量说成场景数量。

实际 stdout 按 LF 规范化、补一个最终 LF，在内存中 gzip/base64 归档：

| 项目 | 实际值 |
| --- | --- |
| 完整结构化观察 UTF-8 bytes | 20041 |
| 完整结构化观察 SHA-256 | 17B31E7FD9B73DE9C1C8232C45AF1E406DB7924893E11C6EF5D200C279187F01 |
| gzip bytes | 3403 |
| 入口退出码 | 0 |
| stderr UTF-8 bytes | 0 |
| 观察摘要与完整记录 Summary | 相同 |
| 本轮意外失败 | 0 |

该归档是实际结构化观察经换行规范化的文本，不是未经处理的物理终端 transcript。完整记录保留每项合成输入、输入长度及散列、预期、实际结果、原生类型诊断与全部检查，而不只留摘要。

## 5. 接收复核与既有文件保护

主协调员在接收侧另行进行只读核对，不称为独立审查员或 Gemini 审查：

1. 解压归档，核对 gzip 长度、完整文本长度与 SHA-256。
2. 对外层 JSON 与解压后的完整 JSON 检查重复属性名，未发现重复键。
3. 比较归档 Summary 与完整记录 Summary，核对 24 个有序场景 ID、94 个预期检查 ID、每项检查值及输入长度／SHA。
4. 按独立编号分段核对前 12 项 ACCEPT、后 12 项 REJECT，以及结果返回和异常隔离；单独核对 Int64 边界诊断字符串。
5. 核对新入口语法错误为 0、24 个字面量输入齐全；新增文件为严格 UTF-8、最终 LF、无尾随空白。
6. 对新增文本及解压记录扫描常见私钥／Token 特征，未命中；该模式扫描不等于一般秘密泄露证明。公开备份内容仅为本项目合成测试与范围说明。
7. 对 24 份既有文件在运行前、运行后核对长度与 SHA-256，均精确匹配。身份集合来自本轮计划所绑定的原 20 份集合与上一轮 4 份传输故障验证文件。

24 份既有文件包含已接受源码、验证入口、历史失败和结果说明；“24 份未变”不表示这些文件全部获得过同一种治理接受。新结果不追溯修改旧 PENDING、不覆盖首轮失败，也不借本轮 PASS 自动接受新测试源码。

## 6. 保留限制及后续范围

- 这是现有两个函数的封闭输入检查，不验证目标业务 Schema、记录的真实性、权限、可信根、来源 provenance、原始 stdout 字节保真或历史报告效力。
- 不覆盖大小写冲突、空属性名、深度／大小上限、Unicode 规范化、超 Int64 数值及所有 JSON 方言；不能推广为通用解析安全认证。
- 不复跑原 189 项，不复跑上一轮 8 项 child 故障，不验证正向真实 Driver SHA 分支、外侧强停止、清理动作自身失败或全部资源收敛。
- 不启动 WP-008 正式执行、不接受 WP-008 正式结果，不自动关闭 B-01、B-02 或 DSP-004；不引入真实材料、外部模型、案件源或其他项目。
- 下一步若继续自主批次，仍仅限已授权的本地合成实现／验证和精确范围的结果复核。来源准入、真实捕获、业务集成和部署需要另外明确授权。
- 阶段性普通 Git 备份仅保存本轮新增资产，不构成治理接受或下游授权。
