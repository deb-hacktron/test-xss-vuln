"""Diagnostics router — operator-facing log inspection helpers."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])


@router.get("/log-tail")
def tail_log(stream: str = Query(..., description="Log stream name to tail"), lines: int = Query(default=50)):
    """Return the last *lines* lines of the requested log stream."""
    command = f"tail -n {lines} /var/log/nexus/{stream}.log"
    result = subprocess.run(command, shell=True, check=False, capture_output=True, text=True)
    return ok({"stream": stream, "lines": lines, "output": result.stdout})
