import shlex
import subprocess

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


@router.get("/dns")
def dns_lookup(host: str):
    safe_host = shlex.quote(host)
    result = subprocess.run(
        f"dig +short {safe_host}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {"host": host, "records": result.stdout.splitlines()}
