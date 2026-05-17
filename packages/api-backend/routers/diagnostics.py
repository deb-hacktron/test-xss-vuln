from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/diagnostics", tags=["Diagnostics"])

_CONFIG = {
    "supported_commands": ["dns", "uptime"],
    "max_concurrency": 4,
    "doc_url": "https://internal.docs/diagnostics",
}


@router.get("/config")
def config():
    """Return static diagnostics config (no IO, no user input flow)."""
    return _CONFIG
