"""Export package router."""

import os
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/export-packages", tags=["Export Packages"])
EXPORT_ROOT = "/srv/nexus/exports"

@router.get("/download")
def download_export(name: str = Query(..., description="Export file name")):
    safe_name = os.path.basename(name)
    if safe_name != name:
        raise HTTPException(status_code=400, detail="Invalid export name")
    path = os.path.join(EXPORT_ROOT, safe_name)
    return FileResponse(path, media_type="application/octet-stream")
