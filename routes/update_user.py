from fastapi import APIRouter
from models import users,User

router=APIRouter()

@router.put("/users/{user_id}")
def update_user(user_id:int, updated_user:User):
    for index, user in enumerate(users):
        if user.id==user_id:
            users[index]=updated_user
            return updated_user
    return {"error":"tea_id not found. There was an error while updating the data"}


