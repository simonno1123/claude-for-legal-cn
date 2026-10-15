# DSP-004 封闭 JSON 记录解析局部验证计划 REV1

## 1. 授权范围

依据 Project Owner 对仅本地合成后续批次的授权及本轮“继续授权批量任务”“继续”，新增唯一局部测试入口、该计划、观察归档与结果说明。只验证已有解析逻辑，不修改任何已接受文件，也不重写历史失败或 PENDING 记录。

这是本项目 claude-for-legal-cn 的合成单元验证，不涉及独立 ACOS 或其他项目。不得解释为正式 WP-008 执行、来源准入、实际业务捕获、集成、部署、C03 激活或 B-01/B-02 关闭。全部上游 LIMITED 保留；DSP-004 为 OPEN / HOLD，B-01、B-02 为 OPEN。

## 2. 固定受测文本与入口

| 角色 | 路径／标识 | SHA-256 | bytes |
| --- | --- | --- | --- |
| 已有解析函数宿主，只读 | validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_VALIDATION_REV2.ps1 | ADAB2850039C9A15C0A175F0028B751F983FC21EB218835102247F9CD50D5262 | 19481 |
| 新合成测试入口 | validation/route_b_c03/wp_008/DSP_004_CLOSED_RECORD_JSON_VALIDATION_REV1.ps1 | 3072E3C5A452AF740197CDE8C86FAA9061C144F0F6A2F189564DE371B721EBC5 | 12022 |
| 固定已有运行文件 | C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe | 362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139 | 不在本表重复记录 |

只通过语法树取得下列两个唯一函数定义的 Extent.Text，保持原文字节；它们的散列是“严格 UTF-8 编码后的提取文本散列”，不是独立源文件散列，也不含函数外换行。

| 函数 | 宿主行 | 提取文本 SHA-256 | UTF-8 bytes |
| --- | --- | --- | --- |
| Check-JsonKeyUniqueness | 30–40 | E573D366827177B9178C3F87C79E383AE8F9E973C473ED42852E1F2428E382CC | 619 |
| Decode-ClosedJson | 41–48 | 458877E0C9AFD1E7E666A2CF23F8FF1722429C8CC3107F43A633EAE6ED2E8A59 | 439 |

提取后再次静态解析，必须仅含这两条函数定义。只在新的固定 PowerShell 进程内建立该函数作用域；严禁执行原宿主的顶层批次、C# 编译、公开组合批次或私有 child 阶段。本轮没有子进程阶段测试、超时测试或 189 项清单复跑。

## 3. 预置场景与预期

预期在解析调用前以独立字面量冻结，不根据实际结果调整。ACCEPT/REJECT 是合成输入的解码结果，不是治理接受。

| ID | 合成场景 | 预期 |
| --- | --- | --- |
| CJ-001 | 空对象 | ACCEPT；零属性对象 |
| CJ-002 | 布尔及字符串 | ACCEPT；原生布尔与字符串值一致 |
| CJ-003 | 嵌套对象 | ACCEPT；嵌套值一致 |
| CJ-004 | 对象数组 | ACCEPT；数组顺序和值一致 |
| CJ-005 | Unicode 转义 | ACCEPT；解码为中文 |
| CJ-006 | 引号与反斜线转义 | ACCEPT；精确字符串一致 |
| CJ-007 | 整数与小数 | ACCEPT；7 与 1.5 |
| CJ-008 | Int64 最大值 | ACCEPT；原生 System.Int64，9223372036854775807 |
| CJ-009 | Int64 最小值 | ACCEPT；原生 System.Int64，-9223372036854775808 |
| CJ-010 | null 与 false | ACCEPT；保留属性、null 与原生 false |
| CJ-011 | 对象外 CR/LF/tab | ACCEPT；不影响内部原生值 |
| CJ-012 | 看似文件读取代码的字符串 | ACCEPT；精确字符串仅作数据，不求值 |
| CJ-013 | 缺少属性值 | REJECT；不返回对象 |
| CJ-014 | 多根对象 | REJECT；不返回对象 |
| CJ-015 | 数组根 | REJECT；不返回对象 |
| CJ-016 | 字符串根 | REJECT；不返回对象 |
| CJ-017 | 数字根 | REJECT；不返回对象 |
| CJ-018 | null 根 | REJECT；不返回对象 |
| CJ-019 | 根对象重复键 | REJECT；不返回对象 |
| CJ-020 | 嵌套对象重复键 | REJECT；不返回对象 |
| CJ-021 | 数组内对象重复键 | REJECT；不返回对象 |
| CJ-022 | 普通键与等价 Unicode 转义键重复 | REJECT；不返回对象 |
| CJ-023 | 更深层数组内重复键 | REJECT；不返回对象 |
| CJ-024 | 尾随逗号 | REJECT；不返回对象 |

