from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from app.models.schema import Blog
from app.models.pydantic_models import BlogCreate


async def create_blog(blog: BlogCreate, db: AsyncSession):
    try:
        new_blog = Blog(title=blog.title,content=blog.content)
        db.add(new_blog)
        await db.commit()
        await db.refresh(new_blog)
        return new_blog
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error while creating blog"
        )


async def get_all_blogs(db: AsyncSession):
    try:
        result = await db.execute(select(Blog))
        blogs = result.scalars().all()
        return blogs
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error while fetching blogs"
        )


async def get_blog(blog_id: int, db: AsyncSession):
    try:
        result = await db.execute(select(Blog).where(Blog.id == blog_id))
        blog = result.scalar_one_or_none()
        if blog is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with ID {blog_id} not found"
            )
        return blog
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error while fetching the blog"
        )


async def update_blog(blog_id: int, updated_blog: BlogCreate, db: AsyncSession):
    try:
        result = await db.execute(select(Blog).where(Blog.id == blog_id))
        blog = result.scalar_one_or_none()

        if blog is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with ID {blog_id} not found"
            )

        for key, value in updated_blog.model_dump().items():
            setattr(blog, key, value)

        db.add(blog)
        await db.commit()
        await db.refresh(blog)
        return blog
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error while updating the blog"
        )


async def delete_blog(blog_id: int, db: AsyncSession):
    try:
        result = await db.execute(select(Blog).where(Blog.id == blog_id))
        blog = result.scalar_one_or_none()

        if blog is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with ID {blog_id} not found"
            )

        await db.delete(blog)
        await db.commit()
        return {"message": f"Blog with ID {blog_id} deleted successfully"}
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error while deleting the blog"
        )
