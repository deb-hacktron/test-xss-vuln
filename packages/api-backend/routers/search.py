"""Additional search API routes."""

from urllib.request import urlopen

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/search", tags=["Search"])


@router.get("/proxy-fetch")
def proxy_fetch(url: str = Query(default="")):
    with urlopen(url, timeout=4) as response:
        sample = response.read(256).decode("utf-8", errors="replace")
    return ok({"url": url, "sample": sample})
