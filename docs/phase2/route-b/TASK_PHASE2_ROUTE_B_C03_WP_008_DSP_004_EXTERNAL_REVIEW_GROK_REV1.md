# DSP-004 外部技术评审意见

**评审者身份**：Grok Bot，所有者张纯熙的助理会话，不在 Claude 记录链之内，没有参与编写被审材料。评审时间是 2026-11-04（北京时间）。
**基线**：simonno1123/claude-for-legal-cn，提交 `110b4ca9bfff1ecb87a41efefdbb249773c7ceba`（合并 PR #56，2026-11-04 16:52:20 +0800）。
**方法**：
- 用 `git clone` 拉到上述提交，逐个文件跑 `sha256sum`，并与 `git cat-file` 的 blob 对照。
- 自己写了一个 CANON-2 编码器，独立重编码 Manifest、重算聚合 SHA。
- 在副本里运行生成程序，不加 `--write`。
- 解析运行记录、collect 结果和事件 XML，做交叉核对。
- 在独立的解释器（Linux 上的 Python 3.13.5）上重跑 harness_rev4，比对 28 个变体的结果。
**访问情况**：没有遇到访问失败。

## 一、逐题结论

**Q1 身份**
- 委托书列出的 20 个文件，字节数和 SHA 与提交逐一相符（20/20），工作区和 blob 两种口径都一致。
- Manifest 的 90 个条目，字节数和 SHA 全部与 bound list `formal_v2` 一致。
- bound list 里的 27 个 ProjectFiles 与仓库文件 27/27 相符。

**Q2 Manifest**
- **CANON-2 编码**：独立重编码后与 Manifest 字节完全相同。没有 BOM、CR、TAB，文件以单个 LF 结尾，键按码点排序，转义规则符合要求。
- **聚合 SHA**：独立重算得到 `6AE76B80BDCB49FB8C6ACCE90E49D860C8CF3420A8D3D982B221183B5DC79713`，相符。
- **生成程序复现**：输出 entries 90，manifest 451503 字节，modules 96，unresolved 0。
- **array policy REV3**：AP-001 到 AP-032 中，只有 AP-001 不合规（3 个根），这一项已作为偏离 1 申报，其余全部合规。
- **§D1 的 9 项偏离**：逐项核对，描述准确。没有发现会影响结论的未申报偏离，只有下面几条 NOTE。

**Q3 运行一致性**
- **PID**：运行记录中 SupervisorPid 6328 = 0x18B8，HarnessPid 1300 = 0x514；与事件 4688 的记录号 75190、75194 对得上，父子关系是 runas → cmd 0x459C → powershell → python。
- **时间链**：完全吻合（UTC，括号内为北京时间）。
  - T0 是 07:56:21.767Z，python 的 4688 在 21.8117Z（15:56:21 北京时间），WMI 记录的 CreatedUtc 是 21.8116540Z。
  - python 的 4689 在 32.3967Z，退出状态 0x0，早于 ExitSeenUtc 32.4031Z。从启动到退出约 10.6 秒，其中 harness 有固定的 10 秒暂停。
  - Supervisor 的 ReleasedUtc 是 34.5827Z，记录写入时间是 34.628Z，powershell 的 4689 在 34.664Z，退出状态 0x0。
  - collect 在 54.83Z，注销事件 4634 在 56.91Z。
- **完整性级别**：cmd、powershell、whoami、python、conhost 全部是 S-1-16-8192（中等），提升类型 %%1936，账户 dsp004val。
- **记录号**：65637 到 75209 连续（9573 条），没有 1102。
- **LockedFiles 743 与 PerFileHashes 742**：结构上就应该是这样。743 = 1（bound list 本身）+ 741 + 1（SELF）；742 = 741 + SELF。数字与预运行绑定里的 ExpectedLockedFiles 743 一致。
- **原生模块**：运行中的 24 个原生模块与 Manifest 的原生条目（EXE 1、CORE_DLL 3、STDLIB_EXT 2、OS_DLL 18）完全相等。
- **Python 模块**：96 个模块名与 Manifest `import_contract.modules` 完全相等；所有有文件来源的模块，其 origin 都在条目里。模块列表与 preflight v2 闭包完全相同，原生模块集合也相同，只是顺序不同。
- **28 个变体**：用独立解释器重跑 harness_rev4，28 个变体的 RuleVerdict、FixtureConformant 和 Observation 与运行记录的 ReportLine 逐条一致，没有差异。合计 28 PASS、full 12、partial 5、not_mapped 11、guard_denied 0。
- **项目侧读取**：本地另加审计钩子记录 open 事件，项目侧实际读取的文件正好是 27 个 ProjectFiles。

**Q4 防护强度**：没有发现夸大到影响结论的说法。有两处需要修正或补充说明，见 N-3 和 N-4。审计钩子不是沙箱、KnownDLLs、宿主管理员这几项，都已声明为局限。

**Q5 治理**：每一步都能找到对应的所有者决定。监督程序和收集程序没有在 P6 里点名，但已通过预运行绑定 F4DD7AC8… 按确切 SHA 间接接受；P8 接受的 6 个文件，SHA 也全部相符。还有两点要注意：决定选项由记录人起草，而且都标了"（推荐）"；P3-CONTRACT 的附加条件由同家族审查来判断。见 N-5。

**Q6 关闭**：现有证据足以支撑关闭，但要先满足下面的条件。

## 二、发现

**阻断项（BLOCKING）**：无。

**非阻断项（NON-BLOCKING）**

