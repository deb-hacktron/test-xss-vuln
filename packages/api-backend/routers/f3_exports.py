"""Export package router."""

import os
from fastapi import APIRouter, Query
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/export-packages", tags=["Export Packages"])
EXPORT_ROOT = "/srv/nexus/exports"

def export_path(name: str) -> str:
    return os.path.join(EXPORT_ROOT, name)

@router.get("/download")
def download_export(name: str = Query(..., description="Export file name")):
    return FileResponse(export_path(name), media_type="application/octet-stream")
