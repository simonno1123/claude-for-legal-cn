#!/usr/bin/env python3
"""Offline validation for the Legal Research Workflow foundation."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path, PurePosixPath


SCHEMA_NAMES = ("research-matter", "research-source", "research-output")


def load_matter_validator_module():
    """Load accepted offline dependencies and format checks."""

    module_name = "matter_workspace_validator_for_legal_research"
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


class LegalResearchValidator:
    """Validate research Schemas, fixtures and Matter/Issue references."""

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
        self.research_root = self.repo_root / "core" / "legal-research"
        self.schema_dir = self.research_root / "schema"
        self.example_dir = self.research_root / "examples"
        self.matter_root = self.repo_root / "core" / "matter-workspace"
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checked = {
            "cross_references": 0,
            "examples": 0,
            "schemas": 0,
            "source_records": 0,
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
                "https://schemas.claude-for-legal-cn.invalid/legal-research/v1/"
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
        paths = [
            (PurePosixPath("research-matter.yaml"), "research-matter"),
            (PurePosixPath("research-output.yaml"), "research-output"),
        ]
        source_paths = sorted((self.example_dir / "sources").glob("*.yaml"))
        if not source_paths:
            self.add_error(self.relative(self.example_dir), "no Research Source fixture")
        for path in source_paths:
            relative = PurePosixPath(path.relative_to(self.example_dir).as_posix())
            paths.append((relative, "research-source"))
        self.checked["source_records"] = len(source_paths)

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
            f"core/legal-research/examples/{relative.as_posix()}",
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

    def validate_cross_references(self) -> None:
        matter_path = self.matter_root / "examples" / "sample-matter" / "matter.yaml"
        matter = self.load_yaml(matter_path)
        issue_dir = self.matter_root / "examples" / "sample-matter" / "issues"
        issues = {}
        for path in sorted(issue_dir.glob("*.yaml")):
            issue = self.load_yaml(path)
            if issue is not None and isinstance(issue.get("id"), str):
                issues[issue["id"]] = issue
        if matter is None:
            return

        research_path = PurePosixPath("research-matter.yaml")
        output_path = PurePosixPath("research-output.yaml")
        research = self.documents.get(research_path)
        output = self.documents.get(output_path)
        if not isinstance(research, dict) or not isinstance(output, dict):
            return

        matter_slug = research.get("matter_slug")
        issue_ref = research.get("issue_ref")
        self.check_equal(research_path, "matter_slug", matter_slug, matter.get("slug"))
        self.checked["cross_references"] += 1
        issue = issues.get(issue_ref)
        if issue is None:
            self.cross_error(research_path, f"unresolved Issue reference: {issue_ref!r}")
        elif issue.get("matter_slug") != matter_slug:
            self.cross_error(research_path, "Issue reference crosses Matter boundary")

        source_documents = {
            relative: document
            for relative, document in self.documents.items()
            if relative.parts and relative.parts[0] == "sources"
        }
        source_ids: dict[str, PurePosixPath] = {}
        for relative, source in source_documents.items():
            source_id = source.get("id")
            self.checked["cross_references"] += 1
            if not isinstance(source_id, str) or not source_id:
                self.cross_error(relative, "source id is missing")
                continue
            if source_id in source_ids:
                self.cross_error(relative, f"duplicate source id: {source_id}")
                continue
            source_ids[source_id] = relative
            self.check_equal(relative, "research_id", source.get("research_id"), research.get("id"))
            self.check_equal(relative, "matter_slug", source.get("matter_slug"), matter_slug)
            self.check_equal(relative, "issue_ref", source.get("issue_ref"), issue_ref)

        self.check_equal(output_path, "research_id", output.get("research_id"), research.get("id"))
        self.check_equal(output_path, "matter_slug", output.get("matter_slug"), matter_slug)
        self.check_equal(output_path, "issue_ref", output.get("issue_ref"), issue_ref)
        referenced_sources = output.get("sources", [])
        if isinstance(referenced_sources, list):
            for source_id in referenced_sources:
                self.checked["cross_references"] += 1
                if source_id not in source_ids:
                    self.cross_error(output_path, f"unresolved source reference: {source_id!r}")

        for section in ("rules", "case_patterns"):
            items = output.get(section, [])
            if not isinstance(items, list):
                continue
            for index, item in enumerate(items):
                if not isinstance(item, dict):
                    continue
                for source_id in item.get("source_refs", []):
                    self.checked["cross_references"] += 1
                    if source_id not in source_ids:
                        self.cross_error(
                            output_path,
                            f"{section}[{index}] has unresolved source reference: "
                            f"{source_id!r}",
                        )

        output_review = output.get("human_review")
        output_review_status = (
            output_review.get("status") if isinstance(output_review, dict) else None
        )
        self.check_equal(
            output_path,
            "review_status",
            output.get("review_status"),
            output_review_status,
        )
        if output.get("review_status") == "approved":
            if not isinstance(output_review, dict) or not output_review.get("reviewer"):
                self.cross_error(output_path, "approved output requires reviewer")
            if not isinstance(output_review, dict) or not output_review.get("reviewed_at"):
                self.cross_error(output_path, "approved output requires reviewed_at")

        research_review = research.get("human_review")
        research_review_status = (
            research_review.get("status") if isinstance(research_review, dict) else None
        )
        if research.get("status") == "approved" and research_review_status != "approved":
            self.cross_error(research_path, "approved Research Matter requires approved human review")
        if research.get("status") == "awaiting_human_review" and research_review_status != "pending":
            self.cross_error(
                research_path,
                "awaiting_human_review requires pending human review",
            )

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
        result = LegalResearchValidator(repo_root).run()
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
