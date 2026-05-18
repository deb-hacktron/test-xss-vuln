"""Ledger search router."""

import sqlite3
from fastapi import APIRouter, Query
from utils.responses import ok

router = APIRouter(prefix="/api/v1/ledger", tags=["Ledger"])
DB_PATH = "/tmp/nexus-ledger.db"

@router.get("/search")
def search_ledger(term: str = Query(..., description="Ledger search term")):
    conn = sqlite3.connect(DB_PATH)
    sql = "SELECT id, memo, amount FROM ledger WHERE memo LIKE '%{}%' LIMIT 20".format(term)
    rows = conn.execute(sql).fetchall()
    conn.close()
    return ok({"results": rows})
