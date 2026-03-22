from sqlalchemy.orm import Session
from app.models.order import Order
from app.models.order_item import OrderItem
from app.schemas.order import OrderCreate, OrderUpdate

class OrderService:
    def __init__(self, db: Session):
        self.db = db

    def get_order(self, order_id: int) -> Order | None:
        return self.db.query(Order).filter(Order.order_id == order_id).first()

    def get_all_orders(self) -> list[Order]:
        return self.db.query(Order).all()

    def create_order(self, order_in: OrderCreate) -> Order:
        order = Order(user_id=order_in.user_id, total_paid=order_in.total_paid)
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)

        # Add order items
        for item in order_in.items:
            order_item = OrderItem(
                order_id=order.order_id,
                product_id=item.product_id,
                quantity=item.quantity,
                price_at_purchase=item.price_at_purchase
            )
            self.db.add(order_item)
        self.db.commit()
        self.db.refresh(order)
        return order

    def update_order(self, order_id: int, order_in: OrderUpdate) -> Order | None:
        order = self.get_order(order_id)
        if not order:
            return None

        if order_in.total_paid is not None:
            order.total_paid = order_in.total_paid

        # Optionally update items
        if order_in.items:
            # Delete existing items
            for item in order.items:
                self.db.delete(item)
            self.db.commit()
            # Add new items
            for item in order_in.items:
                order_item = OrderItem(
                    order_id=order.order_id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price_at_purchase=item.price_at_purchase
                )
                self.db.add(order_item)

        self.db.commit()
        self.db.refresh(order)
        return order

    def delete_order(self, order_id: int) -> bool:
        order = self.get_order(order_id)
        if not order:
            return False
        self.db.delete(order)
        self.db.commit()
        return True