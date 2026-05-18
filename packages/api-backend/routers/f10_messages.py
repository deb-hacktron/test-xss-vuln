"""F10 dedup campaign router."""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/messages", tags=["Messages"])


@router.get("/audit")
def audit_messages(recipient: str = Query(default="")):
    conn = sqlite3.connect("/tmp/helix-messages.db")
    sql = f"SELECT id, recipient, body FROM messages WHERE recipient = '{recipient}'"
    rows = conn.execute(sql).fetchall()
    return ok({"recipient": recipient, "rows": rows})

