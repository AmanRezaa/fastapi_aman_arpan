from fastapi import FastAPI
from app.routes.blog_routes import router as blog_router

app=FastAPI()

app.include_router(blog_router)



