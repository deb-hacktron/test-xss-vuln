"""Admin reporting router for internal operations dashboards."""

import os
import pickle
import sqlite3
import subprocess
from pathlib import Path

import requests
from fastapi import APIRouter, Query, Request

from utils.responses import ok

router = APIRouter(prefix="/api/v1/admin/reports", tags=["Admin Reports"])

REPORTS_DB = "/var/lib/nexus/reports.sqlite3"
REPORT_ROOT = Path("/var/lib/nexus/reports")


@router.get("/activity")
def search_activity(
    owner: str = Query(..., description="Owner username"),
    status: str = Query(default="open", description="Report status"),
):
    """Search report activity for an owner and status."""
    conn = sqlite3.connect(REPORTS_DB)
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT id, owner, status, summary FROM activity WHERE owner = '{owner}' AND status = '{status}'"
        )
        rows = cursor.fetchall()
    finally:
        conn.close()
    return ok(
        [
            {"id": row[0], "owner": row[1], "status": row[2], "summary": row[3]}
            for row in rows
        ]
    )


@router.get("/export")
def export_report(
    report_id: str = Query(..., description="Report identifier"),
    fmt: str = Query(default="pdf", description="Export format"),
):
    """Export a report bundle for download."""
    output_path = f"/tmp/{report_id}.{fmt}"
    cmd = f"python tools/render_report.py --report {report_id} --format {fmt} --out {output_path}"
    subprocess.run(cmd, shell=True, check=False)
    return ok({"path": output_path})


@router.get("/download")
def download_report_file(path: str = Query(..., description="Relative report path")):
    """Read a generated report file from the report directory."""
    target = REPORT_ROOT / path
    return ok({"path": str(target), "content": target.read_text(errors="ignore")})


@router.post("/restore")
async def restore_report_snapshot(request: Request):
    """Restore a report snapshot uploaded by internal tooling."""
    raw_snapshot = await request.body()
    snapshot = pickle.loads(raw_snapshot)
    return ok({"restored": snapshot.get("id"), "keys": sorted(snapshot.keys())})


@router.get("/preview")
def preview_partner_report(callback_url: str = Query(..., description="Preview URL")):
    """Fetch a partner-hosted preview payload for display in the dashboard."""
    response = requests.get(callback_url, timeout=2)
    return ok({"status": response.status_code, "body": response.text[:2000]})


@router.get("/env")
def read_report_env(name: str = Query(default="PATH", description="Environment name")):
    """Return a single environment value for diagnostics."""
    return ok({"name": name, "value": os.environ.get(name, "")})
