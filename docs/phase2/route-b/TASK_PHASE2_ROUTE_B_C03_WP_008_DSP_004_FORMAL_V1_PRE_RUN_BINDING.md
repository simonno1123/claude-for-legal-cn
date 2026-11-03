# DSP-004 正式运行 v1 资产：运行前绑定

按所有者决定 P7-PREPARE，阶段 7 的资产已经准备好，并在安装和任何运行之前按确切字节绑定。运行前审查没有发现阻断项。审查者是全新子代理，与记录人属于同一模型家族。没有安装，没有运行，没有接受。DSP-004 保持 `OPEN / HOLD`。

| 机器记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_FORMAL_V1_PRE_RUN_BINDING.json` | 5898 | `A4A847DCFB9ECE832A379E04AE39B4304999BFB50B39B4C967DFE60D6A6F7F54` |

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `harness_rev3.py` | 25485 | `9F93F66FEB39EB102AA8B8EF94D578E532B50D8D6F50BDB6F00F4341DB53DC8E` |
| `supervisor_formal_v1.ps1` | 26211 | `D8AE28B705932894447CBE9B14038E787077E2F203384A61EF8056467FA3101F` |
| `bound_list_formal_v1.json` | 154458 | `1AC8841274FF77C655B5B9D7D2F9B2B86B18B9065E290F50497D1688D47B8D10` |
| `run_formal_v1.cmd` | 411 | `C1CF428D4F95A00C57FB28F01EE9118C081C99EEF3D8ECA02F0C336FDADD9621` |
| `install_formal_v1.ps1` | 10586 | `5203FA575C4DC03848952CC34915A53AF248CFF2ACB06B7356A6670FA424437D` |
| `install_formal_v1.cmd` | 641 | `4E3CB5E37DB0209432AB55385857BCBB12EA828D4033BBB5EA159D6D7884D1C4` |
| `collect_formal_v1.ps1` | 17175 | `E3AECE809CE279DD068E802BD62C61A606DF2FA4098C8D1A6FBCFC7D5539EBF9` |
| `go_formal_v1.cmd` | 1503 | `95AA6D886E82CD82D02EF5DAB8298BBD8517535B7AF5172083652F22FEADDADE` |

## 1. 安装后的布局

- `C:\Program Files\DSP004Runtime\supervisor_formal_v1`：3 个文件。
- `C:\Program Files\DSP004Runtime\project_v1`：27 个文件，按仓库中的相对路径存放。包括 10 个受测文件、15 个 Fixture、输入 REV4 和 Harness REV3。
- 安装后，运行时目录下共 691 个文件；监督程序运行时锁定 713 个文件。

## 2. 审查结果

审查确认了以下几点：
- 所有交叉引用和散列一致；
- Harness REV3 在 Python 3.12.3 和 3.13 上都是 28 个变体全部通过，场景结果和六侧记录与 REV2 完全相同；
- 约 39 KB 的输出能被 PowerShell 5.1 解析；
- 监督程序的各项检查与 Harness 的输出字段对应；
- 运行时拦截用真实调用测试过；
- 目录结构、锁定数量和访问控制的预期与目标布局吻合。

| 编号 | 问题 | 处理 |
| --- | --- | --- |
| MINOR-1 | supervisor read Totals under StrictMode when the harness printed a Stop | fixed: HX_NoStop computed first; other HX checks skipped on a Stop |
| MINOR-2 | harness docstring overclaimed the scan; some input errors exited 3 | fixed: docstring states getattr allowed and module-attribute calls not caught; input conversion errors now Stop (exit 2) |
| MINOR-5/NOTE-1/NOTE-2 | CR-014 prefix check lenient; enum encoding without module; six-side compares harness constants | kept by design (comparison logic unchanged from accepted REV2; limitation already stated) |
| NOTE-3 | collector and installer write next to themselves | run from the owner's staging folder outside the repository; outputs are redacted before commit |
| NOTE-4 | stale v3/v4 comments in collector | partly fixed |
| NOTE-5 | installer drops v3 host-module, run-account and audit checks | compensated by supervisor re-hash and collector |
| NOTE-6 | no staging script; partial write leaves folders | the recorder stages the files through the device bridge and verifies them by read-back |
| NOTE-7 | Windows import set inferred, not observed; expect _bz2.pyd and _lzma.pyd as new native modules (bound) | first observed in the preflight run |

## 3. 后续步骤

1. 所有者运行 `install_formal_v1.cmd`。这一步只安装，不运行任何程序。
2. 做一次预检运行，观察 Windows 上实际的导入闭包。这一步需要所有者授权。
3. 用已接受的合同、输入、Harness、运行时和预检观察到的闭包生成 Manifest，交所有者接受。
4. 正式运行，需要所有者另行授权。

DSP-004 保持 `OPEN / HOLD`。
