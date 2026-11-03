# DSP-004 正式运行 v2 资产：运行前绑定

**原因**：预检运行 v1 观察到的导入闭包里有 `urllib` 和 `urllib.parse`。它们是被 `importlib.abc` → `importlib.resources` → `pathlib` 这条链间接带进来的。已接受的类型合同把 `urllib` 列为禁止模块，按跨组规则第 8 条，基于这份闭包生成的 Manifest 会被阻断。

**改动**：
- Harness REV4 = REV3 去掉 `importlib.abc` 和 `importlib.util`，改用 `importlib.machinery.ModuleSpec` 和一个普通的查找/装载对象，比较逻辑和输入不变。
- 其余 v2 文件 = v1 文件，只是路径改为 `supervisor_formal_v2`、`project_v2`、`harness_rev4`、`formal_v2_run_record`。
- v1 保持已安装状态，在 v2 的约束清单中列为先前文件。

**审查**：运行前审查没有发现阻断项。审查者是全新子代理，与记录人属于同一模型家族。审查确认了以下几点：
- 与 v1 相比，只有预期的改动；
- 所有交叉引用一致；
- Harness REV4 在 3.12 和 3.13 上 28 个变体全部通过，结果与 REV3 完全相同；
- 导入闭包是 REV3 的真子集，不含任何禁止模块；
- 安装后应有 721 个文件、743 个锁定文件。

没有安装，没有运行，没有接受。DSP-004 保持 `OPEN / HOLD`。

| 机器记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_FORMAL_V2_PRE_RUN_BINDING.json` | 4306 | `F4DD7AC8BEAEA686F1675589910AB9560C8402498DF46A87F6B33B31EA0E1F9E` |

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `harness_rev4.py` | 25803 | `0B2AC413272D048B75904689C3105B4758A31624356D69FD9CF4B81C622D2394` |
| `supervisor_formal_v2.ps1` | 26269 | `3463EC1E62193F84605ADD3FF8A8D695C6E92905F5BE1F68423765B5A023E1D3` |
| `bound_list_formal_v2.json` | 160152 | `19A1CE8D54AF938F86BF81DFA54AD2DC9719F12E498F0483AC8B0B08D486BF50` |
| `run_formal_v2.cmd` | 411 | `ADFBB01E415C2238568B615F351EA6A4DA0E6BB988FDD0140730EF49D8200770` |
| `install_formal_v2.ps1` | 10586 | `A8FF7D77228AEDF207A5AD4D8059C77BE3F5C21B9B4DEBD07BCE93C6A64E0CA8` |
| `install_formal_v2.cmd` | 641 | `AB9B4928CEFC42A5BFCE68F1BCC26D23051DB6CD8AEC772655A16D5ECE7408DB` |
| `collect_formal_v2.ps1` | 17175 | `8F130258F9D5BD9CC6C14FFE4F1BBE270632B66772145EE3B32296B7C1AF4840` |
| `go_formal_v2.cmd` | 1503 | `C941E07347104BB5B1410E524B10F74846831026841F545D8890BCC87E6C2249` |
