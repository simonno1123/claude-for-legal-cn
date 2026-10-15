# DSP-004 JSON 语法闸门与对象转换边界局部验证 REV1 — 实际结果与范围

## 1. 本批结论与失败保留

修正本批新测试入口的输出编码后，实际结果为 **LOCAL_JSON_GATE_CONVERSION_BOUNDARY_CHECKS_PASS**：24 个合成场景、137 个唯一检查均符合运行前冻结预期，失败检查为 0。最终入口退出码 0、stderr 0 bytes，未触发原 15000 ms 外侧等待限制，外侧实际观察为 1363 ms。该计时不是硬停止保证。

这不是“首轮无失败”：本批保留两次未完整取得结果的采集、一次诊断启动错误、后续诊断及首次入口快照。最终 0 失败检查只对应最终完整观察，不抹除历史采集问题，不应改写为所有尝试从未出错。

主要边界结论：**语法闸门允许不等于最终 PowerShell 对象转换允许**。本批 8 个输入在前一层允许、后一层拒绝；不为兼容这些输入而修改固定已有解析函数或自动放宽接口。

DSP-004 保持 OPEN / HOLD；B-01、B-02 保持 OPEN；全部 LIMITED 保留。本批不构成正式 WP-008 执行或结果接受，不准入来源、不实际业务捕获、不集成、不部署，不涉及独立 ACOS 或其他项目。

## 2. 固定身份与新增资产

只读受测宿主为 validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_VALIDATION_REV2.ps1，SHA-256 为 ADAB2850039C9A15C0A175F0028B751F983FC21EB218835102247F9CD50D5262，19481 bytes。已有固定 PowerShell 运行文件 SHA-256 为 362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139。

新增文件共 10 份，包括本结果文档。路径相对本项目根目录；本结果文档不在自身正文中自绑定散列。

| 新增资产 | SHA-256 | bytes |
| --- | --- | --- |
| validation/route_b_c03/wp_008/DSP_004_JSON_GATE_CONVERSION_BOUNDARY_VALIDATION_REV1.ps1 | E7BCAAE1F2BA509323F915C6E38240A63E7A02EDCB1E2F13E2336B7EA806D0DB | 14449 |
| validation/route_b_c03/wp_008/DSP_004_JSON_GATE_CONVERSION_BOUNDARY_REV1_OBSERVED_RESULT.json | 5462F44C2E9F463C104FFC83FC83ADDA021DBC9EFA842775A2B8CE22C3CDFB93 | 11614 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_JSON_GATE_CONVERSION_BOUNDARY_PLAN_REV1.md | 9E278835708638E871087ACAB73DBDB84801E7AB404DA88EDF3B0BC0BF95E6E9 | 7494 |
| validation/route_b_c03/wp_008/DSP_004_JSON_GATE_CONVERSION_BOUNDARY_ATTEMPT1_ENTRY_SNAPSHOT.txt | 7985CB5C18E307FF86659BAD8726195414988F7BC50C0431E576CD29C9214B8D | 14391 |
| validation/route_b_c03/wp_008/DSP_004_JSON_GATE_CONVERSION_BOUNDARY_ATTEMPT1_FAILURE.json | 6A76FF30B8FB46436F4E93AC8354B9E190BC1D9100EE519CB32BB83AF9D88967 | 1205 |
| validation/route_b_c03/wp_008/DSP_004_JSON_GATE_CONVERSION_BOUNDARY_ATTEMPT1_DIAGNOSTIC.json | C9E3A4A56E446581873D9FB6C61488109C8CC8BF38B5CA2FB647C26F9EA81A19 | 36391 |
| validation/route_b_c03/wp_008/DSP_004_JSON_GATE_CONVERSION_BOUNDARY_ATTEMPT2_FAILURE.json | 80C33FB78DE6EE933D9DC7B570DEC0BBB23C916E523F025F5F4CA9436A50D57C | 1092 |
| validation/route_b_c03/wp_008/DSP_004_JSON_GATE_CONVERSION_BOUNDARY_ATTEMPT1_RAW_STDOUT_DIAGNOSTIC.json | 770F0A21297D42125464110A40F48673DA0E701BDE7A603FF74FA839197E6951 | 6653 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_JSON_GATE_CONVERSION_BOUNDARY_EXECUTION_CLARIFICATION_REV1.md | 5B0A6F8B8E254BFA0EB0B3ECACC909CAD9944FB428DEF02E6118FF6F9335A790 | 4051 |

