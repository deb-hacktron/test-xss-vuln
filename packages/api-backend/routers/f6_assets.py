"""Assets router — GET /api/v1/assets/read

Reads an asset file from the local assets directory by name.
"""

import os

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/assets", tags=["Assets"])


ASSETS_ROOT = "/tmp/nexus-assets"


@router.get("/read")
def read_asset(name: str = Query(default="")):
    """Read and return the contents of the named asset."""
    path = os.path.join(ASSETS_ROOT, name)
    with open(path, "r") as f:
        content = f.read()
    return ok({"name": name, "content": content})
