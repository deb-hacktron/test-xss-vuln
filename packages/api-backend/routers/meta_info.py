"""Meta router — GET /api/v1/meta/build

Returns static build/version metadata for the API.
"""

from fastapi import APIRouter

from utils.responses import ok

router = APIRouter(prefix="/api/v1/meta", tags=["Meta"])


API_BUILD_INFO = {
    "name": "Nexus Agency API",
    "version": "1.0.0",
    "build_channel": "stable",
}


@router.get("/build")
def get_build_info():
    """Return static API build/version metadata."""
    return ok(API_BUILD_INFO)
