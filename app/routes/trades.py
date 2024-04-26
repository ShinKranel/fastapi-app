from fastapi import APIRouter
from app.models.models import Trade

router = APIRouter()

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "price": 80, "amount": 2},
    {"id": 2, "user_id": 1, "currency": "BTC", "price": 200, "amount": 5}
]


@router.get("/", status_code=200)
async def get_trades(offset: int = 0, limit: int = 10):
    return fake_trades[offset:][:limit]


@router.post("/")
async def add_trades(trades: list[Trade]):
    fake_trades.extend(trades)
    return fake_trades
