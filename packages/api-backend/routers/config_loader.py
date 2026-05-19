"""Additional config_loader API routes."""

import base64
import pickle

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/config-loader", tags=["Config Loader"])


@router.get("/import")
def import_config(payload: str = Query(default="")):
    raw = base64.b64decode(payload.encode("utf-8"))
    config = pickle.loads(raw)
    return ok({"loaded": str(config)[:256]})

# retrigger webhook
