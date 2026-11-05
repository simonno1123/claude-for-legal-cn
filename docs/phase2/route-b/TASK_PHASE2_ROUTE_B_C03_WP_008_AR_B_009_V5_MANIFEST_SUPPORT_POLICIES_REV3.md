# AR-B-009 V5 Manifest 配套政策 REV3（候选）

本文件是 `validation/route_b_c03/wp_008/ar_b_009_v5/PYTHON_RUNTIME_DEPENDENCY_MANIFEST_REV3.json` 中各项 ArtifactRef 引用的政策来源。

本文件是已接受的配套政策 REV2（所有者决定 V4-ACCEPT-MANIFEST）的修订版，只改了以下几处：
- PROJECT_ROOT 改为 `project_v4`；
- Harness 改为 REV6，输入改为 REV6，约束清单改为 formal v4；
- 生成授权改为 AR-B-009 工作授权；
- §D1 的第 7、10、11 项按 V5 改写。

其余规则与 REV2 相同。本文件**需与 Manifest REV3 一并接受**；接受之前，不授权任何读取、装载或运行。AR-B-009 保持 `OPEN / BLOCKED`。

依据：
- 已接受的类型合同 REV3 与数组政策 REV3；
- 已接受的 Manifest REV2 与配套政策 REV2；
- AR-B-009 工作授权（`.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_AR_B_009_WORK_AUTHORIZATION.md`）；
- V5 修订审查 REV1（`.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_AR_B_009_V5_REVISION_REVIEW_REV1.md`）；
- 正式运行 v3 的结果（导入闭包与预检 v2 相同）。

## §G1 生成授权与角色

- **生成授权**：AR-B-009 工作授权，范围是实现候选 V5 及随后的审查与验证准备，Manifest 的生成属于验证准备。
- **生成角色**（materializer_role）：`RECORDER_ONLY`，即记录人 Claude，不是所有者。
- **Manifest 版本**：`REV3`。

## §R1 根目录、解析、大小写与重解析

| RootId | 规范目录 | 解析方式 |
| --- | --- | --- |
| PROJECT_ROOT | `C:\Program Files\DSP004Runtime\project_v4` | Harness REV6 用 `os.path.join(root, *relative_path.split("/"))` 解析 |
| RUNTIME_ROOT | `C:\Program Files\DSP004Runtime\Python312` | CPython 3.12.10 解释器与 Windows 装载器解析 |
| SYSTEM_ROOT | `C:\Windows\System32` | Windows 装载器解析 |

- **大小写**：NTFS 不区分大小写，但保留大小写。`relative_path` 一律采用约束清单 `bound_list_formal_v4.json` 中的写法。同一路径的不同大小写写法，视为同一文件身份。
- **重解析**：三个根目录下不允许任何重解析点（联接、符号链接）。所有文件的 `reparse_state` 均为 `DIRECT`。依据是监督程序的目录树检查与逐项访问控制检查：每个文件、每个目录都只能是继承形式（REV48 预检中 721 个文件、71 个目录全部通过；正式运行 v4 的目录树另行记录）。System32 下，约束清单绑定了 22 个系统 DLL（身份由 Authenticode `IsOSBinary` 与散列共同确定）；Manifest 只登记其中预检 v2 实际装载的 18 个，其余 4 个不是条目，不得读取。
- **读取范围**：根目录绑定不授予目录枚举权。每一项 ReadScope 都只对应 Manifest 中一个确切的条目文件、用途和阶段。

## §R2 VENV_ROOT

按所有者决定 P6-VENV-ROOT，本环境不使用虚拟环境。`root_bindings` 只含三个根，**这偏离了 AP-001"恰好四个"的要求**。偏离由该决定承担，并需在接受本 Manifest 时一并确认。

## §R3 不属于四个根的启动程序

