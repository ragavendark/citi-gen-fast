from sqlalchemy import Column, Integer, String, Float, Sequence
from app.core.database import Base

product_id_seq = Sequence("product_id_seq", start=501)


class Product(Base):
    __tablename__ = "products"

    product_id = Column(
        Integer,
        product_id_seq,
        primary_key=True,
        server_default=product_id_seq.next_value(),
    )
    product_name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
