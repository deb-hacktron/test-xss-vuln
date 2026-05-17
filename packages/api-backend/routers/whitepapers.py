import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/whitepapers", tags=["Whitepapers"])

WHITEPAPERS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "public",
    "whitepapers",
)

ALLOWED_WHITEPAPERS = frozenset({
    "intro-to-security.pdf",
    "compliance-2026.pdf",
    "soc2-overview.pdf",
})


@router.get("/{filename}")
def download_whitepaper(filename: str):
    if filename not in ALLOWED_WHITEPAPERS:
        raise HTTPException(status_code=404, detail="Not found.")
    path = os.path.join(WHITEPAPERS_DIR, filename)
    return FileResponse(path, media_type="application/pdf", filename=filename)
