"""Negative authorization test for the documented RedFish products endpoint.

Run against a disposable/test environment only. The endpoint is confirmed in the
current source repository at /api/products. If it is intentionally public, choose
a protected endpoint and update this test rather than weakening the assertion.
"""
import os
import sys
import urllib.error
import urllib.request


def main() -> int:
    base_url = os.environ.get("REDFISH_BASE_URL", "").strip().rstrip("/")
    if not base_url:
        print("ERROR: set REDFISH_BASE_URL to a running RedFish test instance.", file=sys.stderr)
        return 2

    url = f"{base_url}/api/products"
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/json"},
        method="GET",
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            status = response.status
    except urllib.error.HTTPError as exc:
        status = exc.code
    except Exception as exc:
        print(f"ERROR: could not reach {url}: {exc}", file=sys.stderr)
        return 2

    if status in (401, 403):
        print(f"PASS: unauthenticated GET {url} was rejected with HTTP {status}.")
        return 0

    print(
        f"FAIL: unauthenticated GET {url} returned HTTP {status}; "
        "expected 401 or 403. Check the security configuration and endpoint exposure.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
