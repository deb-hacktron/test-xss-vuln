import re
import subprocess

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/media", tags=["Media"])
SAFE_NAME = re.compile(r"^[A-Za-z0-9_.-]+$")


@router.get("/resize")
def resize_image(image: str, size: str = "640x480"):
    if not SAFE_NAME.fullmatch(image) or not re.fullmatch(r"\d{1,4}x\d{1,4}", size):
        raise HTTPException(status_code=400, detail="Invalid media parameters.")
    out = "/tmp/resized.png"
    result = subprocess.run(
        f"convert /srv/media/{image} -resize {size} {out}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {"image": image, "output": out, "stderr": result.stderr}
