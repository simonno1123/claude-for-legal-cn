# V8-B 安装与使用（所有者本人操作）

本说明对应设计 `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_V8B_INTEGRITY_DESIGN.md` R3（不启用 B2）。以下每一步都由所有者本人在自己的终端（Windows 的"命令提示符"）里完成，记录人不参与。

## 一、准备

1. **检查 OpenSSH 版本。** 运行 `ssh-keygen -Y sign`。
   - 显示用法说明（包含 `-Y`），可以继续；
   - 显示 `unknown option -- Y`，说明系统自带的 OpenSSH 太旧，需要先升级 Windows 的 OpenSSH 客户端。
2. **建信任文件夹。** 例如 `C:\Users\<您>\c03-trust`。**不要**在 Claude 桌面应用里把它添加为连接文件夹。
3. **生成签名密钥。** 运行下面的命令，按提示设口令：

   ```
   ssh-keygen -t ed25519 -C REVIEWER-01 -f %USERPROFILE%\.ssh\c03_reviewer
   ```

4. **写入公钥清单。** 在信任文件夹中新建 `allowed_signers`，只写一行：

   ```
   REVIEWER-01 namespaces="c03-gate" <这里粘贴 c03_reviewer.pub 文件的全部内容>
   ```

## 二、安装程序副本

1. 在信任文件夹中建目录 `v8b\phase2_runtime\route_b_c03\`。
2. 把下表 4 个文件复制进去。来源二选一：
   - 记录人放在私有目录 `_tools\v8b_install\` 的副本；
   - 从 GitHub 主分支网页逐个下载原始文件。不要用 git 克隆后的文件，Windows 上可能被改成 CRLF 换行，哈希就对不上。
3. 新建两个空文件：`v8b\phase2_runtime\__init__.py` 和 `v8b\phase2_runtime\route_b_c03\__init__.py`。可以用命令 `type nul > __init__.py` 创建。
4. 对每个文件运行 `certutil -hashfile <文件> SHA256`，与下表逐个比对。**任何一个不一致，都不要使用。**

| 文件 | SHA-256 |
| --- | --- |
| `v8b.py` | 见合并 PR 的评审记录（`.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_V8B_IMPL_CODEX_REVIEW.md`） |
| `gate_cli.py` | 同上 |
| `gate_records.py` | 同上 |
| `gate_record_builder.py` | 同上 |
| 两个空的 `__init__.py` | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |

以后升级，同样重新比对、重新复制。仓库或连接文件夹里的新版本，不会自动影响信任文件夹中的副本。

## 三、使用

先设两个变量（每次打开终端都要设一次）：

```
set T=C:\Users\<您>\c03-trust
set P=python -I -S -B %T%\v8b\phase2_runtime\route_b_c03\v8b.py
```

| 时点 | 命令 |
| --- | --- |
| R 形成后 | `%P% sign <复核文件夹> --stage S1 --trust %T% --key %USERPROFILE%\.ssh\c03_reviewer --h <案件停点索引>` |
| （仅 L2）P 形成后，且距 S1 满 24 小时 | 同上，`--stage S2` |
| AUTH 形成后 | 同上，`--stage S3` |
| Q3 形成后，使用 | `%P% use <复核文件夹> --candidate <候选文件> --dest <归档目录> --trust %T% --key %USERPROFILE%\.ssh\c03_reviewer --h <案件停点索引>` |
| 随时核对 | `%P% verify <复核文件夹> --trust %T% --h <案件停点索引> [--output <已发布文件>]` |
| 叫停或撤回 | `%P% withdraw --case <案件代号> --reason <理由> --trust %T%` |
| 中断之后 | `%P% recover --trust %T%` 查看未完成的使用；核对之后用 `--resolve <序号> --as committed` 或 `--as aborted` 登记结果 |

- 每条签名命令会提示输入口令。请先看清终端上的检查结果，再输入口令。
- `--h` 每个阶段都要指向**同一份**停点索引。
- 运行中途中断后，信任文件夹里可能留下 `registry.lock`。先确认没有命令仍在运行，再手工删除它。

## 四、局限

- 一人集中：您本人可以改动信任文件夹，V8-B 不防这一点。
- 时间以您本机时钟为准，不是第三方时间（未启用 B2）。
- 发布目录如果在记录人可写的位置，发布之后的改动无法阻止，只能用 `verify --output` 事后发现。
- 记录人 S3 之后登记、S4 之前删除的停点，以及从未登记的停点，检查点发现不了。
- 无法验证对话中实际作答的模型。
