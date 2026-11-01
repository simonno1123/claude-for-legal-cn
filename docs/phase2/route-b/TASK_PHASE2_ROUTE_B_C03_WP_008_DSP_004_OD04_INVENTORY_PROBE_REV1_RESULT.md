# DSP-004 OD-04 只读清单探测 REV1 结果

本记录写下按路径 B 签署记录 REV2 授权的那一次只读清单探测运行的结果。结果是候选观察，不是证据准入。OD-04 仍是 `DEFER_WITHOUT_EVIDENCE`。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

授权原句：`改签路径 B：以本机 CPython 3.12.10 为验证机候选，授权一次只读清单探测运行（只读取解释器版本、内置与冻结模块、实际加载模块来源），不接受资产、不生成 Manifest、不正式运行、不关闭 DSP-004。`

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_OD04_INVENTORY_PROBE_REV1_RESULT.json` |
| 运行者 | 所有者本人双击启动器，运行一次 |
| 探测脚本 | `validation/route_b_c03/wp_008/dsp004_od04_inventory_probe_rev1/probe_inventory.py`（4184 字节，`F80157752DB49EF4F7D29FC398B00ADA6FAE23B38C7A1245F59D1E2BCEBF1E4F`） |
| 启动器 | `validation/route_b_c03/wp_008/dsp004_od04_inventory_probe_rev1/run_probe.cmd`（259 字节，`12B6F6884B59DCD66DFB2A80EDF7735DC78B193AA9B8B8C9A245521F4700E861`） |
| 脱敏结果 | `validation/route_b_c03/wp_008/dsp004_od04_inventory_probe_rev1/probe_inventory_result.SANITIZED.json` |
| 原始结果 | 只留在所有者本机，33859 字节，`5EA56E1430770B25BFA9BAD8ED79BF8C1F38D0FD56BB65792967BAD6F25A45DD` |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

运行后取回的脚本和启动器，与提交到仓库的字节完全一致。原始结果里含本机绝对路径，所以仓库只保存脱敏副本：路径改用 `CANDIDATE_RUNTIME_ROOT`、`SYSTEM_ROOT`、`PROBE_DIR`、`USER_PROFILE` 等根令牌。

## 0. 运行边界

- 以 `-I -S -B` 运行：隔离模式，不加载 site，不写字节码。
- 只导入批次 Harness 和受测文件直接导入清单里的标准库模块。没有运行 Harness 或受测代码，没有调用 `identity_gate`，没有执行 Fixture。
- 只写出一个结果文件，并且不允许覆盖已有文件。
- 范围说明：除了原句列出的三项，脚本还对进程已加载的原生模块文件做了只读 SHA。记录人在运行前向所有者说明过这一点略超出列出的三项，所有者随后运行了探测。

## 1. 结果

| 编号 | 所见 |
| --- | --- |
| F01 | 解释器报告 3.12.10（`tags/v3.12.10:0cc8128`，MSC v.1943 64 bit），与 REV19 从 `NEWS.txt` 读到的版本一致 |
| F02 | `isolated`、`no_site`、`ignore_environment`、`no_user_site`、`dont_write_bytecode` 都是 1。`sys.path` 只有运行时的 zip、DLLs、Lib 和运行根 |
| F03 | 从运行根加载了 8 个原生模块，SHA 全部与 REV19 的静态记录相同 |
| F04 | 加载了 22 个系统 DLL，全部只读取得 SHA。这补上了 REV19 缺的系统 DLL 字节，但只限于本次实际加载的这一组。其中 `psapi.dll` 是探测脚本自己枚举模块时加载的 |
| F05 | 主机报告 29 个冻结模块名。已加载模块中有 16 个来自冻结副本，包括 `os`、`stat`、`ntpath`、`codecs`、`io`、`abc`。REV19 的 F07 在本机得到核实：对这些模块，Lib 文件不是实际运行的代码 |
| F06 | 51 个模块从 Lib 源文件加载：49 个在 REV19 导入时闭包里，另外 2 个是按名字加载的编码模块（`encodings/gbk.py`、`encodings/utf_8.py`），现已散列。`gbk` 对应 zh-CN 系统区域的代码页 |
| F07 | `-B` 只阻止写入字节码，不阻止读取。从源文件加载的模块在 Lib `__pycache__` 下有对应缓存，REV19 看到这些缓存写于 2026-10-30T21:03Z。加载器到底用了缓存还是源文件，本次没有记录。检查到使用的防替换仍然缺失 |
| F08 | 以上都是解释器在运行中自我报告的。按验证执行包 V3，进程内自检不能作为初始信任根。T0 和调用方一侧的身份仍然缺失 |

22 个系统 DLL 的字节与 SHA 写在机器记录的 `LoadedSystemDlls`。

## 2. OD-04 六个组成部分，REV19 与本次对照

| 组成部分 | REV19（静态） | 本次探测 |
| --- | --- | --- |
| 导入闭包 | 导入时闭包 68 个文件已散列 | 实际加载集已观察：49 个在闭包内，另有 2 个动态编码模块；缓存与源文件未区分 |
| 两侧调用身份 | 无 | 只有被调用方的自我报告 |
| 检查到使用的防替换 | 无 | 无 |
| T0 | 无 | 无 |
| PE | 44 个文件的身份和导入表 | 已加载的运行时原生模块与静态记录一致 |
| OS | 只有名称 | 本次加载的 22 个系统 DLL 已散列 |

## 3. 本记录故意不做的事

- 不准入运行根，不接受任何 SHA，不改 OD-04。
- 不生成 Manifest，不授权正式运行，不完成 FA-08，不关闭 DSP-004。
- 不在仓库保存含本机路径的原始结果。

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
