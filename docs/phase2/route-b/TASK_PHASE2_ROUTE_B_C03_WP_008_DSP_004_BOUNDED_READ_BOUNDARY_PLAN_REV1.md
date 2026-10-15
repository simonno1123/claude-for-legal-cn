# DSP-004 受限字节读取局部验证计划 REV1

## 1. 授权及范围

依据 Project Owner 对后续仅本地合成批次的授权及本轮“继续”，只新增测试用内存流、测试入口、本计划、观察归档和结果说明；不修改任何已接受文件或既有结果、失败记录。

将固定已有监督器源码在新的固定 PowerShell 进程中编译到内存，反射调用其私有 ReadBounded(Stream, int)。不调用 RunStage 或公开组合批次，不启动 child 阶段，不读真实 Driver、案件、管道、套接字或业务来源。新内存流属于测试支架，不是业务组件或已接受接口扩展。

全部 LIMITED 保留；DSP-004 为 OPEN / HOLD，B-01、B-02 为 OPEN。不得把局部测试解释为正式 WP-008、来源准入、实际捕获、集成、部署或独立 ACOS 项目操作。

## 2. 固定身份

| 角色／文件 | SHA-256 | bytes |
| --- | --- | --- |
| 已有限接受受测源码 validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV2.cs | 9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E | 24173 |
| 本批测试内存流 validation/route_b_c03/wp_008/DSP_004_BOUNDED_READ_SYNTHETIC_FIXTURE_REV1.cs | 00EC5B2D1A6998E1E59319EBDD64C30481AF5B38A142155D9D407B19A55893B0 | 3209 |
| 本批测试入口 validation/route_b_c03/wp_008/DSP_004_BOUNDED_READ_BOUNDARY_VALIDATION_REV1.ps1 | 0EBDD2137D7260C3428B0A198D28C4C91134DCDF1A3B6A30B9D71EA200ED4AF6 | 16918 |

固定已有运行文件为 C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe，SHA-256 为 362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139。不安装、更新运行环境或依赖。

新增测试入口从开始就明确设置严格 UTF-8 输出。外侧以原始字节完整接收后再严格解码，保留原始 stdout 与 LF 规范化记录的两份 gzip 及身份。外侧等待预算为 30000 ms，仅用于本批有限测试，不改变受测监督器的 120000 ms 约束，也不构成硬停止保证。

## 3. 合成输入与独立预期

输入字节固定为第 i 位等于 i % 251，长度只取表列值。预期在编译和私有方法调用前以字面量冻结；不由实际返回值生成。

测试流仅支持内存异步读取，可按固定调用序号返回预先建立的 IOException、取消任务或提前零字节。异常不包含真实内容；不伪造来源授权或业务证据。正向与超额场景均为方法任务正常完成，Overflow 标志必须另行记录，不把任务完成说成内容可用。

| ID | 场景 | budget / 输入长度 / 最大分段 | 预期任务状态 | 预期 Count / Overflow / Eof | 流返回字节 / Read 调用次数 |
| --- | --- | --- | --- | --- | --- |
| BR-001 | Zero budget empty | 0 / 0 / 4096 | RanToCompletion | 0 / false / true | 0 / 1 |
| BR-002 | Zero budget detection byte | 0 / 1 / 4096 | RanToCompletion | 1 / true / false | 1 / 1 |
| BR-003 | One-byte budget empty | 1 / 0 / 4096 | RanToCompletion | 0 / false / true | 0 / 1 |
| BR-004 | One-byte budget exact | 1 / 1 / 4096 | RanToCompletion | 1 / false / true | 1 / 2 |
| BR-005 | One-byte budget exceeded | 1 / 2 / 4096 | RanToCompletion | 2 / true / false | 2 / 1 |
| BR-006 | Small budget below | 4 / 3 / 4096 | RanToCompletion | 3 / false / true | 3 / 2 |
| BR-007 | Small budget exact | 4 / 4 / 4096 | RanToCompletion | 4 / false / true | 4 / 2 |
| BR-008 | Small budget exceeded | 4 / 5 / 4096 | RanToCompletion | 5 / true / false | 5 / 1 |
| BR-009 | Chunk boundary below | 4096 / 4095 / 4096 | RanToCompletion | 4095 / false / true | 4095 / 2 |
| BR-010 | Chunk boundary exact | 4096 / 4096 / 4096 | RanToCompletion | 4096 / false / true | 4096 / 2 |
| BR-011 | Chunk boundary exceeded | 4096 / 4097 / 4096 | RanToCompletion | 4097 / true / false | 4097 / 2 |
| BR-012 | Fixed stdout budget below | 262144 / 262143 / 4096 | RanToCompletion | 262143 / false / true | 262143 / 65 |
| BR-013 | Fixed stdout budget exact | 262144 / 262144 / 4096 | RanToCompletion | 262144 / false / true | 262144 / 65 |
| BR-014 | Fixed stdout detection byte | 262144 / 262145 / 4096 | RanToCompletion | 262145 / true / false | 262145 / 65 |
| BR-015 | One-byte fragmented overflow | 4 / 9 / 1 | RanToCompletion | 5 / true / false | 5 / 5 |
| BR-016 | Three-byte fragmented exact | 8 / 8 / 3 | RanToCompletion | 8 / false / true | 8 / 4 |
| BR-017 | I/O fault before any bytes | 8 / 8 / 3 | Faulted | NO RESULT | 0 / 1 |
| BR-018 | I/O fault after prefix | 8 / 8 / 3 | Faulted | NO RESULT | 3 / 2 |
| BR-019 | Canceled first read | 8 / 8 / 3 | Canceled | NO RESULT | 0 / 1 |
| BR-020 | Early EOF after prefix | 8 / 8 / 3 | RanToCompletion | 3 / false / true | 3 / 2 |

