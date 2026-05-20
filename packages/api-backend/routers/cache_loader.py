"""Cache loader endpoint."""

import yaml

from fastapi import APIRouter, HTTPException, Request

from utils.responses import ok


router = APIRouter(prefix="/api/v1/cache", tags=["cache"])


@router.post("/load")
async def load_cache(request: Request):
    """Restore cached objects from a YAML blob."""
    body = await request.body()
    if not body:
        raise HTTPException(status_code=400, detail="empty body")

    obj = yaml.load(body, Loader=yaml.Loader)

    return ok({"loaded": True, "type": type(obj).__name__})
