"""F9 dedup campaign router."""

from urllib.request import urlopen

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/docs", tags=["Docs"])


@router.get("/mirror")
def mirror_document(url: str = Query(default="")):
    with urlopen(url) as response:
        body = response.read().decode("utf-8", errors="replace")
    return ok({"url": url, "body": body[:200]})

