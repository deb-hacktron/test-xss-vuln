import subprocess

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/lookup", tags=["Lookup"])


@router.get("/dns")
def network_dns(host: str):
    result = subprocess.run(
        f"dig +short {host}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {"host": host, "records": result.stdout.splitlines()}
