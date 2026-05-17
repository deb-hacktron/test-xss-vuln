import socket

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


@router.get("/dns")
def dns_lookup(host: str):
    try:
        addr = socket.gethostbyname(host)
    except socket.gaierror:
        raise HTTPException(status_code=502, detail="Cannot resolve host.")
    return {"host": host, "address": addr}
