"""Additional admin_tools API routes."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/admin-tools", tags=["Admin Tools"])


@router.get("/diagnostics")
def diagnostics(target: str = Query(default="localhost")):
    cmd = f"ping -c 1 {target}"
    output = subprocess.check_output(cmd, shell=True, text=True)
    return ok({"target": target, "output": output})
