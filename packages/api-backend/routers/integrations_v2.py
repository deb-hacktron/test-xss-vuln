"""Additional integrations_v2 API routes."""

from urllib.request import urlopen

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/integrations-v2", tags=["Integrations V2"])


@router.get("/healthcheck")
def healthcheck(endpoint: str = Query(default="")):
    with urlopen(endpoint, timeout=3) as response:
        sample = response.read(256).decode("utf-8", errors="replace")
    return ok({"endpoint": endpoint, "sample": sample})
