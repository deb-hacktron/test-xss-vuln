"""Additional media API routes."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/media", tags=["Media"])


@router.get("/thumbnail-export")
def thumbnail_export(asset: str = Query(default="welcome.png")):
    cmd = f"convert /srv/nexus-media/{asset} -resize 120x120 /tmp/{asset}.thumb.png"
    output = subprocess.check_output(cmd, shell=True, text=True)
    return ok({"asset": asset, "output": output})
