from fastapi import HTTPException
from schemas.users.users_schema import User, User_Create, User_Update

users = [
    User(name="user1", email="user1@gmail.com", id=1, is_active=True),
    User(name="user2", email="user2@gmail.com", id=2, is_active=True)
]


class UsersCRUD:
    @staticmethod
    def get_users():
        return users

    @staticmethod
    def get_user_by_id(user_id):
        User | None
        for current_user in users:
            if current_user.id == user_id:
                return current_user
        return None

    @staticmethod
    def create_new_user(user: User_Create):
        new_user = User(
            id=len(users)+1,
            name=user.name,
            email=user.email,
            is_active=True
        )
        users.append(new_user)
        return new_user

    @staticmethod
    def update_user(user: User, data: User_Update):
        if not User:
            raise HTTPException(status_code=404, detail="User not found")
        user.name = data.name
        user.email = data.email
        return user

    @staticmethod
    def deactivate_user(user_id: int):
        user = UsersCRUD.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.is_active = False
        return user

    @staticmethod
    def delete_user(user_id: int):
        user = UsersCRUD.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        users.remove(user)
        return {"message": "User deleted successfully"}


users_crud = UsersCRUD()
