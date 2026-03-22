from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserUpdate
from uuid import UUID


def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: UUID):
    return db.query(User).filter(User.user_id == user_id).first()


def update_user(db: Session, user_id: UUID, data: UserUpdate):
    user = get_user(db, user_id)
    if not user:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: UUID):
    user = get_user(db, user_id)
    if not user:
        return None

    db.delete(user)
    db.commit()
    return user