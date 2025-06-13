from app.models.schema import User
from app.utils.db import users

def get_users():
    return users

def create_user(user:User):
    users.append(user)
    return {"message":"New user added successfully"}

def get_user(user_id:int):
    for index, user in enumerate(users):
        if user.id==user_id:
            return users[index]
    return {"error":"the id not found. There was an error while updating the data"}

def update_user(user_id:int, updated_user:User):
    for index, user in enumerate(users):
        if user.id==user_id:
            users[index]=updated_user
            return updated_user
    return {"error":"the id not found. There was an error while updating the data"}


def delete_user(user_id:int):
    for index, user in enumerate(users):
        if user.id==user_id:
            deleted_user=users.pop(index)
            return deleted_user
    return {"error":"tea_id not found. There was an error while deleting the data"}