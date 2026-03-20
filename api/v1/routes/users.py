from fastapi import APIRouter, Depends
from api.v1.services.user_services import UserService

router = APIRouter(prefix="/users", tags=["users"])


# user_service = UserService()


@router.get("/")
def get_users(user_service: UserService = Depends(UserService.get_users)):
    return user_service.get_users()


# url: loclahost:8000/api/v1/users -- POST
@router.post("/")
def create_user(
    user: dict, user_service: UserService = Depends(UserService.create_user)
):
    return user_service.create_user(user)


# url: loclahost:8000/api/v1/users/1 or /2 --GET
@router.get("/{user_id}")
def get_user_by_id(
    user_id: int, user_service: UserService = Depends(UserService.get_user_by_id)
):
    return user_service.get_user_by_id(user_id)


# url: loclahost:8000/api/v1/users/1 or /2 --PUT
@router.put(
    "/{user_id}",
)
def update_user_by_id(
    user_id: int,
    user: dict,
    user_service: UserService = Depends(UserService.update_user_by_id),
):
    return user_service.update_user_by_id(user_id, user)


# url: loclahost:8000/api/v1/users/1 or /2 --DELETE
@router.delete("/{user_id}")
def get_user_by_id(
    user_id: int, user_service: UserService = Depends(UserService.delete_user_by_id)
):
    return user_service.delete_user_by_id(user_id)
