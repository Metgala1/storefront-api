from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0",
    description="StoreFront API backend"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to StoreFront API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }