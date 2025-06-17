from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
from urllib.parse import urlparse
import os
import ssl
from collections.abc import AsyncGenerator

# ------------------- Load Environment -------------------
load_dotenv()  # loads variables from .env into environment

DATABASE_URL_CLOUD = os.getenv("DATABASE_URL_CLOUD")
if not DATABASE_URL_CLOUD:
    raise RuntimeError("DATABASE_URL_CLOUD is not set in the .env file")

parsed = urlparse(DATABASE_URL_CLOUD)

# Construct the URL safely, include port if available
port = f":{parsed.port}" if parsed.port else ""
ASYNC_NEONDB_DATABASE_URL = f"postgresql+asyncpg://{parsed.username}:{parsed.password}@{parsed.hostname}{port}{parsed.path}"

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
