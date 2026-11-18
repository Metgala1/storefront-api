import logging
from sqlalchemy.orm import Session
from app.repositories.product_repository import ProductRepository

logger = logging.getLogger(__name__)

def get_product(db: Session, product_id: int):
    logger.info(
        "Fetching product with ID%s",
        product_id
    )
    respository = ProductRepository(db)
    
    product = respository.get_by_id(product_id)
    
    if product is None:
        return None
    
    return product
    