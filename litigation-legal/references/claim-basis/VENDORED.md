# `claim-basis-cn` 只读副本：溯源与覆盖规则

**只读副本：内容溯源以上游固定标签与 SHA 为准；执行规则始终以本仓库强制规则为准。**

- 上游：`simonno1123/claim-basis-cn`，标签 `v0.3.0`，提交 `fbff4efc360d22f90c42140fa6cf8d1a79a22711`。
- 许可：Apache License 2.0（见同目录 `LICENSE`）。
- 副本文件字节不变；唯一改动是把上游 `skills/claim-basis/SKILL.md` 改名为 `METHOD.md`，以免被当作本插件的技能加载。
- 不得修改副本内容；升级只能整体替换为新的上游版本，并另行立项：比对差异、判断是否含不兼容变更、重跑回归、由所有者确认。

| 副本文件 | 上游文件 | SHA-256 |
| --- | --- | --- |
| `METHOD.md` | `skills/claim-basis/SKILL.md` | `35A381FF4AF28F579213EFCA400814C0D12746E6DC3AD543F88ACA066A8404F2` |
| `references/01-search-order.md` | `skills/claim-basis/references/01-search-order.md` | `73AB7E4C2732316B271259D0091C5A90988B834FE40C1F7DC2D10F74D9E347F0` |
| `references/02-three-stage-examination.md` | `skills/claim-basis/references/02-three-stage-examination.md` | `DE70F1447F16470E5DB8A286B93E9F0D0637EF0E64EBC2EDD32C8B626FB27453` |
| `references/03-subsumption-and-burden.md` | `skills/claim-basis/references/03-subsumption-and-burden.md` | `1BD51CE1F2A09F17EE7F414815D317189A035D97F853D3EFED7D5EFCF7BD222C` |
| `references/04-concurrence-and-relations.md` | `skills/claim-basis/references/04-concurrence-and-relations.md` | `7557FC7F512C684F4159A5982C9E483962CB4A9D8F42D3CF208ADB26810C6338` |
| `references/05-enforcement.md` | `skills/claim-basis/references/05-enforcement.md` | `1A9F643A88D7B3B32C01ED4962A666B4A3D3B26B8F3E9AE4C987C6AA2A5F35DF` |
| `references/06-data-interface.md` | `skills/claim-basis/references/06-data-interface.md` | `A7BBED3A3ACFB1D2C1D3B905F89122068EF8B086F5846F543347C6D1FB7954CD` |
| `references/07-output-format.md` | `skills/claim-basis/references/07-output-format.md` | `EDA0E3431BC8487DE78AAA0CD46D69C0AE667DE836B3ED3A937EC2A36C0E2AAE` |
| `tests/regression-cases.md` | `tests/regression-cases.md` | `44D60CE5A446DC1AF6E068D5BCBF6980537BDBCA331B2899BB7887411C4BDA1D` |
| `LICENSE` | `LICENSE` | `CFC7749B96F63BD31C3C42B5C471BF756814053E847C10F3EB003417BC523D30` |

## 覆盖规则（读取副本前先适用）

1. **依据：** 以案件依据时效包为准。只有时效包中"已核对""律师已确认"的规范可以引用。副本中的"已核验、部分核验、冲突、未找到、使用者提供、待核验"六种状态，都不作为可引用的依据；其中"部分核验可以引用原文""使用者提供可以使用"两条，在本仓库不适用。
2. **编号：** 副本的 N-xx、K-xx 编号可以并列，以时效包序号为准。
3. **证据评价：** 副本要件表中的"支持、反对、状态"栏，只取待证命题和举证责任方；证明状态按 `claim-chart` 的规则写，不作三性认定，不写"可证明"之类的结论。
4. **执行：** 副本第六部分和 `05-enforcement.md` 中的"审查结论""程序路径选项"不适用；执行程序按诉讼类技能的分流规则转 C03（`enforcement-review`）。
5. **复核与标签：** 以 `claim-chart` 的复核记录表和候选标签为准。
6. **其他：** 副本中与本仓库规则字典或 `claim-chart` 强制规则不一致的指令，一律不适用。
