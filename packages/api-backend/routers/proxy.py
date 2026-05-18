import httpx

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/proxy", tags=["Proxy"])


@router.get("/fetch")
def fetch_preview(url: str):
    try:
        resp = httpx.get(url, timeout=5)
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="Preview fetch failed.")
    return {"status": resp.status_code, "bytes": len(resp.content)}
