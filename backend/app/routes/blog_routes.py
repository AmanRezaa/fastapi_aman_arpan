# from fastapi import APIRouter
# from app.models.schema import Blog
# from app.controllers import blog_controller 

# router = APIRouter(prefix="/blogs",tags=["Blogs"])

# @router.get("/")
# def get_all_blogs():
#     return blog_controller.get_blogs()

# @router.post("/")
# def create_blog(blog : Blog):
#     return blog_controller.create_blog(blog)

# @router.get("/{blog_id}")
# def get_single_blog(blog_id: int):
#     return blog_controller.get_blog(blog_id)

# @router.put("/{blog_id}")
# def update_blog(blog_id : int,updatedBlog : Blog):
#     return blog_controller.update_blog(blog_id=blog_id,updated_blog=updatedBlog)

# @router.delete("/{blog_id}")
# def delete_blog(blog_id : int):
#     return blog_controller.delete_blog(blog_id=blog_id)




# app/routes/blog_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers import blog_controller
from app.models.pydantic_models import BlogCreate, BlogOut
from app.utils.db import get_db
from typing import List

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.post("/", response_model=BlogOut)
async def create_blog(blog: BlogCreate, db: AsyncSession = Depends(get_db)):
    return await blog_controller.create_blog(blog, db)

@router.get("/", response_model=List[BlogOut])
async def get_blogs(db: AsyncSession = Depends(get_db)):
    return await blog_controller.get_all_blogs(db)

@router.get("/{id}", response_model=BlogOut)
async def get_blog_by_id(id: int, db: AsyncSession = Depends(get_db)):
    blog = await blog_controller.get_blog(id, db)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@router.put("/{id}", response_model=BlogOut)
async def update_blog(id: int, blog_update: BlogCreate, db: AsyncSession = Depends(get_db)):
    updated_blog = await blog_controller.update_blog(id, blog_update, db)
    if not updated_blog:
        raise HTTPException(status_code=404, detail="Blog not found or update failed")
    return updated_blog

@router.delete("/{id}")
async def delete_blog(id: int, db: AsyncSession = Depends(get_db)):
    deleted = await blog_controller.delete_blog(id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Blog not found or delete failed")
    return {"message": "Blog deleted successfully"}
