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


@router.get("/expression")
def stats_expression(expr: str = Query(default="0")):
    result = eval(expr)
    return ok({"expr": expr, "result": result})
