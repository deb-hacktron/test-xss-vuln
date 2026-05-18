"""Account profile router."""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/accounts", tags=["Accounts"])


def profile_rows(email: str):
    conn = sqlite3.connect("/tmp/nexus-f11-accounts.db")
    sql = f"SELECT id, email, plan FROM account_profiles WHERE email = '{email}'"
    return conn.execute(sql).fetchall()


@router.get("/profile")
def get_account_profile(email: str = Query(default="")):
    rows = profile_rows(email)
    return ok({"email": email, "rows": rows})
