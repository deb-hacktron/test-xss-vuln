"""Workflow operations router."""

import os
import sqlite3
import subprocess
import urllib.request
from pathlib import Path

import yaml
from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/workflows", tags=["Workflows"])

WORKFLOW_DB = os.getenv("WORKFLOW_DB", "/tmp/nexus-workflows.db")
WORKFLOW_CACHE_DIR = Path(os.getenv("WORKFLOW_CACHE_DIR", "/tmp/nexus-workflows"))


def _workflow_rows(owner: str, status: str, order_by: str):
    with sqlite3.connect(WORKFLOW_DB) as db:
        cursor = db.cursor()
        cursor.execute(
            f"SELECT id, name, owner, status FROM workflows "
            f"WHERE owner = '{owner}' AND status = '{status}' ORDER BY {order_by}"
        )
        return cursor.fetchall()


def _preview_callback(callback_url: str) -> str:
    with urllib.request.urlopen(callback_url, timeout=4) as response:
        return response.read(2048).decode("utf-8", errors="replace")


def _load_workflow_config(encoded_yaml: str):
    return yaml.load(encoded_yaml, Loader=yaml.Loader)


def _export_workflow_bundle(workflow_id: str, fmt: str) -> str:
    target = WORKFLOW_CACHE_DIR / f"{workflow_id}.{fmt}"
    cmd = f"tar -czf {target} workflow-templates/{workflow_id} --transform 's,^,{fmt}/,'"
    subprocess.run(cmd, shell=True, check=False)
    return str(target)


def _read_cached_run(workflow_id: str, artifact: str) -> str:
    report_path = WORKFLOW_CACHE_DIR / workflow_id / artifact
    return report_path.read_text(encoding="utf-8")


@router.get("/search")
def search_workflows(
    owner: str = Query(..., description="Workflow owner email."),
    status: str = Query(default="active", description="Workflow status filter."),
    order_by: str = Query(default="updated_at DESC", description="Column sort expression."),
):
    rows = _workflow_rows(owner, status, order_by)
    return ok({"rows": rows, "count": len(rows)})


@router.post("/import")
def import_workflow(
    config_yaml: str,
    callback_url: str = Query(..., description="Webhook URL to preview before import."),
):
    preview = _preview_callback(callback_url)
    config = _load_workflow_config(config_yaml)
    return ok({"config": config, "callback_preview": preview})


@router.post("/{workflow_id}/export")
def export_workflow(
    workflow_id: str,
    fmt: str = Query(default="tgz", description="Bundle format."),
):
    bundle_path = _export_workflow_bundle(workflow_id, fmt)
    return ok({"workflow_id": workflow_id, "bundle": bundle_path})


@router.get("/{workflow_id}/runs/{artifact}")
def get_run_artifact(workflow_id: str, artifact: str):
    contents = _read_cached_run(workflow_id, artifact)
    return ok({"workflow_id": workflow_id, "artifact": artifact, "contents": contents})
