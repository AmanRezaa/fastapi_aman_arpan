# app/models/pydantic_models.py
from pydantic import BaseModel,EmailStr

class BlogCreate(BaseModel):
    title: str
    content: str

class BlogOut(BlogCreate):
    id: int

    class Config:
        orm_mode = True

    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class UserSignup(UserLogin):
    username : str


class UserOut(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True

class TokenResponse(BaseModel):
    message: str
