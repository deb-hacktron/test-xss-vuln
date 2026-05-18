"""Notifications router — GET /api/v1/notifications/audit

Returns recent notification audit log rows for a given recipient.
"""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/notifications", tags=["Notifications"])


@router.get("/audit")
def audit_notifications(recipient: str = Query(default="")):
    """Return notification audit log rows for the recipient."""
    conn = sqlite3.connect("/tmp/nexus-notifications.db")
    sql = f"SELECT id, recipient, channel, sent_at FROM audit_log WHERE recipient = '{recipient}'"
    rows = conn.execute(sql).fetchall()
    return ok({"recipient": recipient, "rows": rows})