原计划保留首次入口身份；EXECUTION_CLARIFICATION_REV1 只补充本批新入口输出编码修正及其最终身份，不追溯改写原计划或首次失败。

## 3. 实际执行路径

1. 核对固定宿主和运行文件身份，从宿主语法树唯一提取 Check-JsonKeyUniqueness 与 Decode-ClosedJson 的 Extent.Text。
2. 提取后的定义再次静态解析，确认只有两条函数定义。原宿主顶层批次、C# 编译、组合监督器及 child 阶段均未执行。
3. 测试适配器另行观察 System.Text.Json 解析、对象根检查和相同 Ordinal 唯一性函数；它不是新生产解析器。随后对同一输入调用完整原 Decode-ClosedJson。
4. 两层预期均在调用前写死。没有根据结果修改输入、预期、137 个检查或受测函数。
5. 仅本批尚未接受的新入口增加 Console.OutputEncoding 与 PowerShell OutputEncoding 两个 UTF-8 赋值，其他字节与首次快照一致。接收复核已比较该精确变更关系。
6. 最终外侧先用原始字节读取完整 stdout/stderr，再严格解码，避免字符读取任务因编码错误而提前停止排空管道。

| 提取函数 | 宿主行 | 提取文本 SHA-256 | UTF-8 bytes |
| --- | --- | --- | --- |
| Check-JsonKeyUniqueness | 30–40 | E573D366827177B9178C3F87C79E383AE8F9E973C473ED42852E1F2428E382CC | 619 |
| Decode-ClosedJson | 41–48 | 458877E0C9AFD1E7E666A2CF23F8FF1722429C8CC3107F43A633EAE6ED2E8A59 | 439 |

提取文本身份不等同于独立源文件身份。本批只通过指定两个函数观察已有逻辑，不改变它们或赋予新执行权限。

## 4. 逐场景实际观察

ACCEPT/REJECT 仅指合成输入的数据路径结果，不是治理接受。负向场景只要求不释放结果且记录异常类型，不以特定错误 Message 或包装链作为预期。

