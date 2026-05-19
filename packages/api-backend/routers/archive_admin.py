"""Additional archive admin API routes."""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/archive-admin", tags=["Archive Admin"])


@router.get("/index-search")
def index_search(owner: str = Query(default="")):
    conn = sqlite3.connect("/tmp/archive-index.db")
    sql = f"SELECT archive_name, owner, created_at FROM archive_index WHERE owner = '{owner}'"
    rows = conn.execute(sql).fetchall()
    return ok({"owner": owner, "rows": rows})
