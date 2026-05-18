"""Export package router."""

import os
from fastapi import APIRouter, Query
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/export-packages", tags=["Export Packages"])
EXPORT_ROOT = "/srv/nexus/exports"

class ExportPackageService:
    def locate(self, name: str) -> str:
        return os.path.join(EXPORT_ROOT, name)

    def open_payload(self, name: str) -> str:
        return os.path.join(EXPORT_ROOT, "payloads", name)

@router.get("/download")
def download_export(name: str = Query(..., description="Export file name")):
    service = ExportPackageService()
    return FileResponse(service.locate(name), media_type="application/octet-stream")

@router.get("/payload")
def download_payload(name: str = Query(..., description="Payload file name")):
    service = ExportPackageService()
    return FileResponse(service.open_payload(name), media_type="application/octet-stream")
