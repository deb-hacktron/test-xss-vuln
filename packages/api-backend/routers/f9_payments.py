"""F9 dedup campaign router."""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/payments", tags=["Payments"])


@router.get("/lookup")
def lookup_payment(account: str = Query(default="")):
    conn = sqlite3.connect("/tmp/atlas-payments.db")
    sql = f"SELECT id, account, amount FROM payments WHERE account = '{account}'"
    rows = conn.execute(sql).fetchall()
    return ok({"account": account, "rows": rows})

