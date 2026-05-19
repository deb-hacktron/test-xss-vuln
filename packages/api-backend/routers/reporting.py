"""Additional reporting API routes."""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/reporting", tags=["Reporting"])


@router.get("/account-lookup")
def account_lookup(account: str = Query(default="")):
    conn = sqlite3.connect("/tmp/nexus-reporting.db")
    sql = f"SELECT id, balance, tier FROM accounts WHERE account_id = '{account}'"
    rows = conn.execute(sql).fetchall()
    return ok({"account": account, "rows": rows})
