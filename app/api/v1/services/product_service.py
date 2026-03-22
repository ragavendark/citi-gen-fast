from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def get_product(self, product_id: int) -> Product | None:
        return self.db.query(Product).filter(Product.product_id == product_id).first()

    def get_all_products(self) -> list[Product]:
        return self.db.query(Product).all()

    def create_product(self, product_in: ProductCreate) -> Product:
        product = Product(**product_in.model_dump())
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update_product(self, product_id: int, product_in: ProductUpdate) -> Product | None:
        product = self.get_product(product_id)
        if not product:
            return None
        for field, value in product_in.model_dump(exclude_unset=True).items():
            setattr(product, field, value)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete_product(self, product_id: int) -> bool:
        product = self.get_product(product_id)
        if not product:
            return False
        self.db.delete(product)
        self.db.commit()
        return True