目标统计为：17 项正常任务结果，其中 6 项超额、11 项 EOF；2 项 Faulted；1 项 Canceled。受限读取不得释放两个 I/O 失败或取消场景的 BoundedRead 结果。

场景限定：

- BR-015 实际输入有 9 bytes，但预算 4 加 1 个检测字节后停止读取，预期只消耗 5 bytes，不再追求排空整个输入。
- BR-017 与 BR-018 仅在本测试进程内核对原始 IOException 对象的 ReferenceEquals；不把它扩展为跨进程异常对象保留或原失败／清理失败并存保证。
- BR-019 是固定合成取消任务，不是外部取消竞态或真实 I/O 取消。
- BR-020 在合成来源还有未读字节时返回 EOF。ReadBounded 不知道预期来源长度，因此预期只返回 3 bytes 并标记 Eof；这不是完整来源证明。
- 受测方法不拥有传入流；每项另由测试入口 Dispose 自己创建的流。不注入 Dispose、Kill 或资源清理失败。

## 4. 检查计数

计划 187 个唯一检查：

| 检查组 | 数量 |
| --- | --- |
| 受测源码、测试支架、运行文件固定身份；方法与类型形状 | 5 |
| 20×7 项完成／任务状态／结果隔离／流计数／所有权／测试清理／输入未变 | 140 |
| 17×2 项正常结果字段与逐字节正文比较 | 34 |
| 2 项原始 IOException 原生引用身份 | 2 |
| 1 项取消任务与异常类型 | 1 |
| 后置场景／终态计数、受测源码／支架未变、检查计数 | 5 |
| 合计 | 187 |

预期正文只从独立输入前缀及字面量预期长度建立；超额正文预期为原生空 byte[]。最终逐字节比较同时记录长度与 SHA-256，不公开原始合成大字节块。

## 5. 保护集合与留存

38 份既有文件在运行前后检查长度及完整 SHA-256。先核对以下锚点文档身份，再读取限定路径内的身份表，禁止重复路径或越界。四表共 34 个文件，另加 4 个锚点文档。

| 锚点结果文档 | SHA-256 | bytes | 表格文件数 |
| --- | --- | --- | --- |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_LOCAL_COMPOSITION_REV2_RESULT.md | C44D9C96C4F6E2D74CE9EC0F0019BEC07F1D541F0E916EC184ECEB0BED8DEE8A | 12221 | 19 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REV2_STAGE_TRANSPORT_FAULT_REV1_RESULT.md | 33A920C3D3F8550F4B4CA3B2F1AC1CC0D9476F704A18E143B2D7BA51DE3BC53C | 10158 | 3 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_CLOSED_RECORD_JSON_REV1_RESULT.md | 8522AC8662C0617EB92CE1A3F65D7A9255AEFB998E4ED8DEB842B88B6911E203 | 8849 | 3 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_JSON_GATE_CONVERSION_BOUNDARY_REV1_RESULT.md | D175EF4828094A5ED4C729987EEC92C642EE711FAE58C2CE98F5F14AFF2E19CC | 12980 | 9 |

38 份包括已接受源码、历史失败、测试入口及说明；不表示它们均获得同一种治理接受。新批次不改写历史 PENDING 或失败。

接收侧复核原始／规范化记录的 gzip、长度与散列关系，拒绝重复 JSON 键，比较完整记录与 Summary，逐项核对 20 个场景 ID、187 个检查 ID、预置输入／预期及正文身份。该复核由主协调员执行，不冒充独立代理或 Gemini。

如意外失败，先保留首次入口、支架与失败观察，不修改已接受源码或事后调整预期以宣称通过。备份前核对仅本项目新资产、公开适宜性、常见秘密特征、格式、固定 SHA 及远端 main，普通提交／推送，不覆盖历史。备份不等于治理接受。

## 6. 保留限制

不验证真实异步调度、阻塞流、管道压力、读取超时、取消竞态、实际子进程、原始业务输出、完整依赖闭包或外侧强停止。所有测试流读任务预期立即完成。

不复跑原 189 项、完整组合批次或先前解析测试，不推导总体安全／隐私／法律结论。不准入来源、不实际捕获、不集成、不部署，不关闭 DSP-004、B-01、B-02 或任何 LIMITED。真实来源与正式阶段仍须另外明确授权。
