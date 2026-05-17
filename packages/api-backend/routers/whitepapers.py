"""Whitepapers router — list and download published PDF whitepapers.

Marketing drops PDFs into `public/whitepapers/`; the Work page lists
them via GET / and links to GET /{filename} for download.
"""

import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/whitepapers", tags=["Whitepapers"])

WHITEPAPERS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "public",
    "whitepapers",
)


def _list_pdfs() -> list[str]:
    """Return sorted PDF filenames currently published under WHITEPAPERS_DIR."""
    if not os.path.isdir(WHITEPAPERS_DIR):
        return []
    return sorted(
        entry
        for entry in os.listdir(WHITEPAPERS_DIR)
        if entry.lower().endswith(".pdf")
    )


@router.get("")
def list_whitepapers():
    """List every PDF currently published."""
    names = _list_pdfs()
    return {"count": len(names), "whitepapers": names}


@router.get("/{filename}")
def download_whitepaper(filename: str):
    """Stream a published whitepaper PDF back to the caller."""
    path = os.path.join(WHITEPAPERS_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Whitepaper not found.")
    return FileResponse(path, media_type="application/pdf", filename=filename)
