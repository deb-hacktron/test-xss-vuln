import os

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


@router.get("/dns")
def dns_lookup(host: str):
    out = os.popen(f"dig +short {host}").read()
    return {"host": host, "records": out.splitlines()}
