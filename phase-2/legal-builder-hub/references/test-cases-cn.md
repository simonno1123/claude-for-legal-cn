# Legal Builder Hub 回归测试用例

| Case | 场景 | 预期输出 |
|---|---|---|
| 1 | 外部技能含 `ATTORNEY WORK PRODUCT` 默认头 | P0，要求替换为中国“内部法律分析初稿/保密文件”且不得承诺证据特权 |
| 2 | `.mcp.json` 写入真实 API Key | P0，禁止安装，要求改为环境变量占位 |
| 3 | 技能 README 写中国法，SKILL 仍用美国法 | P1，要求文件级一致性修复 |
| 4 | 技能无测试用例 | P1，要求补 `references/test-cases-cn.md` |
| 5 | JSON 不可解析 | P0，禁止进入 Marketplace |
| 6 | Phase 2 实验技能试图加入 Phase 1 默认清单 | P1，要求保持隔离 |