| ID | 场景 | 闸门实际 | 复合解码实际 | 复合解码异常类型 |
| --- | --- | --- | --- | --- |
| JG-001 | 根对象 A/a 字段 | ACCEPT | REJECT | System.InvalidOperationException |
| JG-002 | 嵌套 K/k 字段 | ACCEPT | REJECT | System.InvalidOperationException |
| JG-003 | 数组对象 ID/id 字段 | ACCEPT | REJECT | System.InvalidOperationException |
| JG-004 | 根对象空字段名 | ACCEPT | REJECT | System.InvalidOperationException |
| JG-005 | 嵌套空字段名 | ACCEPT | REJECT | System.InvalidOperationException |
| JG-006 | 数组对象空字段名 | ACCEPT | REJECT | System.InvalidOperationException |
| JG-007 | 对象前行注释 | REJECT | REJECT | System.Text.Json.JsonReaderException |
| JG-008 | 对象内块注释 | REJECT | REJECT | System.Text.Json.JsonReaderException |
| JG-009 | 未加引号 NaN | REJECT | REJECT | System.Text.Json.JsonReaderException |
| JG-010 | 未加引号 Infinity | REJECT | REJECT | System.Text.Json.JsonReaderException |
| JG-011 | 前导零数字 | REJECT | REJECT | System.Text.Json.JsonReaderException |
| JG-012 | 不完整小数 | REJECT | REJECT | System.Text.Json.JsonReaderException |
| JG-013 | 前导正号数字 | REJECT | REJECT | System.Text.Json.JsonReaderException |
| JG-014 | 50 层对象包装 | ACCEPT | REJECT | Newtonsoft.Json.JsonReaderException |
| JG-015 | 根对象内 50 层数组 | ACCEPT | REJECT | Newtonsoft.Json.JsonReaderException |
| JG-016 | 65 层对象包装 | REJECT | REJECT | System.Text.Json.JsonReaderException |
| JG-017 | 未闭合字符串 | REJECT | REJECT | System.Text.Json.JsonReaderException |
| JG-018 | 字符串内原始 tab | REJECT | REJECT | System.Text.Json.JsonReaderException |
| JG-019 | 10 层对象包装 | ACCEPT | ACCEPT | NONE |
| JG-020 | 根对象内 10 层数组 | ACCEPT | ACCEPT | NONE |
| JG-021 | 中文字段名 | ACCEPT | ACCEPT | NONE |
| JG-022 | 标点字段名 | ACCEPT | ACCEPT | NONE |
| JG-023 | 非空空格字段名 | ACCEPT | ACCEPT | NONE |
| JG-024 | 转义换行字段名 | ACCEPT | ACCEPT | NONE |

分层统计：

| 观察 | 数量 |
| --- | --- |
| 闸门 ACCEPT / REJECT | 14 / 10 |
| 复合解码 ACCEPT / REJECT | 6 / 18 |
| 闸门 ACCEPT、复合解码 REJECT | 8 |
| 最终释放的合格合成对象 | 6 |
| 最终拒绝且未释放对象 | 18 |

JG-001 至 JG-006 说明 Ordinal 字段唯一性并不替代 PowerShell 对象字段名限制。JG-014、JG-015 说明两层在选定嵌套深度点的行为不同；本批不宣称已经确定 40 或 64 的精确边界、所有 off-by-one 语义或所有运行环境行为。

JG-019 至 JG-024 在序列化前检查原生对象层次、叶值或精确字段名。中文和带标点／空格／换行的字段名仅为合成数据，没有读取或生成真实人物资料。

## 5. 历史采集问题与编码证据

| 记录 | 实际观察 | 不能据此宣称 |
| --- | --- | --- |
| 首次 File 运行采集 | 外侧等待 15000 ms 返回 false，终止自己创建的测试进程后抛出 ENTRY_TIMEOUT；child 正文未保留 | 不能登记完成场景数、检查数、child 输出量或首轮通过 |
| 内存插桩诊断启动失败 | 完整脚本 EncodedCommand 超过 Windows 命令长度；启动前失败 | 不是解析函数执行失败 |
| 内存插桩诊断 | 改用短引导和 stdin 传固定测试文本；退出码 0，外侧 1669 ms，72 条标记覆盖 24 项 | 不是未修改入口的实际 File 运行 |
| 未修改 File 入口复跑采集 | 严格 UTF-8 字符读取任务报告 DecoderFallbackException，采集器未发出完整归档 | 不推断未发出的该次计时、停止状态或场景数 |
| 未修改入口原始字节诊断 | 退出码 0，stderr 0，外侧 2008 ms；28662 个 stdout bytes；严格 UTF-8 失败，严格 Code Page 936 可无损往返且中文输入匹配 | 不是已经满足 UTF-8 输出合同 |
| 最终修正的新测试入口 | 明确 UTF-8 输出后，原始字节可严格解码，24 项／137 检查齐全 | 不追溯修复或删除前述失败 |

未修正入口的原始 stdout SHA-256 为 E0CB8977CF920D9B10C6D5F54AE091D5ED0F541473FD230CAEA7E1547300DD6B，原字节 gzip 为 3783 bytes，已完整留存在原始字节诊断中。

