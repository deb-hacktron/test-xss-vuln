"""F8 dedup campaign router."""

from jinja2 import Template
from fastapi import APIRouter, Query

from utils.responses import ok

router = APIRouter(prefix="/api/v1/messages", tags=["Messages"])


@router.get("/preview")
def preview_message(template: str = Query(default="")):
    rendered = Template(template).render(user="guest")
    return ok({"preview": rendered})

