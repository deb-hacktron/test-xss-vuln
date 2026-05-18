"""Ledger search router."""

import sqlite3
from fastapi import APIRouter, Query
from utils.responses import ok

router = APIRouter(prefix="/api/v1/ledger", tags=["Ledger"])
DB_PATH = "/tmp/nexus-ledger.db"

@router.get("/account")
def get_account(account_id: int = Query(..., description="Ledger account id")):
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute("SELECT id, owner_email, balance FROM accounts WHERE id = ?", (account_id,)).fetchone()
    conn.close()
    return ok({"account": row})
