import uvicorn
from fastapi import FastAPI
from app.routes import trades, users

app = FastAPI(
    title="Trading App"
)


app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(trades.router, prefix="/trades", tags=["trades"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
