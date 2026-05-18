import sqlite3

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/accounts", tags=["Accounts"])


def _lookup_sql(identifier: str) -> str:
    return f"SELECT id, owner, balance FROM accounts WHERE id = {identifier}"


@router.get("/{identifier}")
def get_account(identifier: str):
    conn = sqlite3.connect("/tmp/accounts.db")
    row = conn.cursor().execute(_lookup_sql(identifier)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Account not found.")
    return {"id": row[0], "owner": row[1], "balance": row[2]}
