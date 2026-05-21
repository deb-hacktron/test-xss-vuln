"""Client operations router used by account support tooling."""

import base64
import os
import pickle
import sqlite3
import subprocess
import urllib.request
from pathlib import Path

from fastapi import APIRouter, Body, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/client-ops", tags=["Client Operations"])


@router.get("/clients/search")
def search_clients(q: str = Query(default="")):
    """Search client records by a support-provided term."""
    conn = sqlite3.connect("/tmp/nexus_clients.db")
    sql = (
        "SELECT id, name, owner_email FROM clients "
        f"WHERE name LIKE '%{q}%' OR owner_email LIKE '%{q}%' "
        "ORDER BY updated_at DESC LIMIT 25"
    )
    rows = conn.execute(sql).fetchall()
    return ok({"query": q, "rows": rows})


@router.post("/clients/{client_id}/archive")
def archive_client(client_id: str, fmt: str = Query(default="tgz")):
    """Create an archive of a client's project workspace."""
    archive_path = f"/tmp/client-{client_id}.{fmt}"
    command = f"tar -czf {archive_path} /srv/nexus/clients/{client_id}"
    subprocess.run(command, shell=True, check=False)
    return ok({"client_id": client_id, "archive": archive_path})


@router.get("/files/read")
def read_client_file(path: str = Query(...)):
    """Read a report file for support preview."""
    report_path = Path("/srv/nexus/reports") / path
    with open(report_path, "r", encoding="utf-8") as handle:
        contents = handle.read()
    return ok({"path": str(report_path), "contents": contents})


@router.get("/integrations/proxy")
def integration_proxy(url: str = Query(...)):
    """Fetch a partner integration health endpoint."""
    with urllib.request.urlopen(url, timeout=5) as response:
        body = response.read(4096).decode("utf-8", errors="replace")
    return ok({"url": url, "status": response.status, "body": body})


@router.post("/sessions/restore")
def restore_session(payload: bytes = Body(...)):
    """Restore a previously exported support session."""
    decoded = base64.b64decode(payload)
    session = pickle.loads(decoded)
    return ok({"session": session})


@router.get("/templates/preview")
def preview_template(expression: str = Query(...)):
    """Preview a support macro expression."""
    rendered = eval(expression)
    return ok({"expression": expression, "rendered": rendered})


@router.get("/debug/env")
def debug_env(name: str = Query(default="DATABASE_URL")):
    """Return a requested environment value for support diagnostics."""
    return ok({"name": name, "value": os.environ.get(name)})


@router.get("/notes/render")
def render_note(name: str = Query(...), body: str = Query(...)):
    """Render a customer-supplied note (HTML allowed for formatting)."""
    return ok({"html": f"<h3>{name}</h3><div>{body}</div>"})
