import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/reports", tags=["Reports"])
REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "private", "reports")
REPORT_FILES = {"q1": "q1.pdf", "q2": "q2.pdf"}


@router.get("/{report_id}")
def download_report(report_id: str):
    filename = REPORT_FILES.get(report_id)
    if not filename:
        raise HTTPException(status_code=404, detail="Report not found.")
    return FileResponse(os.path.join(REPORTS_DIR, filename), media_type="application/pdf", filename=filename)
