from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get_users():
    return [{"id": 1, "name": "Jack Sparrow"}, {"id": 2, "name": "Hector Barbosa"}]
