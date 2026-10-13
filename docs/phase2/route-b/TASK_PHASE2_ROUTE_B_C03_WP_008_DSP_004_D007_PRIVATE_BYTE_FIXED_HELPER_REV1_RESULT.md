# DSP-004 D-007 新私有字节与固定 helper 交接 REV1 — 局部合成结果

## 1. 授权与结论范围

Project Owner 对 D-007 新私有合成字节交接批次回复“批量授权”，允许新候选设计、物化、静态核对、隔离合成验证、结果复核及阶段备份。本次只处理 claude-for-legal-cn 本项目的新候选与固定局部 helper；不修改已接受文件、不访问旧私有字节、不读取真实 Driver、不准入来源、不实际捕获、不集成，不涉及独立 ACOS 或其他项目。

本地验证入口退出码 0；记录结果为 `LOCAL_D007_PRIVATE_FIXED_HELPER_CHECKS_PASS`。815 个唯一核对 ID 全部通过，失败 0；这个数量包括公开返回形状、重复拒绝、188 个既有记录 ID 及 189 个清单 ID 的核对，不是新增 815 个案例。当前批次新增且完成原生返回比较的清单项只有 D-007。

新候选仅待 Project Owner 的固定 SHA 有限接受决定，未自动接受。此前已接受源文件及历史记录保持原文与原 SHA；批次末复核保护集合 48/48 MATCH。DSP-004 保持 OPEN / HOLD，B-01、B-02 保持 OPEN，全部 LIMITED 原样保留。

## 2. 新资产身份

路径相对本项目根目录；全部散列为完整 SHA-256。结果文档不自绑定其自身散列。

| 新资产 | SHA-256 | UTF-8 bytes |
| --- | --- | --- |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_PLAN_REV1.md | E8631517523A7B3F35A581AF4251127D1EA44D47D83E527F9B0D91D2C2260488 | 3945 |
| validation/route_b_c03/wp_008/DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_HANDOFF_CANDIDATE_REV1.cs | 666BF56D68FAC64F67E25B55DA26173593E30E8FEC9D4AC89B5DC489B1E4AFD3 | 19442 |
| validation/route_b_c03/wp_008/DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_VALIDATION_REV1.ps1 | FA17F8C28D9982BC3467B2C4AB4FC8DA213E04E4EAC2BE7044E8FBD7E5C99BA4 | 17269 |
| validation/route_b_c03/wp_008/DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_REV1_OBSERVED_RESULT.json | 6B75D24617EFACAF02CC543B3B54D3F21CFEBE79F5255238FAC44CE57FFA1E3E | 79600 |
| validation/route_b_c03/wp_008/DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_ATTEMPT1_SOURCE_SNAPSHOT.txt | 55B949C55B29820AC35562E5A992B69358A3552AEF2575D4877B44C8CBD7355B | 19295 |
| validation/route_b_c03/wp_008/DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_ATTEMPT1_COMPILE_FAILURE.json | 77C1F88E795715ABCB1B119491FD55EAE3D80887BC0EEE805281289BF4DEB07C | 541 |

## 3. 真实失败留存及修正

首次仅编译检查退出码 1，诊断 CS8600：重复读取返回属性后直接转换为 string 的空值类型检查不成立。该次未调用任何公开候选入口，没有准备 fixture、装载控制端或调用 helper。初始源码完整留存在 ATTEMPT1_SOURCE_SNAPSHOT.txt；失败 JSON 记录实际诊断。二者不作可运行或通过版本使用。

仅修正尚未接受的新候选：每个返回属性读取一次，先要求真实 string，再将同一值用于比较和记录。不修改任何已接受源码。修正后仅编译检查退出码 0；最终验证在另一份全新无 profile 的本地 PowerShell 进程中编译固定候选快照，再执行首次请求与同程序集重复请求。保留首次失败，不宣称零次失败历史。

## 4. 独立预期、准备与原生观察

独立清单来源为 DSP_004_LOCAL_VALIDATION_CARRIER_CANDIDATE_REV1.ps1：完整 SHA-256 `46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C`，70284 bytes；只读核对，不装载或执行该文件。D-007 行明确 20177 个 byte 0 的原生 byte[]，在独立准备摘要与 K-003 不等的前置成立后，预期为 FIXED_DRIVER_SHA_MISMATCH。

