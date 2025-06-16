from app.models.schema import Blog
from app.utils.db import blogs

def get_blogs():
    return blogs

def create_blog(blog:Blog):
    blogs.append(blog)
    return {"message":"New blog added successfully"}

def get_blog(blog_id:int):
    for index, blog in enumerate(blogs):
        if blog.id==blog_id:
            return blogs[index]
    return {"error":"the id not found. There was an error while updating the data"}

def update_blog(blog_id:int, updated_blog:Blog):
    for index, blog in enumerate(blogs):
        if blog.id==blog_id:
            blogs[index]=updated_blog
            return updated_blog
    return {"error":"the id not found. There was an error while updating the data"}


def delete_blog(blog_id:int):
    for index, blog in enumerate(blogs):
        if blog.id==blog_id:
            deleted_blog=blogs.pop(index)
            return deleted_blog
    return {"error":"tea_id not found. There was an error while deleting the data"}