`run_formal_v4.cmd`、`supervisor_formal_v4.ps1`，以及系统的 `cmd.exe`、`powershell.exe`，位于四个根之外。它们的身份由 formal v4 的生成摘要 `prepare_summary.json`、安装器常量和收集脚本的复算来锚定，不作为 Manifest 条目。`runtime_identity.validation_launcher` 指向 Python 解释器本身，即实际被启动、执行验证的程序。

## §S1 启动契约（AP-006）

声明的启动序列如下。这只是声明，不表示已经启动或装载。

| 序号 | step_id | 文件 | 用途 |
| --- | --- | --- | --- |
| 1 | STARTUP-01-PYTHON-EXECUTABLE | RUNTIME_ROOT `python.exe` | VALIDATION_ENTRYPOINT |
| 2 | STARTUP-02-PYTHON-CORE-DLL | RUNTIME_ROOT `python312.dll` | CPYTHON_BOOTSTRAP_LIBRARY |
| 3 | STARTUP-03-VC-RUNTIME | RUNTIME_ROOT `vcruntime140.dll` | CPYTHON_BOOTSTRAP_LIBRARY |
| 4 | STARTUP-04-HARNESS | PROJECT_ROOT `validation/route_b_c03/wp_008/ar_b_009_v5/harness_rev6.py` | VALIDATION_HARNESS_SOURCE |

命令行固定为 `python.exe -I -S -B <harness> <PROJECT_ROOT>`，环境变量只有 4 个（`SystemRoot`、`windir`、`SystemDrive`、`PATH`）。

**配置文件**：解释器没有配置文件（不存在 `pyvenv.cfg`、`._pth`，目录树检查禁止这两种文件）。`runtime_identity.configuration` 因此记为 `NOT_APPLICABLE`。**这偏离了"FileRef 必填"的要求**，需在接受本 Manifest 时一并确认。

## §O1 来源政策与查找顺序（AP-009）

导入时按以下顺序查找：
1. Harness 的私有导入器 `BytesImporter`：只提供 10 个已绑定的受测模块，代码来自已核对散列的字节；对其他 `phase2_runtime.*` 名称一律拒绝。
2. 解释器内建（BuiltinImporter）与冻结（FrozenImporter）模块：绑定到解释器身份（`python312.dll`），不对应任何文件。
3. PathFinder，按 `sys.path` 顺序查找：`python312.zip`（该文件不存在）、`DLLs`、`Lib`、`RUNTIME_ROOT` 本身；每一项分源码和扩展两种查找。
4. DLL 依赖的查找位置依次为：程序目录（RUNTIME_ROOT），然后是 System32（KnownDLLs 属于已知局限 P1-RESIDUALS）。

**调用方归属**：预检只记录了被导入的模块及其装载器，没有逐一记录"由谁导入"。因此，ModuleRecord 的 `caller` 统一绑定到解释器的导入系统，即 `importlib._bootstrap._find_and_load`，并作为局限写明。

## §T1 受信操作政策

| 操作 | 阶段 | 内容限制 | 命名空间限制 | 输入限制 |
| --- | --- | --- | --- | --- |
| STATIC_AST_PARSE | T2 | 只用 `ast.parse` 解析已核对散列的 10 个受测源码，只产生语法树，不执行 | 不写入任何命名空间 | 输入只能是已绑定的源码字节 |
| NORMAL_LITERAL_IMPORT | T1、T3 | 只导入固定的模块名，导入路径按 §O1；T1 不预装受测代码 | 受测模块只进入 `phase2_runtime.*` | 模块名不来自输入数据 |
| DATACLASS_INTERNAL_GENERATION | T1、T3 | 只允许 `dataclasses.py` 在 Harness 和受测源码声明的 dataclass 上生成方法 | 生成的代码只进入被装饰类本身 | Fixture、命令行、环境变量都不能成为生成内容 |

**执行依据**：Harness REV6 沿用的 REV4 第 3 点（扫描）、第 4 点（审计钩子）和第 5 点（私有导入器）；预检运行 v2 中拦截没有触发（`guard_denied` 为 0）。

