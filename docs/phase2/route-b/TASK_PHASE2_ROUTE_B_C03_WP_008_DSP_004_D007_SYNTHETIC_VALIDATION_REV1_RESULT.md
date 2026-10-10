# DSP-004 D-007 准备候选：本地合成验证 REV1 结果

## 1. 授权与范围

Project Owner 对“核对必要环境、编译并运行该候选、计算合成摘要、复核结果”的一次性本地合成验证批次明确回复“是”。本批次不调用 DUT、不运行 189 项计划、不读取真实 driver 或案件材料、不准入业务来源、不集成、不接受候选或签发总体结论。全部已有 LIMITED 保留，不涉及独立 ACOS 或其他项目。

历史静态审查记录保持原样：它描述当时未编译/装载/执行的事实。本次新增记录描述后来单独获准的局部运行，不追溯修改历史。

| 对象 | 仓库路径 | 实际 SHA-256 |
| --- | --- | --- |
| 原准备候选，未修改 | `validation/route_b_c03/wp_008/DSP_004_INDEPENDENT_D007_PREPARATION_CANDIDATE_REV1.cs` | `CFCECB173FB5941958649C7135E77B638BAFF41AAA96074971DE53050BA301B5` |
| 历史静态审查记录，未修改 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_INDEPENDENT_D007_PREPARATION_REV1_STATIC_REVIEW.md` | `8F9997619ADD824253469C2D4C279767FC210BDC804E4E2319B136F349EA7B1D` |
| 新测试脚本，修正后的执行版本 | `validation/route_b_c03/wp_008/DSP_004_INDEPENDENT_D007_PREPARATION_SYNTHETIC_VALIDATION_REV1.ps1` | `FC32F3ED534F8163D7FEFA4E4C524E28CFFFD7DD3D0366FC0C60497E64F0349C` |
| 成功子进程 JSON 数据体 | `validation/route_b_c03/wp_008/DSP_004_D007_SYNTHETIC_VALIDATION_REV1_OBSERVED_RESULT.json` | `3ED83B36CE11F65A2361EA72595CD9EA8756B97EE3E0658C403F9CD39A2BA527` |

候选仍为 7617 UTF-8 bytes / 175 LF；新测试脚本为 14261 bytes / 202 LF。测试脚本只读固定候选的同份字节快照，先验证长度和完整 SHA，再严格 UTF-8 解码并内存编译；未替换或改写候选。

## 2. 必要环境观察与编译方式

实际观察到 PowerShell Core 7.6.5、X64、`.NET 10.0.11`。独立 `dotnet --list-sdks` 未列出 SDK；本机另外列出 .NET 8.0.22 运行时，但本批次并未使用它编译候选。没有下载安装工具、NuGet restore 或写出编译 DLL。

使用现有 PowerShell 的 [Add-Type 内存编译接口](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/add-type?view=powershell-7.6)，只编译固定候选全文。编译后的公共类型数量为 1，名称精确匹配，候选方法实际调用 1 次。

| 观察对象 | 实际值 | 证据限定 |
| --- | --- | --- |
| 使用的 `pwsh.exe` 文件 SHA | `362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139` | 启动前源文件身份观察；不是可信根或执行期间不可替换证明 |
| 显式加载的 Utility 模块 manifest SHA | `D103110AAE93CA1061FAB8ADD8F00EA6110740AC94B236654D0EFB0B08654AAA` | 必要模块身份观察，不证明完整依赖闭包 |
| 编译器命令程序集 | `Microsoft.PowerShell.Commands.Utility, Version=7.6.0.500, Culture=neutral, PublicKeyToken=31bf3856ad364e35` | 实际本地运行元数据，不是签名或可信状态验证 |
| 摘要程序集 | `System.Security.Cryptography, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a` | 实际本地运行元数据 |
| 摘要程序集文件 SHA | `BEE61E6BDEFF9FB0C4F3CBF9D48E9D1D97D12A8BB85D1EEAB9178E818B582EEE` | 本地文件指纹，不证明实际映射字节或全部 native 依赖 |
| 摘要 module version ID | `b7336b9c-2990-4d19-981b-1b564e8bf0f3` | 身份元数据，不是安全认证 |
| 参考路径 provider 类型 | `System.Security.Cryptography.SHA256+Implementation` | 观察到的 .NET 类型，不代表独立密码学实现 |

新子进程使用 `-NoLogo -NoProfile -NonInteractive`，无可见窗口，清空继承环境后仅设置 8 个必要路径/临时目录/遥测关闭变量，显式加载 Utility 模块，禁用模块自动加载。工作目录和 TEMP/TMP 是本次新建临时目录。子进程未接收原继承环境，记录未输出原环境变量值；不据此证明宿主从未处理任何环境值或具备完整凭据隔离。

这些措施是本次局部执行的进程与输入控制，不是 OS 沙箱、完整输出封闭、根信任、独占冻结或跨项目隔离的全面证明。临时目录未作递归清理，不能声称所有任务/资源回收已经验证。

## 3. 实际尝试与失败保留

| 阶段/尝试 | 观察结果 | 候选编译/调用 | 处置 |
| --- | --- | --- | --- |
| 首次环境元数据探针 | 将 Windows PowerShell 的 `CLRVersion` 用于 Core 时遇到 null，探针退出非零 | 未编译，0 次调用 | 改为读取 `Environment.Version` 与 `FrameworkDescription`；不修改候选 |
| 子进程尝试 1 | 新测试脚本第 11 行使用 `Join-Path`，自动模块加载已禁用，启动失败；退出码 1；stdout 0 bytes，stderr 849 bytes；外侧实测 4145 ms，未超时 | 未进入候选源读取/编译，0 次调用 | 仅修正新测试脚本的两处路径拼接，改用 `System.IO.Path.Combine`；失败不删除或解释为通过 |
| 子进程尝试 2 | 退出码 0；stdout 6250 UTF-8 bytes，stderr 0 bytes；双流正常结束；外侧实测 6537 ms，未超时 | 内存编译完成，准备方法 1 次调用 | 成功 JSON 数据体另存，结果逐项核对 |

尝试 1 的新测试脚本指纹为 `72334090A318415DAA1A29347E0A2363E2315F9E4FA47127BB19356877D85477`；只有该未接受测试脚本发生修正，固定准备候选未改。两次子进程尝试不能被合并描述为“首次运行即通过”或“全程零错误”。

外侧为本次测试设置 120000 ms 等待上限及完成后的有限流等待；实际只观察到正常退出路径。超时、树终止、迟到输出、恶意资源耗尽及 5/5 秒停止契约没有被覆盖。65536-byte 输出大小检查发生在完整收集之后，不是流式硬限额。这些观察不关闭上游第⑧项 LIMITED。

## 4. 合成摘要与局部结果

候选在其方法内部准备固定全零合成输入并使用 [SHA256.HashData](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.sha256.hashdata?view=net-10.0)。测试脚本另构造 20177 个零字节，检查原生形状后，使用 `SHA256.Create().ComputeHash` 和不同的 Hex 编码路径作为参考。参考输入与候选私有输入是两份不同数组；没有反射、取出、修改或交接候选的私有数组。

| 数值/关系 | 实际观察 |
| --- | --- |
| 候选返回的合成 SHA-256 | `EC0093EB638D86DDEB4C901BD4C2A2B6583E313F4B3FE61AC7F5FD27465EED33` |
| 另构造输入的参考 SHA-256 | `EC0093EB638D86DDEB4C901BD4C2A2B6583E313F4B3FE61AC7F5FD27465EED33` |
| A/P1 记录中的 K-003 字面量 | `6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210` |
| 候选返回的关系 | `DIFFERENT_FROM_RECORDED_LITERAL` |
| 本次技术结果 | `LOCAL_SYNTHETIC_CHECKS_PASS`；38 项局部检查通过，0 项局部检查失败 |

参考路径独立构造输入且不使用候选返回值生成预期，但与候选共用本机 .NET 密码学栈；它不是独立密码学库/供应商核验。相等摘要不能证明同份数组交接。K-003 只作为记录字面量比较，本批次未独立核验真实 driver 的内容或 SHA。

| 检查组 | 数量 | 本次结果 | 限定 |
| --- | --- | --- | --- |
| SRC | 3 | 3 PASS | 固定源快照的长度、SHA 与 BOM |
| LOAD | 3 | 3 PASS | 新子进程内既有类型排除及实际编译类型身份 |
| API | 6 | 6 PASS | 公开接口形状；不是所有内部行为或权限门证明 |
| ORACLE | 4 | 4 PASS | 另构造的全零输入及参考摘要形状 |
| RUN | 5 | 5 PASS | 单次正常准备返回及摘要/关系一致性 |
| META | 16 | 16 PASS | 16 项公开字符串与预期逐字匹配；不是字符串所否定责任已完成的证明 |
| BOUNDARY | 1 | 1 PASS | 仅准备候选方法调用一次 |
| 合计 | 38 | 38 PASS | 不是 189 项测试、总体安全结论或治理 Grade A |

主协调员从捕获 JSON 重新核对：38 个 ID 唯一、分组计数相加为 38、38 个布尔通过值、0 个失败值、编译完成、调用数 1、无失败类型、候选/参考摘要完整且相同、与 K-003 字面量不同、DUT/189 项调用数均为 0。保存的机器文件是子进程单个完整 JSON 数据体，仅把管道行尾 CRLF 规范为仓库 LF；文件为 6249 bytes / 1 LF，不是完整控制台 transcript，也不包含尝试 1 的 stderr。尝试 1 已在本记录独立保留。

## 5. 未覆盖、固定文件与保留状态

成功机器结果明确列出 9 类未覆盖项：相等关系分支、输入形状失败、摘要形状失败、异常引用保留分支、致命/结果分配失败、DUT 正向 SHA 分支、独占冻结及同份 DUT 使用、可信根/完整依赖、输出封闭与对抗性超时停止。未做故障注入、私有字段修改或替换固定比较字面量来制造覆盖。

本次没有改写候选或任何已接受文件。批次起始工作区干净，运行前核对准备候选固定 SHA；结束后核对准备候选、六份既有保护源码及历史静态记录，八份 SHA 均与既有绑定值相符。六份既有保护源码及历史静态记录未作为执行对象。新测试脚本、新成功 JSON 和本结果记录均不是 Owner 接受决定。

- 合成准备方法：本次已调用，单次正常返回路径及局部关系得到观察。
- 受测 D-007 / 189 项计划：没有调用；整体前置保持 `UNBOUND / NOT_RUN`，不能把局部摘要观察当作已完成完整准入。
- 真实正向 SHA 分支：`NOT COVERED`。
- 同份 DUT 使用/冻结交接：`NOT ESTABLISHED / NOT IMPLEMENTED`。
- 全部 LIMITED 保留；DSP-004 保持 `OPEN / HOLD`；B-01、B-02 保持 `OPEN`。
- 来源准入、真实材料处理、实际业务捕获、集成及任何跨项目操作：未实施，也未由本结果授权。

本项目可以对上述三个新验证文件进行普通 Git 阶段备份。局部通过、结果记录或备份均不接受候选、不自动放行下一批次，不把未覆盖项、启动修复或上游缺口重写为零缺陷或项目完成。
