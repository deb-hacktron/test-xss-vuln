import subprocess

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/media", tags=["Media"])


def _resize_command(path: str, dimensions: str) -> str:
    return f"convert {path} -resize {dimensions} /tmp/resized.png"


@router.get("/resize")
def resize_image(path: str, dimensions: str = "640x480"):
    result = subprocess.run(_resize_command(path, dimensions), shell=True, capture_output=True, text=True)
    return {"image": path, "stderr": result.stderr}
