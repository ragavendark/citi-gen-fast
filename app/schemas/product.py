from pydantic import BaseModel

class ProductBase(BaseModel):
    product_name: str
    description: str | None = None
    price: float

class ProductCreate(ProductBase):
    product_name: str
    price: float

class ProductUpdate(BaseModel):
    product_name: str | None = None
    description: str | None = None
    price: float | None = None

class ProductResponse(ProductBase):
    product_id: int

    class Config:
        from_attributes = True