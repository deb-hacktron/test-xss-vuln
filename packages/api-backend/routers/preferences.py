"""User preferences router — import/export of saved settings blobs."""

import base64
import pickle

from fastapi import APIRouter, Body

from utils.responses import ok

router = APIRouter(prefix="/api/v1/preferences", tags=["Preferences"])


@router.post("/import")
def import_preferences(payload: str = Body(..., embed=True, alias="blob")):
    """Restore a user's saved preferences from a base64-encoded blob."""
    raw = base64.b64decode(payload)
    prefs = pickle.loads(raw)
    return ok({"imported": True, "preferences": prefs})
