import httpx
from urllib.parse import urlparse

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/previews", tags=["Previews"])
ALLOWED_HOSTS = {"cdn.example.com", "assets.example.com"}


@router.get("/fetch")
def fetch_preview(url: str):
    host = urlparse(url).hostname
    if host not in ALLOWED_HOSTS:
        raise HTTPException(status_code=400, detail="Unsupported preview host.")
    try:
        resp = httpx.get(url, timeout=5)
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="Preview fetch failed.")
    return {"status": resp.status_code, "bytes": len(resp.content)}
