from fastapi import APIRouter
from app.models.models import User

router = APIRouter()


fake_users = [
    {"id": 1, "name": "Vika", "degree": [
        {"type_degree": "master", "created_at": "2024-04-27T07:21:00"}
    ]},
    {"id": 2, "name": "Marsel"}
]


@router.get("/{user_id}", response_model=list[User])
async def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


@router.post("/{user_id}")
async def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users))
    current_user[0]['name'] = new_name
    return {"status": 200, "data": current_user}


# def sort_list(li: list):
#     p = 0
#     for i in range(len(li)):
#         if li[i] != 0:
#             li[p], li[i] = li[i], li[p]
#             p += 1
#
#     li[:p] = sorted(li[:p])
