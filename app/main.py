from fastapi import FastAPI, File, Form, Header, Response, Request, UploadFile, Cookie
from fastapi.responses import JSONResponse
from typing import Annotated

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



@app.get("/request-info")
async def request_info(
    user_agent: Annotated[str | None, Header()] = None,
):
    return {
        "user_agent": user_agent
    }

@app.get("/secure")
async def secure_enpoint(
  authorization: Annotated[str , Header()]  
):
    return {
        "authorization_received": True
    }
    
@app.get("/session")
async def read_session(
    session_id: Annotated[str | None , Cookie()] = None
):
    return {
        "session_id": session_id
    }

@app.post("/login")
async def login(response: Response):
    response.set_cookie(
        key="session",
        value="abc123",
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24 * 7
    )
    
    return {
        "message": "Login successful"
    }
    
@app.post("/logout")
async def logout(response: Response):
    response.delete_cookie(
        key="session",
        httponly=True,
        secure=True,
        samesite="lax"
    )
    
    return {
        "message": "Logged out successfully"
    }

@app.post("/login-form")
async def login_form(
    email: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    return {
        "email": email,
        "message": "Form received"
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }