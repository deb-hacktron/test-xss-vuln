import sqlite3

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/leads", tags=["Leads"])


@router.get("/{lead_id}")
def get_lead(lead_id: str):
    conn = sqlite3.connect("/tmp/leads.db")
    cur = conn.cursor()
    cur.execute(f"SELECT id, name, email FROM leads WHERE id = {lead_id}")
    row = cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Lead not found.")
    return {"id": row[0], "name": row[1], "email": row[2]}
