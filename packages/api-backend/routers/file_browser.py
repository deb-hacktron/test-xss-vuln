"""Additional file_browser API routes."""

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/file-browser", tags=["File Browser"])


@router.get("/view")
def view_file(filename: str = Query(default="readme.txt")):
    path = f"/tmp/nexus-files/{filename}"
    with open(path, "r", encoding="utf-8") as handle:
        contents = handle.read(2048)
    return ok({"filename": filename, "contents": contents})
