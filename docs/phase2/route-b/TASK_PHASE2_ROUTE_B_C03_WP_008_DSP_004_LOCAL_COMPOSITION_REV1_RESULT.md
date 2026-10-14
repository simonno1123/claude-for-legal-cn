# DSP-004 本地合成贯通验证 REV1 — 实际结果与保留边界

## 1. 本轮授权与结论

Project Owner 对 writing block 59382 明确回复“确认”，授权仅本地合成贯通验证：新增测试载体组合已有限接受候选、静态核对、隔离装载、合成运行、结果复核及阶段备份。不修改已接受文件，不读取真实 Driver 或案件材料，不准入来源、不实际业务捕获、不业务集成或部署，不涉及独立 ACOS 或其他项目。

修正后的新批次退出码 0：LOCAL_SYNTHETIC_COMPOSITION_CHECKS_PASS。三个新 child 正常退出，本次重新观察并按 ID 去重的清单项为 **189**；父侧检查为 **1999 / 1999**，失败 0。计数包含清单、子记录、传输和历史依赖核对，不是 1999 个独立新场景。本结果不接受新监督器，不形成正式 WP-008 验证、总体结论或缺口关闭。

已有限接受 D-007 源码保持 SHA-256 `666BF56D68FAC64F67E25B55DA26173593E30E8FEC9D4AC89B5DC489B1E4AFD3` 不变。新监督器与新核对入口仍未由 Project Owner 接受。

## 2. 新资产完整身份

路径相对本项目根目录；结果文档不自绑定自身散列。

| 新资产 | SHA-256 | UTF-8 bytes |
| --- | --- | --- |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_LOCAL_COMPOSITION_PLAN_REV1.md | A435F47C839C6B5EE5B5FA5A2239E42A40393527449C6A42972E2D230CD19AC1 | 6833 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV1.cs | 03D037FFAA2F87EA0AE8855A760CA422EF5FA6B827B5452070D52444387500FA | 22783 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_VALIDATION_REV1.ps1 | D804B2EB32FA9ECD7C31305D01615C6251E87BD0CDB47B2593A7C9D04734511F | 14877 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_REV1_OBSERVED_RESULT.json | 2D29C48EA41C4FD200BA1A1D51688A61532855C6968D65AAB81CDED73F10BBFA | 41015 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_ATTEMPT1_SUPERVISOR_SNAPSHOT.txt | 9B5968CE9C8CB6AF066659B588E5B0E16D80811319F42DCB58A30158922DAEA2 | 22783 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_ATTEMPT1_ENTRY_SNAPSHOT.txt | ADB35B39AD227C7FBA8AC7365B0C40C886A20EC1F63A3C64005F9CFB33953819 | 14877 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_ATTEMPT1_FAILURE.json | AEAA9463019755A9EA281559893077802379CE3971F5833A2F762B4D23328AB3 | 8759 |

## 3. 失败历史与修正范围

先进行仅编译检查，未调用入口或创建 child；新监督器编译通过。另有一次结果收集命令的语法错误发生在任何入口调用之前，未执行测试。

第一次实际批次执行退出码 1，父侧检查 196 个，其中 1 个失败；没有形成可消费的新清单项。已实际启动两个 child：RW 正常退出且传输通过；PURE 退出码 1，传输拒绝；D007 未启动。父侧在三阶段完整性检查处停止，未进行重复调用。该次失败记录及当时监督器/核对入口完整源码快照均保留，不冒称零失败历史。

根因位于**新监督器**的快照装载：使用调用运算符执行内存 ScriptBlock，建立了额外局部作用域，而 PURE 固定入口在函数内使用 script: 变量。本次只将新 bootstrap 的执行运算符改为 child 根作用域点源，并更新尚未接受的新核对入口对新监督器的 SHA 绑定；固定入口源码、输入、预期及已接受文件没有改变。点源不发生于父进程或用户已有会话，不将代码注入其环境。

随后在全新本地进程中编译修正后的固定新监督器并执行第二次实际批次。两次执行使用不同源码 SHA 和新的程序集，各自的本地单次门没有被重置；本轮允许的修正与再验证不转移为任何外部单次授权重用。累计实际启动五个固定合成 child；前次 D007 未启动，后次 D007 helper 实际调用一次。

## 4. 修正后实际观察

| 阶段 | 本次新清单项 | child 内记录检查数 | child 退出码 | 阶段耗时 ms | stdout / stderr bytes | 实际记录结果 |
| --- | --- | --- | --- | --- | --- | --- |
| RW | 96 | 390 | 0 | 1196 | 115526 / 0 | LOCAL_REPORTED_RW_CLASSIFICATION_CHECKS_PASS |
| PURE | 92 | 373 | 0 | 1500 | 82913 / 0 | LOCAL_REMAINING_PURE_CHECKS_PASS |
| D007 | 1 | 815 | 0 | 2277 | 83221 / 0 | LOCAL_D007_PRIVATE_FIXED_HELPER_CHECKS_PASS |

