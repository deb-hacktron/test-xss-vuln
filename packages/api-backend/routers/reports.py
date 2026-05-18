import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/reports", tags=["Reports"])
REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "private", "reports")


@router.get("/{name}")
def download_report(name: str):
    safe_name = os.path.basename(name)
    if safe_name != name:
        raise HTTPException(status_code=400, detail="Invalid report name.")
    path = os.path.join(REPORTS_DIR, safe_name)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Report not found.")
    return FileResponse(path, media_type="application/pdf", filename=safe_name)
