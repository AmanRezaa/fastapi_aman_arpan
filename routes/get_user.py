from fastapi import APIRouter
from models import users

router=APIRouter()

@router.get("/")
def read_root():
    return {"message":"Welcome to the home page"}

@router.get("/users")
def get_users():
    return users


