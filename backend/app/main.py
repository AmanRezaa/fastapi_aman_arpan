# from fastapi import FastAPI
# from app.routes.blog_routes import router as blog_router

# app=FastAPI()

# app.include_router(blog_router)

# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.routes import blog_routes
from app.database.utils import engine,Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app  = FastAPI(lifespan=lifespan)

# Include your routers
app.include_router(blog_routes.router)




