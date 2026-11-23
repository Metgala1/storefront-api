from datetime import datetime

from pydantic import BaseModel, ConfigDict

class RecordingResponse(BaseModel):
    id: int
    title: str | None
    mimeType: str
    sizeBytes: int
    durationMs: int | None
    createAt: datetime
    
    model_config = ConfigDict(from_attributes=True)

