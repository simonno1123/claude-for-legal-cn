# V8-B 安装与使用（所有者本人操作）

本说明对应设计 `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_V8B_INTEGRITY_DESIGN.md` R3（不启用 B2）。以下每一步都由所有者本人在自己的终端里完成，记录人不参与。

**终端：** 一律用普通的"命令提示符"（开始菜单输入 `cmd`），不要以管理员身份运行，也不要用 PowerShell。PowerShell 不认 `%USERPROFILE%`、`set`、`<` 等写法，会把文件建到错误的位置；以管理员身份建立的文件，日后用普通窗口可能读写不了。提示符前面带 `PS` 的就是 PowerShell，输入 `cmd` 回车即可切换。用户名含空格的，路径必须加双引号；下文新增的命令都已加上。

## 一、准备

1. **检查 OpenSSH 版本。** 运行 `ssh-keygen -Y sign`。
   - 显示用法说明（包含 `-Y`），或者显示 `Too few arguments for sign: missing namespace`，都说明支持 `-Y`，可以继续；
   - 显示 `unknown option -- Y`，说明系统自带的 OpenSSH 太旧，需要先升级 Windows 的 OpenSSH 客户端。
2. **建信任文件夹。** 运行 `mkdir "%USERPROFILE%\c03-trust"`。**不要**在 Claude 桌面应用里把它添加为连接文件夹。
3. **生成签名密钥。** 用户目录下没有 `.ssh` 文件夹的，ssh-keygen 会报 `No such file or directory`，所以先建文件夹（已有的会提示"已经存在"，不影响）。然后按提示设口令，输入时屏幕不显示字符：

   ```
   mkdir "%USERPROFILE%\.ssh"
   ssh-keygen -t ed25519 -C REVIEWER-01 -f "%USERPROFILE%\.ssh\c03_reviewer"
   ```

   成功时显示 `Your identification has been saved in ...` 和密钥指纹，请记下指纹。

4. **写入公钥清单。** 信任文件夹中的 `allowed_signers` 只能有一行：

   ```
   REVIEWER-01 namespaces="c03-gate" <c03_reviewer.pub 文件的全部内容>
   ```

   先用 `type "%USERPROFILE%\.ssh\c03_reviewer.pub"` 显示公钥，再把下面命令中尖括号部分换成显示的内容，整行输入。重定向写在行首，是为了避免行尾的 `01` 被当作输出句柄吞掉；`>` 会覆盖原有内容，不会叠加：

   ```
   > "%USERPROFILE%\c03-trust\allowed_signers" echo REVIEWER-01 namespaces="c03-gate" <c03_reviewer.pub 的全部内容>
   ```

   写完用 `type "%USERPROFILE%\c03-trust\allowed_signers"` 检查：必须只有一行，并以 `REVIEWER-01` 结尾，后面没有多余内容。

## 二、安装程序副本

1. 在信任文件夹中建目录：`mkdir "%USERPROFILE%\c03-trust\v8b\phase2_runtime\route_b_c03"`。
2. 把下表 4 个文件复制进去。来源二选一：
   - 记录人放在私有目录 `_tools\v8b_install\` 的副本；
   - 从 GitHub 主分支网页逐个下载原始文件。不要用 git 克隆后的文件，Windows 上可能被改成 CRLF 换行，哈希就对不上。
3. 新建两个空文件：`v8b\phase2_runtime\__init__.py` 和 `v8b\phase2_runtime\route_b_c03\__init__.py`。可以用命令 `type nul > __init__.py` 创建。
4. 进入该目录，一次算出各文件的哈希，与下表逐个比对。**任何一个不一致，都不要使用。**

   ```
   cd /d "%USERPROFILE%\c03-trust\v8b\phase2_runtime\route_b_c03"
   for %f in (*.py) do @(echo %f & certutil -hashfile "%f" SHA256 | findstr /r "^[0-9a-f ]*$")
   ```

   certutil 不能对 0 字节的文件计算哈希，对 `__init__.py` 会报 `ERROR_FILE_INVALID`，这不是错误。两个 `__init__.py` 改用 `dir __init__.py ..\__init__.py` 检查，都显示 0 字节即可。

| 文件 | SHA-256 |
| --- | --- |
| `v8b.py` | 见合并 PR 的评审记录（`.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_V8B_IMPL_CODEX_REVIEW.md`） |
| `gate_cli.py` | 同上 |
| `gate_records.py` | 同上 |
| `gate_record_builder.py` | 同上 |
| 两个空的 `__init__.py` | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |

以后升级，同样重新比对、重新复制。仓库或连接文件夹里的新版本，不会自动影响信任文件夹中的副本。

## 二之一、安装确认

1. **密钥与公钥清单是否配套。** 签名时提示输入口令；输错会报 `incorrect passphrase`，重试即可：

   ```
   set T=%USERPROFILE%\c03-trust
   > "%T%\keytest.txt" echo test
   ssh-keygen -Y sign -f "%USERPROFILE%\.ssh\c03_reviewer" -n c03-gate "%T%\keytest.txt"
   ssh-keygen -Y verify -f "%T%\allowed_signers" -I REVIEWER-01 -n c03-gate -s "%T%\keytest.txt.sig" < "%T%\keytest.txt"
   ```

   最后一条应显示 `Good "c03-gate" signature for REVIEWER-01`，指纹与生成密钥时一致。之后可用 `del "%T%\keytest.txt" "%T%\keytest.txt.sig"` 删去测试文件。

2. **程序能否运行：**

   ```
   python -I -S -B "%T%\v8b\phase2_runtime\route_b_c03\v8b.py" recover --trust "%T%"
   ```

   应显示 `"result": "ORPHANS"` 和空列表。提示找不到 `python` 或弹出 Microsoft Store 的，需要先安装 Python。

## 三、使用

先设两个变量（每次打开终端都要设一次）：

```
set T=%USERPROFILE%\c03-trust
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
