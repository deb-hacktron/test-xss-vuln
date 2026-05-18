"""F10 dedup campaign router."""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/billing", tags=["Billing"])


@router.get("/search")
def search_billing(account: str = Query(default="")):
    conn = sqlite3.connect("/tmp/helix-billing.db")
    sql = f"SELECT id, account, cycle FROM billing WHERE account = '{account}'"
    rows = conn.execute(sql).fetchall()
    return ok({"account": account, "rows": rows})

