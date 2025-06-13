from fastapi import APIRouter
from models import users,User

router=APIRouter()

@router.post("/users")
def create_user(user:User):
    users.append(user)
    return {"message":"New user added successfully"}


