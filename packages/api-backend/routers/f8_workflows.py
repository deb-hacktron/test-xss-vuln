"""F8 dedup campaign router."""

import yaml
from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/workflows", tags=["Workflows"])


@router.get("/import")
def import_workflow(document: str = Query(default="")):
    parsed = yaml.load(document, Loader=yaml.Loader)
    return ok({"parsed_type": type(parsed).__name__})

