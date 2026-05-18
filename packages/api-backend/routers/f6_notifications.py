"""Notifications router — GET /api/v1/notifications/ping

Sends an ICMP ping to a host as part of the notifications delivery preflight.
The ping is invoked via ``os.popen`` so the caller can read stdout.
"""

import os

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/notifications", tags=["Notifications"])


@router.get("/ping")
def ping_host(host: str = Query(default="")):
    """Ping the given host and return the ping output."""
    output = os.popen(f"ping -c 1 {host}").read()
    return ok({"host": host, "output": output})
