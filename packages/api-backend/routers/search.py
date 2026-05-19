"""Additional search API routes."""

from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/search", tags=["Search"])


@router.get("/rule-test")
def rule_test(rule: str = Query(default="1 + 1")):
    value = eval(rule)
    return ok({"rule": rule, "value": value})
