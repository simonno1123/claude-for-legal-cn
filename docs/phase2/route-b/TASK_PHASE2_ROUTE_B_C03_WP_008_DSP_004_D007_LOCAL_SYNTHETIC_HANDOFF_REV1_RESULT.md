# DSP-004 D-007：私有槽拒绝与独立固定调用载体的本地合成验证 REV1

## 1. 本轮授权及对象分离

Project Owner 本轮明确“有限接受上一轮固定 SHA 候选，并授权仅本地合成的后续实现与验证批次”。上一轮接受对象是下表中 `904146E082C2CAE73E2E25BAD1549C15DD076E6E206A6FC0854E18A43DA543B3` 源码；只接受该固定源码，不把后续生成物自动接受为治理基线。

原私有槽候选保持原样，其公共 API 仍然没有可执行交接适配器。新验证载体分别测试该候选的准备/拒绝行为，并另外构造自己持有的原生合成数组，对完整固定控制端中的一个 helper 做局部调用。这是两条不同路径：没有反射取出原候选的私有数组，没有修改其拒绝门，也没有把新载体观察转移为原候选的能力。

本轮没有读取真实 driver 或案件材料，没有准入业务来源、实际业务捕获、集成或外部模型调用，不访问独立 ACOS 或其他项目。读取固定本项目控制端源码属于本批次测试代码装载，不是业务来源准入。

| 对象 | 仓库路径 | 实际固定 SHA-256 |
| --- | --- | --- |
| 已有限接受私有槽候选，未修改 | `validation/route_b_c03/wp_008/DSP_004_D007_CONTROLLED_SAME_PAYLOAD_HANDOFF_CANDIDATE_REV1.cs` | `904146E082C2CAE73E2E25BAD1549C15DD076E6E206A6FC0854E18A43DA543B3` |
| 固定控制端源码，未修改 | `validation/route_b_c03/wp_008/DSP_004_OUTER_CONTROLLER_CANDIDATE_REV1.ps1` | `891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB` |
| 新载体，修正后的最终执行版本 | `validation/route_b_c03/wp_008/DSP_004_D007_LOCAL_SYNTHETIC_HANDOFF_VALIDATION_REV1.ps1` | `49D058C495432D6028ED32D33A356CCA0D0F7B02FC8A162FBFB607266C643749` |
| 新局部外侧监督器，最终执行版本 | `validation/route_b_c03/wp_008/DSP_004_D007_LOCAL_SYNTHETIC_HANDOFF_SUPERVISOR_REV1.cs` | `8AACC28D45F9BCFE14DD143116D1861819EAFCDE7B733B75400530216835CD54` |
| 本批次观察记录 | `validation/route_b_c03/wp_008/DSP_004_D007_LOCAL_SYNTHETIC_HANDOFF_REV1_OBSERVED_RESULT.json` | `6A7409AB8ACA3710CA3B63D8BECBFF2B9328CED289EE3BBBD31DDA464F04BB3B` |

新载体为 25015 UTF-8 bytes / 321 LF；新监督器为 12068 bytes / 226 LF。JSON 为 60897 bytes / 1552 LF。三份文件均无 CR、BOM、尾随空白，并以 LF 结束。SHA 由本地系统对实际文件计算，不是外部模型声明。

## 2. 实现及观察边界

- 固定源码只读一次，校验长度和完整 SHA，严格 UTF-8 解码后使用同份快照；不再按路径重新读取候选文本去编译。
- 新监督器在内存编译，启动一个无 profile、非交互的新 PowerShell 子进程。子进程使用新临时目录；清空继承环境后仅设置七项所需路径/遥测关闭变量，不输出原继承环境。没有 SDK 安装、依赖下载、restore 或持久 DLL 输出。
- 已核验的完整载体快照经 stdin 发送；短固定 bootstrap 核验精确长度、SHA 及尾部 EOF 后执行。stdout 使用 65536-byte 正文预算加一个检测字节，stderr 使用零正文预算加一个检测字节；并发读取，不先等待退出再排空输出。
- 内侧装载完整固定控制端十个函数定义，不抽取/改写目标函数片段。新空命令表 runspace 显式采用 `FullLanguage`；这不是 OS 沙箱或受限语言安全边界。
- 只绑定 `Test-DSP004DriverBytesInMemory` 的唯一 `Payload` 参数；检查其完整函数定义与已核验源码相同。调用前实际命令槽持有的原生数组与载体准备数组 `ReferenceEquals` 相同。该检查不是对函数内部参数的插桩证明，也不是不可变冻结证明。
- helper 返回对象的六个 note property 必须均为原生字符串，数量、名称和值与预先固定的独立字面量预期一致；额外输出或任一错误流均不接受。没有通过 DUT 返回值生成预期。
- 两次候选请求和新载体的 helper 调用分开计数；监督器没有自动重试循环或启用开关。修正未接受的新测试文件后才在新的子进程中进行后续尝试。

