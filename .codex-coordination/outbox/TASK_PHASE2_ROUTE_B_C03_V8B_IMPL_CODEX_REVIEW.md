# Codex 评审记录 — V8-B 实现（PR #135）

- 第 1 轮（71ba8dc）：P0 6 项——--h 索引未进入 V8-A 校验；新检查点未先验证延续旧检查点；登记未核对已签 S4 序号（删尾可重放）；签名后未绑定快照（签名期间可换 Q3）；S4 未校验本次使用事件；时间在等待口令前读取。
- 第 2 轮（487d4ea）：P0 1 项——临时文件在可写目录，重命名前可被替换；P1 1 项——max_uses 为空时崩溃。
- 第 3 轮（f722514）：P1 1 项——verify --output 按同名文件取最新登记，未绑定本次 S4。
- 第 4 轮（e34071a）：Didn't find any major issues。
- 测试：V8-B 21 个（CI 要求 ssh-keygen 存在、无跳过；所有者设备上亦通过），V8-A 58 个。

## 安装文件 SHA-256（certutil 比对用；内容与合并提交一致）

| 文件 | SHA-256 |
| --- | --- |
| `v8b.py` | `3F7BA371145D7144B98FCAEBF8A279CD52BCB2169EF81F7058356A94B3D8E832` |
| `gate_cli.py` | `5236957771CEE74CDBE4EE9ACDDD8EF8A19F399254B924340DF975082B2802F5` |
| `gate_records.py` | `97B2BE912A35B84C41AE540D07F60AD998BE9B77F5D1E5AC25FA39E2B141E053` |
| `gate_record_builder.py` | `544DB8857A209D157ECFC19C4326969180AD830C729BB707983694BEFCAB678A` |

- 结论：PASS（Codex 非审核人）。
