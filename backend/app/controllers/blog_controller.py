# from app.models.schema import Blog
# from app.utils.db import blogs

# def get_blogs():
#     return blogs

# def create_blog(blog:Blog):
#     blogs.append(blog)
#     return {"message":"New blog added successfully"}

# def get_blog(blog_id:int):
#     for index, blog in enumerate(blogs):
#         if blog.id==blog_id:
#             return blogs[index]
#     return {"error":"the id not found. There was an error while updating the data"}

# def update_blog(blog_id:int, updated_blog:Blog):
#     for index, blog in enumerate(blogs):
#         if blog.id==blog_id:
#             blogs[index]=updated_blog
#             return updated_blog
#     return {"error":"the id not found. There was an error while updating the data"}


# def delete_blog(blog_id:int):
#     for index, blog in enumerate(blogs):
#         if blog.id==blog_id:
#             deleted_blog=blogs.pop(index)
#             return deleted_blog
#     return {"error":"tea_id not found. There was an error while deleting the data"}




# app/controllers/blog_controller.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from app.models.schema import Blog
from app.models.pydantic_models import BlogCreate

async def create_blog(blog: BlogCreate, db: AsyncSession):
    new_blog = Blog(**blog.dict())
    db.add(new_blog)
    await db.commit()
    await db.refresh(new_blog)
    return new_blog

async def get_all_blogs(db: AsyncSession):
    result = await db.execute(select(Blog))
    return result.scalars().all()

async def get_blog(blog_id: int, db: AsyncSession):
    result = await db.execute(select(Blog).where(Blog.id == blog_id))
    blog = result.scalar_one_or_none()
    return blog

async def update_blog(blog_id: int, updated_blog: BlogCreate, db: AsyncSession):
    result = await db.execute(select(Blog).where(Blog.id == blog_id))
    blog = result.scalar_one_or_none()
    if not blog:
        return None

    for key, value in updated_blog.dict().items():
        setattr(blog, key, value)

    db.add(blog)
    await db.commit()
    await db.refresh(blog)
    return blog

async def delete_blog(blog_id: int, db: AsyncSession):
    result = await db.execute(select(Blog).where(Blog.id == blog_id))
    blog = result.scalar_one_or_none()
    if not blog:
        return None

    await db.delete(blog)
    await db.commit()
    return True



