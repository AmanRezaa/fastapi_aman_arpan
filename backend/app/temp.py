# from fastapi import FastAPI, Request, Depends, HTTPException, status, Response
# from fastapi.responses import JSONResponse
# from app.models.pydantic_models import UserCreate, UserOut, TokenResponse
# from app.auth.utils import hash_password, verify_password, create_access_token, decode_access_token

# from typing import Dict

# app = FastAPI()

# # In-memory fake DB
# fake_db: Dict[str, str] = {}

# @app.post("/signup", response_model=UserOut)
# def signup(user: UserCreate):
#     if user.email in fake_db:
#         raise HTTPException(status_code=400, detail="User already exists")
#     fake_db[user.email] = hash_password(user.password)
#     return {"email": user.email}

# @app.post("/login", response_model=TokenResponse)
# def login(user: UserCreate, response: Response):
#     hashed = fake_db.get(user.email)
#     if not hashed or not verify_password(user.password, hashed):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
    
#     token = create_access_token(data={"sub": user.email})
#     response.set_cookie(
#         key="access_token",
#         value=token,
#         httponly=True,
#         secure=False,  # Set True in production (HTTPS)
#         samesite="lax",
#         path="/"
#     )
#     return {"message": "Login successful"}

# @app.get("/protected", response_model=UserOut)
# def get_current_user(request: Request):
#     token = request.cookies.get("access_token")
#     if not token:
#         raise HTTPException(status_code=401, detail="Not authenticated")

#     email = decode_access_token(token)
#     if not email or email not in fake_db:
#         raise HTTPException(status_code=401, detail="Invalid token")

#     return {"email": email}

# @app.post("/logout")
# def logout(response: Response):
#     response.delete_cookie("access_token", path="/")
#     return {"message": "Logged out successfully"}
