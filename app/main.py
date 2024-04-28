import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app = FastAPI(
    title="Trading App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
