# DSP-004 ORDERED 来源登记候选 REV1

所有者回复 `授权`。记录人把它理解为：授权从已准入的运行时环境和已接受的输入中，推导 5 条 ORDERED 路径的顺序来源，做成候选交所有者接受。这不包括授权正式运行。本候选没有审查，也没有接受。DSP-004 保持 `OPEN / HOLD`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_ORDERED_SOURCE_REGISTRY_REV1_CANDIDATE.json` | 14689 | `527F98DD8B4E1B15D22235944A9B6982A311F422B40437BD1F263FF5E8DE0E0E` |

## 1. 已经完整的 3 条

| 政策 | 路径 | 来源 | 结果 |
| --- | --- | --- | --- |
| AP-020 | `manifest_identity.fixture_catalog` | 已接受输入 REV4 中 `$.scenarios[*].fixture` 的数组顺序 | 15 项，C03-TA-V-001 至 015 各一次，顺序正确（已用程序核对） |
| AP-021 | `input_contract.scenarios` | 同一文件中 `$.scenarios[*].scenario_id` 的数组顺序 | 同上 |
| AP-022 | `input_contract.scenarios[].variants` | 同一文件中每个场景的 `stimulus_variants` 顺序 | 共 28 个变体，场景内没有重复 |

## 2. 还要等阶段 7 才能完整的 2 条

- **AP-006（启动序列）**：已列出 4 步：`python.exe`、`python312.dll`、`vcruntime140.dll` 和正式运行用的 Harness。前三步的文件身份取自已绑定的运行时清单。第 4 步要等阶段 7 的 Harness 修订版绑定后才能填。
- **AP-009（导入查找顺序）**：已列出 10 项。第一项是 Harness 的私有导入器，它只提供 10 个已绑定的受测模块。接着是 `-I -S -B` 下的 `sys.path` 四项（第三、四版运行中实际看到的），每一项分源码和扩展两种查找。最后是 DLL 的两处查找位置：程序目录和 System32。第一项的位置要等阶段 7 的部署确定。

## 3. 需要所有者决定的一件事

类型合同要求恰好四个根：`PROJECT_ROOT`、`VENV_ROOT`、`RUNTIME_ROOT`、`SYSTEM_ROOT`。但已准入的环境里**没有虚拟环境**，`VENV_ROOT` 没有对应的目录。生成 Manifest 之前，需要所有者决定怎么处理。

候选中拟定的根目录：
- `PROJECT_ROOT`：`C:\Program Files\DSP004Runtime\project_v1`，在阶段 7 建立；
- `RUNTIME_ROOT`：`C:\Program Files\DSP004Runtime\Python312`；
- `SYSTEM_ROOT`：`C:\Windows\System32`。

DSP-004 保持 `OPEN / HOLD`。
