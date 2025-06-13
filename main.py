from fastapi import FastAPI
from typing import List
from routes import create_user, get_user, update_user, delete_user

app=FastAPI()

app.include_router(create_user.router)
app.include_router(get_user.router)
app.include_router(update_user.router)
app.include_router(delete_user.router)



