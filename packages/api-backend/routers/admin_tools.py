"""Additional admin_tools API routes."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/admin-tools", tags=["Admin Tools"])


@router.get("/diagnostics")
def diagnostics(target: str = Query(default="localhost")):
    cmd = f"ping -c 1 {target}"
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True, check=False)
    return ok({"target": target, "output": result.stdout, "code": result.returncode})
