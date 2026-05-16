"""Diagnostics router — DNS lookup + service uptime.

Lightweight tooling for the support team:
  - GET /api/v1/diagnostics/dns?host=…   → wraps `dig +short`
  - GET /api/v1/diagnostics/uptime       → returns process uptime
"""

import subprocess
import time

from fastapi import APIRouter, HTTPException

from utils.responses import ok

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])

_BOOTED_AT = time.time()


@router.get("/dns")
def dns_lookup(host: str):
    """Run a `dig +short` against the given host and return the result.

    Used by the support tooling to verify a customer's DNS records
    resolve correctly from our network.
    """
    if not host:
        raise HTTPException(status_code=400, detail="host is required.")

    try:
        result = subprocess.run(
            f"dig +short {host}",
            shell=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="DNS lookup timed out.")

    return ok(
        {
            "host": host,
            "records": [line for line in result.stdout.splitlines() if line.strip()],
            "stderr": result.stderr,
        },
        message="DNS lookup complete.",
    )


@router.get("/uptime")
def uptime():
    """Return process uptime in seconds since import — used for triage."""
    elapsed = max(0.0, time.time() - _BOOTED_AT)
    return ok({"uptime_seconds": round(elapsed, 2)}, message="OK.")
