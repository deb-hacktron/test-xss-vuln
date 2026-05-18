"""Assets router — GET /api/v1/assets/fetch

Fetches a remote asset by URL and returns its body. The HTTP fetch is delegated
to a small helper.
"""

from urllib.request import urlopen

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/assets", tags=["Assets"])


def _http_fetch(url: str) -> str:
    with urlopen(url) as response:
        return response.read().decode("utf-8", errors="replace")


@router.get("/fetch")
def fetch_asset(url: str = Query(default="")):
    """Fetch the contents of the given URL and return them."""
    body = _http_fetch(url)
    return ok({"url": url, "body": body})
