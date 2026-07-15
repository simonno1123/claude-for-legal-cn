#!/usr/bin/env python3
"""Tests for the offline Evidence Validation Framework."""

from __future__ import annotations

import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK_PATH = (
    REPO_ROOT
    / "core"
    / "matter-workspace"
    / "validators"
    / "evidence_validation.py"
)


def load_framework_module():
    spec = importlib.util.spec_from_file_location(
        "matter_workspace_evidence_validation",
        FRAMEWORK_PATH,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Evidence Validation Framework")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


FRAMEWORK = load_framework_module()


class EvidenceValidationFrameworkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.temp_root = Path(self.temporary.name)
        source = REPO_ROOT / "core" / "matter-workspace"
        target = self.temp_root / "core" / "matter-workspace"
        target.mkdir(parents=True)
        for name in ("schema", "templates"):
            shutil.copytree(source / name, target / name)
        self.framework = FRAMEWORK.EvidenceValidationFramework(self.temp_root)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def load_template(self, relative_path: str):
        path = self.framework.template_root / relative_path
        return path, self.framework.yaml.safe_load(path.read_text(encoding="utf-8"))

    def domain_template_paths(self) -> list[Path]:
        paths = []
        for path in self.framework.discover_evidence_templates():
            document = self.framework.yaml.safe_load(path.read_text(encoding="utf-8"))
            module_fields = document.get("module_fields", {})
            if isinstance(module_fields, dict) and module_fields.get("domain"):
                paths.append(path)
        return paths

    def test_result_model_has_required_fields(self) -> None:
        path, _ = self.load_template("civil-litigation/contract-formation.yaml")
        result = self.framework.validate_file(path, profile="template")
        self.assertEqual(
            {"status", "errors", "warnings", "reviewer_required"},
            set(result.to_dict()),
        )

    def test_all_domain_templates_pass_strict_validation(self) -> None:
        paths = self.domain_template_paths()
        self.assertEqual(18, len(paths))
        for path in paths:
            with self.subTest(path=path.name):
                result = self.framework.validate_file(path, profile="template")
                self.assertEqual("PASS", result.status, result.errors)
                self.assertEqual((), result.warnings)
                self.assertTrue(result.reviewer_required)

    def test_all_evidence_templates_use_reusable_validation(self) -> None:
        paths = self.framework.discover_evidence_templates()
        self.assertGreaterEqual(len(paths), 19)
        result = self.framework.validate_files(paths, profile="template")
        self.assertEqual("PASS", result.status, result.errors)
        self.assertTrue(result.warnings)
        self.assertTrue(result.reviewer_required)

    def test_dangling_fact_relationship_fails(self) -> None:
        _, document = self.load_template("civil-litigation/contract-formation.yaml")
        document["fact_relationships"][0]["target_id"] = "fact-not-referenced"
        result = self.framework.validate_document(document, profile="template")
        self.assertEqual("FAIL", result.status)
        self.assertTrue(
            any("target_id is not in fact_refs" in error for error in result.errors)
        )

    def test_verified_evidence_requires_approved_review(self) -> None:
        _, document = self.load_template("civil-litigation/contract-formation.yaml")
        document["status"] = "verified"
        result = self.framework.validate_document(document, profile="record")
        self.assertEqual("FAIL", result.status)
        self.assertIn(
            "verified Evidence requires approved human_review",
            result.errors,
        )

    def test_workflow_entry_accepts_received_evidence(self) -> None:
        path, _ = self.load_template("enforcement/enforcement-basis.yaml")
        result = self.framework.validate_file(path, profile="workflow-entry")
        self.assertEqual("PASS", result.status, result.errors)
        self.assertTrue(result.reviewer_required)

    def test_workflow_entry_rejects_archived_evidence(self) -> None:
        _, document = self.load_template("corporate/corporate-registration.yaml")
        document["status"] = "archived"
        result = self.framework.validate_document(document, profile="workflow-entry")
        self.assertEqual("FAIL", result.status)
        self.assertIn(
            "workflow entry requires Evidence status=received",
            result.errors,
        )

    def test_workflow_entry_defers_classification_with_warning(self) -> None:
        _, document = self.load_template("civil-litigation/performance.yaml")
        document.pop("classification")
        result = self.framework.validate_document(document, profile="workflow-entry")
        self.assertEqual("PASS", result.status, result.errors)
        self.assertTrue(
            any("Classification stage" in warning for warning in result.warnings)
        )

    def test_unlawful_acquisition_cannot_enter_workflow(self) -> None:
        _, document = self.load_template("enforcement/asset-clues.yaml")
        document["acquisition"]["lawfulness"] = "unlawful"
        result = self.framework.validate_document(document, profile="workflow-entry")
        self.assertEqual("FAIL", result.status)
        self.assertIn(
            "unlawfully acquired Evidence cannot enter workflow",
            result.errors,
        )


if __name__ == "__main__":
    unittest.main()
