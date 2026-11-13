from fastapi import FastAPI

app = FastAPI(
    title="StoreFront API",
    description="Backend API powering the storFront application",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to StoreFront API"
    }

@app.post(
    "/products",
    tags=["Products"]
    )
def create_product():
    return {
        "message": "Product created successfully"
    }

@app.get("/products",
         tags=["Products"]
         )
def get_products():
    return {
        "products": [
            {
                "id": 1,
                "name": "Macbook",
                "price": 1200
            },
            {
                "id": 2,
                "name": "iphone",
                "price": 900
            }
        ]
    }

@app.get("/categories",
         tags=["categories"]
         )
def get_categories():
    return {
        "categories": [
            "Electronics",
            "Accessories",
            "Computers"
        ]
    }

@app.get("/brands")
def get_brands():
    return ["Apple", "Samsung", "Dell"]

@app.get("/product-count")
def product_count():
    return 25

@app.delete("/products")
def delete_products():
    return {
        "message": "Products deleted successful"
    }