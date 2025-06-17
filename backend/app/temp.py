# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import Integer, String, select
# from contextlib import asynccontextmanager
# from dotenv import load_dotenv
# from urllib.parse import urlparse
# import os
# import ssl


# # ------------------- Load Environment -------------------
# load_dotenv()  # loads variables from .env into environment

# DATABASE_URL = os.getenv("DATABASE_URL")
# if not DATABASE_URL:
#     raise RuntimeError("DATABASE_URL is not set in the .env file")

# parsed = urlparse(DATABASE_URL)
# ASYNC_NEONDB_DATABASE_URL = f"postgresql+asyncpg://{parsed.username}:{parsed.password}@{parsed.hostname}{parsed.path}"


# # ------------------- DB Setup -------------------
# engine = create_async_engine(
#     ASYNC_NEONDB_DATABASE_URL,
#     echo=True,
#     connect_args={"ssl": ssl.create_default_context()} 
#     )
# async_session = async_sessionmaker(engine, expire_on_commit=False)

# # ------------------- ORM Base -------------------
# class Base(DeclarativeBase):
#     pass


# # ------------------- Model -------------------
# class User(Base):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String, nullable=False)

# # ------------------- Lifespan -------------------
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield
#     await engine.dispose()

# # ------------------- App -------------------
# app = FastAPI(lifespan=lifespan)

# # ------------------- Dependency -------------------
# async def get_session() -> AsyncSession:
#     async with async_session() as session:
#         yield session

# # ------------------- Routes -------------------
# @app.post("/users")
# async def create_user(name: str, session: AsyncSession = Depends(get_session)):
#     user = User(name=name)
#     session.add(user)
#     await session.commit()
#     await session.refresh(user)
#     return {"id": user.id, "name": user.name}

# @app.get("/users/{user_id}")
# async def read_user(user_id: int, session: AsyncSession = Depends(get_session)):
#     result = await session.execute(select(User).where(User.id == user_id))
#     user = result.scalar_one_or_none()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return {"id": user.id, "name": user.name}
