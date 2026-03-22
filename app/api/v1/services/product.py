from sqlalchemy.orm import Session
from models import Product
from schemas import ProductCreate, ProductUpdate
from uuid import UUID


def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session):
    return db.query(Product).filter(not Product.is_deleted).all()


def get_product(db: Session, product_id: UUID):
    return db.query(Product).filter(
        Product.product_id == product_id,
        not Product.is_deleted 
    ).first()


def update_product(db: Session, product_id: UUID, data: ProductUpdate):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product


def soft_delete_product(db: Session, product_id: UUID):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        return None

    product.is_deleted = True
    db.commit()
    return product