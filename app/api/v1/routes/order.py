# app/routers/order.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import OrderCreate, OrderResponse
from api.v1.services import order_service
from dependencies.db import get_db
from typing import List
from uuid import UUID

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderResponse)
def create(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = order_service.create_order(db, order)
    if not db_order:
        raise HTTPException(400, "Invalid product in order")
    return db_order


@router.get("/", response_model=List[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    return order_service.get_orders(db)


@router.get("/{order_id}", response_model=OrderResponse)
def get(order_id: UUID, db: Session = Depends(get_db)):
    order = order_service.get_order(db, order_id)
    if not order:
        raise HTTPException(404, "Order not found")
    return order