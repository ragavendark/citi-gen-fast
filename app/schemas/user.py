from pydantic import BaseModel, EmailStr

# Base schema shared by create/update/response
class UserBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    address: str | None = None
    email: EmailStr

# Schema for user creation (requires first_name and email)
class UserCreate(UserBase):
    first_name: str
    email: EmailStr

# Schema for user update (all optional)
class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    address: str | None = None
    email: EmailStr | None = None

# Schema for user response (includes auto-incremented ID)
class UserResponse(UserBase):
    user_id: int  # <- now int, not UUID

    class Config:
        from_attributes = True  # enables ORM mode for SQLAlchemy models