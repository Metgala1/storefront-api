from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    Query,
    UploadFile,
    status
)

from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.permissions import require_admin
from app.schemas.recording import RecordingResponse
from app.services import recording_service

router = APIRouter(
    prefix="/recordings",
    tags=["Recordings"]
)

DatabaseSession = Annotated[Session , Depends(get_db)]
AdminUser = Annotated[object, Depends(require_admin)]

MAX_FILE_SIZE = 25 * 1024 * 1024

ALLOWED_AUDIO_TYPES = {
    "audio/mpeg",
    "audio/mp4",
    "audio/wav",
    "audio/webm",
    "audio/ogg",
    "audio/aac",
    "audio/flac",
    "audio/3gpp",
    "audio/x-m4a",
}

@router.post(
    "/",
    response_model=RecordingResponse,
   status_code=status.HTTP_201_CREATED,
)
async def upload_recording(
    db: DatabaseSession,
    admin: AdminUser,
    file: Annotated[UploadFile, File()],
    title: Annotated[str | None, Form()] = None,
    duration_ms: Annotated[str | None, Form(ge=0)] = None,
):
    mime_type = (file.content_type or "").split(";")[0].strip().lower()
    
    if mime_type not in ALLOWED_AUDIO_TYPES:
        raise HTTPException(
            status_code=415,
            detail="Unsupported audio format"
        )
    
    data = await file.read(MAX_FILE_SIZE + 1)
    
    if not data:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty"
        )
    
    if len(data) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Audio file exceeds the 25mb limit"
        )
    
    