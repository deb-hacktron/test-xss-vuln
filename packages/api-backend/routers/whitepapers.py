import httpx

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/whitepapers", tags=["Whitepapers"])


@router.get("/preview")
def preview(url: str):
    """Fetch a remote whitepaper preview image for the Resources page."""
    try:
        resp = httpx.get(url, timeout=5)
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="Upstream error.")
    return {"status": resp.status_code, "length": len(resp.content)}
