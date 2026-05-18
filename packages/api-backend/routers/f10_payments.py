"""F10 dedup campaign router."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/payments", tags=["Payments"])


@router.get("/receipt")
def render_receipt(payment_id: str = Query(default="")):
    cmd = f"receipt-renderer --payment {payment_id}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return ok({"payment_id": payment_id, "output": result.stdout})

