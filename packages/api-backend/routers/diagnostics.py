"""Diagnostics router — GET /api/v1/diagnostics/dns

Lightweight DNS lookup endpoint used by the support team to debug
customer-facing DNS issues for whitelabeled deployments. Shells out
to `dig` so the response matches what `dig +short` returns on the
ops box.
"""

import subprocess

from fastapi import APIRouter, HTTPException

from utils.responses import ok

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


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
