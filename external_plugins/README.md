# 外部第三方插件治理政策 (External Vendor Plugins Policy)

为了保障 `claude-for-legal-cn` 默认中国法合规环境的纯净度，所有保留的第三方外部/Vendor插件（如 `cocounsel-legal`）必须遵守以下治理隔离政策：

1. **默认非激活**：外部插件默认不载入核心市场（不登记在 `.claude-plugin/marketplace.json` 中）。
2. **明确法域边界**：外部插件其自身的技能、代理配方和 README 中必须显式标注其法域约束（如：仅供美国法/Westlaw检索）。
3. **禁止静默覆盖**：当用户请求中国 Mainland 法律事务时，系统禁止调用这些外部插件提供未经核验的境外法律结论。
