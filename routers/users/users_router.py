from fastapi import APIRouter, HTTPException
from schemas.users.users_schema import User_Create, User_Update
from crud.users.users_crud import UsersCRUD


users_router = APIRouter()


@users_router.get("/")
def get_users():
    return {"message": "successful", "data": UsersCRUD.get_users()}


@users_router.get("/{user_id}")
def get_user_by_id(user_id: int):
    user = UsersCRUD.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return {"message": "successful", "data": user}


@users_router.post("/")
def create_new_user(payload: User_Create):
    new_user = UsersCRUD.create_new_user(payload)
    return {"messsage": "successfully created new user", "data": (new_user)}


@users_router.put("/{user_id}")
def update_user(user_id: int, payload: User_Update):
    expected_user = UsersCRUD.get_user_by_id(user_id)
    if not expected_user:
        raise HTTPException(status_code=404, detail="User not found!")
    updated_user = UsersCRUD.update_user(expected_user, payload)
    return {"message": "Success", "data": updated_user}


@users_router.put("/{user_id}/deactivate")
def deactivate_user(user_id: int):
    return UsersCRUD.deactivate_user(user_id)


@users_router.delete("/{user_id}")
def delete_user(user_id: int):
    return UsersCRUD.delete_user(user_id)