固定被测控制端为 DSP_004_OUTER_CONTROLLER_CANDIDATE_REV1.ps1：完整 SHA-256 `891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB`，25573 bytes。候选一次读取同份快照，核对 SHA/长度、严格 UTF-8 及十个固定顶层函数定义后，在新空白 FullLanguage runspace 装载整份定义一次。只调用 Test-DSP004DriverBytesInMemory；不调用其他函数、未来 Bootstrap 或单案例入口。无 profile、新进程和空 runspace 是局部隔离方式，不是 OS 沙箱、可信依赖根或完全环境隔离证明。

候选内新建一份私有 20177 零字节数组，并在 helper 调用前以 SHA256.Create().ComputeHash 准备摘要。外侧验证另外新建零字节数组，只作摘要 oracle，从未传入候选或 helper。两份新准备结果相同：`EC0093EB638D86DDEB4C901BD4C2A2B6583E313F4B3FE61AC7F5FD27465EED33`；均不等于 K-003 记录字面量 `6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210`。该摘要来自本次实际计算，不复用历史摘要；它不验证真实 Driver。准备接口与 helper 分离，但仍共享 .NET 密码学栈，不构成密码学 provider 独立性证明。

首次请求观察：控制端读取尝试 1，私有摘要准备调用 1，定义装载 1（输出 0、其他通道 0），固定 helper Invoke 1（返回对象 1、其他通道 0）。调用者命令只含固定函数与 Payload 一个命名参数；调用前后参数 Value 均与私有准备数组 ReferenceEquals，数组形状仍为原生 byte[]、长度 20177、全部零。观察仅限调用者参数槽，不直接证明 callee 引用、全过程冻结或不可并发修改；既有 helper 内部 clone 行为未改变。

六个实际返回字段在 JSON 序列化前比较，均为原生 string；没有用受测返回建立预期或权限：

| 原生字段 | 实际值及独立预期 |
| --- | --- |
| TextCheck | FIXED_DRIVER_SHA_MISMATCH |
| Authority | NOT ESTABLISHED |
| SourceAdmission | NOT ESTABLISHED |
| FrozenHandoff | NOT IMPLEMENTED |
| ChildLengthEofShaVerification | NOT OBSERVED |
| CaseCompletion | NOT ESTABLISHED |

同程序集第二次公开请求返回 REPEATED_LOCAL_D007_REQUEST_REFUSED；源读取、字节准备、摘要、装载和 helper 调用尝试均为 0，无新增摘要或返回字段。这只是新候选的本地一次请求门观察，不是全局一次性授权服务。

首次请求中 Invocation.Dispose、Loader.Dispose、Runspace.Close、Runspace.Dispose、PreparationHasher.Dispose 均返回；首要及次级失败计数 0。公开记录限安全类型、阶段、数量、摘要及合成元数据；原始数组、返回对象和异常持有槽不导出。源码存在原始异常保留及独立清理分支，但本次正常路径没有注入清理故障，不能据此证明故障路径覆盖、跨进程异常留存、完整资源收敛或硬停止能力。记录的局部计时 50 ms 不证明 120/5/5 秒边界。

## 5. 189 项覆盖的精确限定

固定既有读写记录 SHA-256：`492EE32855FDA4E8FABF34586A677BD9BBB3F7CAF377D1BDDF9D2B96C5809451`，记录 96 个局部读写分类项；固定其他纯函数记录 SHA-256：`BA9AAD446C87D1573DF4AA683C99B712F3D6CB80E3897675E1E0EE3064F078B5`，记录 92 个局部项。本批次只核对这些记录及 ID，不重跑此前 188 项，不转移旧私有字节证据。

既有 188 个唯一 ID 不含 D-007；加入本次 D-007 后与固定清单 189 个 ID 的集合精确相等，无缺失或重复。因而可描述为“188 项既有局部纯函数记录，加 1 项新 D-007 观察，覆盖 189 个不同清单项”。第二次拒绝不另增清单项。不得解释为正式 189 项接受、所有原始输入身份冻结、真实 I/O、实际任务/EOF、整体 conformance 或项目已完成。

## 6. 复核和后续边界

本批次为本地执行与自身结果复核，不是第三方或独立子审查员复核；没有调用 Gemini。815 项核对均通过不覆盖未执行的故障注入、极端中断或环境替换路径。

ALL LIMITED RETAINED；正向 Driver SHA 分支 NOT COVERED；Source Admission NOT ESTABLISHED；实际捕获、集成、真实材料、运行时部署及独立 ACOS 操作均不在授权内。只允许按现有阶段备份授权正常提交本项目七个新增文件；备份不构成治理接受。新候选固定 SHA 的接受及任何超出局部合成范围的后续活动仍需 Project Owner 单独决定。
