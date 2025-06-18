
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
app.include_router(blog_routes.router)
# app.mount("/",secure_router(blog_routes.router))



# from fastapi import Request,HTTPException
# from app.models.pydantic_models import UserOut
# from app.auth.utils import decode_access_token

# @app.get("/protected", response_model=UserOut)
# def get_current_user(request: Request):
#     token = request.cookies.get("access_token")
#     if not token:
#         raise HTTPException(status_code=401, detail="Not authenticated")

#     email = decode_access_token(token)

#     return {"email": email}