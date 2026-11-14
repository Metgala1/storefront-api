from fastapi import FastAPI, Query ,HTTPException

from app.schemas.product import ProductCreate ,ProductPatch ,ProductUpdate

app = FastAPI(
    title="StoreFront API",
    description="The backend API for StoreFront.",
    version="1.0.0"
)

products = [
    {
        "id": 1,
        "name": "MacBook Air",
        "category": "computers",
        "price": 1200,
        "description": "Lightweight laptop with all-day battery life, ideal for everyday work and travel.",
    },
    {
        "id": 2,
        "name": "iPhone 17",
        "category": "phones",
        "price": 900,
        "description": "Apple's latest smartphone with a sharp display and a powerful camera system.",
    },
    {
        "id": 3,
        "name": "MacBook Pro",
        "category": "computers",
        "price": 2000,
        "description": "High-performance laptop built for developers, designers, and video editing.",
    },
    {
        "id": 4,
        "name": "Samsung Galaxy",
        "category": "phones",
        "price": 850,
        "description": "Android flagship with a bright AMOLED screen and versatile camera setup.",
    },
    {
        "id": 5,
        "name": "iPad Air",
        "category": "tablets",
        "price": 600,
        "description": "Slim, powerful tablet for drawing, note-taking, and entertainment.",
    },
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

@app.post("/products", status_code=201)
async def create_product(product: ProductCreate):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price,
        "category": product.category,
        "quantity": product.quantity,
        "description": product.description
    }
    
    products.append(new_product)
    
    return {
        "product": new_product
    }

@app.patch("/products/{product_id}")
async def edit_product(product_id: int, product: ProductPatch):
    for  existing_product in products:
        if existing_product["id"] == product_id:
            edited_product = product.model_dump(exclude_unset=True)
            existing_product.update(edited_product)
            
            return existing_product
    
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
            

@app.put("/products/{product_id}")
async def replace_product(product_id: int, product: ProductUpdate):
    for index, existing_product in enumerate(products):
        if existing_product["id"] == product_id:
            updated_product = {
                "id": product_id,
                **product.model_dump()
            }
            
            products[index] = updated_product
            return updated_product
    
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
