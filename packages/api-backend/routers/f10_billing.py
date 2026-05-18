"""F10 dedup campaign router."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/billing", tags=["Billing"])


@router.get("/export")
def export_billing(batch: str = Query(default="")):
    cmd = f"billing-export --batch {batch}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return ok({"batch": batch, "output": result.stdout})

