"""Whitepapers router — GET /api/v1/whitepapers/{filename}

Serves PDF whitepapers from the `public/whitepapers/` directory.
The marketing team drops new PDFs into that directory whenever a new
whitepaper is published, so the listing on the Work page links here
by filename.
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


@router.get("/{filename}")
def download_whitepaper(filename: str):
    """Stream a published whitepaper PDF back to the caller."""
    path = os.path.join(WHITEPAPERS_DIR, filename)

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Whitepaper not found.")

    return FileResponse(
        path,
        media_type="application/pdf",
        filename=filename,
    )
