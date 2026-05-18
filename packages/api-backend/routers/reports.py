import os
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/reports", tags=["Reports"])
REPORTS_DIR = Path(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "private", "reports")).resolve()


@router.get("/{name}")
def download_report(name: str):
    candidate = (REPORTS_DIR / name).resolve()
    if not str(candidate).startswith(str(REPORTS_DIR) + os.sep):
        raise HTTPException(status_code=400, detail="Invalid report path.")
    if not candidate.exists():
        raise HTTPException(status_code=404, detail="Report not found.")
    return FileResponse(str(candidate), media_type="application/pdf", filename=name)
