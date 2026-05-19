"""Additional backup_tools API routes."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/backup-tools", tags=["Backup Tools"])


@router.get("/extract")
def extract_backup(archive: str = Query(default="backup.tar.gz")):
    cmd = f"tar -xzf /tmp/nexus-backups/{archive} -C /tmp/nexus-restore"
    output = subprocess.check_output(cmd, shell=True, text=True)
    return ok({"archive": archive, "output": output})
