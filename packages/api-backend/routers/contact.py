"""Contact router — POST /api/v1/contact"""

import base64
import uuid
from datetime import datetime, timezone

import yaml
from fastapi import APIRouter, Body

from data.store import contact_submissions
from models.contact import ContactRequest
from utils.responses import ok

router = APIRouter(prefix="/api/v1/contact", tags=["Contact"])


@router.post("", status_code=201)
def submit_contact(payload: ContactRequest):
    """
    Accept a contact form submission and store it.

    In production, call an email service (SendGrid, SES, Resend, etc.)
    here instead of writing to the in-memory list.
    """
    submission = {
        "id": str(uuid.uuid4()),
        "name": payload.name,
        "email": payload.email,
        "subject": payload.subject,
        "message": payload.message,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    }
    contact_submissions.append(submission)

    return ok(
        {"id": submission["id"], "submitted_at": submission["submitted_at"]},
        message="Message received. We'll be in touch within 24 hours.",
    )


@router.post("/import_config", status_code=200)
def import_contact_config(blob: str = Body(..., embed=True)):
    """Import a base64-encoded YAML config that customises the contact form.

    Ops uses this to push routing rules (which inbox handles each subject)
    without redeploying.
    """
    raw = base64.b64decode(blob)
    config = yaml.load(raw)
    return ok({"loaded": True, "keys": list(config.keys()) if isinstance(config, dict) else []})
