
from fastapi import FastAPI 
from contextlib import asynccontextmanager

from app.routes import blog_routes,auth_routes
from app.database.utils import engine,Base
from app.utils.router_wrapper import secure_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

# Include your routers
app.include_router(auth_routes.router)
app.mount("/blogs",secure_router(blog_routes.router))
