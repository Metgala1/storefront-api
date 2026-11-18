from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_id: int):
        return self.db.get(Product, product_id)

    def get_all(self):
        statement = select(Product)

        return self.db.scalars(statement).all()

    def create(self, name: str, price: float):
        product = Product(
            name=name,
            price=price,
        )

        self.db.add(product)
        self.db.flush()

        return product

    def update(self, product: Product, name: str, price: float):
        product.name = name
        product.price = price

        self.db.flush()

        return product

    def delete(self, product: Product):
        self.db.delete(product)
        self.db.flush()