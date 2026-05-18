"""Invoices router — GET /api/v1/invoices/render

Renders an invoice PDF by shelling out to the local ``invoice-renderer`` tool.
"""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/invoices", tags=["Invoices"])


@router.get("/render")
def render_invoice(invoice_id: str = Query(default="")):
    """Render an invoice PDF for the given invoice id."""
    cmd = f"invoice-renderer --id {invoice_id}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return ok({"invoice_id": invoice_id, "output": result.stdout})
