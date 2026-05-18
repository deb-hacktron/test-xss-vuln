"""Media probe router."""

import subprocess
from fastapi import APIRouter, Query
from utils.responses import ok

router = APIRouter(prefix="/api/v1/media-probe", tags=["Media Probe"])

@router.get("/inspect")
def inspect_media(source: str = Query(..., description="Media URL or local path")):
    completed = subprocess.run(["ffprobe", "-v", "error", "-show_format", source], capture_output=True, text=True, check=False)
    return ok({"source": source, "output": completed.stdout[:2000]})


@router.get("/inspect-streams")
def inspect_media_streams(source: str = Query(..., description="Media URL or local path")):
    completed = subprocess.run(["ffprobe", "-v", "error", "-show_streams", source], capture_output=True, text=True, check=False)
    return ok({"source": source, "output": completed.stdout[:2000]})
