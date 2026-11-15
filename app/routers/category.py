from fastapi import APIRouter

router = APIRouter(tags=["categories"])

products: list[dict] = [
    {
        "id": 1,
        "name": "MacBook Air",
        "category": "computers",
        "price": 1200,
        "quantity": 10,
        "description": "Lightweight laptop with all-day battery life, ideal for everyday work and travel.",
    },
    {
        "id": 2,
        "name": "iPhone 17",
        "category": "phones",
        "price": 900,
        "quantity": 25,
        "description": "Apple's latest smartphone with a sharp display and a powerful camera system.",
    },
    {
        "id": 3,
        "name": "MacBook Pro",
        "category": "computers",
        "price": 2000,
        "quantity": 5,
        "description": "High-performance laptop built for developers, designers, and video editing.",
    },
    {
        "id": 4,
        "name": "Samsung Galaxy",
        "category": "phones",
        "price": 850,
        "quantity": 15,
        "description": "Android flagship with a bright AMOLED screen and versatile camera setup.",
    },
    {
        "id": 5,
        "name": "iPad Air",
        "category": "tablets",
        "price": 600,
        "quantity": 8,
        "description": "Slim, powerful tablet for drawing, note-taking, and entertainment.",
    },
]

@router.get("")
async def get_categories():
    categories = [p["category"] for p in products]
    return {"count": len(categories), "categories": categories}

@router.get("/{category_id}")
async def get_category_by_id(category_id: str):
    category = [p for p in products if p["category"] == category_id.lower()]
    
    return {
        "category": category
    }
    
    