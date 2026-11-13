from fastapi import FastAPI, Query

app = FastAPI(
    title="StoreFront API",
    description="The backend API for StoreFront.",
    version="1.0.0"
)

products = [
    {"id": 1, "name": "MacBook Air", "category": "computers", "price": 1200},
    {"id": 2, "name": "iPhone 17", "category": "phones", "price": 900},
    {"id": 3, "name": "MacBook Pro", "category": "computers", "price": 2000},
    {"id": 4, "name": "Samsung Galaxy", "category": "phones", "price": 850},
    {"id": 5, "name": "iPad Air", "category": "tablets", "price": 600},
]


@app.get("/products")
def get_products(
    category: str | None = None,
    search: str | None = None,
    limit: int = Query(default=2, ge=1, le=10),
):
    result = products
    if category:
        result = [p for p in result if p["category"].lower() == category.lower()]
    
    if search:
        result = [p for p in result if search.lower() in p["name"].lower()]
    
    result = result[:limit]
    
    return {"count": limit , "products": result}


@app.get("/products/{product_id}")
def get_by_id(product_id: int):
    result = [p for p in products if p["id"] == product_id]
    
    return {
        "product": result
    }