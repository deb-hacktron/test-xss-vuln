"""Theme preview router."""

from fastapi import APIRouter, Query
from jinja2 import Template

from utils.responses import ok

router = APIRouter(prefix="/api/v1/themes", tags=["Themes"])


def render_theme_template(template: str, name: str) -> str:
    return Template(template).render(name=name)


@router.get("/preview")
def preview_theme(template: str = Query(default="Hello {{ name }}"), name: str = Query(default="visitor")):
    rendered = render_theme_template(template, name)
    return ok({"preview": rendered})
