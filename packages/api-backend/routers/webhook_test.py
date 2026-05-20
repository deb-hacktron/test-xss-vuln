"""Additional webhook_test API routes."""

import requests

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/webhook-test", tags=["Webhook Test"])


@router.get("/probe")
def probe(url: str = Query(default="")):
    response = requests.get(url, timeout=3)
    sample = response.text[:256]
    return ok({"url": url, "sample": sample})
