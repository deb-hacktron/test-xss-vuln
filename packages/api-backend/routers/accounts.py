import sqlite3

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/accounts", tags=["Accounts"])


@router.get("/{account_id}")
def get_account(account_id: str):
    try:
        numeric_id = int(account_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid account id.")
    conn = sqlite3.connect("/tmp/accounts.db")
    row = conn.cursor().execute(f"SELECT id, owner, balance FROM accounts WHERE id = {numeric_id}").fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Account not found.")
    return {"id": row[0], "owner": row[1], "balance": row[2]}
