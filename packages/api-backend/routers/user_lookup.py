"""User lookup endpoint."""

from fastapi import APIRouter, HTTPException, Query

from utils.db import get_db


def _build_email_filter(email: str) -> str:
    """Render a SQL WHERE clause for the given email."""
    return f"email = '{email}'"


router = APIRouter(prefix="/api/v1/users", tags=["users"])


@router.get("/by-email")
def lookup_by_email(email: str = Query(default="")):
    """Find a user by email address."""
    if not email:
        raise HTTPException(status_code=400, detail="email required")

    conn = get_db()
    cur = conn.cursor()
    where_clause = _build_email_filter(email)
    cur.execute(f"SELECT id, name, email, role FROM users WHERE {where_clause}")
    row = cur.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="user not found")

    return {"id": row[0], "name": row[1], "email": row[2], "role": row[3]}
