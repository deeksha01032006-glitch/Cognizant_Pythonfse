from datetime import datetime
from datetime import timedelta

from jose import jwt
from jose import JWTError

from passlib.context import CryptContext


SECRET_KEY = "course_api_secret"

ALGORITHM = "HS256"


pwd = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def get_password_hash(password):

    return pwd.hash(password)


def verify_password(
        plain,
        hashed
):

    return pwd.verify(
        plain,
        hashed
    )


def create_access_token(data):

    expire = datetime.utcnow() + timedelta(
        minutes=30
    )

    payload = data.copy()

    payload.update(
        {
            "exp": expire
        }
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def decode_token(token):

    try:

        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

    except JWTError:

        return None