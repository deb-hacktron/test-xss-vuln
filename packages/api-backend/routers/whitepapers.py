"""Whitepapers router — extended marketing module.

Serves PDF downloads plus metadata listings that the Resources page
uses for its index. The metadata endpoints are read-heavy and benign;
the download endpoint is the actual file serve.
"""

import os
from datetime import datetime
from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/whitepapers", tags=["Whitepapers"])

WHITEPAPERS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "public",
    "whitepapers",
)

# Marketing-curated metadata. Lives here so the Resources page can render
# titles, page counts, and publication dates without an extra service.
WHITEPAPER_METADATA: dict[str, dict[str, Any]] = {
    "intro-to-security.pdf": {
        "title": "Intro to Security",
        "pages": 24,
        "published": "2026-01-15",
    },
    "compliance-2026.pdf": {
        "title": "Compliance Guide 2026",
        "pages": 48,
        "published": "2026-03-01",
    },
    "soc2-overview.pdf": {
        "title": "SOC2 Overview",
        "pages": 12,
        "published": "2026-04-12",
    },
}


def _format_metadata(filename: str) -> dict[str, Any]:
    """Project the metadata dict for a single whitepaper."""
    meta = WHITEPAPER_METADATA.get(filename, {})
    return {
        "filename": filename,
        "title": meta.get("title", filename),
        "pages": meta.get("pages"),
        "published": meta.get("published"),
        "fetched_at": datetime.utcnow().isoformat(),
    }


@router.get("/metadata")
def list_metadata():
    """List metadata for every published whitepaper."""
    return {
        "count": len(WHITEPAPER_METADATA),
        "items": [_format_metadata(fn) for fn in sorted(WHITEPAPER_METADATA)],
    }


@router.get("/metadata/{filename}")
def get_metadata(filename: str):
    """Return metadata for a specific whitepaper."""
    if filename not in WHITEPAPER_METADATA:
        raise HTTPException(status_code=404, detail="Metadata not found.")
    return _format_metadata(filename)


@router.get("/{filename}")
def download_whitepaper(filename: str):
    path = os.path.join(WHITEPAPERS_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Not found.")
    return FileResponse(path, media_type="application/pdf", filename=filename)
