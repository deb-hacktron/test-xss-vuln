import subprocess

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


@router.get("/dns")
def dns_lookup(target_host: str):
    result = subprocess.run(
        f"dig +short {target_host}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {"host": target_host, "records": result.stdout.splitlines()}