目标为 12 项接受和 12 项保护性拒绝。只断言拒绝时存在异常类型、不返回结果；不强制预设不同运行环境下的完整异常包装链。只记录最内层异常类型，不记录 Message 或 StackTrace。

计划检查总数为 94：7 项固定身份／函数提取／语法检查，24×3 项判定／返回／异常边界检查，12 项正向原生值检查，3 项后置计数与宿主不变检查。94 个检查不是 94 个独立场景。

## 4. 留存与复核方法

1. 运行前后对 24 份既有文件进行长度和 SHA-256 核对。身份集合来自固定 REV2 结果文档中的 19 行及该文档本身，再加上一轮 4 份私有阶段故障验证资产。
2. 原 20 份集合的锚点文档为 docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_LOCAL_COMPOSITION_REV2_RESULT.md，SHA-256 为 C44D9C96C4F6E2D74CE9EC0F0019BEC07F1D541F0E916EC184ECEB0BED8DEE8A。
3. 追加保护的 4 份文件固定如下：

| 文件 | SHA-256 | bytes |
| --- | --- | --- |
| validation/route_b_c03/wp_008/DSP_004_REV2_STAGE_TRANSPORT_FAULT_VALIDATION_REV1.ps1 | AF4BD16ADA55C264711E5045FF05672F2C5DB5DF442524174105417F642825B9 | 13596 |
| validation/route_b_c03/wp_008/DSP_004_REV2_STAGE_TRANSPORT_FAULT_REV1_OBSERVED_RESULT.json | 8F36D01BBCA45333A147C7E6901ECA1755A6528852A6A5C40E6185198686AB54 | 25734 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REV2_STAGE_TRANSPORT_FAULT_PLAN_REV1.md | 5FFF4A7A0579FA0939E6C75D2564CDC364EDC1B348C0EC4D33AA434E74B76762 | 5437 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REV2_STAGE_TRANSPORT_FAULT_REV1_RESULT.md | 33A920C3D3F8550F4B4CA3B2F1AC1CC0D9476F704A18E143B2D7BA51DE3BC53C | 10158 |

4. 实际 stdout 按 LF 收集、补最终 LF，在内存中 gzip/base64 归档。它是换行规范化后的实际结构化观察，不称原始物理终端 transcript。
5. 接收侧另行解压、重算长度与散列、拒绝重复 JSON 键、比较 Summary 与完整记录、核对场景／检查 ID 集合及独立预期。64 位边界在原生 PowerShell 内比较，归档诊断以十进制字符串及类型名保存，避免 JavaScript 数字舍入。
6. 若意外失败，先保留该次入口、失败观察及精确身份，再区分入口问题与受测问题；不得改写已接受宿主或静默修改预期来获得 PASS。
7. 新增内容仅含合成文本；备份前检查公开适宜性、常见秘密特征、格式、固定身份、文件归属及远端 main 是否变化。仅普通提交／推送本轮新增资产，备份不等于治理接受。

## 5. 保留限制

- 不覆盖 JSON 深度上限、大小上限、Unicode 规范化、大小写冲突、超 Int64 值、所有数字策略或通用反序列化安全性；只报告本表列明的输入。
- 不验证记录业务 Schema、可信根、权限、来源 provenance、原始 child 字节、历史报告真实性或外侧停止能力。
- 本轮与原 189 项、上一轮 8 项私有传输故障的计数分离，不叠加为正式覆盖率。
- 无真实材料、模型／供应商调用、网络数据输入、来源准入、实际捕获、集成或部署。
- 该计划及测试通过不自动接受新增源码、不关闭任何 LIMITED，不改变已接受文件或历史记录。
