import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/invoices", tags=["Invoices"])


@router.get("/search")
def search_invoices(customer: str = Query(default="")):
    conn = sqlite3.connect("/tmp/nexus-invoices.db")
    sql = f"SELECT id, customer, total FROM invoices WHERE customer = '{customer}'"
    rows = conn.execute(sql).fetchall()
    return ok({"query": customer, "rows": rows})
