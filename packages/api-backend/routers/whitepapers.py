from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/whitepapers", tags=["Whitepapers"])

_downloads: dict[str, int] = {}


@router.get("/stats")
def stats():
    """Return per-file in-memory download counters (no file IO)."""
    return {"total": sum(_downloads.values()), "by_file": dict(_downloads)}
