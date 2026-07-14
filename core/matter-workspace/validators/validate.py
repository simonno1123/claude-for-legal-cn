#!/usr/bin/env python3
"""Offline validator for Matter Workspace schemas, templates, and fixtures."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urldefrag, urljoin


SCHEMA_NAMES = (
    "matter",
    "party",
    "fact",
    "evidence",
    "issue",
    "claim",
    "strategy",
    "decision",
)

TEMPLATE_DECLARATION = re.compile(
    r"^# Template schema:\s+(?P<path>\S+)\s*$", re.MULTILINE
)

SAMPLE_SCHEMA_BY_PARENT = {
    "parties": "party",
    "facts": "fact",
    "evidence": "evidence",
    "issues": "issue",
    "claims": "claim",
    "strategies": "strategy",
    "decisions": "decision",
}

RECORD_SECTION_BY_SCHEMA = {
    "parties": "party",
    "facts": "fact",
    "evidence": "evidence",
    "issues": "issue",
    "claims": "claim",
    "strategies": "strategy",
    "decisions": "decision",
}

DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_TIME_PATTERN = re.compile(
    r"^\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}"
    r"(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})$"
)


class DependencyError(RuntimeError):
    """Raised when an offline validation dependency is unavailable."""


def load_dependencies():
    """Load optional validation libraries without attempting installation."""

    try:
        import yaml
        from jsonschema import Draft202012Validator, FormatChecker
        from referencing import Registry, Resource
    except ModuleNotFoundError as exc:
        raise DependencyError(exc.name or "unknown") from exc
    return yaml, Draft202012Validator, FormatChecker, Registry, Resource


def strict_date(value: object) -> bool:
    """Accept an ISO calendar date and never a date-time."""

    if not isinstance(value, str) or not DATE_PATTERN.fullmatch(value):
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def strict_date_time(value: object) -> bool:
    """Accept RFC 3339 date-time values with an explicit timezone."""

    if not isinstance(value, str) or not DATE_TIME_PATTERN.fullmatch(value):
        return False
    normalized = value.replace("t", "T").replace("z", "Z")
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    try:
        parsed = dt.datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.utcoffset() is not None


def create_format_checker(FormatChecker):
    """Create an isolated checker that overrides permissive default formats."""

    checker = FormatChecker()
    checker.checks("date")(strict_date)
    checker.checks("date-time")(strict_date_time)
    return checker


def json_pointer_lookup(document: object, fragment: str) -> None:
    """Resolve a JSON Pointer fragment or raise ValueError."""

    if not fragment:
        return
    decoded = unquote(fragment)
    if not decoded.startswith("/"):
        raise ValueError(f"unsupported non-pointer fragment #{fragment}")
    current = document
    for raw_part in decoded[1:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict) and part in current:
            current = current[part]
            continue
        if isinstance(current, list) and part.isdigit():
            index = int(part)
            if index < len(current):
                current = current[index]
                continue
        raise ValueError(f"unresolved JSON Pointer #{fragment}")


def iter_schema_refs(value: object):
    """Yield every $ref string in deterministic document order."""

    if isinstance(value, dict):
        for key in sorted(value):
            child = value[key]
            if key == "$ref" and isinstance(child, str):
                yield child
            else:
                yield from iter_schema_refs(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_schema_refs(child)


def error_path(error) -> str:
    """Render a stable instance path for a jsonschema validation error."""

    parts = []
    for item in error.absolute_path:
        if isinstance(item, int):
            parts.append(f"[{item}]")
        else:
            prefix = "." if parts else ""
            parts.append(prefix + str(item))
    return "".join(parts) or "<root>"


class MatterWorkspaceValidator:
    """Validate repository Matter Workspace assets without external I/O."""

    def __init__(self, repo_root: Path, dependencies) -> None:
        (
            self.yaml,
            self.Draft202012Validator,
            self.FormatChecker,
            self.Registry,
            self.Resource,
        ) = dependencies
        self.repo_root = repo_root.resolve()
        self.matter_root = self.repo_root / "core" / "matter-workspace"
        self.schema_dir = self.matter_root / "schema"
        self.template_dir = self.matter_root / "templates"
        self.sample_dir = self.matter_root / "examples" / "sample-matter"
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checked = {
            "sample_entities": 0,
            "sample_record_paths": 0,
            "sample_records": 0,
            "sample_references": 0,
            "schema_refs": 0,
            "schemas": 0,
            "self_tests": 0,
            "templates": 0,
        }
        self.schemas: dict[str, dict] = {}
        self.validators = {}
        self.sample_documents: dict[PurePosixPath, dict] = {}
        self.format_checker = create_format_checker(self.FormatChecker)

    def relative(self, path: Path) -> str:
        """Return a repository-relative display path without leaking host data."""

        try:
            return path.resolve().relative_to(self.repo_root).as_posix()
        except ValueError:
            return path.name

    def add_error(self, location: str, message: str) -> None:
        self.errors.append(f"{location}: {message}")

    def load_yaml(self, path: Path):
        try:
            value = self.yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, self.yaml.YAMLError) as exc:
            self.add_error(self.relative(path), f"YAML parse failed: {exc}")
            return None
        if not isinstance(value, dict):
            self.add_error(self.relative(path), "top-level YAML value must be a mapping")
            return None
        return value

    def load_schemas(self) -> None:
        expected = {f"{name}.yaml" for name in SCHEMA_NAMES}
        found = {path.name for path in self.schema_dir.glob("*.yaml")}
        for name in sorted(expected - found):
            self.add_error("core/matter-workspace/schema", f"missing Schema {name}")
        for name in sorted(found - expected):
            self.add_error("core/matter-workspace/schema", f"unexpected Schema {name}")

        for name in SCHEMA_NAMES:
            path = self.schema_dir / f"{name}.yaml"
            if not path.is_file():
                continue
            schema = self.load_yaml(path)
            if schema is None:
                continue
            try:
                self.Draft202012Validator.check_schema(schema)
            except Exception as exc:  # jsonschema exposes version-specific subclasses
                self.add_error(self.relative(path), f"invalid Draft 2020-12 Schema: {exc}")
                continue
            schema_id = schema.get("$id")
            if not isinstance(schema_id, str) or not schema_id:
                self.add_error(self.relative(path), "missing non-empty $id")
                continue
            if not schema_id.startswith(
                "https://schemas.claude-for-legal-cn.invalid/matter-workspace/v1/"
            ):
                self.add_error(self.relative(path), "unexpected or network-capable $id")
                continue
            self.schemas[name] = schema

        self.checked["schemas"] = len(self.schemas)

    def validate_schema_references(self) -> None:
        by_id = {schema["$id"]: schema for schema in self.schemas.values()}
        for name in SCHEMA_NAMES:
            schema = self.schemas.get(name)
            if schema is None:
                continue
            base_id = schema["$id"]
            for ref in iter_schema_refs(schema):
                self.checked["schema_refs"] += 1
                resolved = urljoin(base_id, ref)
                document_id, fragment = urldefrag(resolved)
                target = by_id.get(document_id)
                if target is None:
                    self.add_error(
                        f"core/matter-workspace/schema/{name}.yaml",
                        f"$ref is not in the offline registry: {ref}",
                    )
                    continue
                try:
                    json_pointer_lookup(target, fragment)
                except ValueError as exc:
                    self.add_error(
                        f"core/matter-workspace/schema/{name}.yaml",
                        f"invalid $ref {ref}: {exc}",
                    )

    def build_validators(self) -> None:
        registry = self.Registry()
        for name in SCHEMA_NAMES:
            schema = self.schemas.get(name)
            if schema is None:
                continue
            try:
                registry = registry.with_resource(
                    schema["$id"], self.Resource.from_contents(schema)
                )
            except Exception as exc:
                self.add_error(
                    f"core/matter-workspace/schema/{name}.yaml",
                    f"offline registry load failed: {exc}",
                )
        for name in SCHEMA_NAMES:
            schema = self.schemas.get(name)
            if schema is None:
                continue
            self.validators[name] = self.Draft202012Validator(
                schema,
                registry=registry,
                format_checker=self.format_checker,
            )

    def validate_instance(self, path: Path, schema_name: str, document: dict) -> None:
        validator = self.validators.get(schema_name)
        if validator is None:
            self.add_error(self.relative(path), f"validator unavailable: {schema_name}")
            return
        errors = sorted(
            validator.iter_errors(document),
            key=lambda item: (tuple(str(part) for part in item.absolute_path), item.message),
        )
        for error in errors:
            self.add_error(
                self.relative(path),
                f"{schema_name} validation failed at {error_path(error)}: {error.message}",
            )

    def declared_template_schema(self, path: Path) -> str | None:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            self.add_error(self.relative(path), f"template read failed: {exc}")
            return None
        declarations = TEMPLATE_DECLARATION.findall(text)
        if len(declarations) != 1:
            self.add_error(
                self.relative(path),
                f"expected one Template schema declaration, found {len(declarations)}",
            )
            return None
        declared = declarations[0]
        declared_path = PurePosixPath(declared)
        if declared_path.is_absolute() or "\\" in declared or declared_path.name == "":
            self.add_error(self.relative(path), "unsafe Template schema declaration")
            return None
        if len(declared_path.parts) < 2 or declared_path.parts[-2] != "schema":
            self.add_error(self.relative(path), "Template schema must name schema/<file>.yaml")
            return None
        schema_name = Path(declared_path.name).stem
        if schema_name not in SCHEMA_NAMES:
            self.add_error(self.relative(path), f"unknown Template schema: {schema_name}")
            return None
        if not (self.schema_dir / f"{schema_name}.yaml").is_file():
            self.add_error(self.relative(path), f"missing Template schema: {schema_name}")
            return None
        return schema_name

    def validate_templates(self) -> None:
        paths = sorted(self.template_dir.rglob("*.yaml"))
        self.checked["templates"] = len(paths)
        if not paths:
            self.add_error("core/matter-workspace/templates", "no templates found")
            return
        for path in paths:
            schema_name = self.declared_template_schema(path)
            document = self.load_yaml(path)
            if schema_name is not None and document is not None:
                self.validate_instance(path, schema_name, document)

    def sample_schema_name(self, relative_path: PurePosixPath) -> str | None:
        if relative_path == PurePosixPath("matter.yaml"):
            return "matter"
        if len(relative_path.parts) != 2:
            return None
        return SAMPLE_SCHEMA_BY_PARENT.get(relative_path.parts[0])

    def load_and_validate_sample(self) -> None:
        paths = sorted(self.sample_dir.rglob("*.yaml"))
        self.checked["sample_records"] = len(paths)
        if not paths:
            self.add_error("core/matter-workspace/examples/sample-matter", "no sample records found")
            return
        for path in paths:
            relative_path = PurePosixPath(path.relative_to(self.sample_dir).as_posix())
            schema_name = self.sample_schema_name(relative_path)
            if schema_name is None:
                self.add_error(
                    self.relative(path), "cannot map sample record to a Core Schema"
                )
                continue
            document = self.load_yaml(path)
            if document is None:
                continue
            self.sample_documents[relative_path] = document
            self.validate_instance(path, schema_name, document)

    def reference_error(self, relative_path: PurePosixPath, message: str) -> None:
        self.add_error(
            f"core/matter-workspace/examples/sample-matter/{relative_path.as_posix()}",
            message,
        )

    def validate_ref_list(
        self,
        relative_path: PurePosixPath,
        label: str,
        values: object,
        valid_ids: set[str],
    ) -> None:
        if not isinstance(values, list):
            return
        for value in values:
            self.checked["sample_references"] += 1
            if not isinstance(value, str) or value not in valid_ids:
                self.reference_error(relative_path, f"unresolved {label}: {value!r}")

    def validate_record_path(self, raw_path: object) -> PurePosixPath | None:
        self.checked["sample_record_paths"] += 1
        if not isinstance(raw_path, str) or not raw_path:
            self.add_error(
                "core/matter-workspace/examples/sample-matter/matter.yaml",
                f"invalid record_files path: {raw_path!r}",
            )
            return None
        path = PurePosixPath(raw_path)
        if path.is_absolute() or ".." in path.parts or "." in path.parts or "\\" in raw_path:
            self.add_error(
                "core/matter-workspace/examples/sample-matter/matter.yaml",
                f"unsafe record_files path: {raw_path}",
            )
            return None
        target = self.sample_dir.joinpath(*path.parts)
        try:
            target.resolve().relative_to(self.sample_dir.resolve())
        except ValueError:
            self.add_error(
                "core/matter-workspace/examples/sample-matter/matter.yaml",
                f"record_files path escapes fixture: {raw_path}",
            )
            return None
        if not target.is_file() or target.is_symlink():
            self.add_error(
                "core/matter-workspace/examples/sample-matter/matter.yaml",
                f"record_files target missing or unsafe: {raw_path}",
            )
            return None
        return path

    def reference_errors(self, documents: dict[PurePosixPath, dict]) -> list[str]:
        saved_errors = self.errors
        saved_checked = self.checked.copy()
        self.errors = []
        self.validate_sample_references(documents)
        result = self.errors
        self.errors = saved_errors
        self.checked = saved_checked
        return result

    def validate_sample_references(self, documents=None) -> None:
        documents = documents if documents is not None else self.sample_documents
        matter_path = PurePosixPath("matter.yaml")
        matter = documents.get(matter_path)
        if not isinstance(matter, dict):
            self.reference_error(matter_path, "root Matter record is missing")
            return

        entity_ids: dict[str, PurePosixPath] = {}
        ids_by_schema = {name: set() for name in SAMPLE_SCHEMA_BY_PARENT.values()}
        for relative_path in sorted(documents, key=lambda item: item.as_posix()):
            if relative_path == matter_path:
                continue
            document = documents[relative_path]
            entity_id = document.get("id")
            if not isinstance(entity_id, str) or not entity_id:
                self.reference_error(relative_path, "entity id is missing")
                continue
            if entity_id in entity_ids:
                self.reference_error(
                    relative_path,
                    f"duplicate entity id {entity_id!r}; first seen in {entity_ids[entity_id]}",
                )
                continue
            entity_ids[entity_id] = relative_path
            schema_name = self.sample_schema_name(relative_path)
            if schema_name in ids_by_schema:
                ids_by_schema[schema_name].add(entity_id)

        self.checked["sample_entities"] = len(entity_ids)
        matter_slug = matter.get("slug")
        for relative_path in sorted(documents, key=lambda item: item.as_posix()):
            if relative_path == matter_path:
                continue
            if documents[relative_path].get("matter_slug") != matter_slug:
                self.reference_error(relative_path, "matter_slug does not match root Matter")

        listed_paths: set[PurePosixPath] = set()
        record_files = matter.get("record_files")
        if not isinstance(record_files, dict):
            self.reference_error(matter_path, "record_files mapping is missing")
        else:
            for section in sorted(record_files):
                expected_schema = RECORD_SECTION_BY_SCHEMA.get(section)
                if expected_schema is None:
                    self.reference_error(matter_path, f"unknown record_files section: {section}")
                    continue
                values = record_files[section]
                if not isinstance(values, list):
                    self.reference_error(matter_path, f"record_files.{section} must be a list")
                    continue
                for raw_path in values:
                    path = self.validate_record_path(raw_path)
                    if path is None:
                        continue
                    if path in listed_paths:
                        self.reference_error(matter_path, f"duplicate record_files path: {path}")
                    listed_paths.add(path)
                    actual_schema = self.sample_schema_name(path)
                    if actual_schema != expected_schema:
                        self.reference_error(
                            matter_path,
                            f"record_files.{section} has wrong record type: {path}",
                        )

        expected_paths = set(documents) - {matter_path}
        for missing in sorted(expected_paths - listed_paths, key=lambda item: item.as_posix()):
            self.reference_error(matter_path, f"entity file omitted from record_files: {missing}")
        for extra in sorted(listed_paths - expected_paths, key=lambda item: item.as_posix()):
            self.reference_error(matter_path, f"record_files target is not a loaded entity: {extra}")

        party_ids = ids_by_schema["party"]
        fact_ids = ids_by_schema["fact"]
        evidence_ids = ids_by_schema["evidence"]
        issue_ids = ids_by_schema["issue"]
        claim_ids = ids_by_schema["claim"]
        strategy_ids = ids_by_schema["strategy"]
        decision_ids = ids_by_schema["decision"]

        participants = matter.get("participants", [])
        if isinstance(participants, list):
            for participant in participants:
                if not isinstance(participant, dict):
                    continue
                self.validate_ref_list(
                    matter_path,
                    "participant.party_id",
                    [participant.get("party_id")],
                    party_ids,
                )
        key_facts = matter.get("key_facts", [])
        if isinstance(key_facts, list):
            for fact in key_facts:
                if not isinstance(fact, dict):
                    continue
                self.validate_ref_list(
                    matter_path, "key_facts.fact_id", [fact.get("fact_id")], fact_ids
                )

        top_level_refs = {
            "party_refs": party_ids,
            "fact_refs": fact_ids,
            "evidence_refs": evidence_ids,
            "issue_refs": issue_ids,
            "claim_refs": claim_ids,
        }
        for relative_path in sorted(documents, key=lambda item: item.as_posix()):
            document = documents[relative_path]
            for label, valid_ids in top_level_refs.items():
                self.validate_ref_list(relative_path, label, document.get(label, []), valid_ids)

            schema_name = self.sample_schema_name(relative_path)
            if schema_name == "evidence":
                source = document.get("source", {})
                holder = source.get("holder_party_id") if isinstance(source, dict) else None
                if holder is not None:
                    self.validate_ref_list(
                        relative_path, "source.holder_party_id", [holder], party_ids
                    )
                original_holder = document.get("original_held_by")
                if original_holder is not None:
                    self.validate_ref_list(
                        relative_path, "original_held_by", [original_holder], party_ids
                    )
            elif schema_name == "issue":
                for position in document.get("positions", []):
                    if not isinstance(position, dict):
                        continue
                    party = position.get("party_ref")
                    if party is not None:
                        self.validate_ref_list(
                            relative_path, "positions.party_ref", [party], party_ids
                        )
                    self.validate_ref_list(
                        relative_path,
                        "positions.supporting_refs",
                        position.get("supporting_refs", []),
                        set(entity_ids),
                    )
            elif schema_name == "claim":
                self.validate_ref_list(
                    relative_path,
                    "claimant_refs",
                    document.get("claimant_refs", []),
                    party_ids,
                )
                self.validate_ref_list(
                    relative_path,
                    "respondent_refs",
                    document.get("respondent_refs", []),
                    party_ids,
                )
                self.validate_ref_list(
                    relative_path,
                    "legal_basis_refs",
                    document.get("legal_basis_refs", []),
                    issue_ids,
                )
                for section in ("elements", "defenses"):
                    for item in document.get(section, []):
                        if not isinstance(item, dict):
                            continue
                        self.validate_ref_list(
                            relative_path,
                            f"{section}.fact_refs",
                            item.get("fact_refs", []),
                            fact_ids,
                        )
                        self.validate_ref_list(
                            relative_path,
                            f"{section}.evidence_refs",
                            item.get("evidence_refs", []),
                            evidence_ids,
                        )
            elif schema_name == "strategy":
                selected = document.get("selected_option_id")
                if selected is not None:
                    option_ids = {
                        item.get("id")
                        for item in document.get("options", [])
                        if isinstance(item, dict) and isinstance(item.get("id"), str)
                    }
                    self.validate_ref_list(
                        relative_path, "selected_option_id", [selected], option_ids
                    )
            elif schema_name == "decision":
                input_refs = document.get("input_refs", {})
                if isinstance(input_refs, dict):
                    for key, valid_ids in (
                        ("facts", fact_ids),
                        ("evidence", evidence_ids),
                        ("issues", issue_ids),
                        ("claims", claim_ids),
                        ("strategies", strategy_ids),
                    ):
                        self.validate_ref_list(
                            relative_path,
                            f"input_refs.{key}",
                            input_refs.get(key, []),
                            valid_ids,
                        )
                supersedes = document.get("supersedes")
                if supersedes is not None:
                    self.validate_ref_list(
                        relative_path, "supersedes", [supersedes], decision_ids
                    )

    def format_matches(self, value: str, format_name: str) -> bool:
        try:
            self.format_checker.check(value, format_name)
        except Exception:
            return False
        return True

    def run_self_tests(self) -> None:
        checks = (
            self.format_matches("2025-12-01", "date"),
            not self.format_matches("2025-12-01", "date-time"),
            self.format_matches("2025-12-01T00:00:00+08:00", "date-time"),
            not self.format_matches("2025-12-01T00:00:00", "date-time"),
        )
        self.checked["self_tests"] += 1
        if not all(checks):
            self.add_error("self-test", "strict date/date-time regression failed")

        fact_path = PurePosixPath("facts/fact-contract-formation.yaml")
        fact = self.sample_documents.get(fact_path)
        fact_validator = self.validators.get("fact")
        self.checked["self_tests"] += 1
        if fact is None or fact_validator is None:
            self.add_error("self-test", "Fact mutation prerequisites unavailable")
        else:
            invalid_fact = copy.deepcopy(fact)
            invalid_fact["status"] = "invalid-status"
            if not list(fact_validator.iter_errors(invalid_fact)):
                self.add_error("self-test", "invalid Fact mutation was not rejected")

        matter_path = PurePosixPath("matter.yaml")
        self.checked["self_tests"] += 1
        if matter_path not in self.sample_documents:
            self.add_error("self-test", "path traversal prerequisites unavailable")
        else:
            mutated = copy.deepcopy(self.sample_documents)
            mutated[matter_path]["record_files"]["parties"].append("../outside.yaml")
            mutation_errors = self.reference_errors(mutated)
            if not any("unsafe record_files path" in item for item in mutation_errors):
                self.add_error("self-test", "path traversal mutation was not rejected")

    def run_negative_test(self) -> None:
        fact_path = PurePosixPath("facts/fact-contract-formation.yaml")
        fact = self.sample_documents.get(fact_path)
        validator = self.validators.get("fact")
        self.checked["self_tests"] += 1
        if fact is None or validator is None:
            self.add_error("negative-test", "Fact mutation prerequisites unavailable")
            return
        invalid_fact = copy.deepcopy(fact)
        invalid_fact["status"] = "invalid-status"
        errors = list(validator.iter_errors(invalid_fact))
        if not errors:
            self.add_error("negative-test", "invalid Fact mutation was not rejected")
            return
        self.add_error(
            "negative-test",
            "intentional invalid Fact mutation rejected",
        )

    def run(self, self_test: bool, negative_test: bool) -> dict:
        self.load_schemas()
        self.validate_schema_references()
        self.build_validators()
        self.validate_templates()
        self.load_and_validate_sample()
        self.validate_sample_references()
        if self_test:
            self.run_self_tests()
        if negative_test:
            self.run_negative_test()
        return self.result()

    def result(self) -> dict:
        errors = sorted(set(self.errors))
        warnings = sorted(set(self.warnings))
        return {
            "checked": {key: self.checked[key] for key in sorted(self.checked)},
            "errors": errors,
            "status": "FAIL" if errors else "PASS",
            "warnings": warnings,
        }


def emit(result: dict, output_format: str) -> None:
    if output_format == "json":
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
        return
    print(result["status"])
    checked = " ".join(f"{key}={value}" for key, value in result["checked"].items())
    if checked:
        print(f"checked {checked}")
    for warning in result.get("warnings", []):
        print(f"warning {warning}")
    for error in result["errors"]:
        print(f"error {error}")


def dependency_failure(name: str) -> dict:
    return {
        "checked": {},
        "errors": [f"missing Python dependency: {name}"],
        "status": "FAIL",
        "warnings": [],
    }


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        dest="output_format",
        help="deterministic output format (default: text)",
    )
    test_group = parser.add_mutually_exclusive_group()
    test_group.add_argument(
        "--self-test",
        action="store_true",
        help="run isolated strict-format, invalid-Schema and path-traversal checks",
    )
    test_group.add_argument(
        "--negative-test",
        action="store_true",
        help="inject one in-memory invalid Fact and return deterministic FAIL",
    )
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        dependencies = load_dependencies()
    except DependencyError as exc:
        result = dependency_failure(str(exc))
        emit(result, args.output_format)
        return 2

    repo_root = Path(__file__).resolve().parents[3]
    validator = MatterWorkspaceValidator(repo_root, dependencies)
    result = validator.run(
        self_test=args.self_test,
        negative_test=args.negative_test,
    )
    emit(result, args.output_format)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
