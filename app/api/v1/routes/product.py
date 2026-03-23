from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.api.v1.services.product_service import ProductService
from app.dependencies.db import get_db

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.create_product(product_in)


@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_all_products()


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    product = service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int, product_in: ProductUpdate, db: Session = Depends(get_db)
):
    service = ProductService(db)
    product = service.update_product(product_id, product_in)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    success = service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return None
