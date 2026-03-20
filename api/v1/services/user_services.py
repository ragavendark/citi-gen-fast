class UserService:
    def __init__(self):
        self.users_list = [
            {"id": 1, "name": "Jack Sparrow"},
            {"id": 2, "name": "Hector Barbosa"},
        ]

    def get_users(self):
        return self.users_list

    def create_user(self, user: dict):
        print(f"Recieved {user}")
        self.users_list.append(user)
        return {"status": " post success"}

    def get_user_by_id(self, user_id: int):
        print(f"Received user id: {user_id}")
        for i in self.users_list:
            if i["id"] == user_id:
                return i

    def update_user_by_id(self, user_id: int, user: dict):
        print(f"Received user id: {user_id}")
        for index in range(len(self.users_list)):
            if self.users_list[index]["id"] == user_id:
                self.users_list[index] = user
                return {"status": "update success"}

    def delete_user_by_id(self, user_id: int):
        print(f"Received user id: {user_id}")
        for index in range(len(self.users_list)):
            if self.users_list[index]["id"]== user_id:
                self.users_list.pop(index)
                return {"status": "deletion  success"}
