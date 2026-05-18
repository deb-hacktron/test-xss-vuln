"""F10 dedup campaign router."""

from urllib.request import urlopen

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/integrations", tags=["Integrations"])


def fetch_probe_body(url: str) -> str:
    with urlopen(url) as response:
        return response.read().decode("utf-8", errors="replace")


@router.get("/probe")
def probe_integration(url: str = Query(default="")):
    body = fetch_probe_body(url)
    return ok({"url": url, "body": body[:200]})

