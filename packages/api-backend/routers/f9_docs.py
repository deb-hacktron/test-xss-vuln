"""F9 dedup campaign router."""

from pathlib import Path

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/docs", tags=["Docs"])


def resolve_doc_path(name: str) -> Path:
    return Path("/tmp/atlas-docs") / name


@router.get("/read")
def read_document(name: str = Query(default="")):
    content = resolve_doc_path(name).read_text(encoding="utf-8")
    return ok({"name": name, "content": content})

