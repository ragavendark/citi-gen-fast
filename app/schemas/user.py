from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    address: str | None = None
    email: EmailStr


class UserCreate(UserBase):
    first_name: str
    email: EmailStr


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    address: str | None = None
    email: EmailStr | None = None


class UserResponse(UserBase):
    user_id: int

    class Config:
        from_attributes = True