新监督器方法内记录的全批次耗时为 4984 ms。八项依赖快照运行前 8/8 MATCH，运行后 8/8 MATCH，读取尝试共 16 次。固定已有 pwsh 文件 SHA 为 `362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139`，只读取并核对一次；该身份观察不证明文件路径在执行期间不可替换、可信根或完整依赖闭包。

每个 child 使用无 profile、非交互、隐藏启动、新临时工作目录及清空后补七项的环境；stdin 传入已核验的完整入口快照。child 先核验精确长度、EOF、完整 SHA 和严格 UTF-8，再发出绑定阶段 ID/SHA 的固定 ACK，并执行同份快照。没有在 hash 后用 -File 重新打开该入口。内部固定依赖仍由各入口按原约束另行读取核验，不声称父子共享同一数组对象或三个 child 共用同一 runspace。

三个 child 的双流 EOF、读取任务结束、输入关闭、输出/错误流关闭及 Process.Dispose 返回均被记录；没有 stop/kill 请求，没有首要或次级失败。这里只证明这些本地调用和任务观察，不等于完整引擎、后代或资源收敛。新 stdout 记录传输预算 262144 bytes，未改写固定控制端原 65536-byte 合同。

父侧只在正常退出、完整 ACK、预算内、EOF/任务及本地清理条件成立后消费 JSON；拒绝重复 JSON 键、记录格式错误、失败检查、额外或缺少的 ID。子入口先完成原生比较再序列化；父侧解析 JSON 不重建原生 Int32/Int64、callee 引用或冻结证据。

本次的新 RW Cases 96 项、新 PURE Cases 92 项与新 D007 观察 1 项，集合精确覆盖固定 189 项清单。D007 固定入口内部的历史 188 项 ID 审计依赖仍保留，但父侧没有使用该入口的历史合并字段来回填本次覆盖。三阶段记录检查数合计 1578，其中含元数据和历史记录核对，不是 1578 个新场景。

同一新监督器程序集第二次请求实际返回 REPEATED_COMPOSITION_BATCH_REFUSED，依赖读取 0、child 数 0、运行文件读取 0，无新观测时长。这是当前程序集的本地重复门，不是跨会话授权服务。

## 5. 完整记录存储与复核

成功 envelope 保存摘要和 gzip/base64 编码的完整父侧 JSON。完整数据是实际工具输出解析记录，按 LF 收集后内存压缩，没有删除阶段或检查项；不是未经修改的原始控制台 transcript。解压得到 386892 UTF-8 bytes，完整 SHA-256 为 `D11DDAA65A2446021B93033A7CD02EB53270A560A4919CDBE9D9CF3A4A2A930E`。gzip 大小 28772 bytes；已实际解压复核长度、完整 SHA、189 个 ID 和 1999 个唯一父侧检查 ID。

失败 envelope 同样保存完整父侧记录：解压后 12262 UTF-8 bytes，SHA-256 `D4774C5E067D3A99A9D84EBD8DBE960BAF4AF500FCB9E9A3551890240B320983`。它包括实际部分传输元数据、196 个检查和 1 个失败；失败正文未被公开或补写为成功观察。

所有原入口返回的 CandidateAcceptance、NOT AUTHORIZED、INTEGRATION 等固定字面量均原样保留为该入口自己的记录内容，不据此判定本批次当前授权或 Project Owner 决定；D007 源码的后续有限接受不追溯改写其原核对入口。本结果没有生成 Project Owner 签名、取得时间或治理时间链。

本次由主协调员进行源码、固定预期、传输、解压记录和实际结果交叉核对；没有独立子审查员或 Gemini 调用，不称为独立双审。公开资料只含封闭合成输入、限定语、类型、数量和散列，不含真实事项、原失败流、异常 Message/堆栈或原字节数组。临时目录保留；未递归删除。

## 6. 明确保留的缺口

- 新结果证明三个封闭测试入口在新载体内顺序贯通，不证明单一共享域、单一全程冻结输入或正式 C03 场景贯通。
- 120000/5000/5000 ms 是新测试监督参数；正常短时运行不验证实际 120 秒超时、恶意后代、同步调用硬时限、资源耗尽或真实清理失败路径。编译发生在监督器计时入口之外。
- 准备摘要仍共享 .NET 密码学栈；不证明 provider 独立性、可信依赖根、正向真实 Driver SHA 或真实来源身份。
- 原生比较和保护性拒绝不证明零实际业务 I/O、真实上下文隔离或权限准入；没有接入真实材料或外部服务。
- 本次不执行旧 WP-008 计划的正式场景、不将旧 SHA 证据转用于新源码、不接受新监督器、不关闭 DSP-004、B-01 或 B-02。

全部 LIMITED 保留；DSP-004 OPEN / HOLD，B-01/B-02 OPEN。源码或结果的进一步接受、来源准入、正式验证、实际捕获、业务集成及部署均须适用的独立决定。只允许按既有阶段备份授权普通提交并推送本项目八个新增文件；备份不是治理接受。
