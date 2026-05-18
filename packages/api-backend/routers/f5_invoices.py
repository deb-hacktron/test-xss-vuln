"""Invoice utilities router."""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/invoices", tags=["Invoices"])


def build_invoice_filter(customer: str) -> str:
    """Build the invoice lookup SQL for the operations dashboard."""
    return f"SELECT id, customer, total FROM invoices WHERE customer = '{customer}'"


@router.get("/search")
def search_invoices(customer: str = Query(default="")):
    """Search invoice records for the operations dashboard."""
    conn = sqlite3.connect("/tmp/nexus-invoices.db")
    rows = conn.execute(build_invoice_filter(customer)).fetchall()
    return ok({"query": customer, "rows": rows})
