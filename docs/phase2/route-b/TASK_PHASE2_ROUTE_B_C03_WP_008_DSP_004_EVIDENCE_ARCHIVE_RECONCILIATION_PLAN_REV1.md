# DSP-004 现有合成证据归档核对计划 REV1

## 1. 本批目的与范围

依据 Project Owner 已授权的本项目后续本地合成批次及本轮“继续”，本批不再增加或重跑受测场景，而是对六组既有固定归档进行只读核对，并整理覆盖与未覆盖边界。

只新增本核对入口、本计划、核对观察归档和证据覆盖说明。不改写已接受文件、历史失败、旧计划或状态字面量，不涉及独立 ACOS 或其他项目。执行的是新归档核对器，不是任何受测组件、Python、C# 编译、child 阶段、正式 WP-008 或业务流程。

DSP-004 保持 OPEN / HOLD，B-01、B-02 保持 OPEN，全部 LIMITED 保留。归档哈希匹配和记录自洽不代表来源可信、正式结果接受、来源准入、实际捕获、集成或部署。

## 2. 固定新入口

文件：validation/route_b_c03/wp_008/DSP_004_EVIDENCE_ARCHIVE_RECONCILIATION_REV1.ps1

SHA-256：FCEDC4752FDC490E0E82BC914781FF5B5EA4E5627391C91BE0DF3192035E29A9

UTF-8 bytes：19341

固定已有 PowerShell 运行文件为 C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe，SHA-256 为 362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139。入口明确 UTF-8 输出；外侧按原始字节采集再严格解码，等待预算 60000 ms 只用于本批归档核对，不改变任何受测组件期限。

核对器仅对预先列明的固定文件读取、解压和解析；不执行它们的源码。新核对器的负向保护条件不在本批系统性变异测试，不把正向核对通过写成通用解析／安全认证。

## 3. 六组记录及不混淆的单位

| ID | 归档文件 | 固定物理文件 SHA-256 | 原记录检查数 | 原记录单位数／类别 | 原始输出留存 |
| --- | --- | --- | --- | --- | --- |
| AR-001 | validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_REV2_OBSERVED_RESULT.json | 3DB42CBCAA7C361B78CC1C29719BE6A76009A79DAE4FB0304FF4A93D45D672A4 | 2027 | 189 RECORDED_PLAN_ITEM_IDS | 仅规范化完整记录 |
| AR-002 | validation/route_b_c03/wp_008/DSP_004_REV2_STAGE_TRANSPORT_FAULT_REV1_OBSERVED_RESULT.json | 8F36D01BBCA45333A147C7E6901ECA1755A6528852A6A5C40E6185198686AB54 | 89 | 8 LOCAL_SYNTHETIC_CASES | 仅规范化完整记录 |
| AR-003 | validation/route_b_c03/wp_008/DSP_004_CLOSED_RECORD_JSON_REV1_OBSERVED_RESULT.json | 081F5C2D2A42F2C693555C57875769F996FB4BDD65163EA7213446E9F96FB693 | 94 | 24 LOCAL_SYNTHETIC_CASES | 仅规范化完整记录 |
| AR-004 | validation/route_b_c03/wp_008/DSP_004_JSON_GATE_CONVERSION_BOUNDARY_REV1_OBSERVED_RESULT.json | 5462F44C2E9F463C104FFC83FC83ADDA021DBC9EFA842775A2B8CE22C3CDFB93 | 137 | 24 LOCAL_SYNTHETIC_CASES | 原始测试进程输出另存 |
| AR-005 | validation/route_b_c03/wp_008/DSP_004_BOUNDED_READ_BOUNDARY_REV1_OBSERVED_RESULT.json | 6FDAB9BC2DCD79A8D290D0E417311CD5FCA79E199DA83E42F1AB2A09AE596B52 | 187 | 20 LOCAL_SYNTHETIC_CASES | 原始测试进程输出另存 |
| AR-006 | validation/route_b_c03/wp_008/DSP_004_EXCEPTION_RETENTION_REPRESENTATION_REV1_OBSERVED_RESULT.json | 2E0D13BEED92826DA17957D897499B6E04D3EAB7E31BDAEE9F46AB713BB397A0 | 77 | 13 LOCAL_SYNTHETIC_CASES | 原始测试进程输出另存 |

这些检查数只按原记录分别呈现，不合计为场景总数、完成率、统计独立样本或正式覆盖率。AR-001 的 189 是归档中记录的 plan item ID 数，不等于 189 个新的业务或正式 WP-008 场景。

AR-001 为扁平组合记录，检查位于 ParentChecks；AR-002 为扁平私有阶段记录；AR-003 至 AR-006 为嵌套 Summary 格式。必须逐类处理，缺失预期字段时失败，不用默认零值或其他结构的字段替代。

## 4. 核对规则

每组固定进行十一项核对：

