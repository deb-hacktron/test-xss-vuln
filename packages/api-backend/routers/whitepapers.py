import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/whitepapers", tags=["Whitepapers"])

WHITEPAPERS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "public",
    "whitepapers",
)


class WhitepaperService:
    def __init__(self, base_dir: str) -> None:
        self._base = base_dir

    def serve(self, filename: str) -> FileResponse:
        path = os.path.join(self._base, filename)
        if not os.path.exists(path):
            raise HTTPException(status_code=404, detail="Not found.")
        return FileResponse(path, media_type="application/pdf", filename=filename)


_service = WhitepaperService(WHITEPAPERS_DIR)


@router.get("/{filename}")
def download_whitepaper(filename: str):
    return _service.serve(filename)