- **N-1：结果文件漏报完整性事件**
  - 位置：`DSP_004_FORMAL_RUN_V2_RESULT.json` 的 `AuditCrossCheck`，以及 `TASK_…_FORMAL_RUN_V2_RESULT.md`。
  - 问题：这两份文件只写了 1102 = 0、4625 = 0，没有提 `formal_v2_post_collect_result.json` 中 `IntegrityEvents` 已经记下的事件：
    - 1100（日志服务关闭），2026-11-02T23:28:17.03Z；
    - 4616（系统时间更改），23:28:17.08Z；
    - 4608（系统启动），23:28:45Z。三者合起来就是 11-03 07:28（北京时间）的一次重启。
    - 4719 ×2，11-02T04:14:40.90Z 和 .93Z，子类别 0cce922b、0cce922c，%%8449，即开启进程创建和终止的成功审计。
  - 影响：记录号在重启前后仍然连续，所以风险低。但重启发生在环境准入之后、正式运行之前，属于必须披露的事实。
  - 要求：
    - 补一条说明，写明重启的原因，以及 4616 的 PreviousTime 和 NewTime（collector 只统计了次数，没有导出这两个字段）；
    - 说明重启前后 KnownDLLs 和准入状态没有受影响。

- **N-2：§V1 措辞过时**
  - 位置：`TASK_…_MANIFEST_SUPPORT_POLICIES_REV1.md` 的 §V1。
  - 问题：仍然写着"所有者已决定暂不做外部审查（P1-EXTREVIEW）"，而这一决定已被 P8-EXTREVIEW 取代。
  - 要求：关闭记录里注明这一点，并写明本评审就是在履行 P8-EXTREVIEW。

- **N-3：§X1 的 UNUSED_ASSET"一律不得读取"没有运行时观测**
  - 问题：审计钩子允许只读的 open，也不记录读取。运行时观测到的只有导入闭包和原生模块，看不到运行时侧的非导入读取。我在本地验证了项目侧读取是 27 个文件，但运行时侧（Windows 上）无法从现有证据验证。
  - 要求：把这一条改写成"政策 + 导入闭包观测"，并列为已知局限。

- **N-4：SixSide 的 Consistent 是同义反复**
  - 位置：`harness_rev4.py` 的 `run()` 和 `capture_six_side`。
  - 问题：所谓"实际值"其实是 harness 自己的常量，读回来再和常量比，必然相等；ProviderPortInstanceStatus 被采集了，但没有参与比较。输入里的 limitation 字段已经如实声明了这一点。
  - 要求：任何结论文字都不要把这一项当作信任分离的证据。

- **N-5：治理留痕的局限**
  - 位置：P1 到 P8 的决定文件。
  - 问题：
    - 所有决定都由 Claude 提交，Method 一栏写的是"options drafted by the recorder"，P8 的 RecordedAtUtc 只写了"approx"；
    - 所有者的认可只体现在合并 PR 上，决定本身没有签名；
    - P3-CONTRACT"同家族审查无阻断即接受"，等于由记录人这一方来判断条件是否满足。
  - 要求：所有者作关闭决定时，明确追认这些决定，或者本人签字或提交。

**注记（NOTE）**
1. **收集时会话尚未结束**：`run_formal_v2.cmd` 末尾有 `pause`，collect 时 cmd 还开着。所以 4688 有 58 条、4689 只有 56 条，cmd 0x459C 和 conhost 0x5FC 没有退出事件，注销 4634 在 56.9Z，晚于 CollectedUtc。这是正常现象，建议写进说明。
2. **账户删除后重建**：dsp004val 在 11-02 00:12Z 创建（SID …-1003），00:13Z 删除（4726），04:14:40Z 重建（…-1004）。窗口从第二次创建算起，没有问题。
3. **脱敏文件只能按记录人提供的 SHA 核对**：未脱敏的 SHA BDF9F48E…（运行记录）和 CB38181A…（事件 XML）由记录人提供，外部无法验证脱敏是否如实。我抽查了 SID、主机名、用户路径，没有发现泄漏。
4. **运行记录对管理员不防篡改**：运行记录写在 dsp004val 的 Documents 目录下，宿主管理员可以改动。写入（34.6Z）到收集（54.8Z）之间，没有 dsp004val 的新进程。这属于已接受的残留风险。
5. **SELF 散列只是记录**：监督程序对自身散列只做记录，不做比对，真正的锚点是 collect 时核对的 InstalledFiles 3463EC1E…。这一点没有问题，建议写明。
6. **HX 类检查是子进程自报**：HX_InputSha 等检查依赖 harness 已散列的字节，本身没有增加独立证据；OI 类检查才是外部观测。原生模块是单个时间点的快照，看不到中途卸载的 DLL。
7. **STDLIB_SOURCE 的 `required_by` 统一写成 HARNESS-REV4**：其中包括由受测代码导入的模块，比如 `re`。
8. **lookup_order 的覆盖**：builtin 和 frozen 模块在 lookup_order 里没有 LookupItem（§O1 已说明）；`python312.zip` 只有 SOURCE 一项。
9. **路线图里的受测文件数**：路线图 REV1 §2 写 10 个受测文件，但目录里只有 9 个 `.py`，第 10 个是包 `__init__`。输入 REV4 和 Manifest 都按 10 个处理，前后一致，建议在关闭记录里对一下账。
10. **`mapping.py` 已读取但没有导入**：BytesImporter 一共导入 9 个模块，`mapping.py` 读取了但没有导入，与设计一致。

## 三、关闭前要满足的条件
1. 就 N-1 补充说明 11-02 重启（1100、4616、4608）和 4719，包括 4616 的时间差，并由所有者确认这些事件不影响准入。
2. 所有者另行作出关闭决定，同时追认 P1 到 P8 的决定（N-5），并在关闭记录里注明本评审履行了 P8-EXTREVIEW（N-2）。
3. 把 N-3 和 N-4 写成已知局限；不改也不影响结论，但不能对外表述成更强的保证。

## 四、最终结论
**有条件支持关闭**
