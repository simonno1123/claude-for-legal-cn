# DSP-004 本地合成贯通监督器 REV2 — 期限门有限修订与实际验证记录

## 1. 授权、基线与效力

Project Owner 在本对话明确授权：“授权新增 REV2 修订与仅本地合成验证批次，不修改任何已接受文件。”

本批次只处理 REV1 独立只读复核识别的 P2：最后一次运行后依赖读取及散列后没有最终期限门，核对入口也没有总批次记录耗时上界断言。其静态可能性没有被实际复现，不追溯否定 REV1 4984 ms 正常合成记录或固定源码的会话层有限接受。

REV1 固定源码 SHA-256 为 `03D037FFAA2F87EA0AE8855A760CA422EF5FA6B827B5452070D52444387500FA`。新增 REV2 不覆盖或改写 REV1、已接受控制端、D-007 候选、固定输入清单、三个固定核对入口及原有记录。

允许新增候选、核对入口和结果记录，进行静态核对、编译与仅本地合成执行。本记录不接受 REV2，不构成正式 WP-008 验证、来源准入、实际业务捕获、业务集成、部署或缺口关闭。不访问独立 ACOS 或其他项目；未调用 Gemini、外部模型、连接器或网络服务。

## 2. 新资产身份

路径相对本项目根目录。本结果文档不在正文中自绑定自身 SHA。

| 新资产 | SHA-256 | UTF-8 bytes |
| --- | --- | --- |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV2.cs | 9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E | 24173 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_VALIDATION_REV2.ps1 | ADAB2850039C9A15C0A175F0028B751F983FC21EB218835102247F9CD50D5262 | 19481 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_REV2_OBSERVED_RESULT.json | 3DB42CBCAA7C361B78CC1C29719BE6A76009A79DAE4FB0304FF4A93D45D672A4 | 45615 |

## 3. 修订内容与终点语义

- 新类名为 Dsp004LocalCompositionSupervisorCandidateRev2，仍只有一个公开无参数静态批次入口、没有公开构造器、路径参数、脚本参数、回调、时钟替换或公共测试模式。
- 八项 SourceSpec 固定文件、长度和 SHA 与 REV1 相同，顺序和三个阶段入口不变。
- 每次运行后依赖读取、散列与比较之后，再调用期限检查；最后一次读取跨过期限不会再直接转为批次成功。
- 最终阶段名为 FINAL_BATCH_COMPLETION_DEADLINE。私有 CompleteBatchAtRecordedDeadline 先清除成功标志、记录唯一终点样本，拒绝负值及大于等于 120000 ms 的值，只有检查通过后才设置成功标志。
- 成功判定与 ElapsedMilliseconds 使用同一终点样本，不在成功后重新采样并覆盖该值。失败或未完成分支的耗时仅用于诊断；重复请求仍记录 -1。
- 新核对入口同时检查正常批次记录耗时非负且小于 120000 ms。原有逐阶段完成时刻断言保留。

该有限修订只建立“成功标志对应的记录终点已检查”的语义。线程调度和返回动作仍可能发生在样本之后；它不是物理返回时限、同步调用可中断性、硬停止或完整资源收敛证明。

## 4. 静态核对与实际正常合成

先在单独工具进程中完成 PowerShell 解析、C# 编译、公开接口和八项固定依赖表核对；均通过。此步没有调用候选入口或启动受测 child。随后在新的已有固定 PowerShell 进程中编译 REV2，并运行新增核对入口；它先执行私有标量边界检查，再调用封闭三个阶段及同程序集重复拒绝门。

固定运行文件在执行前读取并匹配 SHA-256 `362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139`。这一文件身份绑定不是可信依赖根、完整依赖闭包或运行期间路径不可替换证明。

实际新增入口退出码 0，结果为 LOCAL_SYNTHETIC_COMPOSITION_CHECKS_PASS。本轮没有发生新的编译或验证失败。REV1 首轮失败源码快照和记录保持原样，不以本轮成功覆盖它们。

| 新运行阶段 | 本次新清单项 | child 检查数 | child 退出码 | 阶段记录耗时 ms | stdout / stderr bytes |
| --- | --- | --- | --- | --- | --- |
| RW | 96 | 390 | 0 | 2501 | 115526 / 0 |
| PURE | 92 | 373 | 0 | 2635 | 82913 / 0 |
| D007 | 1 | 815 | 0 | 3595 | 83221 / 0 |

