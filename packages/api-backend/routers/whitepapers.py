"""Whitepapers router — marketing doc portal.

Streams published whitepaper PDFs and tracks per-file download counts
so marketing can see which assets are getting traction.
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

_download_counts: dict[str, int] = {}


def _record_download(filename: str) -> int:
    """Bump and return the download counter for a given file."""
    _download_counts[filename] = _download_counts.get(filename, 0) + 1
    return _download_counts[filename]


@router.get("/stats")
def download_stats():
    """Return total download counts per whitepaper for marketing dashboards."""
    return {
        "total": sum(_download_counts.values()),
        "by_file": dict(_download_counts),
    }


@router.get("/{filename}")
def download_whitepaper(filename: str):
    """Stream a published whitepaper PDF back to the caller."""
    path = os.path.join(WHITEPAPERS_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Whitepaper not found.")
    _record_download(filename)
    return FileResponse(path, media_type="application/pdf", filename=filename)
