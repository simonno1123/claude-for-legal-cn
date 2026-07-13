"""Generate or validate China-localized MCP configs for first-party modules."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_output(template: dict, module: dict) -> dict:
    servers = copy.deepcopy(template["baseServers"])
    servers.update(copy.deepcopy(module.get("extraServers", {})))

    return {
        "mcpServers": servers,
        "chinaLocalizationNote": (
            "中国版 MCP 配置统一由 scripts/generate-mcp-configs.py 生成。"
            "法律法规和案例能力统一走 legal-data；政府源通常通过本地索引、"
            "人工上传或企业自建采集管道接入；商业源需企业自有授权。"
            f"{module['noteSuffix']}"
        ),
        "recommendedCategories": module["categories"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate module paths and existing .mcp.json files without writing.",
    )
    args = parser.parse_args()

    template = load_json(SCRIPTS_DIR / "mcp-template.json")
    modules = load_json(SCRIPTS_DIR / "mcp-modules.json")["modules"]

    for module in modules:
        target_dir = REPO_ROOT / module["path"]
        if not target_dir.exists():
            raise FileNotFoundError(f"Module path does not exist: {module['path']}")

        target = target_dir / ".mcp.json"
        output = build_output(template, module)

        if args.check:
            if not target.exists():
                raise FileNotFoundError(
                    f"Generated config does not exist: {target.relative_to(REPO_ROOT)}"
                )
            if load_json(target) != output:
                raise ValueError(
                    f"Generated config is stale: {target.relative_to(REPO_ROOT)}"
                )
            print(f"validated {target.relative_to(REPO_ROOT)}")
            continue

        with target.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(output, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        print(f"generated {target.relative_to(REPO_ROOT)}")

    action = "Validated" if args.check else "Generated"
    print(f"\n{action} {len(modules)} .mcp.json files.")


if __name__ == "__main__":
    main()
