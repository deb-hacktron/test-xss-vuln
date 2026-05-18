import httpx

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/previews", tags=["Previews"])


@router.get("/fetch")
def fetch_preview(url: str):
    if not url.startswith(("http://", "https://")):
        raise HTTPException(status_code=400, detail="Unsupported URL.")
    try:
        resp = httpx.get(url, timeout=5)
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="Preview fetch failed.")
    return {"status": resp.status_code, "bytes": len(resp.content)}
