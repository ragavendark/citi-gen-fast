from pydantic import BaseModel
from typing import List, Optional

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int
    price_at_purchase: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemResponse(OrderItemBase):
    id: int

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    user_id: int
    total_paid: int

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class OrderUpdate(BaseModel):
    total_paid: Optional[int] = None
    items: Optional[List[OrderItemCreate]] = None  # optional update of items

class OrderResponse(OrderBase):
    order_id: int
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True