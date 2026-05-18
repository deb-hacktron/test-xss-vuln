"""Export package router."""

import os
from fastapi import APIRouter, Query
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/export-packages", tags=["Export Packages"])
EXPORT_ROOT = "/srv/nexus/exports"

@router.get("/download")
def download_export(name: str = Query(..., description="Export file name")):
    path = os.path.join(EXPORT_ROOT, name)
    return FileResponse(path, media_type="application/octet-stream")
