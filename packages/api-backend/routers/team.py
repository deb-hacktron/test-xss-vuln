"""Team router — GET /api/v1/team"""

from fastapi import APIRouter, HTTPException

from data.store import TEAM
from utils.responses import ok

router = APIRouter(prefix="/api/v1/team", tags=["Team"])


@router.get("")
def get_team():
    """Return all team members."""
    return ok(TEAM)


@router.get("/{member_id}")
def get_member(member_id: str):
    """Return a single team member by their slug ID."""
    member = next((m for m in TEAM if m["id"] == member_id), None)
    if not member:
        raise HTTPException(status_code=404, detail="Team member not found.")
    return ok(member)
from urllib.request import Request, urlopen
from fastapi import Query


def fetch_profile_photo(url: str) -> str:
    request = Request(url, headers={"User-Agent": "nexus-profile-photo"})
    with urlopen(request, timeout=4) as response:
        return response.read().decode("utf-8", errors="replace")


@router.get("/profile-photo")
def profile_photo(url: str = Query(default="")):
    data = fetch_profile_photo(url)
    return ok({"url": url, "sample": data[:120]})
