import secrets

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.recording import Recording


def create_recording(
    db: Session,
    *,
    title: str | None,
    data: bytes,
    mime_type: str,
    duration_ms: int | None,
) -> Recording:
    recording = Recording(
        id=secrets.token_urlsafe(24),
        title=title,
        data=data,
        mimeType=mime_type,
        sizeBytes=len(data),
        durationMs=duration_ms,
    )

    db.add(recording)
    db.commit()
    db.refresh(recording)

    return recording


def get_recordings(
    db: Session,
    skip: int = 0,
    limit: int = 20,
) -> list[Recording]:
    statement = (
        select(Recording)
        .order_by(Recording.createdAt.desc())
        .offset(skip)
        .limit(limit)
    )

    return list(db.scalars(statement).all())


def get_recording(
    db: Session,
    recording_id: str,
) -> Recording | None:
    return db.get(Recording, recording_id)


def delete_recording(
    db: Session,
    recording: Recording,
) -> None:
    db.delete(recording)
    db.commit()