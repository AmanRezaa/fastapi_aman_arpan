from fastapi import FastAPI, APIRouter
from app.middleware.auth_middleware import AuthMiddleware

def secure_router(router: APIRouter) -> FastAPI:
    sub_app = FastAPI()
    sub_app.add_middleware(AuthMiddleware)
    sub_app.include_router(router)
    return sub_app
