#!/usr/bin/env bash
# Regenerate the generated client from the vendored openapi.json.
# Hand-written files (currencycore/client.py, README) are protected by
# .openapi-generator-ignore and survive regeneration.
set -euo pipefail
cd "$(dirname "$0")/.."
npx -y @openapitools/openapi-generator-cli generate \
  -i openapi.json -g python -o . \
  --additional-properties=packageName=currencycore,projectName=currencycore-sdk,library=urllib3