## 3. 实际尝试与修正历史

不能把本批次描述为“首次即成功”“全程零错误”或“85 项覆盖所有能力”。

| 子进程尝试 | 退出/耗时/输出 | 局部检查与失败 | helper 尝试/正常返回 | 处置 |
| --- | --- | --- | --- | --- |
| 1 | exit 1；1793 ms；stdout 9903 bytes；stderr 0 | 67 个已完成检查均通过，随后 `MethodInvocationException`；尚未完成全部检查 | 0 / 0 | 空 InitialSessionState 默认为 NoLanguage；新载体改为显式 FullLanguage。不是目标源码缺陷关闭 |
| 2 | exit 1；2270 ms；stdout 10256 bytes；stderr 0 | 71 项中 70 PASS / 1 FAIL；`ADAPTER-BIND-02` 比较失败 | 0 / 0 | FunctionInfo 保存整个 FunctionDefinitionAst，而非仅 Body；仅修正新载体比较位置 |
| 3 | exit 1；2067 ms；stdout 10810 bytes；stderr 0 | 75 个已完成检查均通过，返回属性读取发生 `PropertyNotFoundException` | 1 / 1 | PowerShell 自动解包返回对象；新载体改用 `.PSObject.Properties`；该次没有完整六字段合格比较 |
| 4 | exit 0；2052 ms；stdout 12470 bytes；stderr 0 | 85 / 85 PASS；0 个失败检查；无主失败或清理失败类型 | 1 / 1 | 成功正常路径观察单独保存，未替换前三次失败 |

尝试 1 的载体 / 监督器 SHA 分别为 `FBEC7D3EA5FE5BEA3A3FD3484746B90EA6C138EFC2C292B8252ADD3E97B4E8F7` / `FAAC19D96010340B04EA349F76B0A81C22857871472BDF22448CF8486AF2EE68`；尝试 2 为 `C04A7C31CE28E665BC97A03ADFACD69B7A3A1B5C09EEDA613B106C8414CE2704` / `4043521D0B0AB723D3D8EFDFA14E75AEB4CAEFE0CB021562AA37F7C15DF714B0`；尝试 3 为 `D5673189564FFE362E844EB262A9B3AC004B8A6A917D7C16AF09C497BA9F0FE9` / `D51D146D9091D217FB24B4554600B9DC37ADCFF51A2DD1140DDF97DBCE2E947C`。前三版是未接受测试文件的历史执行指纹，不是新的治理基线。

尝试 1 原输出中有两条无条件的 handoff/helper-return 限定字符串，错误暗示未完成步骤已有观察，明确隔离，不予采用。最终载体已改为依实际检查进度输出限定语。尝试 2 的 FailureStage 固定标签仍停在装载阶段，应以具体失败的 `ADAPTER-BIND-02` 为准；最终载体也明确记录绑定阶段。失败不是靠后置追认变成通过。

额外进行过一次固定定义装载诊断：成功流 0、Error 流 0、helper 调用 0，确认完整函数 extent 匹配而 Body extent 不匹配。本批次共四个验证子进程、四次原候选准备、八次拒绝请求、五次控制端定义装载尝试（含此诊断）、两次实际 helper 调用及正常返回，仅一次完成全部六字段合格比较。没有运行完整 189 项计划。

机器文件中的尝试 2–4 保存工具输出的父侧 JSON 解析对象，经仓库 JSON/LF 排版；不是未修改的原始 child stdout 或完整 transcript。尝试 1 是明确标注的已观察字段投影。原异常对象只在产生它的进程中保留，输出只记录类型；没有跨进程原异常对象保留承诺。

