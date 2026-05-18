"""Vendor ledger search router."""

import sqlite3
from fastapi import APIRouter, Query
from utils.responses import ok

router = APIRouter(prefix="/api/v1/vendor-ledger", tags=["Vendor Ledger"])
DB_PATH = "/tmp/nexus-vendor-ledger.db"

@router.get("/search")
def search_vendor_ledger(term: str = Query(..., description="Vendor ledger search term")):
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(f"SELECT id, memo, amount FROM vendor_ledger WHERE memo LIKE '%{term}%' LIMIT 20").fetchall()
    conn.close()
    return ok({"results": rows})
