from fastapi import APIRouter
from app.models.schema import Blog
from app.controllers import blog_controller 

router = APIRouter(prefix="/blogs",tags=["Blogs"])

@router.get("/")
def get_all_blogs():
    return blog_controller.get_blogs()

@router.post("/")
def create_blog(blog : Blog):
    return blog_controller.create_blog(blog)

@router.get("/{blog_id}")
def get_single_blog(blog_id: int):
    return blog_controller.get_blog(blog_id)

@router.put("/{blog_id}")
def update_blog(blog_id : int,updatedBlog : Blog):
    return blog_controller.update_blog(blog_id=blog_id,updated_blog=updatedBlog)

@router.delete("/{blog_id}")
def delete_blog(blog_id : int):
    return blog_controller.delete_blog(blog_id=blog_id)