## 4. 成功路径的局部结果与复核

候选私有准备、另构造的 oracle 和新载体自己的准备/调用后数组，摘要均观察为 `EC0093EB638D86DDEB4C901BD4C2A2B6583E313F4B3FE61AC7F5FD27465EED33`；与记录的 K-003 字面量 `6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210` 不同。oracle 使用另外一份数组及不同 .NET SHA API 路径，但仍是同一 .NET 密码学栈，不能称为独立供应商/密码学实现验证。摘要相同不能证明不同路径使用同一个数组。

| 成功检查组 | 数量 | 观察限定 |
| --- | --- | --- |
| SLOT 源快照、装载、公共 API、准备、23 个元数据字段 | 38 | 没有读取私有数组；元数据核验不完成其明确否定的责任 |
| 两次 REQUEST 类型及七字段 | 16 | 首次 `FIRST_REQUEST_REFUSED_UNBOUND`；第二次 `REPEATED_REQUEST_REFUSED`；仅同一实例 |
| DUT-SRC 完整控制端快照 | 3 | 本项目代码快照，不是业务来源准入或可信根 |
| 独立构造 oracle | 4 | 仅合成零字节及记录字面量关系 |
| ADAPTER 准备、装载、绑定、调用后观察 | 14 | 实际命令槽引用及调用前后内容；未插桩 callee，不证明没有瞬间修改 |
| DUT 返回形状、输出流及六字段预期 | 9 | 一次合成 SHA 不匹配返回；不是正向 driver 身份验证 |
| 调用计数边界 | 1 | 仅第四次尝试的精确计数，不抹除前三次尝试 |
| 合计 | 85 | 85 个唯一 ID / 85 个 true / 0 个 false；仅局部正常路径 |

六字段为 `TextCheck=FIXED_DRIVER_SHA_MISMATCH`、`Authority=NOT ESTABLISHED`、`SourceAdmission=NOT ESTABLISHED`、`FrozenHandoff=NOT IMPLEMENTED`、`ChildLengthEofShaVerification=NOT OBSERVED`、`CaseCompletion=NOT ESTABLISHED`。原候选 API 的拒绝行为仍然成立；新 helper 返回不替代它的交接状态。

实际运行元数据：PowerShell 7.6.5、.NET 10.0.11、X64。pwsh 文件指纹为 `362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139`；程序集标识详见机器记录。仅为本地观察，不证明完整依赖闭包、签名信任或运行期间不可替换性。四个子进程均正常结束，stdin close 返回，受控双流结束；这些局部事实不是所有资源或后代结束证明。临时目录保留，未做递归删除。

主协调员进行源码静态核对、计数及结果交叉核对。没有在本轮调用独立子审查员或 Gemini，不能把该自复核记录称为独立双审结论。

## 5. 保留缺口及下一边界

120 秒监测阈值、失败后的 5/5 秒退出/流等待已写入新监督器，但只观察正常路径。同步源码读取、进程启动、输入 close、kill 等调用本身没有可证明的硬时间界限；对抗性超时、超量输出、资源耗尽、并发/重复中断及完整后代收敛均未验证，不能把计时设计提议宣布为成熟执行能力。

以下均继续保留：正向固定 SHA 分支 NOT COVERED；原候选的相等/故障分支、并发保留门、callee 引用插桩、独占不可变冻结、可信宿主/完整依赖、原失败与清理失败并存注入、完整 189 项计划未覆盖。完整 D-007 准入与条目完成 NOT ESTABLISHED；仅本次局部 helper 技术调用已观察，不再笼统声称本批次完全未调用 helper。

本批次前后 19 份已有保护源码/记录按完整 SHA 核对，均未修改。新载体、新监督器和新观察记录尚未由本结果自动接受。原静态审查的历史“未执行”描述保持原样，不能追溯改写成当时已执行。

DSP-004 保持 **OPEN / HOLD**；B-01、B-02 保持 **OPEN**；全部 LIMITED 保留。来源准入、真实材料处理、实际业务捕获、集成、整体安全/法律结论及跨项目操作均未授权/未实施。新增本项目合成验证文件可按阶段备份授权普通提交与推送；备份不等于治理接受或下游放行。
