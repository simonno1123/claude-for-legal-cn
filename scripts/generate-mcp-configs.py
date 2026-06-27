"""Generate China-localized .mcp.json files for all first-party modules."""

from __future__ import annotations

import copy
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    template = load_json(SCRIPTS_DIR / "mcp-template.json")
    modules = load_json(SCRIPTS_DIR / "mcp-modules.json")["modules"]

    for module in modules:
        servers = copy.deepcopy(template["baseServers"])
        servers.update(copy.deepcopy(module.get("extraServers", {})))

        output = {
            "mcpServers": servers,
            "chinaLocalizationNote": (
                "中国版 MCP 配置统一由 scripts/generate-mcp-configs.py 生成。"
                "法律法规和案例能力统一走 legal-data；政府源通常通过本地索引、"
                "人工上传或企业自建采集管道接入；商业源需企业自有授权。"
                f"{module['noteSuffix']}"
            ),
            "recommendedCategories": module["categories"],
        }

        target_dir = REPO_ROOT / module["path"]
        if not target_dir.exists():
            raise FileNotFoundError(f"Module path does not exist: {module['path']}")

        target = target_dir / ".mcp.json"
        with target.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(output, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        print(f"generated {target.relative_to(REPO_ROOT)}")

    print(f"\nGenerated {len(modules)} .mcp.json files.")


if __name__ == "__main__":
    main()
