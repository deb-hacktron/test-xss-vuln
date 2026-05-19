"""Additional ops API routes."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/ops", tags=["Operations"])


@router.get("/log-bundle")
def log_bundle(bundle: str = Query(default="app")):
    cmd = f"tar -czf /tmp/{bundle}.tgz /var/log/nexus/{bundle}"
    output = subprocess.check_output(cmd, shell=True, text=True)
    return ok({"bundle": bundle, "output": output})
