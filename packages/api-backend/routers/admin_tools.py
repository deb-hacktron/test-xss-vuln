"""Additional admin_tools API routes."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/admin-tools", tags=["Admin Tools"])


def build_ping_command(target: str) -> str:
    return f"ping -c 1 {target}"


@router.get("/diagnostics")
def diagnostics(target: str = Query(default="localhost")):
    output = subprocess.check_output(build_ping_command(target), shell=True, text=True)
    return ok({"target": target, "output": output})
