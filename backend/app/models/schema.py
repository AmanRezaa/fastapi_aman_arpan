# from pydantic import BaseModel

# class Blog(BaseModel):
#     title : str
#     content : str
#     author : str
#     created_at : str


# app/models/schema.py
from sqlalchemy import Column, Integer, String
from app.utils.db import Base

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)


