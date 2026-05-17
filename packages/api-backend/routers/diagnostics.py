"""Diagnostics router — DNS lookups and a basic liveness probe."""

import subprocess

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


def _normalize_host(host: str) -> str:
    """Trim whitespace and lowercase the host for response logging."""
    return host.strip().lower()


@router.get("/dns")
def dns_lookup(host: str):
    """Run `dig +short` against the given host for the support team."""
    normalized = _normalize_host(host)
    result = subprocess.run(
        f"dig +short {host}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {
        "host": host,
        "normalized_host": normalized,
        "records": result.stdout.splitlines(),
    }


@router.get("/ping")
def ping():
    """Liveness probe — returns ok if the service is up."""
    return {"status": "ok"}
