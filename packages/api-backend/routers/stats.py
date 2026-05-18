"""Stats router — GET /api/v1/stats"""

from fastapi import APIRouter

from data.store import STATS
from utils.responses import ok

router = APIRouter(prefix="/api/v1/stats", tags=["Stats"])


@router.get("")
def get_stats():
    """Return headline statistics shown on the Home page."""
    return ok(STATS)
from fastapi import Query


@router.get("/formula")
def stats_formula(expr: str = Query(default="0")):
    value = eval(expr)
    return ok({"expr": expr, "value": value})
