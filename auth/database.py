from typing import AsyncGenerator, TYPE_CHECKING

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi_users.models import ID
from sqlalchemy import String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.models.models import role
from config import DB_NAME, DB_PORT, DB_HOST, DB_USER, DB_PASS

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    if TYPE_CHECKING:  # pragma: no cover
        id: int
        email: str
        username: str
        role_id: ForeignKey(role.c.id)
        registered_at: TIMESTAMP
        hashed_password: str
        is_active: bool
        is_superuser: bool
        is_verified: bool
    else:
        email: Mapped[str] = mapped_column(
            String(length=320), unique=True, index=True, nullable=False
        )
        username: Mapped[str] = mapped_column(
            String(length=320), nullable=False
        )
        role_id: Mapped[ForeignKey(role.c.id)] = mapped_column(
            ForeignKey(role.c.id), nullable=False
        )
        registered_at: Mapped[TIMESTAMP] = mapped_column(
            TIMESTAMP, nullable=False
        )
        hashed_password: Mapped[str] = mapped_column(
            String(length=1024), nullable=False
        )
        is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
        is_superuser: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )
        is_verified: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
