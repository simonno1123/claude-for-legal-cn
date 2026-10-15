# DSP-004 JSON 语法闸门与对象转换边界局部验证计划 REV1

## 1. 本批范围

Project Owner 要求继续已授权的本地合成批量任务。本批仅新增局部测试入口、计划、观察归档和结果说明；不修改已接受源码、既有测试、结果或失败历史。

检查固定已有解析函数的两层边界：

- 闸门观察：System.Text.Json 解析、对象根要求、原有 Ordinal 字段唯一性函数。
- 复合解码：原有 Decode-ClosedJson，包含上述闸门及限定 Depth 40 的 PowerShell 对象转换。

闸门观察器只是本批测试适配器，不是新生产解析器。对同一输入分别观察两层，避免把语法与字段唯一性允许误称为最终可用对象。ACCEPT/REJECT 是合成数据路径判定，不是治理接受。

范围仍为本项目 claude-for-legal-cn。不涉及独立 ACOS、外部模型、真实材料、来源准入、业务捕获、集成或部署。全部 LIMITED 保留；DSP-004 为 OPEN / HOLD，B-01、B-02 为 OPEN。

## 2. 固定身份及原文提取

| 角色 | 路径 | SHA-256 | bytes |
| --- | --- | --- | --- |
| 只读受测函数宿主 | validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_VALIDATION_REV2.ps1 | ADAB2850039C9A15C0A175F0028B751F983FC21EB218835102247F9CD50D5262 | 19481 |
| 本批新测试入口 | validation/route_b_c03/wp_008/DSP_004_JSON_GATE_CONVERSION_BOUNDARY_VALIDATION_REV1.ps1 | 7985CB5C18E307FF86659BAD8726195414988F7BC50C0431E576CD29C9214B8D | 14391 |

使用已有固定运行文件 C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe，SHA-256 为 362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139，不下载或安装运行环境。

从语法树唯一取得下列函数 Extent.Text，核对严格 UTF-8 编码后的提取文本长度与 SHA，再次确认只含两条函数定义。它们不被修改；原宿主顶层批次不执行。

| 函数 | 原宿主行 | 提取文本 SHA-256 | UTF-8 bytes |
| --- | --- | --- | --- |
| Check-JsonKeyUniqueness | 30–40 | E573D366827177B9178C3F87C79E383AE8F9E973C473ED42852E1F2428E382CC | 619 |
| Decode-ClosedJson | 41–48 | 458877E0C9AFD1E7E666A2CF23F8FF1722429C8CC3107F43A633EAE6ED2E8A59 | 439 |

提取文本身份不是独立源文件身份。新入口只在新的固定 PowerShell 进程内加载这两个函数定义；不编译 C#，不运行组合批次或 child 阶段，不运行原 189 项清单。

## 3. 运行前冻结的独立预期

24 个输入及两层预期先以代码字面量固定。深度输入仅在内存中按固定次数加包，不使用文件、代码求值或任何外部数据。

| ID | 场景 | 闸门预期 | 解码预期 |
| --- | --- | --- | --- |
| JG-001 | 根对象 A/a 大小写近似字段 | ACCEPT | REJECT |
| JG-002 | 嵌套对象 K/k 字段 | ACCEPT | REJECT |
| JG-003 | 数组对象 ID/id 字段 | ACCEPT | REJECT |
| JG-004 | 根对象空字段名 | ACCEPT | REJECT |
| JG-005 | 嵌套对象空字段名 | ACCEPT | REJECT |
| JG-006 | 数组对象空字段名 | ACCEPT | REJECT |
| JG-007 | 根对象前的行注释 | REJECT | REJECT |
| JG-008 | 对象内块注释 | REJECT | REJECT |
| JG-009 | 未加引号 NaN | REJECT | REJECT |
| JG-010 | 未加引号 Infinity | REJECT | REJECT |
| JG-011 | 数字前导零 | REJECT | REJECT |
| JG-012 | 小数点后缺少数字 | REJECT | REJECT |
| JG-013 | 数字前导正号 | REJECT | REJECT |
| JG-014 | 50 层对象包装 | ACCEPT | REJECT |
| JG-015 | 根对象内 50 层数组包装 | ACCEPT | REJECT |
| JG-016 | 65 层对象包装 | REJECT | REJECT |
| JG-017 | 字符串未闭合 | REJECT | REJECT |
| JG-018 | 字符串内未转义 tab | REJECT | REJECT |
| JG-019 | 10 层对象包装 | ACCEPT | ACCEPT |
| JG-020 | 根对象内 10 层数组包装 | ACCEPT | ACCEPT |
| JG-021 | 中文字段名与合成值 | ACCEPT | ACCEPT |
| JG-022 | 点号／方括号字段名 | ACCEPT | ACCEPT |
| JG-023 | 非空空格字段名 | ACCEPT | ACCEPT |
| JG-024 | 转义换行字段名 | ACCEPT | ACCEPT |

