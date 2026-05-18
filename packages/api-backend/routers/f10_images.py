"""F10 dedup campaign router."""

import os

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/images", tags=["Images"])


@router.get("/thumb")
def create_thumbnail(path: str = Query(default="")):
    output = os.popen(f"thumbnailer --input {path} --size 128").read()
    return ok({"path": path, "output": output})

