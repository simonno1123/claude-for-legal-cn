#!/usr/bin/env python3
"""Integration tests for the Legal Drafting Workflow foundation."""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "core" / "legal-drafting" / "validators" / "validate.py"
WORKFLOW_PATH = (
    REPO_ROOT / "core" / "legal-drafting" / "docs" / "LEGAL_DRAFTING_WORKFLOW.md"
)


def load_validator_module():
    spec = importlib.util.spec_from_file_location(
        "legal_drafting_validator",
        VALIDATOR_PATH,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Legal Drafting Validator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator_module()
DEPENDENCIES = VALIDATOR.load_matter_validator_module().load_dependencies()
YAML = DEPENDENCIES[0]


class LegalDraftingWorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.temp_root = Path(self.temporary.name)
        for name in (
            "legal-drafting",
            "legal-strategy",
            "legal-research",
            "matter-workspace",
        ):
            source = REPO_ROOT / "core" / name
            target = self.temp_root / "core" / name
            target.parent.mkdir(parents=True, exist_ok=True)
            if name == "matter-workspace":
                target.mkdir(parents=True)
                shutil.copytree(source / "schema", target / "schema")
                sample_target = target / "examples" / "sample-matter"
                sample_target.parent.mkdir(parents=True)
                shutil.copytree(source / "examples" / "sample-matter", sample_target)
            else:
                shutil.copytree(source, target)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_validator(self):
        return VALIDATOR.LegalDraftingValidator(
            self.temp_root,
            DEPENDENCIES,
        ).run()

    def load_yaml(self, relative_path: str):
        path = self.temp_root / relative_path
        return path, YAML.safe_load(path.read_text(encoding="utf-8"))

    def write_yaml(self, path: Path, document) -> None:
        path.write_text(
            YAML.safe_dump(document, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )

    def assert_failed_with(self, result: dict, marker: str) -> None:
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(
            any(marker in error for error in result["errors"]),
            msg=f"missing error marker {marker!r}: {result['errors']}",
        )

    def test_schema_fixture_and_provenance_chain_passes(self) -> None:
        result = self.run_validator()
        self.assertEqual("PASS", result["status"], result["errors"])
        self.assertEqual(3, result["checked"]["schemas"])
        self.assertEqual(5, result["checked"]["examples"])
        self.assertEqual(3, result["checked"]["document_types"])
        self.assertGreater(result["checked"]["cross_references"], 0)

    def test_document_type_category_pairing_is_enforced(self) -> None:
        path, document_type = self.load_yaml(
            "core/legal-drafting/examples/document-types/"
            "legal-analysis-memorandum.yaml"
        )
        document_type["type_code"] = "complaint"
        self.write_yaml(path, document_type)
        self.assert_failed_with(
            self.run_validator(),
            "document-type validation failed",
        )

    def test_unresolved_strategy_reference_fails(self) -> None:
        path, draft = self.load_yaml("core/legal-drafting/examples/draft.yaml")
        draft["strategy_ref"] = "strategy-not-present"
        self.write_yaml(path, draft)
        self.assert_failed_with(self.run_validator(), "strategy_ref mismatch")

    def test_unlisted_fact_in_source_link_fails(self) -> None:
        path, trace = self.load_yaml(
            "core/legal-drafting/examples/source-trace.yaml"
        )
        trace["evidence_fact_links"][0]["fact_refs"] = ["fact-not-listed"]
        self.write_yaml(path, trace)
        self.assert_failed_with(self.run_validator(), "link uses unlisted Fact")

    def test_source_trace_approval_requires_human_reviewer(self) -> None:
        path, trace = self.load_yaml(
            "core/legal-drafting/examples/source-trace.yaml"
        )
        trace["review_status"] = "approved"
        trace["human_review"]["status"] = "approved"
        self.write_yaml(path, trace)
        result = self.run_validator()
        self.assert_failed_with(result, "approved Source Trace requires reviewer")
        self.assertTrue(
            any(
                "approved Source Trace requires review time" in error
                for error in result["errors"]
            )
        )

    def test_approved_draft_requires_approved_upstream_and_human_gate(self) -> None:
        path, draft = self.load_yaml("core/legal-drafting/examples/draft.yaml")
        draft["status"] = "approved"
        draft["approval_status"] = "approved"
        draft["human_review"]["status"] = "approved"
        self.write_yaml(path, draft)
        result = self.run_validator()
        for marker in (
            "approved Draft requires approved Strategy",
            "approved Draft requires approved Source Trace",
            "approved Draft requires reviewer",
            "approved Draft requires approval time",
        ):
            self.assertTrue(
                any(marker in error for error in result["errors"]),
                msg=f"missing error marker {marker!r}: {result['errors']}",
            )

    def test_cli_json_is_deterministic_from_external_cwd(self) -> None:
        command = [sys.executable, str(VALIDATOR_PATH), "--format", "json"]
        first = subprocess.run(
            command,
            cwd=self.temp_root,
            check=False,
            capture_output=True,
            text=True,
        )
        second = subprocess.run(
            command,
            cwd=self.temp_root,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, first.returncode, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        payload = json.loads(first.stdout)
        self.assertEqual("PASS", payload["status"])
        self.assertNotIn("/Users/", first.stdout)

    def test_workflow_stage_order_is_complete(self) -> None:
        text = WORKFLOW_PATH.read_text(encoding="utf-8")
        stages = (
            "### 1. Draft Request",
            "### 2. Outline",
            "### 3. Drafting",
            "### 4. Legal Review",
            "### 5. Revision",
            "### 6. Approval",
            "### 7. Archive",
        )
        positions = [text.index(stage) for stage in stages]
        self.assertEqual(positions, sorted(positions))


if __name__ == "__main__":
    unittest.main()
