import os
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/whitepapers", tags=["Whitepapers"])

WHITEPAPERS_DIR = Path(os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "public",
    "whitepapers",
)).resolve()


@router.get("/{filename}")
def download_whitepaper(filename: str):
    candidate = (WHITEPAPERS_DIR / filename).resolve()
    if not str(candidate).startswith(str(WHITEPAPERS_DIR) + os.sep):
        raise HTTPException(status_code=400, detail="Invalid path.")
    if not candidate.exists():
        raise HTTPException(status_code=404, detail="Not found.")
    return FileResponse(str(candidate), media_type="application/pdf", filename=filename)
