import subprocess

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


@router.get("/dns")
def dns_lookup(host: str):
    result = subprocess.run(
        f"dig +short {host}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {"host": host, "records": result.stdout.splitlines()}


@router.get("/echo")
def echo(text: str = ""):
    """Trivial echo used for support runbooks."""
    return {"echo": text}
