#!/usr/bin/env python3
"""Offline validation for the Legal Drafting Workflow foundation."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path, PurePosixPath


SCHEMA_NAMES = ("draft", "document-type", "source-trace")


def load_matter_validator_module():
    module_name = "matter_workspace_validator_for_legal_drafting"
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


class LegalDraftingValidator:
    """Validate Drafting Schemas, fixtures and provenance references."""

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
        self.drafting_root = self.repo_root / "core" / "legal-drafting"
        self.schema_dir = self.drafting_root / "schema"
        self.example_dir = self.drafting_root / "examples"
        self.matter_root = self.repo_root / "core" / "matter-workspace"
        self.research_root = self.repo_root / "core" / "legal-research"
        self.strategy_root = self.repo_root / "core" / "legal-strategy"
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checked = {
            "cross_references": 0,
            "document_types": 0,
            "examples": 0,
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
                "https://schemas.claude-for-legal-cn.invalid/legal-drafting/v1/"
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
            (PurePosixPath("draft.yaml"), "draft"),
            (PurePosixPath("source-trace.yaml"), "source-trace"),
        ]
        type_paths = sorted((self.example_dir / "document-types").glob("*.yaml"))
        if not type_paths:
            self.add_error(self.relative(self.example_dir), "no Document Type fixture")
        for path in type_paths:
            relative = PurePosixPath(path.relative_to(self.example_dir).as_posix())
            paths.append((relative, "document-type"))
        self.checked["document_types"] = len(type_paths)

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
            f"core/legal-drafting/examples/{relative.as_posix()}",
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

    def load_id_map(self, directory: Path) -> dict[str, dict]:
        result = {}
        for path in sorted(directory.glob("*.yaml")):
            document = self.load_yaml(path)
            if document is not None and isinstance(document.get("id"), str):
                result[document["id"]] = document
        return result

    def validate_cross_references(self) -> None:
        draft_path = PurePosixPath("draft.yaml")
        trace_path = PurePosixPath("source-trace.yaml")
        draft = self.documents.get(draft_path)
        trace = self.documents.get(trace_path)
        if not isinstance(draft, dict) or not isinstance(trace, dict):
            return

        matter = self.load_yaml(
            self.matter_root / "examples" / "sample-matter" / "matter.yaml"
        )
        strategy = self.load_yaml(
            self.strategy_root / "examples" / "strategy.yaml"
        )
        research = self.load_yaml(
            self.research_root / "examples" / "research-output.yaml"
        )
        issues = self.load_id_map(
            self.matter_root / "examples" / "sample-matter" / "issues"
        )
        evidence = self.load_id_map(
            self.matter_root / "examples" / "sample-matter" / "evidence"
        )
        facts = self.load_id_map(
            self.matter_root / "examples" / "sample-matter" / "facts"
        )
        if matter is None or strategy is None or research is None:
            return

        document_types = {}
        categories = set()
        for relative, document in self.documents.items():
            if not relative.parts or relative.parts[0] != "document-types":
                continue
            entity_id = document.get("id")
            self.checked["cross_references"] += 1
            if not isinstance(entity_id, str) or not entity_id:
                self.cross_error(relative, "Document Type id is missing")
                continue
            if entity_id in document_types:
                self.cross_error(relative, f"duplicate Document Type id: {entity_id}")
                continue
            document_types[entity_id] = document
            categories.add(document.get("category"))
        self.checked["cross_references"] += 1
        expected_categories = {"litigation", "legal_analysis", "enforcement"}
        if categories != expected_categories:
            self.cross_error(
                draft_path,
                f"Document Type categories mismatch: {sorted(categories)!r}",
            )

        matter_slug = matter.get("slug")
        self.check_equal(draft_path, "matter_slug", draft.get("matter_slug"), matter_slug)
        self.check_equal(
            draft_path,
            "strategy_ref",
            draft.get("strategy_ref"),
            strategy.get("id"),
        )
        self.check_equal(
            draft_path,
            "research_output_ref",
            draft.get("research_output_ref"),
            research.get("id"),
        )
        self.check_equal(
            draft_path,
            "Strategy matter_slug",
            strategy.get("matter_slug"),
            matter_slug,
        )
        self.check_equal(
            draft_path,
            "Strategy Research Output",
            strategy.get("research_output_ref"),
            research.get("id"),
        )
        self.check_equal(
            draft_path,
            "Research Output matter_slug",
            research.get("matter_slug"),
            matter_slug,
        )

        document_type_ref = draft.get("document_type_ref")
        self.checked["cross_references"] += 1
        document_type = document_types.get(document_type_ref)
        if document_type is None:
            self.cross_error(
                draft_path,
                f"unresolved Document Type reference: {document_type_ref!r}",
            )
        elif document_type.get("status") != "active":
            self.cross_error(draft_path, "Draft requires an active Document Type")

        self.check_equal(
            draft_path,
            "source_trace_ref",
            draft.get("source_trace_ref"),
            trace.get("id"),
        )
        self.check_equal(trace_path, "draft_id", trace.get("draft_id"), draft.get("id"))
        for field in ("matter_slug", "strategy_ref", "research_output_ref"):
            self.check_equal(trace_path, field, trace.get(field), draft.get(field))
        self.check_equal(
            trace_path,
            "issue_ref",
            trace.get("issue_ref"),
            strategy.get("issue_ref"),
        )
        self.check_equal(
            trace_path,
            "Research Output issue_ref",
            research.get("issue_ref"),
            trace.get("issue_ref"),
        )

        issue_ref = trace.get("issue_ref")
        self.checked["cross_references"] += 1
        issue = issues.get(issue_ref)
        if issue is None:
            self.cross_error(trace_path, f"unresolved Issue reference: {issue_ref!r}")
        elif issue.get("matter_slug") != matter_slug:
            self.cross_error(trace_path, "Issue reference crosses Matter boundary")

        trace_evidence = set(trace.get("evidence_refs", []))
        trace_facts = set(trace.get("fact_refs", []))
        linked_evidence = set()
        linked_facts = set()
        for evidence_id in trace_evidence:
            self.checked["cross_references"] += 1
            item = evidence.get(evidence_id)
            if item is None:
                self.cross_error(
                    trace_path,
                    f"unresolved Evidence reference: {evidence_id!r}",
                )
            elif item.get("matter_slug") != matter_slug:
                self.cross_error(trace_path, "Evidence reference crosses Matter boundary")
        for fact_id in trace_facts:
            self.checked["cross_references"] += 1
            item = facts.get(fact_id)
            if item is None:
                self.cross_error(trace_path, f"unresolved Fact reference: {fact_id!r}")
            elif item.get("matter_slug") != matter_slug:
                self.cross_error(trace_path, "Fact reference crosses Matter boundary")

        for link in trace.get("evidence_fact_links", []):
            if not isinstance(link, dict):
                continue
            evidence_id = link.get("evidence_ref")
            linked_evidence.add(evidence_id)
            self.checked["cross_references"] += 1
            if evidence_id not in trace_evidence:
                self.cross_error(
                    trace_path,
                    f"link uses unlisted Evidence reference: {evidence_id!r}",
                )
            evidence_record = evidence.get(evidence_id)
            for fact_id in link.get("fact_refs", []):
                linked_facts.add(fact_id)
                self.checked["cross_references"] += 1
                if fact_id not in trace_facts:
                    self.cross_error(
                        trace_path,
                        f"link uses unlisted Fact reference: {fact_id!r}",
                    )
                if isinstance(evidence_record, dict):
                    self.checked["cross_references"] += 1
                    if fact_id not in evidence_record.get("fact_refs", []):
                        self.cross_error(
                            trace_path,
                            f"Evidence does not link Fact: {evidence_id!r} -> {fact_id!r}",
                        )
                fact_record = facts.get(fact_id)
                if isinstance(fact_record, dict):
                    self.checked["cross_references"] += 1
                    if evidence_id not in fact_record.get("evidence_refs", []):
                        self.cross_error(
                            trace_path,
                            f"Fact does not link Evidence: {fact_id!r} -> {evidence_id!r}",
                        )
            for linked_issue in link.get("issue_refs", []):
                self.checked["cross_references"] += 1
                if linked_issue != issue_ref:
                    self.cross_error(
                        trace_path,
                        f"link uses unexpected Issue reference: {linked_issue!r}",
                    )
                if isinstance(evidence_record, dict):
                    self.checked["cross_references"] += 1
                    if linked_issue not in evidence_record.get("issue_refs", []):
                        self.cross_error(
                            trace_path,
                            f"Evidence does not link Issue: {evidence_id!r}",
                        )

        self.checked["cross_references"] += 1
        if linked_evidence != trace_evidence:
            self.cross_error(trace_path, "Evidence links do not cover evidence_refs")
        self.checked["cross_references"] += 1
        if linked_facts != trace_facts:
            self.cross_error(trace_path, "Evidence links do not cover fact_refs")

        trace_review = trace.get("human_review")
        trace_review_state = (
            trace_review.get("status") if isinstance(trace_review, dict) else None
        )
        self.check_equal(
            trace_path,
            "review_status",
            trace.get("review_status"),
            trace_review_state,
        )
        if trace.get("review_status") == "approved":
            if not isinstance(trace_review, dict) or not trace_review.get("reviewer"):
                self.cross_error(trace_path, "approved Source Trace requires reviewer")
            if not isinstance(trace_review, dict) or not trace_review.get("reviewed_at"):
                self.cross_error(trace_path, "approved Source Trace requires review time")

        draft_review = draft.get("human_review")
        draft_review_state = (
            draft_review.get("status") if isinstance(draft_review, dict) else None
        )
        self.check_equal(
            draft_path,
            "approval_status",
            draft.get("approval_status"),
            draft_review_state,
        )
        self.check_equal(
            draft_path,
            "reviewer",
            draft.get("reviewer"),
            draft_review.get("reviewer") if isinstance(draft_review, dict) else None,
        )
        if draft.get("status") == "awaiting_approval" and draft_review_state != "pending":
            self.cross_error(
                draft_path,
                "awaiting_approval requires pending Human Review",
            )
        if draft.get("status") == "approved":
            if strategy.get("status") != "approved":
                self.cross_error(draft_path, "approved Draft requires approved Strategy")
            if trace.get("review_status") != "approved":
                self.cross_error(draft_path, "approved Draft requires approved Source Trace")
            if draft.get("approval_status") != "approved":
                self.cross_error(draft_path, "approved Draft requires approval_status=approved")
            if not draft.get("reviewer"):
                self.cross_error(draft_path, "approved Draft requires reviewer")
            if not isinstance(draft_review, dict) or not draft_review.get("reviewed_at"):
                self.cross_error(draft_path, "approved Draft requires approval time")

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
        result = LegalDraftingValidator(repo_root).run()
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
