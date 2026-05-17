import logging
import subprocess

from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


@router.get("/dns")
def dns_lookup(host: str):
    logger.info("dns lookup: %s", host)
    result = subprocess.run(
        f"dig +short {host}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {"host": host, "records": result.stdout.splitlines()}