1. 物理归档文件长度与 SHA-256。
2. 外层归档及解压完整 JSON 的属性名唯一性。
3. 完整文本预置长度与 SHA-256，解压输出不得超出预置长度。
4. gzip 字节长度。
5. 原归档记录的退出码为 0；只核对记录值，不声称新执行。
6. 原记录 Outcome 与固定预期字符串一致；不建立新总体业务结论。
7. 完整记录与摘要的类型化投影一致。
8. 原记录检查 ID 唯一、数量及记录值为 true；不是重跑那些断言。
9. 原记录单位 ID 唯一及数量正确。
10. 归档中记载的源码身份与固定预期一致。
11. 原始输出证据的存在／缺失按预期如实分类；存在时核对原始字节与规范化记录的确定关系，缺失时保持缺失。

摘要比较保留 JsonElement 原始 Number token，不通过 JavaScript Number 或 GetDouble 重写 Int64 边界；对象按属性名比较，数组保持顺序。AR-001 的 Stages 必须按显式映射与 ActualStageRecords／Transport／ReceivedParsedRecord 核对，其余摘要字段逐项与完整记录比较。AR-002 的整段 Cases 必须与完整记录匹配，不能只核对总体 PASS 字样。

AR-001 同时核对三个归档 child record 的检查表及 plan item ID 并集；D007 使用 NewPlanItemIds，RW／PURE 使用 Cases.Id。仍只证明这些归档内容相互一致，不能补证源代码中的原生类型、实际来源或未留存的 child 正文字节。

AR-004 至 AR-006 另存的原始 stdout 只属于各自测试进程，不是 AR-001／AR-002 中缺失的 child raw body。AR-001、AR-002、AR-003 不得因规范化 JSON 完整而被标成已有原始字节见证。

## 5. 保护与历史参考

47 份固定既有文件来自以下六个文档的 41 条身份行及六个文档自身；先核对文档完整身份再使用表格，禁止重复路径或越界。

| 锚点结果文档 | SHA-256 | bytes | 身份表文件数 |
| --- | --- | --- | --- |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_LOCAL_COMPOSITION_REV2_RESULT.md | C44D9C96C4F6E2D74CE9EC0F0019BEC07F1D541F0E916EC184ECEB0BED8DEE8A | 12221 | 19 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REV2_STAGE_TRANSPORT_FAULT_REV1_RESULT.md | 33A920C3D3F8550F4B4CA3B2F1AC1CC0D9476F704A18E143B2D7BA51DE3BC53C | 10158 | 3 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_CLOSED_RECORD_JSON_REV1_RESULT.md | 8522AC8662C0617EB92CE1A3F65D7A9255AEFB998E4ED8DEB842B88B6911E203 | 8849 | 3 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_JSON_GATE_CONVERSION_BOUNDARY_REV1_RESULT.md | D175EF4828094A5ED4C729987EEC92C642EE711FAE58C2CE98F5F14AFF2E19CC | 12980 | 9 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_BOUNDED_READ_BOUNDARY_REV1_RESULT.md | 9B47CA2BEC57B30B4BD34EDF25E7E5A8D552048F203516158BCFD4B7EC65E611 | 10338 | 4 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_EXCEPTION_RETENTION_REPRESENTATION_REV1_RESULT.md | AD097F7ED78BACEE6CF401FCDC6162F01289B0C6E7075AD783C73E47B846A19D | 10403 | 3 |

另核对以下两个文档的只读身份，用于说明正式准备与来源绑定要求；它们的形成时状态、候选标签或 NOT AUTHORIZED 字面量不被当成本轮授权／撤销，也不覆盖后来单独发生的接受。

| 历史要求参考 | 当前读取文件 SHA-256 | bytes |
| --- | --- | --- |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_OPERATIONAL_VALIDATION_PLAN.md | E9643D0993532A1E1603B66F95CD288F394BDDA621EFB6784B256CECFC915E6D | 23939 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md | 6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA | 54703 |

B-01 的准备根绑定与 B-02 的唯一字节编码要求只作范围参考；其具体源身份、前置接受和准入尚不能由六组合成断言自动建立。旧正式计划的固定源码表也不能在本批被自动迁移到已受控替换的后续源码。

## 6. 本批核对计数与留存

计划 71 个唯一归档核对检查：3 项前置身份，6×11 项每组核对，2 项后置身份／检查计数。

这些 71 项不是新受测场景，不与 2027、89、94、137、187、77 相加。记录独立的 AuditChecks 字段，防止误称业务测试。

同时留存本次核对进程原始 stdout 和 LF 规范化完整结构化记录及散列。接收侧另行解压、核对身份、摘要、六组 ID 和 71 个核对 ID；复核由主协调员完成，不冒充第三方模型或独立代理。

意外失败先保留本次入口与观察，不改写既有文件或弱化核对规则以获得 PASS。备份仅普通提交／推送四份本批新资产，检查公开适宜性、秘密特征、格式及远端 main；备份不等于治理接受。

## 7. 本批不能填补的缺口

既有断言未被重新执行；JSON 本身不能独立重建原生 Int32／Int64 类型身份。未留存的原始 stdout 或 child body 不能由重排／重序列化 JSON 追溯补造。

不新增真实清理故障、硬停止、完整资源收敛、跨 child 引用冻结、可信根、正式材料或来源准入证据。不接受 WP-008 正式结果、不关闭 DSP-004、B-01、B-02 或任何 LIMITED。
