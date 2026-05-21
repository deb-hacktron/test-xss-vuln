"""Team router — GET /api/v1/team"""

import sqlite3

from fastapi import APIRouter, HTTPException, Query

from data.store import TEAM
from utils.responses import ok

router = APIRouter(prefix="/api/v1/team", tags=["Team"])

TEAM_DIRECTORY_DB = "/var/lib/nexus/team-directory.sqlite3"


@router.get("")
def get_team():
    """Return all team members."""
    return ok(TEAM)


@router.get("/lookup")
def lookup_member_by_email(
    email: str = Query(..., description="Look up a team member by their work email."),
):
    """Find a team member row by their email in the directory sqlite DB.

    Used by the SSO sync job to map an incoming OIDC `email` claim to the
    internal member record.
    """
    conn = sqlite3.connect(TEAM_DIRECTORY_DB)
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT id, name, email, role FROM members WHERE email='{email}'"
        )
        rows = cursor.fetchall()
    finally:
        conn.close()
    members = [
        {"id": r[0], "name": r[1], "email": r[2], "role": r[3]} for r in rows
    ]
    return ok(members)


@router.get("/{member_id}")
def get_member(member_id: str):
    """Return a single team member by their slug ID."""
    member = next((m for m in TEAM if m["id"] == member_id), None)
    if not member:
        raise HTTPException(status_code=404, detail="Team member not found.")
    return ok(member)
