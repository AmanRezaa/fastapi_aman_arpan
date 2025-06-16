# app/models/pydantic_models.py
from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    content: str

class BlogOut(BlogCreate):
    id: int

    class Config:
        orm_mode = True
