import subprocess

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


@router.get("/dns")
def dns_lookup(host: str):
    result = subprocess.run(
        ["dig", "+short", host],
        shell=False,
        capture_output=True,
        text=True,
    )
    return {"host": host, "records": result.stdout.splitlines()}