预期闸门允许 14 项、拒绝 10 项；复合解码允许 6 项、拒绝 18 项。8 项应观察到闸门允许但复合转换拒绝，这是预置限制场景，不自动当作新产品缺陷或隐私／安全 Finding。

正向对象在序列化前核对原生叶值、包装层次、字段数量或精确字段名。负向只断言不释放结果且存在异常类型，不强制预设异常包装链、Message 或 StackTrace。

计划 137 个检查：7 项身份／原文提取／静态解析检查，24×5 项两层判定／异常边界／返回隔离检查，6 项正向原生值检查，4 项后置场景计数／分层计数／源码不变／检查计数。检查数不等于独立场景数。

## 4. 既有文件保护与结果留存

运行前、运行后保护 28 份既有文件。集合按以下三个已经固定散列的结果文档读取表格，再加各文档自身；先核对文档散列，后使用其身份表。仅接受本项目规定路径前缀，禁止重复路径或路径越界。

| 锚点结果文档 | SHA-256 | bytes | 身份表行数 |
| --- | --- | --- | --- |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_LOCAL_COMPOSITION_REV2_RESULT.md | C44D9C96C4F6E2D74CE9EC0F0019BEC07F1D541F0E916EC184ECEB0BED8DEE8A | 12221 | 19 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REV2_STAGE_TRANSPORT_FAULT_REV1_RESULT.md | 33A920C3D3F8550F4B4CA3B2F1AC1CC0D9476F704A18E143B2D7BA51DE3BC53C | 10158 | 3 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_CLOSED_RECORD_JSON_REV1_RESULT.md | 8522AC8662C0617EB92CE1A3F65D7A9255AEFB998E4ED8DEB842B88B6911E203 | 8849 | 3 |

三表共 25 个文件加 3 个锚点文档，为 28 个唯一文件。它们包括已接受源码、历史失败及观察资料；不表示所有文件获得了同一种治理接受。

本批实际 stdout 换行规范化为 LF、补最终 LF，在内存中 gzip/base64 归档，保留所有合成输入、输入长度与 SHA、两层预期与实际、异常类型、原生诊断及全部检查。不把规范化记录叫未经处理的物理终端 transcript。

接收侧另行解压、重算身份、拒绝重复 JSON 键、比较 Summary、逐项核对 24 个场景和 137 个检查的独立 ID 集合。若意外失败，先保留该次入口原文和失败观察，不能默改既有文件或事后调整预期以宣称通过。

备份仅处理本批新增的本项目公开适宜合成资产。核对秘密特征、格式、固定身份和远端 main；只作普通提交与推送，不强推，不把备份解释为接受。

## 5. 限定与未授权事项

- 只检查表列输入，不确定精确最大深度边界；50／65／10 是本批选定深度点，不是所有嵌套与运行环境保证。
- 不测试超 Int64 数值、Unicode 规范化冲突、大小／资源上限、全部 JSON 方言或通用反序列化安全性。
- 对大小写相近与空字段名观察到的拒绝，不能外推为所有 JSON 合法对象都可转换，亦不等于一般数据保真或业务 Schema 接受。
- 不复跑上一批 24 项或原 189 项，不作 child 字节、停止计时、清理失败或完整组合监督器覆盖声明。
- 不启动正式 WP-008，不接受正式结果，不关闭 DSP-004、B-01、B-02 或任何 LIMITED。
- 不读取真实 Driver／案件材料，不准入来源、不实际捕获、不集成、不部署，不涉及独立 ACOS 或其他项目。
