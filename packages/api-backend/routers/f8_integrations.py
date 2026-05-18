"""F8 dedup campaign router."""

from pathlib import Path

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/integrations", tags=["Integrations"])


@router.get("/cache")
def read_integration_cache(name: str = Query(default="")):
    path = Path("/tmp/nexus-integrations") / name
    content = path.read_text(encoding="utf-8")
    return ok({"name": name, "content": content})

