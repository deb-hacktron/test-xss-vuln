"""F10 dedup campaign router."""

import base64
import pickle

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/archives", tags=["Archives"])


@router.get("/restore")
def restore_archive(blob: str = Query(default="")):
    payload = base64.b64decode(blob)
    restored = pickle.loads(payload)
    return ok({"type": type(restored).__name__})

