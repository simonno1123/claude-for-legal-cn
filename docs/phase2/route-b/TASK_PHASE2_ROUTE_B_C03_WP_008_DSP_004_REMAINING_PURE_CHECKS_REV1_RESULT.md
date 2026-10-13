# DSP-004 剩余纯函数项 REV1：实际本地观察与覆盖核对

## 1. 范围和绑定

按 Project Owner“接受并继续”及既有仅本地合成范围推进，不修改任何已接受文件，不准入来源、不实际捕获、不集成，不涉及独立 ACOS 或其他项目。本结果不接受新测试入口或授予下游权限。

| 新资产 | 实际 SHA-256 | 格式 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REMAINING_PURE_CHECKS_PLAN_REV1.md` | `75031439CCA403F94F12374001C58271270344A97D138FA0BB2298485D2F57E2` | 3292 UTF-8 bytes / 22 LF |
| `validation/route_b_c03/wp_008/DSP_004_REMAINING_PURE_CHECKS_VALIDATION_REV1.ps1` | `39614FA04D50971921117E46066F73E548925C817398CDD4560B9C50A0CD5869` | 23193 bytes / 183 LF |
| `validation/route_b_c03/wp_008/DSP_004_REMAINING_PURE_CHECKS_ATTEMPT1_ENTRY_SNAPSHOT.ps1` | `289F610BA5B9D57001B296929971E733995BA913261BCFAB6CC578B0C9725302` | 23176 bytes / 183 LF |
| `validation/route_b_c03/wp_008/DSP_004_REMAINING_PURE_CHECKS_ATTEMPT1_FAILURE.json` | `ACE850DDE2AA3FA191CC2CF6B137D9D62B71ED023A7050E75AA0DC63286C3FBB` | 1596 bytes / 53 LF |
| `validation/route_b_c03/wp_008/DSP_004_REMAINING_PURE_CHECKS_REV1_OBSERVED_RESULT.json` | `BA9AAD446C87D1573DF4AA683C99B712F3D6CB80E3897675E1E0EE3064F078B5` | 119720 bytes / 4343 LF |

每次入口均读取同份固定清单 `46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C`、控制端 `891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB` 快照，核验完整 SHA/长度，严格解码、核对参考行及十个顶层函数定义后，在新空白 FullLanguage runspace 装载控制端定义。清单源只读，不执行；没有读取 GetFixedContract 中四个上游路径。

## 2. 首次失败的保留与修正

第一次运行退出码 1：五项前置检查通过，进行一个直接 getter 调用后，在新验证入口捕获返回对象的环节产生 `System.Management.Automation.PropertyNotFoundException`。清单项目完成数 0、假检查数 0 不等于整批通过。该次 getter 调用不能补登记为 M-001 原生比较完成。

首次入口直接访问枚举对象的 `BaseObject` 属性，PowerShell 的动态对象表面并不保证该属性存在。仅修改本轮未接受测试入口，改为经 `PSObject.BaseObject` 访问；PSCustomObject 保留其属性载体，不丢弃成员。前一入口的完整字节快照与原 SHA 一致，失败 JSON 完整保留。没有修改控制端、清单或既有接受文件，没有将失败归因为目标控制端缺陷。

两次运行合计两个新 runspace 装载、96 次直接目标调用；第一次 1 次未比较完成，第二次 95 次对应 92 个清单项。目标函数内部的正常 helper 调用不包含在“直接目标调用”计数中，也不据此增加清单项目数。没有重试 Driver 或实际业务调用。

## 3. 第二次实际结果

第二次入口退出码 0，`LOCAL_REMAINING_PURE_CHECKS_PASS`。五项前置检查加 92 项各四项检查，共 373 个唯一检查全部 true，0 个 false，无入口级失败或清理失败类型。92 个清单项完成原生比较；M-004 至 M-006 每项包含两个直接 getter 调用，因此该次直接调用数为 95，而非 92。

| 组 | 项目数 | 实际局部观察 |
| --- | --- | --- |
| M-001 至 M-006 | 6 | 三键 Hashtable 集合、26 条独立 tuple 序列、27 个固定属性逐项类型/值/集合比较；修改第一返回副本不污染第二返回 |
| RQ-001 至 RQ-018 | 18 | 原生 bool：8 true、10 false；大小写、空白、null、Boolean、Int32、object[] 拒绝按原清单保持 |
| D-001 至 D-006 | 6 | 三项 NATIVE_BYTES_REQUIRED、三项 EXACT_DRIVER_LENGTH_REQUIRED；其他固定否定字段完整保留 |
| F-001 至 F-062 | 62 | 29 条 ALLOWLISTED_FRAME_TEXT_ONLY、33 条 FRAME_REJECTED；记录 Action、ProtectionRecord 和七项否定字段 |
| 合计 | 92 | 文本/类型/分类核对，不是执行、输入准入或业务完成 |

M-004 修改调用者首个 Hashtable 的 CaseId，第二次首个 Hashtable 引用不同且内容符合独立 A 表。M-005 替换的是测试持有的管道捕获数组槽位，不声称 getter 直接返回数组。M-006 修改第一份调用者对象的字段及嵌套槽位；第二份返回仍符合 K/A/T 独立预期，CaseContract/StatusCombinations 数组及首个 Hashtable 引用不同。这些行为和局部引用观察不证明冻结、并发安全或全部依赖可信。

D-003 使用清单 REV2 开头明确收缩的原生 Int32 0；保留的原 int[] 历史行未改写。没有读取真实 Driver、计算其正向匹配或补造来源/冻结资格。F 的 byte[] 通过持有属性和命名参数传入，包含缺失 LF、CRLF、BOM、非 ASCII、零/空白/多帧/字段错配等固定变异；拒绝不是正常 I/O 成功。保护帧和 STOP_BATCH 帧不计实际案例完成。

所有装载/调用的错误、警告、调试、详细、信息和进度通道均核对；先完成原生类型/值比较，再序列化。JSON 保存各次实际工具输出的完整父侧解析对象、按两空格/LF 排版，不是未修改的原始控制台 transcript。Close/Dispose 调用返回仅为本地观察，不证明完整引擎或资源收敛。

## 4. 与前一批的去重覆盖

前一批观察文件 SHA-256 为 `492EE32855FDA4E8FABF34586A677BD9BBB3F7CAF377D1BDDF9D2B96C5809451`，结果记录 SHA-256 为 `AF6782B3FCF3ABBC83B4833291FA621A387E9C882F524488B501433EB876CB23`。该批只覆盖 RD 52 和 WR 44，共 96 个不同 ID；本批只覆盖 M/RQ/D-001..006/F 共 92 个不同 ID。二者 ID 不重叠，共 188 个已作局部原生比较的清单项目，不能以 390+373 个检查实例或其他载体的结果代替项目数。

| 原 189 项清单组 | 此两批项目覆盖 | 未覆盖 |
| --- | --- | --- |
| M 6 | 6 | 0 |
| RQ 18 | 18 | 0 |
| D 7 | 6 | 1：D-007 |
| F 62 | 62 | 0 |
| RD 52 | 52 | 0 |
| WR 44 | 44 | 0 |
| 合计 | 188 | 1 |

D-007 保持 NOT_RUN：本轮没有建立原清单要求的同一私有准备字节与受控交接绑定，未读取/反射以前的私有字节，也不以另一份相同长度零数组或历史 helper 局部观察转移结果。补齐该项须另行明确唯一准备/交接候选、固定 SHA、原生同一对象使用和独立预期边界；不得通过修改已接受源码或准入真实 Driver 跳过。

## 5. 当前限定与后续边界

38 份既有保护文件及前一批四份已形成记录均保持完整 SHA 一致。只有新验证入口在首次失败后作上述未接受测试准备修正，首次完整版本和失败记录保留。没有修改已接受文件，没有调用单案例入口、Bootstrap、Python、真实 I/O 任务、Driver 或案件材料，也没有启动测试子进程。

由主协调员作静态与实际结果交叉核对，未调用独立子审查员或 Gemini，不称为独立双审。新源码/输入的有限接受记录不转移为跨来源准入或完整执行资格。

DSP-004 仍 OPEN / HOLD；B-01、B-02 仍 OPEN；全部 LIMITED 保留。188 个纯函数项的局部核对不构成完整 189 项、真实隔离、完整停止能力或项目总体完成。候选集成、真实来源、实际捕获、运行时及独立 ACOS 操作均未授权。阶段普通提交/推送仅作可公开本项目文件备份，不等于治理接受。
