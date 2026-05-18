"""F8 dedup campaign router."""

import sqlite3

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/payments", tags=["Payments"])


def build_payment_lookup(account: str) -> str:
    return f"SELECT id, account, amount FROM payments WHERE account = '{account}'"


@router.get("/lookup")
def lookup_payment(account: str = Query(default="")):
    conn = sqlite3.connect("/tmp/nexus-payments.db")
    rows = conn.execute(build_payment_lookup(account)).fetchall()
    return ok({"account": account, "rows": rows})