审计钩子不是防篡改沙箱，这一点已作为局限写明。

## §X1 排除政策

按类型合同 §3.8，十个排除类别全部列出，判定依据如下：

| 类别 | 判定 |
| --- | --- |
| SITE_PACKAGES | 不在 `sys.path` 上（`-S`），预检闭包中没有任何 `site-packages` 路径 |
| INSTALLATION_TOOL | 运行时目录中的安装工具（`ensurepip`、`pip` 等）不在闭包中 |
| DEVELOPMENT_HEADER | 运行时没有安装开发头文件（`include`、`libs` 不在 653 个文件中，或不被读取） |
| UNUSED_TEST_ASSET | `Lib/test`、`Lib/idlelib/idle_test` 等不在闭包中 |
| TK_TCL | `tcl`、`tkinter` 不在闭包中 |
| PACKAGE_METADATA | 不读取 `.dist-info` / `.egg-info` |
| DOCUMENTATION | `LICENSE.txt`、`NEWS.txt` 等不读取 |
| BYTECODE | 目录树检查禁止 `.pyc`；以 `-B` 运行，并由私有导入器从源码字节构建模块 |
| CACHE | 禁止 `__pycache__` 目录；`empty_pycache_prefix` 必须为空 |
| UNUSED_ASSET | 653 个运行时文件中，凡不在 Manifest 条目内的，一律不得读取 |

条目与排除类别之间的归属，以预检闭包加约束清单的路径为准，不靠猜测。没有 EXACT_PATH 规则。

## §C1 条目分类与标识

- **`entry_id`** 写作 `<category>:<root_id>:<relative_path>`。所有这种形式的标识构成"绑定的标识集"（P6-ENTRY-ID）。
- **`required_by`** 的标识集为：`BOOTSTRAP`、`HARNESS-REV6`、`SUBJECT-IMPORT`、`EXTENSION-_hashlib`、`PE-CLOSURE`。
- **类别、装载类型与读取阶段**：

| 来源 | 类别 | 装载类型 | read_phase |
| --- | --- | --- | --- |
| RUNTIME_ROOT 下的 `python.exe` | PYTHON_EXECUTABLE | EXECUTABLE | `T1` |
| 预检中的 `python312.dll`、`python3.dll`、`vcruntime140.dll` | CPYTHON_CORE_DLL | DLL | `T1` |
| `Lib/` 下、由 SourceFileLoader 装载的模块 | STDLIB_SOURCE | SOURCE | `T1,T3` |
| `DLLs/_hashlib.pyd` | STDLIB_EXTENSION | EXTENSION | `T1,T3` |
| `DLLs/libcrypto-3.dll` | STDLIB_EXTENSION | DLL | `T1,T3` |
| 预检中出现的 System32 DLL | OS_RUNTIME_DLL | DLL | `T1` |
| Harness | HARNESS_SOURCE | SOURCE | `T1` |
| 10 个受测源码 | SUBJECT_SOURCE | SOURCE | `T2,T3` |
| 15 个 Fixture | FIXTURE_INPUT | DATA | `T2` |
| 输入候选 REV6 | SCENARIO_INPUT_BINDING | DATA | `T2` |

- **读取阶段的含义**：标准库模块的 `T1,T3` 表示"允许读取的窗口"，不是逐阶段观察到的事实；预检没有记录每个模块是在哪个阶段导入的。
- **`mapping.py`**：它在 T2 被读取并核对散列，但不被导入。因此它的 `read_phase` 仍按受测源码记为 `T2,T3`，局限中写明"未导入"。
- **`network_capable`**：仅 `WS2_32.dll` 为 `true`（Windows 套接字库），其余为 `false`。这只是分类，不是行为证明。
- **`executable`**：仅 `python.exe` 为 `true`。
- **`typing.io`、`typing.re`**：这两个是 `typing.py` 在运行时登记的伪模块，没有自己的文件，在 `import_contract.modules` 中按 SOURCE 记录，身份归到 `Lib/typing.py`。

