from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from app.auth.utils import decode_access_token

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.cookies.get("access_token")
        email = decode_access_token(token) if token else None

        if not email:
            return Response(content="Unauthorized", status_code=401)

        request.state.user_email = email
        return await call_next(request)
