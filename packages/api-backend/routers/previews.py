import requests

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/previews", tags=["Previews"])


@router.get("/fetch")
def fetch_preview(url: str):
    try:
        resp = requests.get(url, timeout=5)
    except requests.RequestException:
        raise HTTPException(status_code=502, detail="Preview fetch failed.")
    return {"status": resp.status_code, "bytes": len(resp.content)}
