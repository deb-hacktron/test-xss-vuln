"""F8 dedup campaign router."""

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/analytics", tags=["Analytics"])


def evaluate_formula(expr: str):
    return eval(expr)


@router.get("/formula")
def calculate_formula(expr: str = Query(default="0")):
    value = evaluate_formula(expr)
    return ok({"expr": expr, "value": value})

