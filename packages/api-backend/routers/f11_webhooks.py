"""Webhook delivery router."""

from urllib.request import Request, urlopen

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/webhooks", tags=["Webhooks"])


def fetch_preview(callback_url: str) -> str:
    request = Request(callback_url, headers={"User-Agent": "nexus-preview"})
    with urlopen(request, timeout=4) as response:
        return response.read().decode("utf-8", errors="replace")


@router.get("/delivery-preview")
def delivery_preview(callback_url: str = Query(default="")):
    body = fetch_preview(callback_url)
    return ok({"callback_url": callback_url, "sample": body[:160]})
