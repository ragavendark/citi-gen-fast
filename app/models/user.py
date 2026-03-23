from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from app.core.database import Base

user_id_seq = Sequence("user_id_seq", start=101)


class User(Base):
    __tablename__ = "users"

    user_id = Column(
        Integer, user_id_seq, primary_key=True, server_default=user_id_seq.next_value()
    )
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False, index=True)

    orders = relationship("Order", back_populates="user", cascade="all, delete")
