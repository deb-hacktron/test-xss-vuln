import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/reports", tags=["Reports"])
REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "private", "reports")


def _report_path(slug: str) -> str:
    return os.path.join(REPORTS_DIR, slug)


@router.get("/{slug}")
def download_report(slug: str):
    target = _report_path(slug)
    if not os.path.exists(target):
        raise HTTPException(status_code=404, detail="Report not found.")
    return FileResponse(target, media_type="application/pdf", filename=slug)
