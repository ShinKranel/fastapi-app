from fastapi_users.authentication import CookieTransport, JWTStrategy

cookie_transport = CookieTransport(
    cookie_name="bonds",
    cookie_max_age=3600
)

SECRET = "SECRET"


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)
