"""F8 dedup campaign router."""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/reports", tags=["Reports"])


@router.get("/lookup")
def lookup_report(owner: str = Query(default="")):
    conn = sqlite3.connect("/tmp/nexus-reports.db")
    sql = f"SELECT id, owner, name FROM reports WHERE owner = '{owner}'"
    rows = conn.execute(sql).fetchall()
    return ok({"owner": owner, "rows": rows})

