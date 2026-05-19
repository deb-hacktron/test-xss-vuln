"""Additional deploy operations API routes."""

import subprocess

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/deploy-ops", tags=["Deploy Ops"])


@router.get("/rollout-log")
def rollout_log(
    namespace: str = Query(default="default"),
    service: str = Query(default="web"),
):
    command = f"kubectl logs deployment/{service} --namespace {namespace} --tail=20"
    result = subprocess.run(command, shell=True, text=True, capture_output=True, check=False)
    return ok({"namespace": namespace, "service": service, "logs": result.stdout})