## §B1 观察与局限处置

- 每个变体的观察政策，就是输入 REV6 中该变体规则的 `raw_requirement` 与 `fixture_mapping`。V4 新增的 14 个变体，以及 V5 新增变体中未映射的 20 个，都是不映射 Fixture 的原始检查（`SUPPLEMENTARY_RAW_CHECK`）；V5 新增变体中另有 8 个映射到 Fixture，覆盖等级为 `PARTIAL_LIMITED`。
- 覆盖类别为 PARTIAL_LIMITED 或 OBSERVE_ONLY_LIMITED 的场景，其变体的局限处置引用所有者决定 P5-LIMITED（`DSP_004_PHASES_2_TO_5_OWNER_DECISIONS_REV1.json`）；FULL 场景的变体，局限处置为空数组。

## §V1 审查与所有者决定政策

- **审查**：Manifest 与本文件由一个没看过编写过程的全新子代理审查。审查者与记录人属于同一模型家族，所有者已决定暂不做外部审查（P1-EXTREVIEW）。
- **接受**：Manifest 与本文件都需要所有者按确切 SHA 接受。
- **运行**：Manifest 不授予执行权（`execution_grant_in_manifest` 为 false）。正式运行需要所有者另行授权。

## §D1 需要所有者在接受时一并确认的偏离

1. `root_bindings` 只有三个根（§R2，P6-VENV-ROOT）。
2. `runtime_identity.configuration` 为 `NOT_APPLICABLE`（§S1）。
3. 启动程序与监督程序在四个根之外（§R3）。
4. ModuleRecord 的 `caller` 统一归到解释器导入系统（§O1）。
5. 标准库模块的读取阶段是允许窗口，不是逐阶段观察（§C1）。
6. P6-VENV-ROOT 的原文是把 VENV_ROOT "记为不适用"；Manifest 的做法是直接省略这一项，不另设标记（§R2）。
7. Manifest REV3 绑定的 V5 资产尚未被接受，需随本 Manifest 一并接受。这些资产包括：V5 源码、输入 REV6、Harness REV6、约束清单 formal v4，以及配套的安装、监督和收集脚本。
8. 本文件和第 7 项所列资产作为来源被引用时尚未接受，需随本 Manifest 一并接受。ORDERED 来源登记已在 P6-ACCEPT-MANIFEST 中接受，沿用不变。
9. `typing.io`、`typing.re` 两个伪模块的身份归到 `Lib/typing.py`；`__main__` 的身份归到 Harness（§C1）。
10. **导入闭包沿用预检 v2 的观察结果。**
    - 正式运行 v3 已证实，V4 的闭包与预检 v2 相同。
    - V5 只新增了 `hashlib`、`json`、`dataclasses.fields` 三处导入，它们本来就在闭包中，因此预计闭包不变。
    - 正式运行 v4 会逐一核对，不一致即不予验收。
11. **PROJECT_ROOT 的完整性证据是 formal v4 的生成摘要与安装器常量，而不是安装结果。**
    - 原因：安装与运行在同一次启动中完成，生成 Manifest 时还没有安装结果。
    - 安装结果会由收集脚本复算，并随运行结果一并记录。

## §E1 REV1 的审查记录（沿用，供参考）

全新子代理审查（同一模型家族，非外部）的结论：1 个阻断项，3 个非阻断项，6 个注记。
- 阻断项：`capability.py` 中的 dataclass 未列为声明位置。已在生成程序中补上，并重新生成 Manifest。
- 三个非阻断项：已作为上面的第 6 至第 8 项列入。
- 注记处理：第 9 项已列入；`__main__` 的装载符号已改正；生成程序的运行说明已改正。其余注记保留为已知局限，不改动：
  - `python312.zip` 只有源码查找一项；
  - 查找序列中的目录路径；
  - 用 `ntdll.dll` 作为系统装载器的身份；
  - `unresolved_count` 由构造决定（未解析的文件会直接中止生成）。
