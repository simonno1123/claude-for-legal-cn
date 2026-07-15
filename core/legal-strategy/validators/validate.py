#!/usr/bin/env python3
"""Offline validation for the Legal Strategy Workflow foundation."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path, PurePosixPath


SCHEMA_NAMES = ("strategy", "strategy-option", "risk-assessment")


def load_matter_validator_module():
    module_name = "matter_workspace_validator_for_legal_strategy"
    existing = sys.modules.get(module_name)
    if existing is not None:
        return existing
    path = (
        Path(__file__).resolve().parents[2]
        / "matter-workspace"
        / "validators"
        / "validate.py"
    )
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Matter Workspace Validator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


class LegalStrategyValidator:
    """Validate Strategy Schemas, fixtures and upstream Core references."""

    def __init__(self, repo_root: Path, dependencies=None) -> None:
        self.repo_root = repo_root.resolve()
        self.core = load_matter_validator_module()
        self.dependencies = dependencies or self.core.load_dependencies()
        (
            self.yaml,
            self.Draft202012Validator,
            self.FormatChecker,
            self.Registry,
            self.Resource,
        ) = self.dependencies
        self.strategy_root = self.repo_root / "core" / "legal-strategy"
        self.schema_dir = self.strategy_root / "schema"
        self.example_dir = self.strategy_root / "examples"
        self.matter_root = self.repo_root / "core" / "matter-workspace"
        self.research_root = self.repo_root / "core" / "legal-research"
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checked = {
            "cross_references": 0,
            "examples": 0,
            "option_records": 0,
            "risk_records": 0,
            "schemas": 0,
        }
        self.schemas: dict[str, dict] = {}
        self.validators = {}
        self.documents: dict[PurePosixPath, dict] = {}

    def relative(self, path: Path) -> str:
        try:
            return path.resolve().relative_to(self.repo_root).as_posix()
        except ValueError:
            return path.name

    def add_error(self, location: str, message: str) -> None:
        self.errors.append(f"{location}: {message}")

    def load_yaml(self, path: Path):
        try:
            document = self.yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, self.yaml.YAMLError) as exc:
            self.add_error(self.relative(path), f"YAML parse failed: {exc}")
            return None
        if not isinstance(document, dict):
            self.add_error(self.relative(path), "top-level YAML value must be a mapping")
            return None
        return document

    def load_schemas(self) -> None:
        matter_path = self.matter_root / "schema" / "matter.yaml"
        matter_schema = self.load_yaml(matter_path)
        if matter_schema is not None:
            self.schemas["matter"] = matter_schema

        expected = {f"{name}.yaml" for name in SCHEMA_NAMES}
        found = {path.name for path in self.schema_dir.glob("*.yaml")}
        for name in sorted(expected - found):
            self.add_error(self.relative(self.schema_dir), f"missing Schema {name}")
        for name in sorted(found - expected):
            self.add_error(self.relative(self.schema_dir), f"unexpected Schema {name}")

        for name in SCHEMA_NAMES:
            path = self.schema_dir / f"{name}.yaml"
            if not path.is_file():
                continue
            schema = self.load_yaml(path)
            if schema is None:
                continue
            try:
                self.Draft202012Validator.check_schema(schema)
            except Exception as exc:
                self.add_error(
                    self.relative(path),
                    f"invalid Draft 2020-12 Schema: {exc}",
                )
                continue
            schema_id = schema.get("$id")
            if not isinstance(schema_id, str) or not schema_id.startswith(
                "https://schemas.claude-for-legal-cn.invalid/legal-strategy/v1/"
            ):
                self.add_error(self.relative(path), "unexpected or missing $id")
                continue
            self.schemas[name] = schema
        self.checked["schemas"] = sum(
            1 for name in SCHEMA_NAMES if name in self.schemas
        )

    def build_validators(self) -> None:
        registry = self.Registry()
        for name, schema in self.schemas.items():
            schema_id = schema.get("$id")
            if not isinstance(schema_id, str):
                continue
            try:
                registry = registry.with_resource(
                    schema_id,
                    self.Resource.from_contents(schema),
                )
            except Exception as exc:
                self.add_error(
                    f"core schema {name}",
                    f"offline registry load failed: {exc}",
                )
        checker = self.core.create_format_checker(self.FormatChecker)
        for name in SCHEMA_NAMES:
            schema = self.schemas.get(name)
            if schema is None:
                continue
            self.validators[name] = self.Draft202012Validator(
                schema,
                registry=registry,
                format_checker=checker,
            )

    def validate_instance(self, path: Path, schema_name: str, document: dict) -> None:
        validator = self.validators.get(schema_name)
        if validator is None:
            self.add_error(self.relative(path), f"validator unavailable: {schema_name}")
            return
        errors = sorted(
            validator.iter_errors(document),
            key=lambda item: (
                tuple(str(part) for part in item.absolute_path),
                item.message,
            ),
        )
        for error in errors:
            self.add_error(
                self.relative(path),
                f"{schema_name} validation failed at "
                f"{self.core.error_path(error)}: {error.message}",
            )

    def load_examples(self) -> None:
        paths = [(PurePosixPath("strategy.yaml"), "strategy")]
        option_paths = sorted((self.example_dir / "options").glob("*.yaml"))
        risk_paths = sorted((self.example_dir / "risks").glob("*.yaml"))
        if not option_paths:
            self.add_error(self.relative(self.example_dir), "no Strategy Option fixture")
        if not risk_paths:
            self.add_error(self.relative(self.example_dir), "no Risk fixture")
        for path in option_paths:
            relative = PurePosixPath(path.relative_to(self.example_dir).as_posix())
            paths.append((relative, "strategy-option"))
        for path in risk_paths:
            relative = PurePosixPath(path.relative_to(self.example_dir).as_posix())
            paths.append((relative, "risk-assessment"))
        self.checked["option_records"] = len(option_paths)
        self.checked["risk_records"] = len(risk_paths)

        for relative, schema_name in paths:
            path = self.example_dir.joinpath(*relative.parts)
            if not path.is_file():
                self.add_error(self.relative(path), "fixture is missing")
                continue
            document = self.load_yaml(path)
            if document is None:
                continue
            self.documents[relative] = document
            self.validate_instance(path, schema_name, document)
        self.checked["examples"] = len(self.documents)

    def cross_error(self, relative: PurePosixPath, message: str) -> None:
        self.add_error(
            f"core/legal-strategy/examples/{relative.as_posix()}",
            message,
        )

    def check_equal(
        self,
        relative: PurePosixPath,
        field: str,
        actual: object,
        expected: object,
    ) -> None:
        self.checked["cross_references"] += 1
        if actual != expected:
            self.cross_error(
                relative,
                f"{field} mismatch; expected {expected!r}, found {actual!r}",
            )

    def collect_ids(self, prefix: str) -> dict[str, PurePosixPath]:
        result = {}
        for relative, document in self.documents.items():
            if not relative.parts or relative.parts[0] != prefix:
                continue
            entity_id = document.get("id")
            self.checked["cross_references"] += 1
            if not isinstance(entity_id, str) or not entity_id:
                self.cross_error(relative, "entity id is missing")
                continue
            if entity_id in result:
                self.cross_error(relative, f"duplicate entity id: {entity_id}")
                continue
            result[entity_id] = relative
        return result

    def validate_cross_references(self) -> None:
        matter = self.load_yaml(
            self.matter_root / "examples" / "sample-matter" / "matter.yaml"
        )
        issues = {}
        issue_dir = self.matter_root / "examples" / "sample-matter" / "issues"
        for path in sorted(issue_dir.glob("*.yaml")):
            issue = self.load_yaml(path)
            if issue is not None and isinstance(issue.get("id"), str):
                issues[issue["id"]] = issue
        evidence_ids = set()
        evidence_dir = self.matter_root / "examples" / "sample-matter" / "evidence"
        for path in sorted(evidence_dir.glob("*.yaml")):
            evidence = self.load_yaml(path)
            if evidence is not None and isinstance(evidence.get("id"), str):
                evidence_ids.add(evidence["id"])

        research_output = self.load_yaml(
            self.research_root / "examples" / "research-output.yaml"
        )
        research_source_ids = set()
        source_dir = self.research_root / "examples" / "sources"
        for path in sorted(source_dir.glob("*.yaml")):
            source = self.load_yaml(path)
            if source is not None and isinstance(source.get("id"), str):
                research_source_ids.add(source["id"])

        strategy_path = PurePosixPath("strategy.yaml")
        strategy = self.documents.get(strategy_path)
        if matter is None or research_output is None or not isinstance(strategy, dict):
            return
        matter_slug = strategy.get("matter_slug")
        issue_ref = strategy.get("issue_ref")
        self.check_equal(strategy_path, "matter_slug", matter_slug, matter.get("slug"))
        self.checked["cross_references"] += 1
        issue = issues.get(issue_ref)
        if issue is None:
            self.cross_error(strategy_path, f"unresolved Issue reference: {issue_ref!r}")
        elif issue.get("matter_slug") != matter_slug:
            self.cross_error(strategy_path, "Issue reference crosses Matter boundary")

        self.check_equal(
            strategy_path,
            "research_output_ref",
            strategy.get("research_output_ref"),
            research_output.get("id"),
        )
        self.check_equal(
            strategy_path,
            "Research Output matter_slug",
            research_output.get("matter_slug"),
            matter_slug,
        )
        self.check_equal(
            strategy_path,
            "Research Output issue_ref",
            research_output.get("issue_ref"),
            issue_ref,
        )

        option_ids = self.collect_ids("options")
        risk_ids = self.collect_ids("risks")
        strategy_id = strategy.get("id")
        for relative, document in self.documents.items():
            if relative.parts and relative.parts[0] in {"options", "risks"}:
                self.check_equal(relative, "strategy_id", document.get("strategy_id"), strategy_id)
                self.check_equal(relative, "matter_slug", document.get("matter_slug"), matter_slug)
                self.check_equal(relative, "issue_ref", document.get("issue_ref"), issue_ref)

        for option_id in strategy.get("option_refs", []):
            self.checked["cross_references"] += 1
            if option_id not in option_ids:
                self.cross_error(strategy_path, f"unresolved option reference: {option_id!r}")
        for risk_id in strategy.get("risk_refs", []):
            self.checked["cross_references"] += 1
            if risk_id not in risk_ids:
                self.cross_error(strategy_path, f"unresolved risk reference: {risk_id!r}")

        for relative, option in self.documents.items():
            if not relative.parts or relative.parts[0] != "options":
                continue
            for risk_id in option.get("risk_refs", []):
                self.checked["cross_references"] += 1
                if risk_id not in risk_ids:
                    self.cross_error(relative, f"unresolved risk reference: {risk_id!r}")

        for relative, risk in self.documents.items():
            if not relative.parts or relative.parts[0] != "risks":
                continue
            for evidence_id in risk.get("evidence_refs", []):
                self.checked["cross_references"] += 1
                if evidence_id not in evidence_ids:
                    self.cross_error(relative, f"unresolved Evidence reference: {evidence_id!r}")
            for source_id in risk.get("research_source_refs", []):
                self.checked["cross_references"] += 1
                if source_id not in research_source_ids:
                    self.cross_error(
                        relative,
                        f"unresolved Research Source reference: {source_id!r}",
                    )

        recommendation = strategy.get("recommendation")
        selected = (
            recommendation.get("selected_option_ref")
            if isinstance(recommendation, dict)
            else None
        )
        if selected is not None:
            self.checked["cross_references"] += 1
            if selected not in option_ids:
                self.cross_error(strategy_path, f"unresolved selected option: {selected!r}")

        approval = strategy.get("human_approval")
        approval_state = approval.get("status") if isinstance(approval, dict) else None
        self.check_equal(
            strategy_path,
            "approval_status",
            strategy.get("approval_status"),
            approval_state,
        )
        if strategy.get("status") == "awaiting_human_approval" and approval_state != "pending":
            self.cross_error(
                strategy_path,
                "awaiting_human_approval requires pending Human Approval",
            )
        if strategy.get("status") == "approved":
            if strategy.get("approval_status") != "approved":
                self.cross_error(strategy_path, "approved Strategy requires approval_status=approved")
            if selected is None:
                self.cross_error(strategy_path, "approved Strategy requires selected option")
            if not isinstance(recommendation, dict) or not recommendation.get("rationale"):
                self.cross_error(strategy_path, "approved Strategy requires rationale")
            if not isinstance(recommendation, dict) or not recommendation.get("decision_owner"):
                self.cross_error(strategy_path, "approved Strategy requires decision owner")
            if not isinstance(approval, dict) or not approval.get("reviewer"):
                self.cross_error(strategy_path, "approved Strategy requires approving reviewer")
            if not isinstance(approval, dict) or not approval.get("reviewed_at"):
                self.cross_error(strategy_path, "approved Strategy requires approval time")

    def run(self) -> dict[str, object]:
        self.load_schemas()
        self.build_validators()
        self.load_examples()
        self.validate_cross_references()
        return {
            "status": "FAIL" if self.errors else "PASS",
            "checked": dict(sorted(self.checked.items())),
            "errors": self.errors,
            "warnings": self.warnings,
        }


def render_text(result: dict[str, object]) -> str:
    lines = [str(result["status"])]
    checked = result.get("checked", {})
    if isinstance(checked, dict):
        lines.append(
            "checked " + " ".join(f"{key}={checked[key]}" for key in sorted(checked))
        )
    lines.extend(f"warning {item}" for item in result.get("warnings", []))
    lines.extend(f"error {item}" for item in result.get("errors", []))
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("json", "text"), default="text")
    args = parser.parse_args(argv)
    repo_root = Path(__file__).resolve().parents[3]
    try:
        result = LegalStrategyValidator(repo_root).run()
    except Exception as exc:
        result = {
            "status": "FAIL",
            "checked": {},
            "errors": [f"validator initialization failed: {exc}"],
            "warnings": [],
        }
        exit_code = 2
    else:
        exit_code = 0 if result["status"] == "PASS" else 1
    print(
        json.dumps(result, ensure_ascii=False, sort_keys=True)
        if args.format == "json"
        else render_text(result)
    )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
