import jwt
import datetime

from rest_framework.exceptions import AuthenticationFailed

from .constants import KEY, ALGORITH


def generate_token(user):
    if KEY is None:
        raise AuthenticationFailed("Secret key not found.")

    payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow(),
    }

    return jwt.encode(payload, KEY, algorithm=ALGORITH)
