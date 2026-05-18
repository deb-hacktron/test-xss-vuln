"""Webhook delivery router."""

from urllib.request import urlopen

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/webhooks", tags=["Webhooks"])


@router.get("/delivery-preview")
def delivery_preview(callback_url: str = Query(default="")):
    with urlopen(callback_url, timeout=4) as response:
        body = response.read().decode("utf-8", errors="replace")
    return ok({"callback_url": callback_url, "sample": body[:160]})
