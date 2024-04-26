from datetime import datetime
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON

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
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", ForeignKey(role.c.id)),
    Column("password", String, nullable=False)
)



from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=8)
    price: float = Field(ge=0)
    amount: float = Field(ge=0)


class DegreeType(Enum):
    newbie = "newbie"
    master = "master"


class Degree(BaseModel):
    type_degree: DegreeType
    created_at: datetime


class User(BaseModel):
    id: int = Field(ge=1)
    name: str
    degree: list[Degree] | None = []
