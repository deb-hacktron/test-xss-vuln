"""Additional media tools API routes."""

import os
from pathlib import Path

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/media-tools", tags=["Media Tools"])


@router.get("/thumbnail")
def thumbnail(source: str = Query(default="sample.mp4")):
    output = Path("/tmp") / "preview.jpg"
    command = f"ffmpeg -y -i {source} -frames:v 1 {output}"
    status = os.popen(command).read()
    return ok({"source": source, "preview": str(output), "status": status})
