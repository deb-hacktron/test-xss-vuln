"""Assets router — GET /api/v1/assets/read

Reads an asset file from the local assets directory by name.
Path resolution is delegated to a small helper.
"""

import os

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/assets", tags=["Assets"])


ASSETS_ROOT = "/tmp/nexus-assets"


def _resolve_asset_path(name: str) -> str:
    return os.path.join(ASSETS_ROOT, name)


@router.get("/read")
def read_asset(name: str = Query(default="")):
    """Read and return the contents of the named asset."""
    path = _resolve_asset_path(name)
    with open(path, "r") as f:
        content = f.read()
    return ok({"name": name, "content": content})
