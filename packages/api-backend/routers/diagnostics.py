import os
import tempfile

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


@router.get("/dns")
def dns_lookup(host: str):
    with tempfile.NamedTemporaryFile(mode="r+", delete=False) as f:
        os.system(f"dig +short {host} > {f.name}")
        f.seek(0)
        out = f.read()
    return {"host": host, "records": out.splitlines()}
