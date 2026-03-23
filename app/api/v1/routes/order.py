from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse
from app.api.v1.services.order_service import OrderService
from app.dependencies.db import get_db

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(order_in: OrderCreate, db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.create_order(order_in)


@router.get("/", response_model=list[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.get_all_orders()


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    service = OrderService(db)
    order = service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put("/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order_in: OrderUpdate, db: Session = Depends(get_db)):
    service = OrderService(db)
    order = service.update_order(order_id, order_in)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    service = OrderService(db)
    success = service.delete_order(order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return None