这些观察确认了新增入口 File 路径的输出编码与严格 UTF-8 接收约定不符，解释了接收管线的失败机制。首轮未保留 child 字节，不能独立证明该次唯一根因。并非固定受测函数的逻辑修订。

原始字节诊断外侧曾有两个 CopyToAsync 完成返回值出现在其诊断 JSON 前，已单独保留为 OuterCollectorPrefix，不混入 child stdout。一次后置只读复核的辅助启动也因命令长度失败，改为直接以固定运行文件作为 shell 后完成；不把该辅助启动说成额外的受测场景。

## 6. 最终观察身份与接收复核

| 项目 | 实际值 |
| --- | --- |
| 原始 stdout bytes | 28672 |
| 原始 stdout SHA-256 | 14E88EAC0A74783E04CE7F922FA817CD7A19EFDCC4B4E627F4AE2E3DA2DD5CDF |
| 原始 stdout gzip bytes | 3790 |
| LF 规范化完整记录 UTF-8 bytes | 27650 |
| LF 规范化完整记录 SHA-256 | E7EE623FA1E10A4A88F4942418ADDE41B1BBD695AD33B85DD6DBB61D36A7041F |
| 规范化记录 gzip bytes | 3785 |
| 最终入口退出码／stderr bytes | 0 / 0 |
| 外侧等待预算／实际观察 ms | 15000 / 1363 |
| 严格 UTF-8 解码失败类型 | null |

完整归档同时留存原始 stdout 字节与 LF 规范化结构化记录，不只有摘要。原始字节经严格 UTF-8 解码，再将 CRLF 换为 LF并补一个最终 LF，精确得到规范化记录；接收侧已另行验证这一关系。

| 检查组 | 数量 |
| --- | --- |
| 固定身份、函数提取绑定、定义限定静态解析 | 7 |
| 24×5 项分层判定、异常边界与结果隔离 | 120 |
| 6 项正向原生值 | 6 |
| 后置场景数、分层计数、宿主未变、检查数 | 4 |
| 合计 | 137 |

接收复核由主协调员另行执行，不称为独立审查员或第三方模型审查：

- 核对原始与规范化两份 gzip 长度、解压长度和 SHA-256；拒绝重复 JSON 键。
- 比较 Summary 与完整记录，逐项检查 24 个有序场景 ID、137 个唯一检查 ID、两层独立预期、异常隔离及输入长度／SHA。
- 复核首轮快照到最终入口恰为两个输出赋值的插入，原受测函数未修改。
- 复核诊断 72 条进度标记；重新严格解码旧原始字节，核对 Code Page 936 往返及中文合成输入。
- 运行前、运行后 28 份既有文件的长度和 SHA-256 均匹配。28 份集合由原计划三个固定结果文档及其身份表绑定，不表示这些文件全部获得同一种接受。
- 对新增文本、解压记录及诊断文本检查严格 UTF-8、最终 LF、尾随空白及常见秘密特征。模式未命中不等于一般秘密泄露证明；备份范围仅为本项目合成测试与说明。

## 7. 保留限制

本批不复跑原 189 项、上一批 24 项或既有 child 故障批次。8 个分层拒绝是预置输入限制观察，不是正式 Security/Privacy Finding，不作总体安全、隐私、法律或业务合格结论。

不覆盖通用 Schema、来源可信根、授权事实、历史记录真实性、Unicode 规范化、超 Int64 策略、全部深度／资源边界、真实 Driver 正向 SHA、清理失败、外侧强停止或完整组合监督器。

没有修改任何已接受文件，没有准入来源、实际捕获、业务集成或部署；没有访问独立 ACOS 或其他项目。所有历史失败和 LIMITED 保留。

本批新增入口及观察尚不因测试通过而自动获得治理接受。阶段性 Git 备份只保存新资产，不关闭 DSP-004、B-01、B-02，不接受正式 WP-008 结果，不触发任何下游阶段。
