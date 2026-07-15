#!/usr/bin/env python3
"""Integration tests for the Legal Research Workflow foundation."""

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
VALIDATOR_PATH = REPO_ROOT / "core" / "legal-research" / "validators" / "validate.py"
WORKFLOW_PATH = (
    REPO_ROOT / "core" / "legal-research" / "docs" / "LEGAL_RESEARCH_WORKFLOW.md"
)


def load_validator_module():
    spec = importlib.util.spec_from_file_location(
        "legal_research_validator",
        VALIDATOR_PATH,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Legal Research Validator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator_module()
DEPENDENCIES = VALIDATOR.load_matter_validator_module().load_dependencies()
YAML = DEPENDENCIES[0]


class LegalResearchWorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.temp_root = Path(self.temporary.name)
        research_source = REPO_ROOT / "core" / "legal-research"
        research_target = self.temp_root / "core" / "legal-research"
        research_target.parent.mkdir(parents=True)
        shutil.copytree(research_source, research_target)

        matter_source = REPO_ROOT / "core" / "matter-workspace"
        matter_target = self.temp_root / "core" / "matter-workspace"
        matter_target.mkdir(parents=True)
        shutil.copytree(matter_source / "schema", matter_target / "schema")
        sample_target = matter_target / "examples" / "sample-matter"
        sample_target.parent.mkdir(parents=True)
        shutil.copytree(
            matter_source / "examples" / "sample-matter",
            sample_target,
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_validator(self):
        return VALIDATOR.LegalResearchValidator(
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

    def test_schema_fixture_and_issue_chain_passes(self) -> None:
        result = self.run_validator()
        self.assertEqual("PASS", result["status"], result["errors"])
        self.assertEqual(3, result["checked"]["schemas"])
        self.assertEqual(3, result["checked"]["examples"])
        self.assertEqual(1, result["checked"]["source_records"])
        self.assertGreater(result["checked"]["cross_references"], 0)

    def test_invalid_source_type_fails(self) -> None:
        path, source = self.load_yaml(
            "core/legal-research/examples/sources/source-sample-law.yaml"
        )
        source["source_type"] = "foreign-provider-default"
        self.write_yaml(path, source)
        self.assert_failed_with(self.run_validator(), "research-source validation failed")

    def test_unresolved_issue_reference_fails(self) -> None:
        path, research = self.load_yaml(
            "core/legal-research/examples/research-matter.yaml"
        )
        research["issue_ref"] = "issue-not-present"
        self.write_yaml(path, research)
        self.assert_failed_with(self.run_validator(), "unresolved Issue reference")

    def test_unresolved_output_source_fails(self) -> None:
        path, output = self.load_yaml(
            "core/legal-research/examples/research-output.yaml"
        )
        output["sources"].append("research-source-not-present")
        self.write_yaml(path, output)
        self.assert_failed_with(self.run_validator(), "unresolved source reference")

    def test_approved_output_requires_human_review_identity(self) -> None:
        path, output = self.load_yaml(
            "core/legal-research/examples/research-output.yaml"
        )
        output["review_status"] = "approved"
        output["human_review"]["status"] = "approved"
        self.write_yaml(path, output)
        result = self.run_validator()
        self.assert_failed_with(result, "approved output requires reviewer")
        self.assertTrue(
            any("approved output requires reviewed_at" in item for item in result["errors"])
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
            "### 1. Issue Identification",
            "### 2. Question Framing",
            "### 3. Source Collection",
            "### 4. Rule Extraction",
            "### 5. Case Analysis",
            "### 6. Legal Position",
            "### 7. Human Review",
        )
        positions = [text.index(stage) for stage in stages]
        self.assertEqual(positions, sorted(positions))


if __name__ == "__main__":
    unittest.main()
