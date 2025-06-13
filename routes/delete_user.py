from fastapi import APIRouter
from models import users

router=APIRouter()

@router.delete("/users/{user_id}")
def delete_user(user_id:int):
    for index, user in enumerate(users):
        if user.id==user_id:
            deleted_user=users.pop(index)
            return deleted_user
    return {"error":"tea_id not found. There was an error while deleting the data"}

