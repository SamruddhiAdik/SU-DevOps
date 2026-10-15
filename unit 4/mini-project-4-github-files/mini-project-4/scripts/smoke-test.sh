#!/usr/bin/env bash
set -euo pipefail
BASE_URL="${1:?Usage: bash scripts/smoke-test.sh http://HOST}"
BASE_URL="${BASE_URL%/}"

echo "1/3 Checking health..."
curl --fail --silent --show-error "${BASE_URL}/api/health"
echo
echo "2/3 Checking students..."
curl --fail --silent --show-error "${BASE_URL}/api/students"
echo
echo "3/3 Posting demo marks..."
curl --fail --silent --show-error -X POST "${BASE_URL}/api/marks" \
  -H "Content-Type: application/json" \
  -d '{"student_id":1,"course":"Cloud Computing","marks":88}'
echo
echo "Smoke tests completed."
