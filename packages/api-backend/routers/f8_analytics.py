"""F8 dedup campaign router."""

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/analytics", tags=["Analytics"])


@router.get("/formula")
def calculate_formula(expr: str = Query(default="0")):
    value = eval(expr)
    return ok({"expr": expr, "value": value})

