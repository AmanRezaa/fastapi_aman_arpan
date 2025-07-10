from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from urllib.parse import urlparse
import ssl
from collections.abc import AsyncGenerator

from config.config import settings


DATABASE_URL_CLOUD = settings.DATABASE_URL_CLOUD

parsed = urlparse(DATABASE_URL_CLOUD)


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
