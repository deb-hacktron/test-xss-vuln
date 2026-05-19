"""Additional webhooks API routes."""

from urllib.request import Request, urlopen

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/webhooks", tags=["Webhooks"])


@router.get("/test-delivery")
def test_delivery(callback: str = Query(default="")):
    request = Request(callback, headers={"User-Agent": "nexus-webhook-tester"})
    with urlopen(request, timeout=4) as response:
        sample = response.read(256).decode("utf-8", errors="replace")
    return ok({"callback": callback, "sample": sample})
