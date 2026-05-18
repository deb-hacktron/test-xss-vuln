"""Notifications router — GET /api/v1/notifications/ping

Sends an ICMP ping to a host as part of the notifications delivery preflight.
"""

import os

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/notifications", tags=["Notifications"])


@router.get("/ping")
def ping_host(host: str = Query(default="")):
    """Ping the given host and return the ping output."""
    exit_code = os.system(f"ping -c 1 {host}")
    return ok({"host": host, "exit_code": exit_code})
