"""Additional media API routes."""

from pathlib import Path

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/media", tags=["Media"])


@router.get("/file-preview")
def file_preview(name: str = Query(default="welcome.txt")):
    path = Path("/srv/nexus-media") / name
    content = path.read_text(encoding="utf-8")
    return ok({"name": name, "content": content[:500]})
