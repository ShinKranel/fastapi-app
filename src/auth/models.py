from datetime import datetime
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON)
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", ForeignKey(role.c.id)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)


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
        id: Mapped[int] = mapped_column(
            Integer, unique=True, index=True, nullable=False, primary_key=True
        )
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
