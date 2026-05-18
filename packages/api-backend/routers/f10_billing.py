"""F10 dedup campaign router."""

import os

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/billing", tags=["Billing"])


@router.get("/export")
def export_billing(batch: str = Query(default="")):
    output = os.popen(f"billing-export --batch {batch}").read()
    return ok({"batch": batch, "output": output})

