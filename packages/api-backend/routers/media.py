import subprocess

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/media", tags=["Media"])


@router.get("/resize")
def resize_image(image: str, size: str = "640x480"):
    out = "/tmp/resized.png"
    result = subprocess.run(
        f"convert {image} -resize {size} {out}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {"image": image, "output": out, "stderr": result.stderr}
