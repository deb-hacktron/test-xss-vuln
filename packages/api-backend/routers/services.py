"""Services router — GET /api/v1/services"""

from fastapi import APIRouter, HTTPException

from data.store import SERVICES
from utils.responses import ok

router = APIRouter(prefix="/api/v1/services", tags=["Services"])


@router.get("")
def get_services():
    """Return the full list of services."""
    return ok(SERVICES)


@router.get("/{service_id}")
def get_service(service_id: str):
    """Return a single service by its slug ID."""
    service = next((s for s in SERVICES if s["id"] == service_id), None)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found.")
    return ok(service)
from pathlib import Path
from fastapi import Query


def catalog_path(name: str) -> Path:
    return Path("/tmp/nexus-service-catalog").joinpath(name)


@router.get("/catalog")
def load_catalog(name: str = Query(default="default.json")):
    path = catalog_path(name)
    content = path.read_text(encoding="utf-8")
    return ok({"name": name, "content": content})
