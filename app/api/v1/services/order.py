from sqlalchemy.orm import Session
from models import Order
from models import OrderItem
from models import Product
from schemas import OrderCreate
from uuid import UUID


def create_order(db: Session, order: OrderCreate):
    db_order = Order(user_id=order.user_id, total_paid=0)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    total = 0

    for item in order.items:
        product = db.query(Product).filter(
            Product.product_id == item.product_id,
            not Product.is_deleted
        ).first()

        if not product:
            return None

        total += float(product.price) * item.quantity

        db_item = OrderItem(
            order_id=db_order.order_id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(db_item)

    db_order.total_paid = total
    db.commit()
    db.refresh(db_order)

    return db_order


def get_orders(db: Session):
    return db.query(Order).all()


def get_order(db: Session, order_id: UUID):
    return db.query(Order).filter(Order.order_id == order_id).first()