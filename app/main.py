from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routers import category, products, users
from app.schemas.product import ProductNotFoundException

app = FastAPI(title="StoreFront API", version="1.0.0")


@app.exception_handler(ProductNotFoundException)
async def product_not_found_handle(request: Request, exc: ProductNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "error": {"code": "PRODUCT_NOT_FOUND", "message": "Product not found"},
        },
    )


app.include_router(products.router, prefix="/products")

app.include_router(category.router, prefix="/categories")

app.include_router(users.router, prefix="/users")
