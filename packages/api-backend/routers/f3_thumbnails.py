"""Thumbnail probe router."""

import subprocess
from fastapi import APIRouter, Query
from utils.responses import ok

router = APIRouter(prefix="/api/v1/thumbnail-probe", tags=["Thumbnail Probe"])

@router.get("/inspect")
def inspect_thumbnail(source: str = Query(..., description="Thumbnail URL or local path")):
    cmd = f"ffprobe -v error -show_streams {source}"
    completed = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=False)
    return ok({"source": source, "output": completed.stdout[:2000]})
