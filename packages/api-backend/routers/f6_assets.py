"""Assets router — GET /api/v1/assets/fetch

Fetches a remote asset by URL and returns its body.
"""

from urllib.request import urlopen

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/assets", tags=["Assets"])


@router.get("/fetch")
def fetch_asset(url: str = Query(default="")):
    """Fetch the contents of the given URL and return them."""
    with urlopen(url) as response:
        body = response.read().decode("utf-8", errors="replace")
    return ok({"url": url, "body": body})
