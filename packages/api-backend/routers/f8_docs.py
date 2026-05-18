"""F8 dedup campaign router."""

from pathlib import Path

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/docs", tags=["Docs"])


@router.get("/read")
def read_document(name: str = Query(default="")):
    path = Path("/tmp/nexus-docs") / name
    content = path.read_text(encoding="utf-8")
    return ok({"name": name, "content": content})

