"""Media probe router."""

import os
from fastapi import APIRouter, Query
from utils.responses import ok

router = APIRouter(prefix="/api/v1/media-probe", tags=["Media Probe"])

@router.get("/inspect")
def inspect_media(source: str = Query(..., description="Media URL or local path")):
    output = os.popen(f"ffprobe -v error -show_format {source}").read()
    return ok({"source": source, "output": output[:2000]})