本批次被检查的终点样本为 **8747 ms**。八项运行前依赖快照及八项运行后身份核对均匹配，读取尝试为 16。三个阶段的退出、EOF、读取任务结束及本地关闭/Dispose 返回标志成立；没有 stop/kill 请求或异常清理注入。

同一 REV2 程序集第二次公开请求实际拒绝，未再次读取依赖或运行文件，未启动 child。私有边界检查不调用公开入口，不重置该单次门，不创建 child、runspace 或输入载荷。

本次 RW Cases 96、PURE Cases 92 和 D007 新观察 1 项，与固定清单精确对应 **189 个唯一 ID**。没有使用 D007 的历史 CombinedLocalPurePlanItems 字段回填新覆盖。三个 child 的 1578 个检查含元数据与历史 ID 核对，并不是 1578 个新场景。

## 5. 六个独立预期的私有期限门合成检查

核对入口在当前编译的 REV2 程序集中，直接通过反射调用同一私有终点方法。预期数值、异常类型、允许标志和结果字面量预先独立写在新增核对入口；不从该方法返回值反推预期。分别核对实际异常类型、原生 Int64 记录样本、原生 Boolean 允许标志及 Outcome 字符串。

| ID | 合成终点 ms | 独立预期 | 实际允许标志 | 实际异常类型 | 比较结果 |
| --- | --- | --- | --- | --- | --- |
| TD-001 | 0 | 允许成功 | true | NONE | PASS |
| TD-002 | 119999 | 允许成功 | true | NONE | PASS |
| TD-003 | 120000 | 拒绝 | false | System.TimeoutException | PASS |
| TD-004 | 120001 | 拒绝 | false | System.TimeoutException | PASS |
| TD-005 | 9223372036854775807 | 拒绝 | false | System.TimeoutException | PASS |
| TD-006 | -1 | 拒绝无效时长 | false | System.InvalidOperationException | PASS |

六项各有四个原生/字面量断言，全部成立；四次预期拒绝不是测试失败。它们只测试私有标量门，没有真实等待 120 秒、减小正常批次预算、注入时钟、制造末尾文件读取停滞或复现完整超时/清理路径。不将这六项计入固定 189 项清单。

## 6. 父侧检查、完整归档与接收核对

父侧检查实际为 **2027 / 2027**，唯一 ID 2027、失败检查 0。相比 REV1 的 1999 项，新增 28 项：私有方法/字段形状 2 项、六个边界的四类断言 24 项、边界数量 1 项、正常批次终点耗时 1 项。它们是检查项，不是 2027 个独立新场景。

成功 envelope 以 gzip/base64 保存本次完整父侧 JSON，包含所有阶段解析记录、189 项 ID、2027 项检查及六个边界记录。工具实际输出按 LF 拼接并补一个末尾 LF后压缩，不称为未经修改的原始控制台 transcript。

- 完整解压记录：391606 UTF-8 bytes。
- 完整记录 SHA-256：`CB06EC4381F57F19B5C043B60935104D9C4AB0A6AA99FD395321750A387D09F5`。
- gzip：29352 bytes。
- 物理 envelope：45615 bytes，身份见第 2 节。

归档格式化仅更改 JSON 字符串之外的空白；没有对数值进行浮点重写。实际解压重新核对了 TD-005 的原生 Int64 最大值 `9223372036854775807`，完整长度和 SHA、Summary 与完整记录逐字段一致性均通过。envelope 和完整记录均没有重复 JSON 键。

主协调员接收核对还重构了 189 项集合和 2027 项父检查命名空间：旧父检查 ID 仅用于核对不变的命名空间，28 项新 ID 从新增规则构造；没有用历史结果补写本次布尔值。新三个 child 检查 ID 与固定入口命名空间一致，实际检查值均为原生布尔 true。

原始 child 正文在解析前由核对入口核对散列，但归档仅保存解析后的 JSON 与传输散列，未另行保留原始正文排版字节。本轮接收核对不冒称可从解析记录独立重算原始 child 正文 SHA，完整归档散列也不等于运行来源或 OS 隔离证明。

本轮为主协调员内部实现与结果复核，不是新的独立子审查或 Cross-Vendor 双审；没有据此签发总体安全、隐私、法律合规或正式验证结论。

## 7. 原文件保真与失败历史

执行前后对以下 16 份既有文件重新读取并核对散列与长度，全部保持不变：

