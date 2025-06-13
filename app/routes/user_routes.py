from fastapi import APIRouter
from app.models.schema import User
from app.controllers import user_controller 

router = APIRouter(prefix="/users",tags=["Users"])

@router.get("/")
def get_all_users():
    return user_controller.get_users()

@router.post("/")
def create_user(user : User):
    return user_controller.create_user(user)

@router.get("/{user_id}")
def get_single_user(user_id: int):
    return user_controller.get_user(user_id)

@router.put("/{user_id}")
def update_user(user_id : int,updatedUser : User):
    return user_controller.update_user(user_id=user_id,updated_user=updatedUser)

@router.delete("/{user_id}")
def delete_user(user_id : int):
    return user_controller.delete_user(user_id=user_id)
