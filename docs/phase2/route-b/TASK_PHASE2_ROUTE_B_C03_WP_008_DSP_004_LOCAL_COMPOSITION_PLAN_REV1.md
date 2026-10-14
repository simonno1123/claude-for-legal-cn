# DSP-004 本地合成贯通验证批次 — REV1

## 授权和范围

Project Owner 对 writing block 59382 的批次授权回复“确认”。允许在新增测试载体内组合已有限接受候选，完成设计、物化、静态核对、隔离装载、合成运行、结果复核和阶段备份。不修改已接受文件，不读取真实 Driver 或案件材料，不准入来源、不实际业务捕获、不业务集成或部署，不访问独立 ACOS 或其他项目。

唯一新增执行载体为 `validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV1.cs`；唯一新增外侧核对入口为 `validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_VALIDATION_REV1.ps1`。新增载体尚未被 Project Owner 接受。

## 固定依赖

所有下列路径相对本项目根目录，除固定已有 PowerShell 运行文件。缺失、长度或完整 SHA 不一致时不得启动任何子进程；运行后再核对。不修改固定入口中的任何代码或预期。

| 角色 | 文件 | SHA-256 | bytes |
| --- | --- | --- | --- |
| 固定输入清单（只读） | validation/route_b_c03/wp_008/DSP_004_LOCAL_VALIDATION_CARRIER_CANDIDATE_REV1.ps1 | 46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C | 70284 |
| 固定控制端 | validation/route_b_c03/wp_008/DSP_004_OUTER_CONTROLLER_CANDIDATE_REV1.ps1 | 891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB | 25573 |
| 已有限接受 D-007 源码 | validation/route_b_c03/wp_008/DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_HANDOFF_CANDIDATE_REV1.cs | 666BF56D68FAC64F67E25B55DA26173593E30E8FEC9D4AC89B5DC489B1E4AFD3 | 19442 |
| 读写核对入口 | validation/route_b_c03/wp_008/DSP_004_REPORTED_RW_CLASSIFICATION_VALIDATION_REV1.ps1 | FBF43F9789E1034D91B944DBAAE76CF09BC46C659985874809803310B995F1E8 | 18807 |
| 其他纯函数入口 | validation/route_b_c03/wp_008/DSP_004_REMAINING_PURE_CHECKS_VALIDATION_REV1.ps1 | 39614FA04D50971921117E46066F73E548925C817398CDD4560B9C50A0CD5869 | 23193 |
| D-007 核对入口 | validation/route_b_c03/wp_008/DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_VALIDATION_REV1.ps1 | FA17F8C28D9982BC3467B2C4AB4FC8DA213E04E4EAC2BE7044E8FBD7E5C99BA4 | 17269 |
| D-007 入口内部历史记录依赖；只供旧 ID 核对，不计本次新观察 | validation/route_b_c03/wp_008/DSP_004_REPORTED_RW_CLASSIFICATION_REV1_OBSERVED_RESULT.json | 492EE32855FDA4E8FABF34586A677BD9BBB3F7CAF377D1BDDF9D2B96C5809451 | 168431 |
| D-007 入口内部历史记录依赖；只供旧 ID 核对，不计本次新观察 | validation/route_b_c03/wp_008/DSP_004_REMAINING_PURE_CHECKS_REV1_OBSERVED_RESULT.json | BA9AAD446C87D1573DF4AA683C99B712F3D6CB80E3897675E1E0EE3064F078B5 | 119720 |

固定运行文件：`C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe`；实际读取并固定 SHA-256 为 `362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139`。这是文件身份绑定，不是可信根、完整依赖闭包或执行期间路径不可替换证明。

## 三个固定阶段与独立预期

| 阶段 | 新核对项 | 入口检查数 | 固定预期 |
| --- | --- | --- | --- |
| RW | RD-001 至 RD-052、WR-001 至 WR-044，共 96 项 | 390 | LOCAL_REPORTED_RW_CLASSIFICATION_CHECKS_PASS；96 个原生比较通过 |
| PURE | M-001 至 M-006、RQ-001 至 RQ-018、D-001 至 D-006、F-001 至 F-062，共 92 项 | 373 | LOCAL_REMAINING_PURE_CHECKS_PASS；92 个原生比较通过 |
| D007 | 仅 D-007，新私有 20177 零字节，先准备摘要 | 815 | LOCAL_D007_PRIVATE_FIXED_HELPER_CHECKS_PASS；helper 一次，重复请求无 helper 调用 |

阶段顺序固定 RW → PURE → D007。不创建通用执行接口，无脚本、路径、fixture、回调或权限开关参数。每个新编译程序集只允许一次批次请求；第二次拒绝且不读取依赖或启动 child。这个门不等于全局授权服务。

## 快照交接和输出边界

父侧读取各固定入口的同份字节快照并核对 SHA/长度、严格 UTF-8；不在验证后用 -File 重开入口。通过 stdin 将该快照送入无 profile、非交互、隐藏的新 child；固定小型 bootstrap 先核对精确长度、EOF、完整 SHA 和 UTF-8，然后报告包含阶段 ID/SHA 的固定 ACK，再在 child 根作用域点源执行同份快照。点源仅用于恢复入口内部 script: 变量与其他变量的一致作用域；不是在父进程或现有用户会话中注入定义。原入口中的 exit 语义、原生比较、预期和限定语全部保留。

子进程使用新临时工作目录，清空继承环境，仅补七个必要目录/遥测关闭项。这不是 OS 沙箱证明，也不证明完整环境或 .NET/PowerShell 依赖可信。原入口各自按其既有约束读取并核验固定源文件；本轮不声称跨三个 child 共享同一个 runspace、引用或冻结字节对象。

新增载体 stdout 预算固定为 262144 bytes 加一个检测字节，stderr 零正文加一个检测字节。这是**新测试记录传输预算**，不是把原控制端 65536-byte 合同改大。并发正数有界读取；溢出或 stderr 出现后停止，不无限排空。只有 child 正常退出、双流 EOF、完整 ACK、在预算内且本地清理返回时才公开合成 JSON 正文；失败输出和异常 Message/堆栈不公开。

新载体使用全批次共享 120000 ms 的单调检查期限，失败后的 child 退出等待 5000 ms，读取任务等待 5000 ms。这里只设计新的测试监督参数，不转移为旧监督器的成熟能力。同步文件读取、启动、关闭、kill、Dispose 不具有已证明硬时限；正常短时运行也不能证明实际超时、恶意后代或完整资源收敛。

## 外侧核对与覆盖限定

原生比较发生在固定 child 入口内并先于 JSON；父侧 JSON 比较只是记录传输核对，不代替原生类型、callee 引用或冻结证明。父侧拒绝重复 JSON 键、格式错误、额外阶段、ID 重复、缺项、未完成比较及失败计数。完整实际 child 记录分开留存，不能用预期回填。

189 项集合必须从**本次** RW/PURE 实际 Cases 与本次 D-007 新观察重新构造，并与固定清单 ID 集合核对。D-007 入口内部重读两份历史 ID 记录的检查仍是历史依赖审计，不将它的 CombinedLocalPurePlanItems 字段用作本次新覆盖证明。三个阶段检查数合计 1578，其中含元数据及历史记录核对，不等于 1578 个新案例。

全部 LIMITED、正向 Driver SHA NOT COVERED、Source Admission NOT ESTABLISHED、DSP-004 OPEN / HOLD、B-01/B-02 OPEN 保留。不修改历史状态、不接受新载体、不关闭缺口、不产生正式 WP-008 验证或总体结论。自身结果复核不是独立双审；本批次没有第三方调用授权。