| 既有文件 | SHA-256 | bytes |
| --- | --- | --- |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV1.cs | 03D037FFAA2F87EA0AE8855A760CA422EF5FA6B827B5452070D52444387500FA | 22783 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_VALIDATION_REV1.ps1 | D804B2EB32FA9ECD7C31305D01615C6251E87BD0CDB47B2593A7C9D04734511F | 14877 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_REV1_OBSERVED_RESULT.json | 2D29C48EA41C4FD200BA1A1D51688A61532855C6968D65AAB81CDED73F10BBFA | 41015 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_LOCAL_COMPOSITION_REV1_RESULT.md | B7EA00F012AC95B01ED4F0CB00C58B373944E702592366B65DF08DFA31649AD5 | 9215 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_LOCAL_COMPOSITION_PLAN_REV1.md | A435F47C839C6B5EE5B5FA5A2239E42A40393527449C6A42972E2D230CD19AC1 | 6833 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_ATTEMPT1_SUPERVISOR_SNAPSHOT.txt | 9B5968CE9C8CB6AF066659B588E5B0E16D80811319F42DCB58A30158922DAEA2 | 22783 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_ATTEMPT1_ENTRY_SNAPSHOT.txt | ADB35B39AD227C7FBA8AC7365B0C40C886A20EC1F63A3C64005F9CFB33953819 | 14877 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_ATTEMPT1_FAILURE.json | AEAA9463019755A9EA281559893077802379CE3971F5833A2F762B4D23328AB3 | 8759 |
| validation/route_b_c03/wp_008/DSP_004_LOCAL_VALIDATION_CARRIER_CANDIDATE_REV1.ps1 | 46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C | 70284 |
| validation/route_b_c03/wp_008/DSP_004_OUTER_CONTROLLER_CANDIDATE_REV1.ps1 | 891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB | 25573 |
| validation/route_b_c03/wp_008/DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_HANDOFF_CANDIDATE_REV1.cs | 666BF56D68FAC64F67E25B55DA26173593E30E8FEC9D4AC89B5DC489B1E4AFD3 | 19442 |
| validation/route_b_c03/wp_008/DSP_004_REPORTED_RW_CLASSIFICATION_VALIDATION_REV1.ps1 | FBF43F9789E1034D91B944DBAAE76CF09BC46C659985874809803310B995F1E8 | 18807 |
| validation/route_b_c03/wp_008/DSP_004_REMAINING_PURE_CHECKS_VALIDATION_REV1.ps1 | 39614FA04D50971921117E46066F73E548925C817398CDD4560B9C50A0CD5869 | 23193 |
| validation/route_b_c03/wp_008/DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_VALIDATION_REV1.ps1 | FA17F8C28D9982BC3467B2C4AB4FC8DA213E04E4EAC2BE7044E8FBD7E5C99BA4 | 17269 |
| validation/route_b_c03/wp_008/DSP_004_REPORTED_RW_CLASSIFICATION_REV1_OBSERVED_RESULT.json | 492EE32855FDA4E8FABF34586A677BD9BBB3F7CAF377D1BDDF9D2B96C5809451 | 168431 |
| validation/route_b_c03/wp_008/DSP_004_REMAINING_PURE_CHECKS_REV1_OBSERVED_RESULT.json | BA9AAD446C87D1573DF4AA683C99B712F3D6CB80E3897675E1E0EE3064F078B5 | 119720 |

## 8. 保留的 LIMITED 与下一边界

本次在新增 REV2 中补齐末尾记录期限门并增加对应正常断言，六个私有标量边界及封闭合成运行通过；不把静态修补与私有门测试扩大为真实末尾读取超时的复现证明。

全部既有 LIMITED 保留：同步文件读取、启动、Close、Kill、Dispose 硬时限未证明；异常清理及恶意后代路径未测试；完整依赖根、OS 隔离、跨 child 共享引用/冻结、callee 引用、provider 独立性和正向真实 Driver SHA 未建立。正常编译及返回过程的全部耗时不属于候选内终点样本。

REV1 和 D-007 固定源码的会话层有限接受不自动转移到 REV2。REV2 候选接受：PENDING PROJECT OWNER DECISION。

DSP-004：OPEN / HOLD。B-01、B-02：OPEN。来源准入、实际业务捕获、业务集成及部署：NOT AUTHORIZED。没有修改任何已接受文件，不涉及独立 ACOS 或其他项目。

四个新增文件可按既有阶段备份授权进行普通提交与推送；备份不等于候选、结果或治理状态接受，不关闭任何缺口。
