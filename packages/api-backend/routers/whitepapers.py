"""Whitepapers router — search and download published PDFs.

Used by the Resources page to let visitors filter the published
whitepapers by filename substring and download a specific PDF.
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


def _filter_pdfs(query: str) -> list[str]:
    """Return PDF filenames whose name contains `query` (case-insensitive)."""
    if not os.path.isdir(WHITEPAPERS_DIR):
        return []
    q = query.lower()
    return sorted(
        entry
        for entry in os.listdir(WHITEPAPERS_DIR)
        if entry.lower().endswith(".pdf") and q in entry.lower()
    )


@router.get("/search")
def search_whitepapers(q: str = ""):
    """Filter published whitepapers by filename substring."""
    matches = _filter_pdfs(q)
    return {"query": q, "count": len(matches), "matches": matches}


@router.get("/{filename}")
def download_whitepaper(filename: str):
    """Stream a published whitepaper PDF back to the caller."""
    path = os.path.join(WHITEPAPERS_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Whitepaper not found.")
    return FileResponse(path, media_type="application/pdf", filename=filename)
