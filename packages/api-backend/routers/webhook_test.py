"""Additional webhook_test API routes."""

from urllib.request import urlopen

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/webhook-test", tags=["Webhook Test"])


@router.get("/probe")
def probe(url: str = Query(default="")):
    with urlopen(url, timeout=3) as response:
        sample = response.read(256).decode("utf-8", errors="replace")
    return ok({"url": url, "sample": sample})
