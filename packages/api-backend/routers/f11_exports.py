"""Export bundle router."""

import sqlite3
import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/exports", tags=["Exports"])


@router.get("/bundle")
def bundle_export(name: str = Query(default="default")):
    cmd = f"tar -czf /tmp/{name}.tgz /srv/exports/{name}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return ok({"name": name, "stderr": result.stderr, "code": result.returncode})


@router.get("/index")
def export_index(owner: str = Query(default="")):
    conn = sqlite3.connect("/tmp/nexus-f11-exports.db")
    query = f"SELECT id, owner, created_at FROM export_index WHERE owner = '{owner}'"
    rows = conn.execute(query).fetchall()
    return ok({"owner": owner, "rows": rows})
