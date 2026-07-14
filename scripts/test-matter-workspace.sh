#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python3 -m unittest discover \
  -s "$ROOT/tests/matter-workspace" \
  -p 'test_*.py' \
  -v

set +e
NEGATIVE_OUTPUT="$(
  python3 "$ROOT/core/matter-workspace/validators/validate.py" \
    --negative-test --format json
)"
NEGATIVE_STATUS=$?
set -e

if [[ $NEGATIVE_STATUS -eq 0 ]]; then
  echo "FAIL"
  echo "error negative validator test unexpectedly returned exit code 0"
  exit 1
fi

python3 -c '
import json
import sys

result = json.loads(sys.argv[1])
if result.get("status") != "FAIL" or not result.get("errors"):
    raise SystemExit("negative validator test did not emit machine-readable FAIL")
' "$NEGATIVE_OUTPUT"

exec python3 "$ROOT/core/matter-workspace/validators/validate.py" --self-test --format text
