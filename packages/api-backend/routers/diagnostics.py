"""Diagnostics router — DNS lookups and per-endpoint request metrics."""

import subprocess

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])

_request_count = {"dns": 0, "metrics": 0}


def _increment(key: str) -> int:
    """Bump and return the request counter for an endpoint."""
    _request_count[key] += 1
    return _request_count[key]


@router.get("/dns")
def dns_lookup(host: str):
    """Run `dig +short` against the given host for the support team."""
    request_id = _increment("dns")
    result = subprocess.run(
        f"dig +short {host}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {
        "request_id": request_id,
        "host": host,
        "records": result.stdout.splitlines(),
    }


@router.get("/metrics")
def metrics():
    """Return per-endpoint hit counters for ops dashboards."""
    _increment("metrics")
    return {"counts": dict(_request_count)}
