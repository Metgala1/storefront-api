from fastapi import FastAPI

from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers
from app.routers.auth import router as auth_router
from app.routers.categories import router as categories_router
from app.routers.products import router as products_router

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0",
    description="StoreFront API backend"
)
register_exception_handlers(app)

app.include_router(auth_router, prefix="/api/v1")
app.include_router(products_router, prefix="/api/v1")
app.include_router(categories_router, prefix="/api/v1")
