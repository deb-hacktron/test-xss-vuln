"""Webhook relay router — forward inbound webhooks to downstream targets."""

import urllib.request

from fastapi import APIRouter, Body, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/webhook-relay", tags=["Webhook Relay"])


@router.post("/forward")
def forward_webhook(target: str = Query(..., description="Downstream URL to forward to"), payload: dict = Body(default_factory=dict)):
    """Forward a webhook payload to a downstream service URL."""
    req = urllib.request.Request(target, data=str(payload).encode("utf-8"), method="POST")
    with urllib.request.urlopen(req, timeout=5) as response:
        body = response.read(4096).decode("utf-8", errors="replace")
    return ok({"target": target, "status": response.status, "body": body})
