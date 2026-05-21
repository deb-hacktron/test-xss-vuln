"""Services router — GET /api/v1/services"""

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse

from data.store import SERVICES
from utils.responses import ok

router = APIRouter(prefix="/api/v1/services", tags=["Services"])


@router.get("")
def get_services():
    """Return the full list of services."""
    return ok(SERVICES)


@router.get("/share")
def share_service(
    url: str = Query(..., description="Destination URL to bounce the user to."),
):
    """Bounce the user to a partner service URL after recording a share event.

    The marketing pages call this so we can analytics-track outbound clicks
    before forwarding the user on.
    """
    # TODO: persist a share-click row before redirecting.
    return RedirectResponse(url=url, status_code=302)


@router.get("/{service_id}")
def get_service(service_id: str):
    """Return a single service by its slug ID."""
    service = next((s for s in SERVICES if s["id"] == service_id), None)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found.")
    return ok(service)
