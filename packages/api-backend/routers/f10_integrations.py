"""F10 dedup campaign router."""

from urllib.request import urlopen

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/integrations", tags=["Integrations"])


@router.get("/probe")
def probe_integration(url: str = Query(default="")):
    with urlopen(url) as response:
        body = response.read().decode("utf-8", errors="replace")
    return ok({"url": url, "body": body[:200]})

