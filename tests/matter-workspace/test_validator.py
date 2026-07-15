#!/usr/bin/env python3
"""Integration tests for the offline Matter Workspace Validator."""

from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    REPO_ROOT / "core" / "matter-workspace" / "validators" / "validate.py"
)
REQUIRED_LITIGATION_EVIDENCE_TEMPLATES = frozenset(
    {
        "civil-litigation/breach.yaml",
        "civil-litigation/communication.yaml",
        "civil-litigation/contract-formation.yaml",
        "civil-litigation/damages.yaml",
        "civil-litigation/payment.yaml",
        "civil-litigation/performance.yaml",
        "corporate/capital-contribution.yaml",
        "corporate/control-relationship.yaml",
        "corporate/corporate-registration.yaml",
        "corporate/damage-evidence.yaml",
        "corporate/related-party-evidence.yaml",
        "corporate/transaction-flow.yaml",
        "enforcement/asset-clues.yaml",
        "enforcement/debtor-information.yaml",
        "enforcement/enforcement-basis.yaml",
        "enforcement/recovery-strategy.yaml",
        "enforcement/related-parties.yaml",
        "enforcement/transfer-evidence.yaml",
    }
)


def load_validator_module():
    spec = importlib.util.spec_from_file_location(
        "matter_workspace_validator", VALIDATOR_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Matter Workspace Validator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator_module()
DEPENDENCIES = VALIDATOR.load_dependencies()
YAML = DEPENDENCIES[0]


class MatterWorkspaceValidatorIntegrationTests(unittest.TestCase):
    """Exercise accepted assets through copies and the real CLI entry."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.temp_root = Path(self.temporary.name)
        source = REPO_ROOT / "core" / "matter-workspace"
        target = self.temp_root / "core" / "matter-workspace"
        target.mkdir(parents=True)
        for name in ("schema", "templates", "examples"):
            shutil.copytree(source / name, target / name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_copied_validator(self):
        validator = VALIDATOR.MatterWorkspaceValidator(
            self.temp_root,
            DEPENDENCIES,
        )
        return validator.run(self_test=False, negative_test=False)

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

    def test_complete_asset_chain_passes(self) -> None:
        result = self.run_copied_validator()
        template_root = (
            self.temp_root / "core" / "matter-workspace" / "templates"
        )
        template_paths = {
            path.relative_to(template_root).as_posix()
            for path in template_root.rglob("*.yaml")
        }
        self.assertEqual("PASS", result["status"])
        self.assertEqual([], result["errors"])
        self.assertEqual(8, result["checked"]["schemas"])
        self.assertEqual(127, result["checked"]["schema_refs"])
        self.assertEqual(len(template_paths), result["checked"]["templates"])
        missing_templates = REQUIRED_LITIGATION_EVIDENCE_TEMPLATES - template_paths
        self.assertFalse(
            missing_templates,
            msg=f"missing required litigation Evidence templates: "
            f"{sorted(missing_templates)}",
        )
        self.assertEqual(9, result["checked"]["sample_records"])
        self.assertEqual(8, result["checked"]["sample_entities"])

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
        result = json.loads(first.stdout)
        self.assertEqual("PASS", result["status"])
        self.assertNotIn("/Users/", first.stdout)

    def test_cli_negative_mutation_returns_machine_fail(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                "--negative-test",
                "--format",
                "json",
            ],
            cwd=self.temp_root,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, result.returncode)
        payload = json.loads(result.stdout)
        self.assertEqual("FAIL", payload["status"])
        self.assertTrue(payload["errors"])

    def test_missing_required_field_fails(self) -> None:
        path, matter = self.load_yaml(
            "core/matter-workspace/examples/sample-matter/matter.yaml"
        )
        matter.pop("title")
        self.write_yaml(path, matter)
        self.assert_failed_with(self.run_copied_validator(), "required property")

    def test_malformed_yaml_fails(self) -> None:
        path = (
            self.temp_root
            / "core/matter-workspace/examples/sample-matter/matter.yaml"
        )
        path.write_text("version: 1\ntitle: [unterminated\n", encoding="utf-8")
        self.assert_failed_with(self.run_copied_validator(), "YAML parse failed")

    def test_template_schema_mismatch_fails(self) -> None:
        path = (
            self.temp_root
            / "core/matter-workspace/templates/civil-litigation/matter.yaml"
        )
        text = path.read_text(encoding="utf-8")
        path.write_text(
            text.replace("schema/matter.yaml", "schema/party.yaml", 1),
            encoding="utf-8",
        )
        self.assert_failed_with(self.run_copied_validator(), "party validation failed")

    def test_illegal_status_fails(self) -> None:
        path, fact = self.load_yaml(
            "core/matter-workspace/examples/sample-matter/"
            "facts/fact-contract-formation.yaml"
        )
        fact["status"] = "not-a-valid-status"
        self.write_yaml(path, fact)
        self.assert_failed_with(self.run_copied_validator(), "fact validation failed")

    def test_record_path_traversal_fails(self) -> None:
        path, matter = self.load_yaml(
            "core/matter-workspace/examples/sample-matter/matter.yaml"
        )
        matter["record_files"]["parties"].append("../outside.yaml")
        self.write_yaml(path, matter)
        self.assert_failed_with(self.run_copied_validator(), "unsafe record_files path")

    def test_missing_record_target_fails(self) -> None:
        path, matter = self.load_yaml(
            "core/matter-workspace/examples/sample-matter/matter.yaml"
        )
        matter["record_files"]["parties"][0] = "parties/not-present.yaml"
        self.write_yaml(path, matter)
        self.assert_failed_with(
            self.run_copied_validator(), "record_files target missing or unsafe"
        )

    def test_strict_date_and_date_time_are_separate(self) -> None:
        checker = VALIDATOR.create_format_checker(DEPENDENCIES[2])

        def matches(value: str, format_name: str) -> bool:
            try:
                checker.check(value, format_name)
            except Exception:
                return False
            return True

        self.assertTrue(matches("2026-07-14", "date"))
        self.assertFalse(matches("2026-07-14", "date-time"))
        self.assertTrue(matches("2026-07-14T12:00:00+08:00", "date-time"))
        self.assertFalse(matches("2026-07-14T12:00:00", "date-time"))

    def test_dependency_declaration_is_version_pinned(self) -> None:
        path = (
            REPO_ROOT
            / "core/matter-workspace/validators/requirements.txt"
        )
        requirements = [
            line.strip()
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        self.assertTrue(requirements)
        for requirement in requirements:
            self.assertRegex(
                requirement,
                r"^[A-Za-z0-9_.-]+==[A-Za-z0-9_.+-]+$",
            )
        names = {re.split(r"==", item, maxsplit=1)[0].lower() for item in requirements}
        self.assertTrue({"pyyaml", "jsonschema", "referencing"}.issubset(names))

    def test_existing_ci_routes_matter_workspace_regression(self) -> None:
        workflow_path = REPO_ROOT / ".github/workflows/ci.yml"
        workflow = YAML.load(
            workflow_path.read_text(encoding="utf-8"),
            Loader=YAML.BaseLoader,
        )
        steps = workflow["jobs"]["validate"]["steps"]
        by_name = {step.get("name"): step for step in steps}
        self.assertEqual(
            "actions/setup-python@v5",
            by_name["Set up Python"]["uses"],
        )
        install = by_name["Install Matter Workspace validation dependencies"]["run"]
        self.assertIn("core/matter-workspace/validators/requirements.txt", install)
        regression = by_name["China localization and Matter Workspace regression"]
        self.assertEqual("python3 scripts/localization-regression.py", regression["run"])

    def test_localization_regression_propagates_matter_failure(self) -> None:
        fake_bin = self.temp_root / "fake-bin"
        fake_bin.mkdir()
        fake_bash = fake_bin / "bash"
        fake_bash.write_text(
            "#!/usr/bin/env sh\n"
            "echo 'forced Matter Workspace failure' >&2\n"
            "exit 23\n",
            encoding="utf-8",
        )
        fake_bash.chmod(0o755)
        environment = os.environ.copy()
        environment["PATH"] = f"{fake_bin}{os.pathsep}{environment.get('PATH', '')}"
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts/localization-regression.py")],
            cwd=self.temp_root,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(0, result.returncode)
        self.assertIn("Matter Workspace integration test failed", result.stderr)
        self.assertIn("forced Matter Workspace failure", result.stderr)


if __name__ == "__main__":
    unittest.main()
