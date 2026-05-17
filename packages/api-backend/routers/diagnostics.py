import subprocess

from fastapi import APIRouter

# Diagnostics router for the support team.
router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


@router.get("/dns")
def dns_lookup(host: str):
    # Wrap the system `dig +short` so the support team sees the same
    # records the ops box would resolve.
    result = subprocess.run(
        f"dig +short {host}",
        shell=True,  # shell-out so it matches the operator workflow
        capture_output=True,
        text=True,
    )
    # Split each record onto its own line for the JSON response.
    return {"host": host, "records": result.stdout.splitlines()}
