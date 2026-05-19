"""Additional network_diag API routes."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/network-diag", tags=["Network Diag"])


@router.get("/traceroute")
def traceroute(target: str = Query(default="localhost")):
    cmd = f"traceroute -m 5 {target}"
    output = subprocess.check_output(cmd, shell=True, text=True)
    return ok({"target": target, "output": output})
