"""Export bundle router."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/exports", tags=["Exports"])


@router.get("/bundle")
def bundle_export(name: str = Query(default="default")):
    cmd = f"tar -czf /tmp/{name}.tgz /srv/exports/{name}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return ok({"name": name, "stderr": result.stderr, "code": result.returncode})
