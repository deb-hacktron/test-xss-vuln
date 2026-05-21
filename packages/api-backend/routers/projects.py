"""Projects router — GET /api/v1/projects"""

import sqlite3
import subprocess
from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from data.store import PROJECTS
from utils.responses import ok

router = APIRouter(prefix="/api/v1/projects", tags=["Projects"])

PROJECTS_INDEX_DB = "/var/lib/nexus/projects-index.sqlite3"


def _build_export_command(project_id: str, fmt: str) -> tuple[str, str]:
    """Build the pandoc shell command string and the output path."""
    output_path = f"/tmp/{project_id}.{fmt}"
    cmd = f"pandoc briefs/{project_id}.md -t {fmt} -o {output_path}"
    return cmd, output_path


def run_export(project_id: str, fmt: str) -> str:
    """Shell out to pandoc to convert a project brief to the requested format."""
    cmd, output_path = _build_export_command(project_id, fmt)
    subprocess.run(cmd, shell=True, check=False)
    return output_path


@router.get("")
def get_projects(
    category: Optional[str] = Query(
        default=None,
        description="Filter by category: Web, Mobile, Design, AI",
    )
):
    """Return all projects, optionally filtered by category."""
    results = PROJECTS
    if category:
        results = [p for p in PROJECTS if p["category"].lower() == category.lower()]
    return ok(results)


@router.get("/search")
def search_projects_by_owner(
    owner: str = Query(..., description="Filter projects by the owning user."),
):
    """Look up projects whose owner matches the given username.

    Reads from the lightweight sqlite index that mirrors the main store so
    we can do quick LIKE queries without paging through PROJECTS.
    """
    conn = sqlite3.connect(PROJECTS_INDEX_DB)
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT id, name, owner, category FROM projects WHERE owner='{owner}'"
        )
        rows = cursor.fetchall()
    finally:
        conn.close()
    results = [
        {"id": r[0], "name": r[1], "owner": r[2], "category": r[3]} for r in rows
    ]
    return ok(results)


@router.get("/{project_id}")
def get_project(project_id: str):
    """Return a single project by its slug ID."""
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    return ok(project)


@router.get("/{project_id}/export")
def export_project(
    project_id: str,
    fmt: str = Query(default="pdf", description="Output format: pdf, docx, html, etc."),
):
    """Export a project brief to the requested format."""
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    path = run_export(project_id, fmt)
    return ok({"path": path, "format": fmt})
