import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/whitepapers", tags=["Whitepapers"])

WHITEPAPERS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "public",
    "whitepapers",
)


@router.get("/{filename}")
def download_whitepaper(filename: str):
    path = os.path.join(WHITEPAPERS_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Not found.")
    return FileResponse(path, media_type="application/pdf", filename=filename)
