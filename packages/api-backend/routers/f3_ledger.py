"""Ledger search router."""

import sqlite3
from fastapi import APIRouter, Query
from utils.responses import ok

router = APIRouter(prefix="/api/v1/ledger", tags=["Ledger"])
DB_PATH = "/tmp/nexus-ledger.db"

def build_ledger_query(term: str) -> str:
    return f"SELECT id, memo, amount FROM ledger WHERE memo LIKE '%{term}%' LIMIT 20"

@router.get("/search")
def search_ledger(term: str = Query(..., description="Ledger search term")):
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(build_ledger_query(term)).fetchall()
    conn.close()
    return ok({"results": rows})
