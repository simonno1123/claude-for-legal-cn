#!/usr/bin/env python3
"""Integration tests for the Legal Strategy Workflow foundation."""

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
VALIDATOR_PATH = REPO_ROOT / "core" / "legal-strategy" / "validators" / "validate.py"
WORKFLOW_PATH = (
    REPO_ROOT / "core" / "legal-strategy" / "docs" / "LEGAL_STRATEGY_WORKFLOW.md"
)


def load_validator_module():
    spec = importlib.util.spec_from_file_location(
        "legal_strategy_validator",
        VALIDATOR_PATH,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Legal Strategy Validator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator_module()
DEPENDENCIES = VALIDATOR.load_matter_validator_module().load_dependencies()
YAML = DEPENDENCIES[0]


class LegalStrategyWorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.temp_root = Path(self.temporary.name)
        for name in ("legal-strategy", "legal-research", "matter-workspace"):
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
        return VALIDATOR.LegalStrategyValidator(
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

    def test_schema_fixture_and_research_chain_passes(self) -> None:
        result = self.run_validator()
        self.assertEqual("PASS", result["status"], result["errors"])
        self.assertEqual(3, result["checked"]["schemas"])
        self.assertEqual(7, result["checked"]["examples"])
        self.assertEqual(2, result["checked"]["option_records"])
        self.assertEqual(4, result["checked"]["risk_records"])
        self.assertGreater(result["checked"]["cross_references"], 0)

    def test_invalid_risk_type_fails(self) -> None:
        path, risk = self.load_yaml(
            "core/legal-strategy/examples/risks/risk-legal.yaml"
        )
        risk["risk_type"] = "predicted-win-rate"
        self.write_yaml(path, risk)
        self.assert_failed_with(self.run_validator(), "risk-assessment validation failed")

    def test_unresolved_research_output_fails(self) -> None:
        path, strategy = self.load_yaml(
            "core/legal-strategy/examples/strategy.yaml"
        )
        strategy["research_output_ref"] = "research-output-not-present"
        self.write_yaml(path, strategy)
        self.assert_failed_with(self.run_validator(), "research_output_ref mismatch")

    def test_unresolved_option_reference_fails(self) -> None:
        path, strategy = self.load_yaml(
            "core/legal-strategy/examples/strategy.yaml"
        )
        strategy["option_refs"].append("strategy-option-not-present")
        self.write_yaml(path, strategy)
        self.assert_failed_with(self.run_validator(), "unresolved option reference")

    def test_approved_strategy_requires_human_selection(self) -> None:
        path, strategy = self.load_yaml(
            "core/legal-strategy/examples/strategy.yaml"
        )
        strategy["status"] = "approved"
        strategy["approval_status"] = "approved"
        strategy["human_approval"]["status"] = "approved"
        self.write_yaml(path, strategy)
        result = self.run_validator()
        self.assert_failed_with(result, "approved Strategy requires selected option")
        for marker in (
            "approved Strategy requires rationale",
            "approved Strategy requires decision owner",
            "approved Strategy requires approving reviewer",
            "approved Strategy requires approval time",
        ):
            self.assertTrue(any(marker in error for error in result["errors"]))

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
            "### 1. Research Result",
            "### 2. Issue Assessment",
            "### 3. Option Generation",
            "### 4. Risk Review",
            "### 5. Strategy Decision",
            "### 6. Human Approval",
        )
        positions = [text.index(stage) for stage in stages]
        self.assertEqual(positions, sorted(positions))


if __name__ == "__main__":
    unittest.main()
