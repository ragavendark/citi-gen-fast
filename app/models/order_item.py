from sqlalchemy import Column, Integer, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from app.core.database import Base

order_item_id_seq = Sequence("order_item_id_seq", start=2001)


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(
        Integer,
        order_item_id_seq,
        primary_key=True,
        server_default=order_item_id_seq.next_value(),
    )
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_at_purchase = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product")
