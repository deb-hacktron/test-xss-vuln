import subprocess

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


@router.get("/dns")
def dns_lookup(host: str):
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
    return {"host": host, "records": result.stdout.splitlines()}
