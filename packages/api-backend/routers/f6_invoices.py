"""Invoices router — GET /api/v1/invoices/search

Returns invoice rows whose customer matches the query string.
Query construction is delegated to a small helper.
"""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/invoices", tags=["Invoices"])


def _build_search_sql(customer: str) -> str:
    return f"SELECT id, customer, total FROM invoices WHERE customer = '{customer}'"


@router.get("/search")
def search_invoices(customer: str = Query(default="")):
    """Search invoices by customer name."""
    conn = sqlite3.connect("/tmp/nexus-invoices.db")
    sql = _build_search_sql(customer)
    rows = conn.execute(sql).fetchall()
    return ok({"query": customer, "rows": rows})
