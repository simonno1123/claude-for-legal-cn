# 快速入门

**60 秒上手。** 按以下步骤安装并开始使用插件。

## 在 Claude Cowork 中安装

1. [下载 Claude Desktop](https://claude.com/download)
2. 获取 Claude Cowork 访问权限
3. 按照以下视频中的指示操作：

https://github.com/user-attachments/assets/51394f0a-5277-4fe2-b81c-5c5e9ac876b5

## 在 Claude Code 中安装

1. **打开 Claude Code**（在终端中）或 **Claude Cowork**（桌面应用）。不确定用的是哪个？如果你看到的是带 Claude 的终端窗口，那就是 Claude Code。

2. **添加插件市场。** 在 Claude Code 中输入 `/plugin marketplace add `（末尾带空格），然后**将解压后的 `claude-for-legal-cn` 文件夹拖到终端窗口中** — 它会自动填入路径。按回车确认。

   （或直接输入完整路径：`/plugin marketplace add /Users/你的用户名/Desktop/claude-for-legal-cn`）

3. **安装插件。** 从下表中选择适合你工作的插件，然后执行：
   ```
   /plugin install privacy-legal@claude-for-legal-cn
   ```

4. **⚠️ 重启 Claude Code。** 关闭并重新打开。此步骤不可跳过 — 插件在重启后才会生效。

5. **运行初始配置。** 快速模式约 2 分钟，完整模式约 10-15 分钟。
   ```
   /privacy-legal:cold-start-interview
   ```

6. **连接法律研究工具。** 未连接研究工具时，所有引用将被标记为未验证。在 Cowork 中：设置 → 连接器 → 添加法律数据库（如北大法宝）。在 Claude Code 中：插件已在配置中列出研究工具 MCP，首次使用时会提示你授权。

## 安装为用户级而非项目级

运行 `/plugin install` 时，可能会被问到是仅为当前项目安装还是为所有项目安装（用户级）。**请选择用户级。**

原因：项目级安装会阻止插件读取项目文件夹外的文件 — 你放在"下载"中的合同文件、"文档"中的协议、云盘中的案卷都将无法访问。用户级安装不会给予插件额外的文件访问权限 — 插件只能读取你明确指向的文件或当前目录中的文件。它只是意味着插件可以在任何文件夹中工作。

如果已经安装了项目级并想切换：`/plugin uninstall <插件名>`，然后从主目录执行 `/plugin install <插件名>@claude-for-legal-cn`。

## 哪个插件适合我？

| 你的角色 | 安装… | 首条命令 |
|---|---|---|
| 数据合规/个人信息保护律师 | `privacy-legal` | `/privacy-legal:use-case-triage` |
| 商事合同律师/法务 | `commercial-legal` | `/commercial-legal:review` |
| 公司法/公司治理律师 | `corporate-legal` | `/corporate-legal:governance-audit` |
| 劳动法律师/人力资源法务 | `employment-legal` | `/employment-legal:wage-hour-qa` |
| 产品法务 | `product-legal` | `/product-legal:is-this-a-problem` |
| 知识产权律师/专利代理师 | `ip-legal` | `/ip-legal:clearance` |
| 诉讼律师（企业内部或律所） | `litigation-legal` | `/litigation-legal:matter-intake` |
| 监管合规律师 | `regulatory-legal` | `/regulatory-legal:reg-feed-watcher` |
| AI 治理负责人 | `ai-governance-legal` | `/ai-governance-legal:use-case-triage` |
| 法律诊所指导教师（Phase 2） | `legal-clinic` | `/legal-clinic:cold-start-interview` |
| 法学院学生（Phase 2） | `law-student` | `/law-student:cold-start-interview` |
| 法律科技/寻找扩展技能 | `legal-builder-hub` | `/legal-builder-hub:registry-browser` |

## 安装的内容

每个插件通过初始配置问卷了解你的工作方式，将信息写入实践档案文件（`~/.claude/plugins/config/claude-for-legal/<插件名>/CLAUDE.md`），后续所有技能都会读取该档案。实践档案属于你 — 可以直接编辑、重新运行配置、或让技能自动更新。

**所有输出均为初稿，供执业律师审阅。** 插件会标注不确定的内容、按来源标记引用、并在执行不可逆操作前设置审批门禁。律师负责审阅、验证并承担专业责任。插件使审阅更快，但不能替代律师审阅。

## 插件包含的内容

10 个默认第一序列插件、2 个 Phase 2 教育/公益模块、5 个托管代理 cookbook，以及统一中国法律数据层和若干占位连接器。完整参考见 [README.md](README.md)。

## 遇到问题？

- **安装后提示"命令未找到"** → 你跳过了第 4 步。请重启 Claude Code。
- **提示"请先运行配置"** → 在使用其他命令前先运行 `/<插件名>:cold-start-interview`。
- **引用被标记为 `[待查证]`** → 请连接法律研究工具（第 6 步）。未连接时，所有引用来自训练数据而非实时数据库。
- **提示"无法读取[文件]"** → 通常是因为插件安装为项目级，而文件在项目文件夹之外。参见上方"安装为用户级而非项目级" — 重新安装为用户级或将文件移入项目文件夹。
- **插件没有某项功能** → 运行 `/legal-builder-hub:related-skills-surfacer` 寻找更匹配的技能，或查看插件 README 的"本插件不做的事"部分。
