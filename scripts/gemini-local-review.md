# 本地 Gemini 审查脚本使用说明

这个脚本用于在本机终端直接调用 Gemini API，绕开 Codex MCP 环境中可能出现的网络、地区或工具权限限制。

## 1. 准备 API Key

推荐使用环境变量：

```powershell
$env:GEMINI_API_KEY="你的 Gemini API Key"
```

也可以把 API Key 放在仓库外的个人密钥文件中，再由脚本读取。不要把 API Key、`.env`、`*.key`、`review-packets/` 或 `review-results/` 提交到仓库。

## 2. 进入项目根目录

```powershell
cd <你的本地仓库路径>\claude-for-legal-cn
```

## 3. 只生成审查包，手动粘贴给 Gemini

```powershell
python scripts\gemini_local_review.py --module ip-legal --dry-run
```

生成的审查包会写入：

```text
review-packets/
```

## 4. 直接调用 Gemini API

```powershell
python scripts\gemini_local_review.py --module ip-legal --model gemini-3.5-flash
```

审查结果会写入：

```text
review-results/
```

## 5. 常用模块审查顺序

```powershell
python scripts\gemini_local_review.py --module ai-governance-legal --model gemini-3.5-flash
python scripts\gemini_local_review.py --module ip-legal --model gemini-3.5-flash
python scripts\gemini_local_review.py --module regulatory-legal --model gemini-3.5-flash
```

如果模型名不可用，请替换为你账号控制台中已开通的 Gemini 模型名称。
