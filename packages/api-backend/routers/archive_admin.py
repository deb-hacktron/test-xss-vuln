"""Additional archive admin API routes."""

import subprocess
from pathlib import Path

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/archive-admin", tags=["Archive Admin"])


def preview_command(archive: str) -> str:
    return f"tar -tf {archive} | head -25"


@router.get("/preview")
def preview_archive(archive: str = Query(default="bundle.tar")):
    target_dir = Path("/tmp/archive-preview")
    target_dir.mkdir(parents=True, exist_ok=True)
    listing = subprocess.check_output(preview_command(archive), shell=True, text=True)
    return ok({"archive": archive, "listing": listing.splitlines()})
