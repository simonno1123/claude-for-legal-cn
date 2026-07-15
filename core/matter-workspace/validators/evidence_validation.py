#!/usr/bin/env python3
"""Offline structural validation for Evidence records and templates."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


PROFILES = ("record", "template", "workflow-entry")
EVIDENCE_TEMPLATE_DECLARATION = re.compile(
    r"^# Template schema:\s+\S*schema/evidence\.yaml\s*$", re.MULTILINE
)


def load_core_validator_module():
    """Load the accepted Matter Workspace Validator without package changes."""

    module_name = "matter_workspace_core_validator_for_evidence"
    existing = sys.modules.get(module_name)
    if existing is not None:
        return existing
    path = Path(__file__).with_name("validate.py")
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Matter Workspace Validator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


@dataclass(frozen=True)
class EvidenceValidationResult:
    """Machine-readable result with no legal conclusion or automatic repair."""

    errors: tuple[str, ...]
    warnings: tuple[str, ...]
    reviewer_required: bool

    @property
    def status(self) -> str:
        return "FAIL" if self.errors else "PASS"

    def to_dict(self) -> dict[str, object]:
        return {
            "status": self.status,
            "errors": list(self.errors),
            "warnings": list(self.warnings),
            "reviewer_required": self.reviewer_required,
        }


class EvidenceValidationFramework:
    """Validate Evidence structure, template contracts and workflow entry."""

    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root.resolve()
        self.core = load_core_validator_module()
        self.dependencies = self.core.load_dependencies()
        self.yaml = self.dependencies[0]
        workspace = self.core.MatterWorkspaceValidator(
            self.repo_root,
            self.dependencies,
        )
        workspace.load_schemas()
        workspace.validate_schema_references()
        workspace.build_validators()
        if workspace.errors:
            raise RuntimeError("; ".join(workspace.errors))
        self.evidence_validator = workspace.validators.get("evidence")
        if self.evidence_validator is None:
            raise RuntimeError("Evidence Schema validator is unavailable")
        self.template_root = (
            self.repo_root / "core" / "matter-workspace" / "templates"
        )

    @staticmethod
    def _add(items: list[str], message: str) -> None:
        if message not in items:
            items.append(message)

    def _schema_errors(self, document: dict) -> list[str]:
        errors = sorted(
            self.evidence_validator.iter_errors(document),
            key=lambda item: (
                tuple(str(part) for part in item.absolute_path),
                item.message,
            ),
        )
        return [
            f"schema.{self.core.error_path(error)}: {error.message}"
            for error in errors
        ]

    @staticmethod
    def _reviewer_required(document: dict) -> bool:
        review = document.get("human_review")
        return not isinstance(review, dict) or review.get("status") != "approved"

    def _validate_review_state(
        self,
        document: dict,
        errors: list[str],
    ) -> None:
        review = document.get("human_review")
        if not isinstance(review, dict):
            return
        status = review.get("status")
        reviewer = review.get("reviewer")
        reviewed_at = review.get("reviewed_at")
        if status in {"approved", "rejected"}:
            if not reviewer:
                self._add(errors, f"human_review.{status} requires reviewer")
            if not reviewed_at:
                self._add(errors, f"human_review.{status} requires reviewed_at")
        if status == "pending" and reviewed_at is not None:
            self._add(errors, "human_review.pending cannot have reviewed_at")
        if document.get("status") == "verified" and status != "approved":
            self._add(errors, "verified Evidence requires approved human_review")

    def _validate_relationships(
        self,
        document: dict,
        errors: list[str],
    ) -> None:
        for ref_field, relationship_field in (
            ("fact_refs", "fact_relationships"),
            ("issue_refs", "issue_relationships"),
        ):
            refs = document.get(ref_field)
            valid_refs = set(refs) if isinstance(refs, list) else set()
            relationships = document.get(relationship_field, [])
            if not isinstance(relationships, list):
                continue
            for index, relationship in enumerate(relationships):
                if not isinstance(relationship, dict):
                    continue
                target = relationship.get("target_id")
                if isinstance(target, str) and target not in valid_refs:
                    self._add(
                        errors,
                        f"{relationship_field}[{index}].target_id is not in "
                        f"{ref_field}: {target}",
                    )

    def _template_requirement(
        self,
        strict: bool,
        errors: list[str],
        warnings: list[str],
        message: str,
    ) -> None:
        self._add(errors if strict else warnings, message)

    def _validate_template(
        self,
        document: dict,
        errors: list[str],
        warnings: list[str],
    ) -> None:
        module_fields = document.get("module_fields")
        if not isinstance(module_fields, dict) or module_fields.get("template") is not True:
            self._add(errors, "template requires module_fields.template=true")
            return
        strict = bool(module_fields.get("domain"))
        if document.get("classification") is None:
            self._template_requirement(
                strict,
                errors,
                warnings,
                "template classification is missing",
            )
        review = document.get("human_review")
        if not isinstance(review, dict) or review.get("required") is not True:
            self._template_requirement(
                strict,
                errors,
                warnings,
                "template requires a Human Review Gate",
            )
        elif review.get("status") != "pending":
            self._template_requirement(
                strict,
                errors,
                warnings,
                "template Human Review Gate must start pending",
            )

        for ref_field, relationship_field in (
            ("fact_refs", "fact_relationships"),
            ("issue_refs", "issue_relationships"),
        ):
            refs = document.get(ref_field)
            relationships = document.get(relationship_field)
            if not refs:
                self._template_requirement(
                    strict,
                    errors,
                    warnings,
                    f"template requires at least one {ref_field} entry",
                )
                continue
            if not relationships:
                self._template_requirement(
                    strict,
                    errors,
                    warnings,
                    f"template requires at least one {relationship_field} entry",
                )
                continue
            targets = {
                item.get("target_id")
                for item in relationships
                if isinstance(item, dict) and isinstance(item.get("target_id"), str)
            }
            missing = sorted(set(refs) - targets)
            if missing:
                self._template_requirement(
                    strict,
                    errors,
                    warnings,
                    f"template has unmapped {ref_field}: {missing}",
                )

    def _validate_workflow_entry(
        self,
        document: dict,
        errors: list[str],
        warnings: list[str],
    ) -> None:
        if document.get("status") != "received":
            self._add(errors, "workflow entry requires Evidence status=received")
        review = document.get("human_review")
        if not isinstance(review, dict) or review.get("required") is not True:
            self._add(errors, "workflow entry requires a Human Review Gate")
        elif review.get("status") != "pending":
            self._add(errors, "workflow entry Human Review Gate must be pending")
        if document.get("classification") is None:
            self._add(
                warnings,
                "classification is pending and must be resolved at Classification stage",
            )
        acquisition = document.get("acquisition")
        if isinstance(acquisition, dict) and acquisition.get("lawfulness") == "unlawful":
            self._add(errors, "unlawfully acquired Evidence cannot enter workflow")

    def validate_document(
        self,
        document: object,
        profile: str = "record",
    ) -> EvidenceValidationResult:
        if profile not in PROFILES:
            raise ValueError(f"unsupported validation profile: {profile}")
        if not isinstance(document, dict):
            return EvidenceValidationResult(
                errors=("Evidence document must be a mapping",),
                warnings=(),
                reviewer_required=True,
            )

        errors = self._schema_errors(document)
        warnings: list[str] = []
        self._validate_review_state(document, errors)
        self._validate_relationships(document, errors)
        if profile == "template":
            self._validate_template(document, errors, warnings)
        elif profile == "workflow-entry":
            self._validate_workflow_entry(document, errors, warnings)
        return EvidenceValidationResult(
            errors=tuple(errors),
            warnings=tuple(warnings),
            reviewer_required=self._reviewer_required(document),
        )

    def _display_path(self, path: Path) -> str:
        try:
            return path.resolve().relative_to(self.repo_root).as_posix()
        except ValueError:
            return path.name

    def validate_file(
        self,
        path: Path,
        profile: str = "record",
    ) -> EvidenceValidationResult:
        try:
            document = self.yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, self.yaml.YAMLError) as exc:
            return EvidenceValidationResult(
                errors=(f"YAML read failed: {exc}",),
                warnings=(),
                reviewer_required=True,
            )
        return self.validate_document(document, profile=profile)

    def validate_files(
        self,
        paths: list[Path],
        profile: str,
    ) -> EvidenceValidationResult:
        errors: list[str] = []
        warnings: list[str] = []
        reviewer_required = False
        for path in sorted(paths, key=lambda item: item.as_posix()):
            label = self._display_path(path)
            result = self.validate_file(path, profile=profile)
            errors.extend(f"{label}: {message}" for message in result.errors)
            warnings.extend(f"{label}: {message}" for message in result.warnings)
            reviewer_required = reviewer_required or result.reviewer_required
        return EvidenceValidationResult(
            errors=tuple(errors),
            warnings=tuple(warnings),
            reviewer_required=reviewer_required,
        )

    def discover_evidence_templates(self) -> list[Path]:
        paths = []
        for path in sorted(self.template_root.rglob("*.yaml")):
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                continue
            if EVIDENCE_TEMPLATE_DECLARATION.search(text):
                paths.append(path)
        return paths


def render_text(result: EvidenceValidationResult) -> str:
    lines = [
        result.status,
        f"reviewer_required={str(result.reviewer_required).lower()}",
    ]
    lines.extend(f"warning {message}" for message in result.warnings)
    lines.extend(f"error {message}" for message in result.errors)
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--profile", choices=PROFILES, default="record")
    parser.add_argument("--templates", action="store_true")
    parser.add_argument("--format", choices=("json", "text"), default="text")
    args = parser.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[3]
    try:
        framework = EvidenceValidationFramework(repo_root)
    except Exception as exc:
        payload = EvidenceValidationResult(
            errors=(f"framework initialization failed: {exc}",),
            warnings=(),
            reviewer_required=True,
        )
        print(
            json.dumps(payload.to_dict(), ensure_ascii=False, sort_keys=True)
            if args.format == "json"
            else render_text(payload)
        )
        return 2

    if args.templates:
        if args.paths:
            parser.error("--templates cannot be combined with paths")
        paths = framework.discover_evidence_templates()
        profile = "template"
    else:
        if not args.paths:
            parser.error("provide at least one Evidence YAML path or --templates")
        paths = [path.resolve() for path in args.paths]
        profile = args.profile

    result = framework.validate_files(paths, profile=profile)
    if args.format == "json":
        print(json.dumps(result.to_dict(), ensure_ascii=False, sort_keys=True))
    else:
        print(render_text(result))
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
