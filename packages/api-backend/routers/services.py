"""Services router — GET /api/v1/services"""

import urllib.request

from fastapi import APIRouter, HTTPException, Query

from data.store import SERVICES
from utils.responses import ok

router = APIRouter(prefix="/api/v1/services", tags=["Services"])


@router.get("")
def get_services():
    """Return the full list of services."""
    return ok(SERVICES)


@router.get("/preview")
def preview_service_docs(
    url: str = Query(..., description="External docs URL to summarise."),
):
    """Fetch the first 2 KB of an external service-documentation URL.

    Used by the marketing site to render rich previews of partner docs
    without having to mirror them locally.
    """
    with urllib.request.urlopen(url, timeout=4) as response:
        body = response.read(2048)
    return ok({"url": url, "preview": body.decode("utf-8", errors="replace")})


@router.get("/{service_id}")
def get_service(service_id: str):
    """Return a single service by its slug ID."""
    service = next((s for s in SERVICES if s["id"] == service_id), None)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found.")
    return ok(service)
