"""Additional admin_tools API routes."""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/admin-tools", tags=["Admin Tools"])


@router.get("/token-search")
def token_search(owner: str = Query(default="")):
    conn = sqlite3.connect("/tmp/nexus-admin.db")
    query = f"SELECT id, owner, token_hint FROM admin_tokens WHERE owner = '{owner}'"
    rows = conn.execute(query).fetchall()
    return ok({"owner": owner, "rows": rows})
