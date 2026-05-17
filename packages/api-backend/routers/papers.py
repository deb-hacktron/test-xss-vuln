import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/papers", tags=["Papers"])

PAPERS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "public",
    "papers",
)


@router.get("/{filename}")
def download_paper(filename: str):
    path = os.path.join(PAPERS_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Not found.")
    return FileResponse(path, media_type="application/pdf", filename=filename)
