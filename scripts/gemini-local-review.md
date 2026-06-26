# 本机 Gemini 审查脚本使用说明

这个脚本用于绕开 Codex 的 `gemini-review` MCP 外发限制，由你自己的 Windows 终端直接调用 Gemini API。

## 1. 准备 API Key

默认读取：

```text
C:\Users\Administrator\Desktop\gemini_api.md
```

也可以用环境变量：

```powershell
$env:GEMINI_API_KEY="你的 Gemini API Key"
```

不要把 API Key 放进仓库。`.gitignore` 已排除 `gemini_api.md`、`.env`、`*.key`、`review-packets/` 和 `review-results/`。

## 2. 进入项目根目录

```powershell
cd C:\Users\Administrator\Documents\Codex\2026-06-19\ni\work\claude-for-legal-cn
```

## 3. 只生成审查包，手动粘贴给 Gemini

```powershell
python scripts\gemini_local_review.py --module ip-legal --dry-run
```

生成的文件在：

```text
review-packets/
```

## 4. 直接调用 Gemini API

```powershell
python scripts\gemini_local_review.py --module ip-legal --model gemini-3.5-flash
```

结果会写入：

```text
review-results/
```

## 5. 后续模块建议顺序

```powershell
python scripts\gemini_local_review.py --module ai-governance-legal --model gemini-3.5-flash
python scripts\gemini_local_review.py --module ip-legal --model gemini-3.5-flash
python scripts\gemini_local_review.py --module regulatory-legal --model gemini-3.5-flash
```

如果模型名报错，把 `--model gemini-3.5-flash` 换成你账号控制台里可用的模型名。
