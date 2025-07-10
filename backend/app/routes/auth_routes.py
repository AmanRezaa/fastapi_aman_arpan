from fastapi import APIRouter, Depends, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.utils import get_db
from app.models.pydantic_models import UserLogin,UserSignup, UserOut
import app.controllers.auth_controller as controller

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup")
async def signup(user: UserSignup, db: AsyncSession = Depends(get_db)):
    return await controller.signup(user, db)

@router.post("/login")
async def login(user: UserLogin, response: Response, db: AsyncSession = Depends(get_db)):
    return await controller.login(user, db, response)

@router.post("/logout")
async def logout(response: Response):
    return controller.logout(response)
