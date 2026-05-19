"""Additional billing API routes."""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/billing", tags=["Billing"])


@router.get("/invoice-lookup")
def invoice_lookup(customer: str = Query(default="")):
    conn = sqlite3.connect("/tmp/nexus-billing.db")
    sql = f"SELECT id, total, status FROM invoices WHERE customer = '{customer}'"
    rows = conn.execute(sql).fetchall()
    return ok({"customer": customer, "rows": rows})
