from fastapi import Request, Response, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.pydantic_models import UserLogin,UserSignup, UserOut
from app.models.schema import User
from app.auth.utils import hash_password, verify_password, create_access_token, decode_access_token
from sqlalchemy.future import select

# Signup
async def signup(user: UserSignup, db: AsyncSession):
    existing_email = await db.execute(select(User).where(User.email == user.email))
    if existing_email.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_pw = hash_password(user.password)
    new_user = User(email=user.email, username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {"email" : new_user.email}

# Login
async def login(user: UserLogin, db: AsyncSession, response: Response):
    result = await db.execute(select(User).where(User.email == user.email))
    db_user = result.scalar_one_or_none()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})
    response.set_cookie("access_token", token, httponly=True, samesite="lax")
    return {"message": "Login successful"}

# Logout
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logged out"}
