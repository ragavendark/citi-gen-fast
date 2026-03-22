# app/routers/user.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse, UserUpdate
from api.v1.services import user_service
from dependencies import get_db
from typing import List
from uuid import UUID

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.get("/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get(user_id: UUID, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update(user_id: UUID, data: UserUpdate, db: Session = Depends(get_db)):
    user = user_service.update_user(db, user_id, data)
    if not user:
        raise HTTPException(404, "User not found")
    return user


@router.delete("/{user_id}")
def delete(user_id: UUID, db: Session = Depends(get_db)):
    user = user_service.delete_user(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return {"message": "Deleted"}