from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
from urllib.parse import urlparse
import os
import ssl
from collections.abc import AsyncGenerator

# ------------------- Load Environment -------------------

# Check if .env exists in current directory
if not os.getenv("DATABASE_URL_CLOUD"):
    dotenv_path = os.path.join(os.getcwd(), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        raise FileNotFoundError(
            f""".env file not found in current directory: {os.getcwd()}\n
             Either create a .env file or set DATABASE_URL_CLOUD via terminal or shell.\n
             
             DATABASE_URL_CLOUD=your-url uvicorn app.main:app --reload \n
             uvicorn app.main:app --reload --env-file .env \n

             for docker run it from where your .env is located \n

             docker run -p 8000:8000 --env-file .env   fastapi-blog-app:1.0.0
             
             
             """
        )



DATABASE_URL_CLOUD = os.getenv("DATABASE_URL_CLOUD")
if not DATABASE_URL_CLOUD:
    raise RuntimeError("DATABASE_URL_CLOUD is not set in the .env file")

# print("Got : ",DATABASE_URL_CLOUD)

parsed = urlparse(DATABASE_URL_CLOUD)
# print("Got p : ",parsed)
# print("Got p : ",parsed.username)
# print("Got p : ",parsed.password)
# print("Got p : ",parsed.hostname)
# print("Got p : ",parsed.path)

# Construct the URL safely, include port if available
ASYNC_NEONDB_DATABASE_URL = f"postgresql+asyncpg://{parsed.username}:{parsed.password}@{parsed.hostname}{parsed.path}"


# ------------------- DB Setup -------------------
engine = create_async_engine(
    ASYNC_NEONDB_DATABASE_URL,
    echo=True,
    connect_args={"ssl": ssl.create_default_context()} 
)
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
