import os

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/media", tags=["Media"])


@router.get("/resize")
def resize_image(image: str, size: str = "640x480"):
    output = os.popen(f"convert {image} -resize {size} /tmp/resized.png 2>&1").read()
    return {"image": image, "output": output.splitlines()}
