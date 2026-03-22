from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import ProductCreate, ProductResponse, ProductUpdate
from app import product_service
from dependencies.db import get_db
from typing import List
from uuid import UUID

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)


@router.get("/", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return product_service.get_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get(product_id: UUID, db: Session = Depends(get_db)):
    product = product_service.get_product(db, product_id)
    if not product:
        raise HTTPException(404, "Product not found")
    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update(product_id: UUID, data: ProductUpdate, db: Session = Depends(get_db)):
    product = product_service.update_product(db, product_id, data)
    if not product:
        raise HTTPException(404, "Product not found")
    return product


@router.delete("/{product_id}")
def delete(product_id: UUID, db: Session = Depends(get_db)):
    product = product_service.soft_delete_product(db, product_id)
    if not product:
        raise HTTPException(404, "Product not found")
    return {"message": "Soft deleted"}