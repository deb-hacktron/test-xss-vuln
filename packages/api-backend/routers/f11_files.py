"""File download router."""

from pathlib import Path

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/files", tags=["Files"])


@router.get("/download")
def download_file(name: str = Query(default="readme.txt")):
    target = Path("/tmp/nexus-f11-files") / name
    content = target.read_text(encoding="utf-8")
    return ok({"name": name, "content": content})
