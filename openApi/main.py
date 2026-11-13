from fastapi import FastAPI

app = FastAPI(
    title="StoreFront API",
    description="The backend API for StoreFront.",
    version="1.0.0"
)


@app.get(
    "/",
    tags=["General"],
    summary="API welcome endpoint"
)
def root():
    """
    Returns a welcome message.
    """
    return {
        "message": "Welcome to StoreFront API"
    }


@app.get(
    "/health",
    tags=["General"],
    summary="Check API health"
)
def health_check():
    """
    Returns the current API health status.
    """
    return {
        "status": "healthy",
        "service": "storefront-api"
    }


@app.get(
    "/products",
    tags=["Products"],
    summary="Retrieve all products"
)
def get_products():
    """
    Returns all available StoreFront products.
    """
    return {
        "products": [
            {
                "id": 1,
                "name": "MacBook Air",
                "price": 1200,
                "quantity": 10
            }
        ]
    }

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    return {
        "product_id": product_id
    }

@app.get(
    "/categories",
    tags=["Categories"],
    summary="Retrieve all categories"
)
def get_categories(): 
    """
    Returns available product categories.
    """
    return {
        "categories": [
            "Electronics",
            "Accessories",
            "Computers"
        ]
    }