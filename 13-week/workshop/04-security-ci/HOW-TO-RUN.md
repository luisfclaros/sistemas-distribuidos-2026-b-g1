# CP4 — Run the negative authorization test

## What it checks

The test sends an unauthenticated `GET /api/products` request to a running RedFish test instance. The endpoint path is present in the current source repository's `ProductController`. The expected result is HTTP `401` or `403`.

This is a negative security test: if the endpoint returns `200`, the test fails and indicates that the endpoint may be accessible without authentication. Do not change the expected status to make the test green; first verify the intended access policy with the team.

## Run locally

1. Start RedFish in a disposable local/test environment.
2. Set the base URL (do not include `/api/products`):
   - PowerShell: `$env:REDFISH_BASE_URL = "http://localhost:8080"`
   - Bash: `export REDFISH_BASE_URL="http://localhost:8080"`
3. Run: `python 13-week/workshop/04-security-ci/test_negative_authorization.py`
4. Record the actual result and fix the security configuration if the test fails.

## CI workflow

The workflow in `.github/workflows/w13-security-gate.yml` is a proposal for a manually triggered check. Supply a test-environment base URL when running it. Do not point this test at production; it deliberately sends unauthenticated requests.

## Related backlog story

[Reject invalid and expired JWTs on protected API routes](https://github.com/code-corhuila/redfish-docs/issues/4)

## Important limitation

The workflow and test have been added as files, but they have not been executed against a running RedFish deployment in this session. The team must run them and retain the real CI result as evidence.
