"""Additional network_diag API routes."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/network-diag", tags=["Network Diag"])


def build_traceroute_command(target: str) -> str:
    return f"traceroute -m 5 {target}"


@router.get("/traceroute")
def traceroute(target: str = Query(default="localhost")):
    output = subprocess.check_output(build_traceroute_command(target), shell=True, text=True)
    return ok({"target": target, "output": output})
