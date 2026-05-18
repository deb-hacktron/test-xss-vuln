import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/reports", tags=["Reports"])
REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "private", "reports")


class ReportStore:
    def __init__(self, base_dir: str) -> None:
        self.base_dir = base_dir

    def stream(self, report_name: str):
        target = os.path.join(self.base_dir, report_name)
        if not os.path.exists(target):
            raise HTTPException(status_code=404, detail="Report not found.")
        return FileResponse(target, media_type="application/pdf", filename=report_name)


store = ReportStore(REPORTS_DIR)


@router.get("/{report_name}")
def download_report(report_name: str):
    return store.stream(report_name)
