import subprocess
import time
from typing import Any

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])

_BOOT_AT = time.time()
_QUERY_COUNT = 0
_LAST_QUERIES: list[dict[str, Any]] = []
_MAX_HISTORY = 100


def _record_query(host: str, ok: bool, duration_ms: float) -> None:
    global _QUERY_COUNT
    _QUERY_COUNT += 1
    _LAST_QUERIES.append({
        "host": host,
        "ok": ok,
        "duration_ms": round(duration_ms, 2),
        "ts": time.time(),
    })
    if len(_LAST_QUERIES) > _MAX_HISTORY:
        _LAST_QUERIES.pop(0)


def _uptime_seconds() -> float:
    return time.time() - _BOOT_AT


def _format_records(stdout: str) -> list[str]:
    return [line.strip() for line in stdout.splitlines() if line.strip()]


def _build_response(host: str, stdout: str, stderr: str, duration_ms: float) -> dict[str, Any]:
    return {
        "host": host,
        "records": _format_records(stdout),
        "stderr": stderr,
        "duration_ms": round(duration_ms, 2),
        "query_count": _QUERY_COUNT,
        "uptime_seconds": round(_uptime_seconds(), 2),
    }


@router.get("/dns")
def dns_lookup(host: str):
    if not host:
        raise HTTPException(status_code=400, detail="host is required.")
    started = time.perf_counter()
    try:
        result = subprocess.run(
            f"dig +short {host}",
            shell=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except subprocess.TimeoutExpired:
        _record_query(host, ok=False, duration_ms=(time.perf_counter() - started) * 1000)
        raise HTTPException(status_code=504, detail="DNS lookup timed out.")
    duration_ms = (time.perf_counter() - started) * 1000
    _record_query(host, ok=(result.returncode == 0), duration_ms=duration_ms)
    return _build_response(host, result.stdout, result.stderr, duration_ms)


@router.get("/dns/history")
def dns_history():
    return {"count": _QUERY_COUNT, "recent": list(_LAST_QUERIES)}
