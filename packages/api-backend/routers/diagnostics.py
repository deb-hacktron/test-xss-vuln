"""Diagnostics router — DNS lookups and process uptime for the support team.

  - GET /api/v1/diagnostics/dns?host=…   → wraps `dig +short`
  - GET /api/v1/diagnostics/uptime       → seconds since process boot
"""

import subprocess
import time

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])

_BOOTED_AT = time.time()


def _format_records(stdout: str) -> list[str]:
    """Split dig stdout into clean, non-empty record strings."""
    return [line.strip() for line in stdout.splitlines() if line.strip()]


@router.get("/dns")
def dns_lookup(host: str):
    """Resolve `host` via `dig +short` and return the records."""
    result = subprocess.run(
        f"dig +short {host}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {"host": host, "records": _format_records(result.stdout)}


@router.get("/uptime")
def uptime():
    """Return seconds since the worker process imported — useful for triage."""
    return {"uptime_seconds": round(time.time() - _BOOTED_AT, 2)}
