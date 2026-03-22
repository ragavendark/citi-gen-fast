from sqlalchemy import Column, Integer, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from app.core.database import Base

order_id_seq = Sequence("order_id_seq", start=1001)

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, order_id_seq, primary_key=True, server_default=order_id_seq.next_value())
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    total_paid = Column(Integer, nullable=False)

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete")