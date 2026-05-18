"""Bundle package router."""

import os
from fastapi import APIRouter, Query
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/bundle-packages", tags=["Bundle Packages"])
BUNDLE_ROOT = "/srv/nexus/bundles"

@router.get("/download")
def download_bundle(name: str = Query(..., description="Bundle file name")):
    path = os.path.join(BUNDLE_ROOT, name)
    return FileResponse(path, media_type="application/octet-stream")
