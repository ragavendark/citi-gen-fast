from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import List

# User Schema


class UserBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    address: str | None = None
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    address: str | None = None


class UserResponse(UserBase):
    user_id: UUID

    class Config:
        from_attributes = True

# Product Schema
class ProductBase(BaseModel):
    product_name: str
    description: str | None = None
    price: float = Field(gt=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    product_name: str | None = None
    description: str | None = None
    price: float | None = None


class ProductResponse(ProductBase):
    product_id: UUID
    is_deleted: bool

    class Config:
        from_attributes = True

#OrderItem Schema

class OrderItemBase(BaseModel):
    product_id: UUID
    quantity: int = Field(gt=0)


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemResponse(OrderItemBase):
    id: int

    class Config:
        from_attributes = True

# Order Schema

class OrderBase(BaseModel):
    user_id: UUID


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderUpdate(BaseModel):
    total_paid: float | None = None


class OrderResponse(BaseModel):
    order_id: UUID
    user_id: UUID
    total_paid: float | None = None
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True
