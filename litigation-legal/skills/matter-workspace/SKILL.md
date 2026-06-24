---
name: matter-workspace
description: >
  中国案件工作区管理。创建、切换、列示、归档案件材料目录，隔离不同案件上下文。
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

## 强制规则

- 工作区只管理文件和上下文，不替代 `matter-intake` 的收案/立案审查。
- 不跨案件读取材料，除非用户明确要求并确认不存在保密/利益冲突问题。

## 子命令

- `new <slug>`：创建案件目录。
- `list`：列出案件工作区。
- `switch <slug>`：切换当前案件。
- `close <slug>`：归档案件工作区；正式结案仍应运行 `matter-close`。
- `none`：退出当前案件上下文。

## 目录结构

```text
matters/
  [slug]/
    matter.md
    history.md
    evidence/
    pleadings/
    preservation/
    hearing/
    enforcement/
```

## `matter.md` 模板

```markdown
# 案件：[名称]

**Slug:** [slug]
**当事人：**
**程序路径：** 诉讼/仲裁/执行/监管
**法院/仲裁委：**
**阶段：**
**关键期限：**

## 案情摘要

## 诉请/抗辩

## 证据目录

## 保全/执行

## 外部律师
```
