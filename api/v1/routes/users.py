from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])
users_list = [{"id": 1, "name": "Jack Sparrow"}, {"id": 2, "name": "Hector Barbosa"}]


@router.get("/")
def get_users():
    return users_list


# url: loclahost:8000/api/v1/users -- POST
@router.post("/")
def create_user(user: dict):
    print(f"Recieved {user}")
    users_list.append(user)
    return {"status": "success"}


# url: loclahost:8000/api/v1/users/1 or /2 --GET
@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    print(f"Received user id: {user_id}")
    for i in users_list:
        if i["id"] == user_id:
            return i


@router.put("/{user_id}")
def get_user_by_id(user_id: int, user: dict):
    print(f"Received user id: {user_id}")
    for index in range(len(users_list)):
        if users_list[index]["id"] == user_id:
            users_list[index] = user
            return {"status": "update success"}

@router.delete("/{user_id}")
def get_user_by_id(user_id: int):
    print(f"Received user id: {user_id}")
    for index in range(len(users_list)):
        if users_list[index]["id"] == user_id:
            users_list.pop(index)
            return {"status": "deletion  success"}