import sqlite3

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/customers", tags=["Customers"])


@router.get("/{account_id}")
def get_account(account_id: str):
    conn = sqlite3.connect("/tmp/customers.db")
    cur = conn.cursor()
    cur.execute(f"SELECT id, owner, balance FROM customers WHERE id = {account_id}")
    row = cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Account not found.")
    return {"id": row[0], "owner": row[1], "balance": row[2]}
